# -*- coding: utf-8 -*-


from ast import literal_eval
from collections import OrderedDict
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, MissingError
from odoo.osv import expression
from lxml import etree, html
import logging
from random import randint
from odoo.addons.website.models.website_snippet_filter import WebsiteSnippetFilter

class DevqueWebsiteFilters(WebsiteSnippetFilter):
    _inherit = 'website.snippet.filter'

    def _render(self, template_key, limit, search_domain=None, with_sample=False, **custom_template_data):
        """Renders the website dynamic snippet items"""
        self.ensure_one()
        assert '.dynamic_filter_template_' in template_key, _("You can only use template prefixed by dynamic_filter_template_ ")
        if search_domain is None:
            search_domain = []

        if self.website_id and self.env['website'].get_current_website() != self.website_id:
            return ''

        if self.model_name.replace('.', '_') not in template_key:
            return ''

        records = self._prepare_values(limit=limit, search_domain=search_domain)

        is_sample = with_sample and not records
        if is_sample:
            records = self._prepare_sample(limit)
        content = self.env['ir.qweb'].with_context(inherit_branding=False)._render(template_key, dict(
            records=records,
            is_sample=is_sample,
            **custom_template_data,
        ))
        return [etree.tostring(el, encoding='unicode', method='html') for el in html.fromstring('<root>%s</root>' % str(content)).getchildren()]

