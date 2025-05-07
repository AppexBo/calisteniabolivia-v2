from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_siat_service(self):
        self.ensure_one()  # Para evitar procesar múltiples movimientos a la vez
        if self.invoice_line_ids:
            first_product = self.invoice_line_ids[0].product_id
            return first_product.siat_service_id.codigoActividad if first_product.siat_service_id else ''
        return 'No funciona'
