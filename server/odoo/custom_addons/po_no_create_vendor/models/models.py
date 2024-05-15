# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class po_no_create_vendor(models.Model):
#     _name = 'po_no_create_vendor.po_no_create_vendor'
#     _description = 'po_no_create_vendor.po_no_create_vendor'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

