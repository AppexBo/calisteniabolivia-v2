from odoo import api, fields, models
from dateutil.relativedelta import relativedelta

class AccountPayment(models.Model):
    _inherit = 'account.move'

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
                ultimo_numero = self.env['account.move'].search_count(domain) + 1
                secuencial = f"{ultimo_numero:05d}"  # Formato '00001', '00002', etc.
                record.mes_secuencia = f"{mes} {secuencial}"
            else:
                record.mes_secuencia = ''

    @api.model
    def create(self, vals):
        record = super(AccountPayment, self).create(vals)
        record._compute_mes_secuencia()  # Asegurar que se calcule al crear
        return record