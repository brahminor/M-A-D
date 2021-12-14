# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class account_payment_register(models.TransientModel):
	_inherit = "account.payment.register"

	def action_create_payments(self):
		"""
        -vérifier si on n'a pas ajouté la facture à la liste des factures appartenant à 
        tous les sites, si c'est le cas ou l'ajoute --> cette fonction est utile pour
        les factures payées directement depuis le pos après la validation de la cmd
        pos
        """
		res = super(account_payment_register, self).action_create_payments()
		if self._context.get('active_id'):
			if not self.env['factures.sites'].search([('facture_id', '=', self._context.get('active_id'))]):
				self.env['factures.sites'].create({
					'facture_id': self._context.get('active_id'),
					})
		return res
