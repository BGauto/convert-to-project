from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)


class CrmLeadConvert2Project(models.TransientModel):
    _name = "crm.lead.convert2project"
    _description = "Lead convert to Project"

    project_id = fields.Many2one(comodel_name="project.project", string="Project")    

    def convert_to_project_action(self):
        lead_id = self.env['crm.lead'].browse(self._context.get('active_ids',[]))
        project_new = self.env['project.project'].create({'name' : lead_id.name, 'lead_opportunity_id': lead_id.id})
        tasks_to_copy = self.project_id.task_ids

        for task in tasks_to_copy:
            self.env['project.task'].create({'name': task.name, 
                                             'project_id': project_new.id,
                                             'parent_id': task.parent_id.id,
                                             'description':task.description,
                                             'subtask_project_id':task.subtask_project_id})

        lead_id.project_id = project_new.id

        return {
                "type": "ir.actions.act_window",
                "res_model": "project.project",
                "views": [[False, "form"]],
                "res_id": project_new.id,
                "target": "current",
               }