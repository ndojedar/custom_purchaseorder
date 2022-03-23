# -*- coding: utf-8 -*-

from odoo import models, fields, _


class CustomPurchaseOrder(models.Model):
    _inherit = "purchase.order"

    datos_entrega = fields.Many2one(
        comodel_name='res.partner', 
        string='Dirección de Entrega'
    )

    produccion_estimada = fields.Monetary(
        string='Producción estimada', 
        compute='_calc_produccion_estimada', 
        store=True, 
        readonly=True
    )

    pva_estimado = fields.Monetary(
        string='Producción VA estimada', 
        compute='_calc_pva_estimado', 
        store=True, 
        readonly=True
    )


    def _calc_produccion_estimada(self):
        for rec in self:
            val = 0.0
            vforecast = self.env['project.task'].search([('id', '=', rec.forecast_id.id)])
            rec.produccion_estimada = rec.amount_untaxed * 1.5 * vforecast.sales_factor if vforecast else val


    def _calc_pva_estimado(self):
        for rec in self:
            val = 0.0
            if rec.forecast_id:
                if rec.produccion_estimada and rec.produccion_estimada > 0:
                    rec.pva_estimado = rec.produccion_estimada - rec.amount_untaxed
                else:
                    rec.pva_estimado = val - rec.amount_untaxed
            else:
                rec.pva_estimado = val



