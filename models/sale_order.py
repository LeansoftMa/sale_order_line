# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, _

class SaleOrderLine(models.Model):   
    _inherit = "sale.order.line"
    
    order_ref = fields.Char('Order Reference',related='order_id.name')   
    customer_id = fields.Many2one('res.partner',related='order_id.partner_id')
    date_order = fields.Date('Date',related='order_id.date_order')
    commitment_date = fields.Date('Date livraison',related='order_id.commitment_date')
    partner_shipping_id = fields.Many2one('res.partner',related='order_id.partner_shipping_id')


