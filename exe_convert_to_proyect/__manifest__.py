# -*- coding: utf-8 -*-
{
    'name': "Convert to Project",

    'summary': """
        Turn an opportunity into a project""",

    'description': """
        Converts an opportunity to a project and can copy tasks from an existing project 
    """,
    
    'author': "Brenda Gauto _ Exemax",
    'website': "http://www.exemax.com.ar",
    'category': 'Project',
    'version': '0.1',
    'depends': ['base','crm', 'project'],
    'data': [
        'wizard/convert_project_views.xml',
        'views/views.xml',
    ],
}
