# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Crm_Project(models.Model):
    _inherit = 'crm.lead'

    project_id = fields.Many2one(comodel_name='project.project', string='Project New', tracking=True)
    project_new = fields.Integer(related='project_id.id')
    project_count = fields.Integer(compute='_compute_project_data', string="Number of Projects")
    project_ids = fields.One2many('project.project', 'lead_opportunity_id', string='Projects')
    
    def action_view_project_created(self):
        return self.env['project.project'].browse(self._context.get('id',[]))

    @api.depends('project_ids.lead_opportunity_id')
    def _compute_project_data(self):
        for rec in self:
            project_cnt = 0
            for proj in rec.project_ids:
                project_cnt += 1
                    
            rec.project_count = project_cnt

    def action_view_project(self):
        action = self.env["ir.actions.act_window"]._for_xml_id("exe_convert_to_proyect.project_action_kanban_view")
        action['domain'] = [('lead_opportunity_id', '=', self.id)]
        return action


class Project_Crm(models.Model):
    _inherit = 'project.project'

    lead_opportunity_id = fields.Many2one('crm.lead', 'Opportunity')

