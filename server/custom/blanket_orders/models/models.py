# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class blanket_orders(models.Model):
#     _name = 'blanket_orders.blanket_orders'
#     _description = 'blanket_orders.blanket_orders'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from datetime import datetime, time
from odoo import fields, models, api, _

class PurchaseRequisitionLine(models.Model):
    _inherit = "purchase.requisition.line"

    def _prepare_purchase_order_line(self, name, product_qty=0.0, price_unit=0.0, taxes_ids=False):
        self.ensure_one()
        result = super()._prepare_purchase_order_line(name, product_qty=product_qty,price_unit=price_unit, taxes_ids=taxes_ids)
        result['date_planned'] = datetime.combine((self.schedule_date if self.schedule_date else datetime.now()), time.min)
        result['requisition_line_id'] = self.id
        return result


class PurchaseOrderLine(models.Model):
    _inherit='purchase.order.line'

    requisition_line_id = fields.Many2one('purchase.requisition.line', string='Purchase Agreement Line') 
    
    

class PurchaseOrder(models.Model):
    _inherit='purchase.order'
    
    @api.onchange('date_planned')
    def onchange_date_planned(self):
        if self.date_planned:
            if self.requisition_id:
                for line in self.order_line.filtered(lambda line: not line.display_type):
                    line.update({
                        'date_planned' : datetime.combine(line.requisition_line_id.schedule_date 
                        if line.requisition_line_id.schedule_date else datetime.now(), time.min),
                    })
            else:
                self.order_line.filtered(lambda line: not line.display_type).date_planned = self.date_planned