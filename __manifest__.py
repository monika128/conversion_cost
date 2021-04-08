# -*- coding: utf-8 -*-
{
    'name': "conversion_cost",

    'summary': """
        Cost Conversion""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/po_orderline_view.xml',
        'views/product_template.xml',
        'views/product_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}