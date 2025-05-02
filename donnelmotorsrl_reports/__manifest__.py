{
	"name" : "Reportes Donnel Motor SRL",
	"version" : "17.0.0.0",
	"category" : "",
	"depends" : [
		'base',
		'project',
        'sale',
	],
	"author": "AppexBo",
	'summary': 'Los reportes solicitados',
	"description": "Los reportes solicitados",
	"website" : "https://www.appexbo.com/",
	"auto_install": False,
	"installable": True,
	"license": "LGPL-3",
	"data": [
		##adicionar los campos al formulario de servicios externos
		'views/project_task_add_fields.xml',
		#editar el reportes de orden Cotizacion en PDF
		'reports/new_sale_report_saleorder.xml',
		'reports/layout_standart_reportes_saleorder.xml',
		
		
		
		#reportes de compra
		'reports/new_report_purchaseorder.xml',
		'reports/layout_header_report_purchaseorder.xml',
		
		##formato de papel estandar
		'reports/paper_format.xml',
	],
}