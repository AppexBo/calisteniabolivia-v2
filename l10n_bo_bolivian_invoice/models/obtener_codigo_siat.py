from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    codigo_actividad_siat = fields.Char(
        string="Código Actividad SIAT",
        compute='_compute_codigo_actividad_siat',
        store=True
    )

    @api.depends('invoice_line_ids.siat_service_id')
    def _compute_codigo_actividad_siat(self):
        for move in self:
            line = next((l for l in move.invoice_line_ids if l.siat_service_id), None)
            move.codigo_actividad_siat = line.siat_service_id.codigoActividad if line else ''
