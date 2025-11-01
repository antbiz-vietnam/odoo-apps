# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class TelegramDescriptionController(http.Controller):
    @http.route('/telegram_description', auth='user')
    def telegram_description(self):
        return request.render('telegram_chat_integration.telegram_description_template')

