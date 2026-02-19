{
    'name': "IT Helpdesk Lite",
    'summary': "Gestión de incidencias de equipos",
    'author': "Martina",
    'category': 'Services/Helpdesk',
    'version': '0.1',
    'depends': ['base', 'mail', 'maintenance'], # Importante: maintenance para los equipos
'data': [
    'security/helpdesk_security.xml',
    'security/ir.model.access.csv',
    'data/ir_sequence_data.xml',
    'data/it_ticket_stage_data.xml',
    'data/cron_data.xml',
    'views/it_ticket_views.xml',
    'views/menu_views.xml',
],

    'license': 'LGPL-3',
    'application': True,    # <--- ESTO es lo que le dice a Odoo que es una App
    'installable': True,
    'auto_install': False,
}
