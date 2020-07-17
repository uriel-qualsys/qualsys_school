import logging
_logger = logging.getLogger(__name__)

from odoo import models, fields, api

class QualsysCourses(models.Model):
    _name = 'qualsys.courses'
    _description = 'Cursos Escuela'

    @api.depends('attendees_ids')
    def get_attendees_number(self):
        for data in self:
            data.attendees_number = len(data.attendees_ids)

    name = fields.Char(string="Curso", required=True)
    code = fields.Char(string="Codigo", required=True)
    duration = fields.Integer(string="Duración", required=True)
    start_date = fields.Date(string="Fecha de Inicio", required=True)
    end_date = fields.Date(string="Fecha de Termino", required=True)
    school_id = fields.Many2one('qualsys.school', string="Escuela")
    teacher_id = fields.Many2one('res.users', string="Profesor")
    attendees_ids = fields.One2many('qualsys.attendees', 'courses_id', string = "Asistentes", required=True)
    attendees_number = fields.Integer(compute=get_attendees_number, string="Cantidad de Asistentes")


    
    
    
