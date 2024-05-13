# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class module_test2(models.Model):
#     _name = 'module_test2.module_test2'
#     _description = 'module_test2.module_test2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

