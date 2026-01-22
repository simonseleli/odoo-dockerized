from odoo import models, fields, api


class RealEstate(models.Model):
    _name = 'estate.property'  # Database table name: hospital_patient
    _description = 'Real Estate Details'
    _inherit = ['mail.thread']


    name = fields.Char(string='Patient Name', required=True, tracking=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability', tracking=True)
    expected_price = fields.Float(string='Expected Price', tracking=True, required=True)
    selling_price = fields.Float(string="Selling Price", tracking=True)
    garden_orientation = fields.Selection([
        ('north', 'North'), 
        ('south', 'South'),
        ('east', 'East'), 
        ('west', 'West')], 
        string="Garden Orientation", tracking=True
    )
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Integer(string="garage")
    garden = fields.Boolean(string="Has Gardern")
    garden_area = fields.Integer(string="Garden Area")

