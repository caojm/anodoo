# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KarmaRank(models.Model):
    _inherit = 'gamification.karma.rank'
     
    category = fields.Selection(selection_add=[('elearn', '在线学习')])
