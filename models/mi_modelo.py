#models/mi_modelo.py
from odoo import models, fields

class MiModulo(models.Model):
    _name = 'mi_modulo'
    _description = 'Mi modulo de prueba'
    
    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción')
    