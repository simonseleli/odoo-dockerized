from odoo import models, fields, api


class TrainTicket(models.Model):
    _name = "train.ticket"
    _rec_name = "passenger_id"
    _description = "Train Ticket"

    booking_id = fields.Many2one('train.booking', string="Booking", required=True, readonly=True)
    passenger_id = fields.Many2one('train.passenger', string="Passenger", related='booking_id.passenger_id', store=True)
    train_id = fields.Many2one('train.booking.train', string="Train", related='booking_id.train_id', store=True)
    from_station_id = fields.Many2one('train.booking.station', string="From", related='booking_id.from_station_id', store=True)
    to_station_id = fields.Many2one('train.booking.station', string="To", related='booking_id.to_station_id', store=True)
    seat_count = fields.Integer(string="Number of Seats", related='booking_id.seat_count', store=True)
    booking_date = fields.Datetime(string="Booking Date", related='booking_id.booking_date', store=True)
    ticket_number = fields.Char(string="Ticket Number", required=True, readonly=True, copy=False, default="New")

    @api.model
    def create(self, vals):
        if vals.get('ticket_number', 'New') == 'New':
            vals['ticket_number'] = self.env['ir.sequence'].next_by_code('train.ticket') or 'New'
        return super().create(vals)
