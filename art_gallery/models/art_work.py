# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ArtWork(models.Model):
    _name = 'art.work'
    _description = 'Art Work'

    name = fields.Char(string='Name')
    artist_id = fields.Many2one(string='Artist', comodel_name='res.partner')
    phone = fields.Char(string='Artist Phone', related='artist_id.phone', readonly=False)
    currator_id = fields.Many2one(string='Currator', comodel_name='res.users')

    length = fields.Float(string='Length')
    width = fields.Float(string='Width')
    
    frame = fields.Selection(string='Frame',
                             selection=[('gold', 'Gold'),
                                        ('black', 'Black'),
                                        ('none', 'None')])
    
    product_ids = fields.Many2many(string='Optional Products', comodel_name='product.product')
    
    finished_date = fields.Date(string='Finished Date')
    
    art_image = fields.Image(string='Art Image')