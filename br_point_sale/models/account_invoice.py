# -*- coding: utf-8 -*-
# © 2016 Danimar Ribeiro <danimaribeiro@gmail.com>, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models
from .account_journal import metodos


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    metodo_pagamento = fields.Selection(metodos, string=u'Método de Pagamento')
    
    def _prepare_edoc_vals(self, inv):
        
        res = super(AccountInvoice, self)._prepare_edoc_vals(inv)
        res['metodo_pagamento'] = inv.metodo_pagamento
        
        return res