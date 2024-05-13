# -*- coding: utf-8 -*-
# from odoo import http


# class BlanketOrders(http.Controller):
#     @http.route('/blanket_orders/blanket_orders', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/blanket_orders/blanket_orders/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('blanket_orders.listing', {
#             'root': '/blanket_orders/blanket_orders',
#             'objects': http.request.env['blanket_orders.blanket_orders'].search([]),
#         })

#     @http.route('/blanket_orders/blanket_orders/objects/<model("blanket_orders.blanket_orders"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('blanket_orders.object', {
#             'object': obj
#         })

