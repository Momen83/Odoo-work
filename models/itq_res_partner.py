from odoo import api,models,fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    total_contracts_price = fields.Float(string="Total Contracts Price", compute='_compute_total_contracts_price')
    customer_contract_ids = fields.One2many(comodel_name="itq.customer", inverse_name="customer",
                                            string="Customer Contracts")

    @api.depends('customer_contract_ids.price', 'customer_contract_ids.status')
    def _compute_total_contracts_price(self):
        for partner in self:
            confirmed_contracts = partner.customer_contract_ids.filtered(lambda c: c.status == 'confirmed')
            partner.total_contracts_price = sum(confirmed_contracts.mapped('price'))