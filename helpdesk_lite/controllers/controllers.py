# -*- coding: utf-8 -*-
# from odoo import http


# class HelpdeskLite(http.Controller):
#     @http.route('/helpdesk_lite/helpdesk_lite', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/helpdesk_lite/helpdesk_lite/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('helpdesk_lite.listing', {
#             'root': '/helpdesk_lite/helpdesk_lite',
#             'objects': http.request.env['helpdesk_lite.helpdesk_lite'].search([]),
#         })

#     @http.route('/helpdesk_lite/helpdesk_lite/objects/<model("helpdesk_lite.helpdesk_lite"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('helpdesk_lite.object', {
#             'object': obj
#         })

