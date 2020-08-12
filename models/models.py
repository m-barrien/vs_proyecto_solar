# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class vs_proyecto_solar(models.Model):
#     _name = 'vs_proyecto_solar.vs_proyecto_solar'
#     _description = 'vs_proyecto_solar.vs_proyecto_solar'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
