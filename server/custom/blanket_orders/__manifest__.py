# -*- coding: utf-8 -*-
'''
{
    'name': "blanket_orders",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
'''
{

    #'name': 'blanket_orders',
    'version': '1.2',
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'sequence': 30,
    
    'description': """
Long Description of your modules
    """,
    'author': 'kimtuyen',
    'company': 'Company Name',
    'website': 'https://www.website.com',
    'category': 'blanket_orders',
    'depends': [
        'purchase_requisition',
        'base',
        'purchase',
    
        ],
    'data': [
        'security/ir.model.access.csv',
        
        
   ],
    'application': True,
}
