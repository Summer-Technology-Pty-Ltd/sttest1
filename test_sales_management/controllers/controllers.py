# -*- coding: utf-8 -*-
# from odoo import http


# class TestSalesManagement(http.Controller):
#     @http.route('/test_sales_management/test_sales_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_sales_management/test_sales_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_sales_management.listing', {
#             'root': '/test_sales_management/test_sales_management',
#             'objects': http.request.env['test_sales_management.test_sales_management'].search([]),
#         })

#     @http.route('/test_sales_management/test_sales_management/objects/<model("test_sales_management.test_sales_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_sales_management.object', {
#             'object': obj
#         })
