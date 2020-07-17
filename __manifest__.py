# -*- coding: utf-8 -*-
{
    'name': "Escuela Qualsys",
    'summary': "Modulo de Capacitación en el Curso de Inducción Qualsys",
    'description': "El modulo tiene como objetivo la gestión de cursos de una escuela con varias sedes y los cursos que se imparten en ella.",
    'author': "J. Uriel Ochoa Barreto",
    'version': '0.1',
    'depends': ['base'],
    
    'data': [
        'views/qualsys_school_views.xml',
        'views/qualsys_courses_views.xml',
        'views/qualsys_attendees_views.xml',
        'security/ir.model.access.csv',
    ],

    'demo': [
    ],
}