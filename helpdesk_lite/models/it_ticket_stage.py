from odoo import models, fields

class ItTicketStage(models.Model):
    _name = 'it.ticket.stage'
    _description = 'Etapas de Incidencia'
    _order = 'sequence, id'

    name = fields.Char('Nombre', required=True)
    sequence = fields.Integer('Secuencia', default=10)
    fold = fields.Boolean('Plegado en Kanban')
    is_closed = fields.Boolean('Etapa de cierre') # Para saber si está resuelto