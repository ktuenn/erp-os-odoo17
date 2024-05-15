# -*- coding: utf-8 -*-
# from odoo import http


# class Po-report(http.Controller):
#     @http.route('/po-report/po-report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/po-report/po-report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('po-report.listing', {
#             'root': '/po-report/po-report',
#             'objects': http.request.env['po-report.po-report'].search([]),
#         })

#     @http.route('/po-report/po-report/objects/<model("po-report.po-report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('po-report.object', {
#             'object': obj
#         })

