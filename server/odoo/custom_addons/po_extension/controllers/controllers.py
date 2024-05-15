# -*- coding: utf-8 -*-
# from odoo import http


# class PoExtension(http.Controller):
#     @http.route('/po_extension/po_extension', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/po_extension/po_extension/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('po_extension.listing', {
#             'root': '/po_extension/po_extension',
#             'objects': http.request.env['po_extension.po_extension'].search([]),
#         })

#     @http.route('/po_extension/po_extension/objects/<model("po_extension.po_extension"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('po_extension.object', {
#             'object': obj
#         })

