from odoo import models, fields
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char('Title',required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date('Available From',copy=False,default=lambda self: fields.Date.today() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer('Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer('Garden Area (sqm)')
    garden_orientation = fields.Selection(
      string='Garden Orientation',
      selection=[
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
      ],
      help="The orientation of the garden"
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='Status',
        required=True,
        copy=False,
        default='new',
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled'),
        ],
        help="The status of the property"
    )
