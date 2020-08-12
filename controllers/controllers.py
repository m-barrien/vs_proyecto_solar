# -*- coding: utf-8 -*-
# from odoo import http


# class VsProyectoSolar(http.Controller):
#     @http.route('/vs_proyecto_solar/vs_proyecto_solar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vs_proyecto_solar/vs_proyecto_solar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vs_proyecto_solar.listing', {
#             'root': '/vs_proyecto_solar/vs_proyecto_solar',
#             'objects': http.request.env['vs_proyecto_solar.vs_proyecto_solar'].search([]),
#         })

#     @http.route('/vs_proyecto_solar/vs_proyecto_solar/objects/<model("vs_proyecto_solar.vs_proyecto_solar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vs_proyecto_solar.object', {
#             'object': obj
#         })
