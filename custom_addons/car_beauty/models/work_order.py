from odoo import models, fields

class CarBeautyWorkOrder(models.Model):
    _name = 'car.beauty.work.order'
    _description = '美容工單'

    name = fields.Char('工單編號', required=True)
    customer_id = fields.Many2one('res.partner', string='客戶', required=True)
    date = fields.Date('日期', required=True, default=fields.Date.today)
    state = fields.Selection([
        ('draft', '草稿'),
        ('confirmed', '確認'),
        ('done', '完成'),
        ('cancelled', '取消')
    ], string='狀態', default='draft')
