# -*- coding: utf-8 -*-
# from odoo import http


# class PoNoCreateVendor(http.Controller):
#     @http.route('/po_no_create_vendor/po_no_create_vendor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/po_no_create_vendor/po_no_create_vendor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('po_no_create_vendor.listing', {
#             'root': '/po_no_create_vendor/po_no_create_vendor',
#             'objects': http.request.env['po_no_create_vendor.po_no_create_vendor'].search([]),
#         })

#     @http.route('/po_no_create_vendor/po_no_create_vendor/objects/<model("po_no_create_vendor.po_no_create_vendor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('po_no_create_vendor.object', {
#             'object': obj
#         })

