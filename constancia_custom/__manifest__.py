# -*- coding: utf-8 -*-
{
    'name': "Certificado eLearning Custom",

    'summary': """
        Añade la funcionalidad para personalizar la firma de la constancia, ademas añade codigo QR con enlace de validacion de la expedicion de la misma""",

    'description': """
        Añade la funcionalidad para personalizar la firma de la constancia, ademas añade codigo QR con enlace de validacion de la expedicion de la misma
    """,

    'author': "Marxim TI & SD",
    'price': '30.00',
    'currency': 'USD',
    'website': "http://marxim.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website/Website',
    'version': '15.0.2',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['website_slides','survey','website_slides_survey'],

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
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
