# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Itqan Customer',
    'version': '1.0.0',
    'category': 'Customer Contract',
    'author':'Moamen Hatem',
    'summary': 'Customer Contract',
    'description': """Customer Contract""",
    'depends': ['base'],
    'demo': [],
    'data':[
        'security/ir.model.access.csv',
        'views/itq_customer_view.xml',
        'views/res_partner_views.xml'
    ],
    'application':True,
    'license': 'LGPL-3',
}
