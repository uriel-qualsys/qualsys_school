import logging
_logger = logging.getLogger(__name__)

from odoo import models, api, fields

class QualsysAssignSchool(models.TransientModel):
    _name = 'qualsys.assign.school'
    _description = 'Asignación de Escuela a Curso'
    school_id = fields.Many2one('qualsys.school', string="Escuela")
    
    def assign_school(self):
        course = dict(self._context or {})
        courses = self.env['qualsys.courses'].browse(course.get('active_ids'))
        courses.write({'school_id':self.school_id.id})
        pass

