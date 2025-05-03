from odoo import api, fields, models
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from num2words import num2words
from datetime import datetime



class SecuenciaMes(models.Model):
    _inherit = 'sale.order'

    mes_secuencia = fields.Char(
        string="Secuencia por Mes",
        compute='_compute_mes_secuencia',
        store=True
    )

    def number_to_word(self, number: float):
        decimal_part = int(round(number % 1, 2) * 100)
        integer_part = int(number)
        # obtener el idioma actual
        lang = self.env.context.get('lang', 'es_ES')
        return f"{num2words(integer_part, lang=lang)} con {decimal_part}/100 {self.currency_id.symbol}"

    def amount_to_text(self, amount):
        # Usar num2words para convertir el monto en número a texto
        return num2words(amount, lang='es')
    @api.depends('date_order')
    def _compute_mes_secuencia(self):
        for record in self:
            if record.date_order:
                # Convertir a fecha para evitar errores por hora
                fecha = record.date_order.date()
                mes = fecha.strftime('%m')
                start_of_month = fecha.replace(day=1)
                end_of_month = (start_of_month + relativedelta(months=1))

                domain = [
                    ('date_order', '>=', datetime.combine(start_of_month, datetime.min.time())),
                    ('date_order', '<', datetime.combine(end_of_month, datetime.min.time())),
                ]
                if record.id:
                    domain.append(('id', '!=', record.id))

                count = self.env['sale.order'].search_count(domain) + 1
                secuencia = f"{count:05d}"
                record.mes_secuencia = f"-{mes}-{secuencia}"
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