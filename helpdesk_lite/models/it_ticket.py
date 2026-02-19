from odoo import models, fields, api, _
from datetime import timedelta
from odoo.exceptions import ValidationError


class ItTicket(models.Model):
    _name = 'it.ticket'
    _description = 'Ticket de IT'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Característica Intermedia 1: Chatter

    name = fields.Char(string='Referencia', required=True, copy=False, readonly=True, default=lambda self: _('Nuevo'))
    description = fields.Html(string='Descripción')

    # Relacionales
    equipment_id = fields.Many2one('maintenance.equipment', string='Equipo Afectado')
    user_id = fields.Many2one('res.users', string='Asignado a', default=lambda self: self.env.user)
    stage_id = fields.Many2one('it.ticket.stage', string='Etapa', group_expand='_read_group_stage_ids', tracking=True)

    priority = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta'),
        ('3', 'Crítica'),
    ], string='Prioridad', default='1')

    # Campos de tiempo
    sla_hours = fields.Float(string='Horas SLA', default=24.0)
    deadline = fields.Datetime(string='Fecha Límite', compute='_compute_deadline', store=True)
    is_overdue = fields.Boolean(string='Vencido', compute='_compute_is_overdue')

    # Campo Computado + @api.depends
    @api.depends('create_date', 'sla_hours')
    def _compute_deadline(self):
        for ticket in self:
            if ticket.create_date and ticket.sla_hours:
                ticket.deadline = ticket.create_date + timedelta(hours=ticket.sla_hours)
            else:
                ticket.deadline = False

    # Campo Computado (sin store, dinámico)
    def _compute_is_overdue(self):
        now = fields.Datetime.now()
        for ticket in self:
            ticket.is_overdue = ticket.deadline and ticket.deadline < now

    # Secuencia (Sobreescribir create)
    @api.model
    def create(self, vals):
        if vals.get('name', _('Nuevo')) == _('Nuevo'):
            vals['name'] = self.env['ir.sequence'].next_by_code('it.ticket') or _('Nuevo')
        return super(ItTicket, self).create(vals)

    # Constraint SQL o Python
    @api.constrains('stage_id')
    def _check_close_comment(self):
        for ticket in self:
            if ticket.stage_id.is_closed and not ticket.description:
                raise ValidationError("No puedes cerrar un ticket sin una descripción/solución.")

    # Acciones de Botones
    def action_assign_me(self):
        self.user_id = self.env.user

    # Hack para que el kanban muestre todas las columnas
    @api.model
    def _read_group_stage_ids(self, stages, domain, order=None, **kwargs):  # <--- AÑADE 'order' AQUÍ
        search_order = order or 'sequence,id'
        return stages.search([], order=search_order)

    @api.model
    def check_overdue_tickets(self):
        # Buscar tickets abiertos y vencidos
        overdue_tickets = self.search([
            ('is_overdue', '=', True),
            ('stage_id.is_closed', '=', False)
        ])
        for ticket in overdue_tickets:
            # Crear una actividad para avisar al usuario
            ticket.activity_schedule(
                'mail.mail_activity_data_todo',
                user_id=ticket.user_id.id,
                note='Este ticket ha vencido. Por favor revísalo.'
            )