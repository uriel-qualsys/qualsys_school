#attendees
import logging
_logger = logging.getLogger(__name__)

from odoo import models, fields, api

class QualsysAttendees(models.Model):
    _name = 'qualsys.attendees'
    _description = 'Asistentes al Curso'
    
    @api.depends('partner_id')
    def get_partner_name(self):
        self.name = self.partner_id.name

    name = fields.Char(compute=get_partner_name, string="Alumno", required=True)
    partner_id = fields.Many2one('res.partner', string="Asistente")
    age = fields.Integer(string="Edad", required=True)
    courses_id = fields.Many2one('qualsys.courses', string="Curso")





