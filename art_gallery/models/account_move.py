# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'
    
    art_work_id = fields.Many2one(comodel_name='art.work', string='Art Work')
