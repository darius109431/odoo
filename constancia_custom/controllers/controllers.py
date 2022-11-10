# -*- coding: utf-8 -*-
from odoo import http


class ConstanciaCustom(http.Controller):
    @http.route('/constancias/verify', auth='public', website=True)
    def verify(self, **kwargs):
        if kwargs['access_token']:
            constancia = http.request.env['survey.user_input'].sudo().search([('access_token','=',kwargs['access_token'])])
            if constancia:
                return http.request.render('constancia_custom.verificar_ok',{'constancia': constancia})
        else:
            return 'Debe especificar un token'
    
    @http.route('/constancias/print', auth='user', website=True)
    def print_cert(self, **kwargs):
        if kwargs['id'] and kwargs['access_token']:

            r = http.request.env.ref('survey.certification_report').sudo()

            pdf = r.sudo()._render_qweb_pdf([int(kwargs['id'])])[0]
            pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', len(pdf))]
            return http.request.make_response(pdf, headers=pdfhttpheaders)

#     @http.route('/constancia_custom/constancia_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('constancia_custom.listing', {
#             'root': '/constancia_custom/constancia_custom',
#             'objects': http.request.env['constancia_custom.constancia_custom'].search([]),
#         })

#     @http.route('/constancia_custom/constancia_custom/objects/<model("constancia_custom.constancia_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('constancia_custom.object', {
#             'object': obj
#         })
