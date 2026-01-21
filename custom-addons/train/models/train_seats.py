from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TrainBookingSeat(models.Model):
    _name = 'train.booking.seat'
    _description = 'Train Seat'

    seat_number = fields.Integer(string='Seat Number', required=True)
    is_booked = fields.Boolean(string='Is Booked', default=False)
    booking_id = fields.Many2one('train.booking', string='Booking')
    train_id = fields.Many2one('train.booking.train', string="Train", related="booking_id.train_id", store=True)
    route_id = fields.Many2one('train.booking.route', string="Route", related="booking_id.route_id", store=True)

    # When a seat is booked, update the availability
    def book_seat(self):
        if self.is_booked:
            raise ValidationError("Seat already booked!")
        self.is_booked = True


