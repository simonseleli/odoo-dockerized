from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'  # Database table name: hospital_patient
    _description = 'Patient Details'
    _inherit = ['mail.thread']


    name = fields.Char(string='Patient Name', required=True, tracking=True)
    email = fields.Char(string='Email', tracking=True)
    phone = fields.Char(string='Phone', tracking=True)
    date_of_birth = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)

    # address = fields.Text(string='Address')
    # booking_ids = fields.One2many(
    #     'train.booking',
    #     'passenger_id',
    #     string='Bookings'
    # )

    # user_id = fields.Many2one(
    #     'res.users',
    #     string="System User",
    #     help="Link to the system user"
    # )

    # @api.model_create_multi
    # def create(self, vals_list):
    #     users = self.env['res.users'].sudo()
    #     group_passenger = self.env.ref('train.group_train_passenger')  # Ensure this exists

    #     for vals in vals_list:
    #         # Create a user for this passenger if they don't already have one
    #         if 'user_id' not in vals or not vals['user_id']:
    #             # Generate a login name (email if available, otherwise name-based)
    #             login = vals.get('email') or f"{vals.get('name').replace(' ', '').lower()}@train.com"

    #             user_vals = {
    #                 'name': vals.get('name'),
    #                 'login': login,
    #                 'password': 'passenger123',  # Set default password (should be changed later)
    #                 'groups_id': [(4, group_passenger.id)],  # Assign Passenger role
    #             }
    #             user = users.create(user_vals)
    #             vals['user_id'] = user.id  # Link the created user to the passenger

    #     return super().create(vals_list)