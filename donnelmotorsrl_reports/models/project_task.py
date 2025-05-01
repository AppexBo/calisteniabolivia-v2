from odoo import api, fields, models
from odoo.exceptions import ValidationError

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