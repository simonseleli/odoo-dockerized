from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TrainBooking(models.Model):
    _name = "train.booking"
    _description = "Train Ticket Booking"
    _order = "booking_date desc"

    name = fields.Char(string="Booking Reference", required=True, copy=False, readonly=True, default="New")
    passenger_id = fields.Many2one(
        'train.passenger',
        string="Passenger",
        required=True)
    route_id = fields.Many2one("train.booking.route", string="Route", required=True)
    train_id = fields.Many2one("train.booking.train", string="Train", related="route_id.train_id", store=True)
    from_station_id = fields.Many2one("train.booking.station", string="From", related="route_id.from_station_id",
                                      store=True)
    to_station_id = fields.Many2one("train.booking.station", string="To", related="route_id.to_station_id", store=True)
    seat_count = fields.Integer(string="Number of Seats", required=True, default=1)
    booking_date = fields.Datetime(string="Booking Date", default=fields.Datetime.now)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string="Status", default="draft", required=True)

    ticket_ids = fields.One2many('train.ticket', 'booking_id', string="Tickets")
    ticket_count = fields.Integer(compute='_compute_ticket_count', string="Ticket Count")

    @api.model
    def create(self, vals):
        route = self.env["train.booking.route"].browse(vals.get("route_id"))
        train = route.train_id

        if not train:
            raise ValidationError("No train assigned to the selected route!")

        seat_count = vals.get("seat_count", 1)
        if seat_count <= 0:
            raise ValidationError("Number of seats must be positive!")

        if train.available_seats < seat_count:
            raise ValidationError(f"Only {train.available_seats} seats available on {train.name}!")

        if vals.get("name", "New") == "New":
            vals["name"] = self.env["ir.sequence"].next_by_code("train.booking") or "New"

        return super().create(vals)

    def action_confirm(self):
        for booking in self:
            if booking.state not in ('draft', 'cancelled'):
                continue

            if booking.train_id.available_seats < booking.seat_count:
                raise ValidationError(
                    f"Only {booking.train_id.available_seats} seats available on {booking.train_id.name}!"
                )

            if not booking.ticket_ids:
                self.env['train.ticket'].create({
                    'booking_id': booking.id,
                })

            booking.state = "confirmed"

    def action_cancel(self):
        self.filtered(lambda b: b.state == 'confirmed').write({'state': 'cancelled'})

    @api.constrains('seat_count')
    def _check_seat_count(self):
        for booking in self:
            if booking.seat_count <= 0:
                raise ValidationError("Number of seats must be positive!")

    @api.onchange('route_id')
    def _onchange_route(self):
        if self.route_id and self.route_id.train_id:
            return {
                'warning': {
                    'title': "Seat Availability",
                    'message': f"Available seats: {self.route_id.train_id.available_seats}"
                }
            }

    def _compute_ticket_count(self):
        for booking in self:
            booking.ticket_count = len(booking.ticket_ids)

    def action_view_tickets(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tickets',
            'view_mode': 'tree,form',
            'res_model': 'train.ticket',
            'domain': [('booking_id', '=', self.id)],
            'context': {'default_booking_id': self.id},
        }

