# -*- coding: utf-8 -*-

from odoo import models, fields


class expenseNew(models.Model):
    _name = 'hr.expense'

    _inherit = 'hr.expense' 
    expense_new_id = fields.Many2one('hr.expense',
                                     help="This is a many2one field in expense_new module, and this field is used as a link to hr.expense module")

    sale_order_id = fields.Many2one('sale.order',string='Sale Order', readonly=True, required= False, states={'draft': [('readonly', False)], 'refused': [('readonly', False)]})


