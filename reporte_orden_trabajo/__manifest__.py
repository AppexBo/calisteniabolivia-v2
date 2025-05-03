# -*- coding:utf-8 -*-
{
    'name': 'Reporte Orden Trabajo v18',
    'version': '1.0',
    'depends': [
        'base', 
        'sale',
        'account',
        'purchase',
    ],
    'author': 'APPEX BOLIVIA SRL.',
    'summary': 'Reporte Orden Trabajo v18',
    'data': [
    'reports/formato_papel.xml',
      'reports/boton_imprimir_pdf.xml',
      'reports/cabecera_pdf.xml',
      'reports/cuerpo_pdf.xml',
      'views/project_task_add_fields.xml',
    ],
    'installable': True,
}