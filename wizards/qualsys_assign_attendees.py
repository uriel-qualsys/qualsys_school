import logging
_logger = logging.getLogger(__name__)

from odoo import models, api, fields

class QualsysAssignCourse(models.TransientModel):
    _name = 'qualsys.assign.course'
    _description = "Asigna uno o mas cursos a un estudiante"

    courses_id = fields.Many2one('qualsys.courses', string="Curso")

    def assign_course(self):
        pass
