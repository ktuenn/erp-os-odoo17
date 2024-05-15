# -*- coding: utf-8 -*-
# from odoo import http


# class E:\download\odoo17\server\custom(http.Controller):
#     @http.route('/e:\download\odoo17\server\custom/e:\download\odoo17\server\custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/e:\download\odoo17\server\custom/e:\download\odoo17\server\custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('e:\download\odoo17\server\custom.listing', {
#             'root': '/e:\download\odoo17\server\custom/e:\download\odoo17\server\custom',
#             'objects': http.request.env['e:\download\odoo17\server\custom.e:\download\odoo17\server\custom'].search([]),
#         })

#     @http.route('/e:\download\odoo17\server\custom/e:\download\odoo17\server\custom/objects/<model("e:\download\odoo17\server\custom.e:\download\odoo17\server\custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('e:\download\odoo17\server\custom.object', {
#             'object': obj
#         })

