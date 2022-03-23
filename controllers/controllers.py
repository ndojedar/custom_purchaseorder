# -*- coding: utf-8 -*-
# from odoo import http


# class CustomPurchaseorder(http.Controller):
#     @http.route('/custom_purchaseorder/custom_purchaseorder/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_purchaseorder/custom_purchaseorder/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_purchaseorder.listing', {
#             'root': '/custom_purchaseorder/custom_purchaseorder',
#             'objects': http.request.env['custom_purchaseorder.custom_purchaseorder'].search([]),
#         })

#     @http.route('/custom_purchaseorder/custom_purchaseorder/objects/<model("custom_purchaseorder.custom_purchaseorder"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_purchaseorder.object', {
#             'object': obj
#         })
