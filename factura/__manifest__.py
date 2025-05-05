# -*- coding:utf-8 -*-
{
    'name': 'Factura v18',
    'version': '1.0',
    'depends': [
        'base', 
       'l10n_bo_bolivian_invoice',
       'account',
    ],
    'author': 'APPEX BOLIVIA SRL.',
    'summary': 'Factura',
    'data': [
    'reports/formato_papel.xml',
      'reports/boton_imprimir_pdf.xml',
      'reports/cuerpo_pdf.xml',
    ],
    'installable': True,
}