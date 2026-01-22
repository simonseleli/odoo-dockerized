{
    'name': 'Real Estate',
    'version': '1.0',
    'author': 'Simons',
    'summary': 'Simons System',
    'depends': [
        'base',
        'mail',
        'product',
        'account'
    ],
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        # 'data/sequence.xml',
        # 'views/train_views.xml',
        'views/estate_property_views.xml',
        # 'views/patients_views.xml',
        # 'views/train_ticket_views.xml',
        # 'views/train_route_views.xml',
        # 'views/available_trains_views.xml',
        'views/estate_menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}