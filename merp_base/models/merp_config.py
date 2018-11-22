from odoo import models, fields, api


class merpConfig(models.Model):
    _name = 'merp.config'
    _rec_name = 'key'

    key = fields.Char(required=True, index=True)
    value = fields.Text(required=True)

    _sql_constraints = [
        ('key_uniq', 'unique (key)', 'Key must be unique.')
    ]

    @api.model
    def get_param(self, key, default=False):
        params = self.search_read([('key', '=', key)], fields=['value'], limit=1)
        return params[0]['value'] if params else default

    @api.model
    def set_param(self, key, value):
        param = self.search([('key', '=', key)])

        vals = {'value': value}
        if param:
            if value is not False and value is not None:
                param.write(vals)
            else:
                param.unlink()
        else:
            if value is not False and value is not None:
                vals.update(key=key)
                self.create(vals)

        return False
