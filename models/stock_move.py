# -*- coding: utf-8 -*-
from openerp import models, fields, _


class StockMove(models.Model):

    _inherit = 'stock.move'

    package_number = fields.Char('Package number')
