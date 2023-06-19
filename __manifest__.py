# -*- coding: utf-8 -*-
{
    'name': "Technical_Exam",
    'summary': """
        Technical Exam""",
    'description': """
        Long description of module's purpose
    """,
    'author': "khodary",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
        'account'
    ],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'security/registration_security.xml',
        'views/partner_inherit.xml',
        'views/registration_view.xml',
        'views/registration_menu.xml',
        'data/sequence.xml',
    ],
}
