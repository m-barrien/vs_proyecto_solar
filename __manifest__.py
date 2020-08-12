# -*- coding: utf-8 -*-
{
    'name': "Proyectos Solares",

    'summary': """
        Administrador de proyectos solares""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Vincent Solar",
    'website': "https://www.vincentsolar.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/proyecto_solar.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
