from odoo import models, fields

class TrainStation(models.Model):
    _name = "train.booking.station"
    _description = "Train Station"

    name = fields.Char(string="Station Name", required=True)
    code = fields.Char(string="Station Code", required=True, )
    active = fields.Boolean(string="Active", default=True)