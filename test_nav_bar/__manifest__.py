# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'TEST Customer: TEST Change Header Color',
    'version': '1.0',
    'category': 'Custom Development',
    'sequence': 50,
    'summary': """Change Header Color""",
    'depends': ['web_enterprise'],
    'description': """
* Change Header Color: #32CD32

""",
    'data': [
        'views/webclient_templates.xml',
    ],
    'license': 'OEEL-1',
    'installable': True,
    'auto_install': False,
}
