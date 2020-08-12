# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProyectoSolar(models.Model):
	_name = 'vs.proyectosolar'
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_description = 'Tabla Proyectos Solares'

	partner_id = fields.Many2one('res.partner', string="Cliente")
	name = fields.Char(string="Nombre de Proyecto", required=True)
	descripcion = fields.Text(string="Descripcion & Notas")
	kilowatts_num = fields.Float(string="kWp Efectivos")
	tipo_fv = fields.Selection([
		("ongrid", "ONGRID"),
		("offgrid", "OFFGRID")
	], string="Tipo PY Fotovoltaico", default="")
	fase_te4 = fields.Selection([
		("0" , "0. Sin iniciar"),
		("1" , "1.1 Solicitud de Informacion"),
		("1.2" , "1.2 Respuesta Solicitud de Informacion"),
		("2" , "2.1. Solicitud de Conexion"),
		("2.2" , "2.2 Respuesta Solicitud de Conexion"),
		("3" , "3.1 Manifestacion de Conformidad"),
		("3.2" , "3.2 Respuesta Manifestacion de Conformidad"),
		("4" , "4.1 Solicitud de Conexion"),
		("4.2" , "4.2 Respuesta a Solicitud de Conexion"),
		("5" , "5. TE4 Publicado"),
		("6" , "6. Cliente con Netbilling"),
		("autoconsumo" , "0. Solo Autoconsumo")
	], string="Fase TE4", default="0")
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
