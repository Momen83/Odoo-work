from odoo import api,models,fields


class CustomerContract(models.Model):
    _name = 'itq.customer'

    customer = fields.Many2one(comodel_name="res.partner", string="Customer", required=True)
    start_date = fields.Date(string="Starting Date")
    end_date = fields.Date(string="End Date")
    price = fields.Float(string="Price")
    average_day_price = fields.Float(string = "Average Day Price" , compute='_compute_average_day_price')
    last_user_change_status = fields.Many2one(comodel_name='res.users', string="Last User Change Status"
                                              , compute = '_compute_last_user_change_status' ,
                                               store = True
                                              )
    status = fields.Selection(
         [
             ('draft',"Draft"),
             ('confirmed',"Confirmed"),
             ('ended',"Ended"),
             ("cancelled","Cancelled")
         ]
         , default='draft',required=True
     )

    def write(self, vals):

        if vals.get('status',False):

            for record in self:
                record.last_user_change_status = self.env.user.id

        result = super(CustomerContract, self).write(vals)

        return result

    @api.onchange('start_date')
    def _onchange_start_date(self):
        if self.start_date:
            self.end_date = False

   # @api.depends('start_date','end_date')
   # def _compute_number_of_days(self):
   #     for record in self:
   #         if record.start_date and record.end_date:
   #             date_difference = record.end_date - record.start_date
   #             record.number_of_days = date_difference.days + 1
   #         else:
    #            record.number_of_days = 0



    @api.depends('price','start_date','end_date')
    def _compute_average_day_price(self):
        for record in self:
            number_of_days = 0
            if record.start_date and record.end_date:
                date_difference = record.end_date - record.start_date
                number_of_days = date_difference.days + 1

            if number_of_days != 0:
                record.average_day_price = record.price / number_of_days
            else:
                record.average_day_price = 0.0

    # @api.depends('status')
    # def _compute_last_user_change_status(self):
    #     for record in self:
    #         if record.status:
    #             record.last_user_change_status = self.env.user.id
