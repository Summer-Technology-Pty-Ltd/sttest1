# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_limit = fields.Integer(string="Credit Limit")
    is_over_credit = fields.Boolean(Stirng="Over Credit")
    act_cl_exceeded = fields.Selection([('do_nothing', 'Do Nothing'),
                                        ('warn', 'Warn'),
                                        ('put_on_hold', 'Put on hold')],
                                       string="Action when credit limit is exceeded")


    @api.onchange('credit_limit', 'credit')
    def _onchange_credit(self):
        if self.credit_limit > self.credit:
            self.is_over_credit = True
        else:
            self.is_over_credit = False

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def partner_id_warning_message(self):
        if self.partner_id and self.partner_id.is_over_credit:
            act_cl_exceeded = self.partner_id.act_cl_exceeded
            if act_cl_exceeded == 'warn':
                return {'warning': {'title': _("Warning"), 'message': 'Warning this customer exceeded his credit limit!'}}
            if act_cl_exceeded == 'put_on_hold':
                self.partner_id = False
                return {
                    'warning': {'title': _("Warning"), 'message': 'This customer is on hold!'}}


