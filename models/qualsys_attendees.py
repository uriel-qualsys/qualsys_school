#attendees
import logging
_logger = logging.getLogger(__name__)

from odoo import models, fields, api

class QualsysAttendees(models.Model):
    _name = 'qualsys.attendees'
    _description = 'Asistentes al Curso'

    partner_id = fields.Many2one('res.partner', string="Asistente")
    age = fields.Integer(string="Edad", required=True)
    courses_id = fields.Many2one('qualsys.courses')





