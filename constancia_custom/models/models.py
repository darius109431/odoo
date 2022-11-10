from odoo import _, api, fields, models, tools
import base64

class SurveySurvey(models.Model):

    _inherit = 'survey.survey'

    head_text = fields.Char('Titulo de Documento', required=True, default='CONSTANCIA')
    subhead_text = fields.Char('Subtitulo de Documento', required=True, default='DE PARTICIPACION')
    # signature = fields.Binary(string='Firma')

class SurveyUserinput(models.AbstractModel):

    _inherit = 'survey.user_input'

    def process_pdf_cert(self):
        pdf = self.env.ref('survey.certification_report').sudo()._render_qweb_pdf(self.ids)
        b64_pdf = base64.b64encode(pdf[0])
        name = "Certificado_%s" % rec.partner_id.name
        return b64_pdf