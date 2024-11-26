{
    'name': '汽車美容管理',
    'version': '1.0',
    'category': 'Services',
    'summary': '管理汽車美容服務',
    'description': """汽車美容服務管理系統""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/work_order_views.xml',
    ],
    'installable': True,
    'application': True,
}
