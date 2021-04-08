# -*- coding: utf-8 -*-
from odoo import http

# class ConversionCost(http.Controller):
#     @http.route('/conversion_cost/conversion_cost/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/conversion_cost/conversion_cost/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('conversion_cost.listing', {
#             'root': '/conversion_cost/conversion_cost',
#             'objects': http.request.env['conversion_cost.conversion_cost'].search([]),
#         })

#     @http.route('/conversion_cost/conversion_cost/objects/<model("conversion_cost.conversion_cost"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('conversion_cost.object', {
#             'object': obj
#         })