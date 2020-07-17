import logging
_logger = logging.getLogger(__name__)

from odoo import models, fields, api


class QualsysSchool(models.Model):
    _name = 'qualsys.school'
    _description = 'Escuela de Prueba'

    @api.depends('courses_ids')
    def get_courses_number(self):
        for data in self:
            data.courses_number = len(data.courses_ids)
    
    name = fields.Char(string = "Escuela", required=True)
    street  = fields.Char(string = "Calle")
    street_number  = fields.Char(string = "No Exterior", size=10)
    city  = fields.Char(string = "Ciudad", required=True)
    phone_one  = fields.Char(string = "Teléfono Principal", size=13, required= True)
    phone_two  = fields.Char(string = "Teléfono Secundario", size=13)
    email  = fields.Char(string = "Correo Electrónico")
    country = fields.Many2one('res.country', string = "Pais")
    state = fields.Many2one('res.country.state', string = "Estado")
    courses_ids = fields.One2many('qualsys.courses', 'school_id', string = "Curso", required=True)
    courses_number  = fields.Integer(compute= get_courses_number, string="Cantidad de Cursos")




