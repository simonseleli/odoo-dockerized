from odoo import models, fields
from odoo.exceptions import UserError

class TrainBookingWizard(models.TransientModel):
    _name = 'train.booking.wizard'
    _description = 'Train Booking Wizard'
    #
    # passenger_id = fields.Many2one('train.passenger', string='Passenger', required=True)
    # station_from = fields.Many2one('train.station', string='From Station', required=True)
    # station_to = fields.Many2one('train.station', string='To Station', required=True)
    # train_id = fields.Many2one('train.train', string='Train', required=True)
    # booking_date = fields.Datetime(string='Booking Date', default=fields.Datetime.now)
    #
    # def action_book(self):
    #     # Ensure that the train is available for the selected stations
    #     available_trains = self.env['train.train'].search([
    #         ('station_ids.id', 'in', [self.station_from.id, self.station_to.id])
    #     ])
    #
    #     if not available_trains:
    #         raise UserError("No trains are available between these stations.")
    #
    #     # Create the booking record
    #     booking = self.env['train.booking'].create({
    #         'train_id': self.train_id.id,
    #         'passenger_id': self.passenger_id.id,
    #         'station_from': self.station_from.id,
    #         'station_to': self.station_to.id,
    #         'booking_date': self.booking_date,
    #         'status': 'confirmed',  # Set status to confirmed
    #         'receipt_number': self.env['ir.sequence'].next_by_code('train.booking.receipt')
    #     })
    #
    #     # Return a message for confirmation or any other post-booking action
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'train.booking',
    #         'res_id': booking.id,
    #         'view_mode': 'form',
    #         'target': 'new',
    #     }




