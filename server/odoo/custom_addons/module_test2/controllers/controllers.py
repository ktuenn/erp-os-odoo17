# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleTest2(http.Controller):
#     @http.route('/module_test2/module_test2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_test2/module_test2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_test2.listing', {
#             'root': '/module_test2/module_test2',
#             'objects': http.request.env['module_test2.module_test2'].search([]),
#         })

#     @http.route('/module_test2/module_test2/objects/<model("module_test2.module_test2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_test2.object', {
#             'object': obj
#         })

