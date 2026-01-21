{
    'name': 'Hospital Management System',
    'version': '1.0',
    'author': 'TheBIGCHOBO',
    # 'category': 'Train Booking System/Groups',
    'summary': 'A Hospital Management System',
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
        # 'views/station_views.xml',
        # 'views/train_booking_views.xml',
        'views/patients_views.xml',
        # 'views/train_ticket_views.xml',
        # 'views/train_route_views.xml',
        # 'views/available_trains_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}