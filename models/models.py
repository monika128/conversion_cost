# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit ='product.template'

    value_inr = fields.Monetary(string="Cost in INR",track_visibility=True)

class ProductProduct(models.Model):
    _inherit ='product.product'

    value_inr = fields.Monetary(string="Cost in INR",track_visibility=True)

class PurchaseOrderLine(models.Model):
    _inherit ='purchase.order.line'

    value_usd = fields.Monetary(string="Cost in USD")

class PurchaseOrder(models.Model):
    _inherit ='purchase.order'
    
    def button_confirm(self):
        
        for rec in self.order_line:
            rec.product_id.value_inr = rec.value_usd * 75
        return super(PurchaseOrder, self).button_confirm()
        

        
        