from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Train(models.Model):
    _name = "train.booking.train"
    _description = "Train Information"
    _order = "name asc"

    name = fields.Char(string="Train Name", required=True, copy=True)
    code = fields.Char(string="Train Code", required=True)
    capacity = fields.Integer(string="Capacity", required=True)
    train_type = fields.Selection([
        ('express', 'Express'),
        ('passenger', 'Passenger'),
        ('freight', 'Freight')
    ], string="Train Type", required=True, default='passenger')

    active = fields.Boolean(string="Active", default=True)

    booked_seats = fields.Integer(
        string="Booked Seats",
        compute="_compute_booked_seats",
        store=True,
        help="Total confirmed booked seats"
    )

    available_seats = fields.Integer(
        string="Available Seats",
        compute="_compute_available_seats",
        store=True,
        help="Available seats (Capacity - Booked seats)"
    )

    booking_ids = fields.One2many(
        "train.booking",
        "train_id",
        string="Bookings",
        domain=[('state', '=', 'confirmed')]
    )

    @api.depends("booking_ids.seat_count")
    def _compute_booked_seats(self):
        for train in self:
            train.booked_seats = sum(train.booking_ids.mapped("seat_count"))

    @api.depends("capacity", "booked_seats")
    def _compute_available_seats(self):
        for train in self:
            train.available_seats = max(0, train.capacity - train.booked_seats)

    @api.constrains('capacity')
    def _check_capacity(self):
        for train in self:
            if train.capacity <= 0:
                raise ValidationError("Train capacity must be positive!")








