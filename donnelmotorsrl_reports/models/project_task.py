from odoo import api, fields, models
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from num2words import num2words

import logging

_logger = logging.getLogger(__name__)

class ProjectTask(models.Model):
    _inherit = 'project.task'
    _description = "Project Task"

    tipo_vehiculo = fields.Char(string='Tipo Vehículo', store=True, required=True)
    color_vehiculo = fields.Char(string='Color', store=True, required=True)
    vin_vehiculo = fields.Char(string='VIN', store=True, required=True)
    placa_vehiculo = fields.Char(string='Placa', store=True, required=True)
    kilometraje_vehiculo = fields.Char(string='Kilometraje', store=True, required=True)
    year_vehiculo = fields.Integer(
        string='Año',
        store=True,
        required=True
    )

    @api.constrains('year_vehiculo')
    def _check_year_format(self):
        for record in self:
            if record.year_vehiculo:
                # Validación para 4 dígitos (1000-9999)
                if record.year_vehiculo < 1000 or record.year_vehiculo > 9999:
                    raise ValidationError("El año debe ser un número de exactamente 4 dígitos (ej: 2023)")
                

class SecuenciaMes(models.Model):
    _inherit = 'sale.order'

    mes_secuencia = fields.Char(string="Secuencia por Mes", compute='_compute_mes_secuencia', store=True)

    @api.depends('date', 'journal_id', 'journal_id.type')
    def _compute_mes_secuencia(self):
        for record in self:
            if record.date and record.journal_id and record.journal_id.type:
                # Extraer el mes en formato 'MM' (ej. '03' para marzo)
                mes = record.date.strftime('%m')
                # Definir el rango del mes actual
                start_of_month = record.date.replace(day=1)
                end_of_month = start_of_month + relativedelta(months=1)
                
                # Dominio para contar movimientos en el mismo mes y tipo de diario
                domain = [
                    ('date', '>=', start_of_month),
                    ('date', '<', end_of_month),
                    ('journal_id.type', '=', record.journal_id.type),  # Filtrar por tipo de diario
                ]
                # Excluir el registro actual si ya existe
                if record.id:
                    domain.append(('id', '!=', record.id))
                
                # Contar los movimientos previos en este mes y tipo de diario, y sumar 1
                ultimo_numero = self.env['sale.order'].search_count(domain) + 1
                secuencial = f"{ultimo_numero:05d}"  # Formato '00001', '00002', etc.
                record.mes_secuencia = f"-{mes}-{secuencial}"
            else:
                record.mes_secuencia = ''

    @api.model
    def create(self, vals):
        record = super(SecuenciaMes, self).create(vals)
        record._compute_mes_secuencia()  # Asegurar que se calcule al crear
        return record
    
    codigo_A1_or_A2 = fields.Char(
        string='Código A1 o A2',
        compute='_compute_codigo_fiscal',
        store=False
    )

    @api.depends('company_id.company_registry')
    def _compute_codigo_fiscal(self):
        for record in self:
            if record.company_id.company_registry == '100':
                record.codigo_A1_or_A2 = "A1"
            elif record.company_id.company_registry == '200':
                record.codigo_A1_or_A2 = "A2"
            else:
                record.codigo_A1_or_A2 = ""