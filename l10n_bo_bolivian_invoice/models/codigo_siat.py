from odoo import _, api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_siat_service(self, move):
        if move.invoice_line_ids:
            first_product = move.invoice_line_ids[0].product_id
            return first_product.siat_service_id.name if first_product.siat_service_id else ''
        return ''