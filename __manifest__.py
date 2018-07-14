# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016-TODAY Linserv Aktiebolag, Sweden (<http://www.linserv.se>).
#
##############################################################################

{
    'name': 'Hr Expense',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Expenses Validation, Invoicing',
    'description': """
        Long description of module's purpose
    """,

    'author': "Linserv Consulting AB",
    'website': "http://www.linserv.se",
  "contributors": [
        'pragya Chhabra <pragyachhabbra@gmail.com>'
    ],
    "license": "",
    'depends': ['sale', 'hr_expense'],
    'data': [

        'views/hr_expense_views.xml',

    ],

    'installable': True,
    'application': True,
}
