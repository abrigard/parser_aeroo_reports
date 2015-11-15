from openerp.report import report_sxw
from openerp.report.report_sxw import rml_parse

class Parser(rml_parse):
    def __init__(self, cr, uid, name, context):
        super(self.__class__, self).__init__(cr, uid, name, context)

        # extra code to be able to user <for></for> and proces more than one row per page
        
        model = self.pool.get(context['active_model'])
        ids = context['active_ids']
        rows = model.browse(cr, uid, ids, context=context)
        self.localcontext.update({
            'rows': rows
        }) 
