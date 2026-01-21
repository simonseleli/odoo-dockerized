from odoo import models, fields

class TrainRoute(models.Model):
    _name = "train.booking.route"
    _description = "Train Route"

    name = fields.Char(string="Route Name",required=True)

    from_station_id = fields.Many2one(
        "train.booking.station",
        string="From Station",
        required=True
    )
    to_station_id = fields.Many2one(
        "train.booking.station",
        string="To Station",
        required=True
    )
    train_id = fields.Many2one(
        "train.booking.train",
        string="Train",
        required=True
    )


