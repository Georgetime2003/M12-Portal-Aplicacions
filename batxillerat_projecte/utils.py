from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required
from .decorators import professor_encarregat
from .models import Solicitud

# Impresora per generar un pdf amb el llistat d'alumnes i seminari assignat
@login_required
@professor_encarregat
def render_pdf_view(request):
    template_path = 'batx_seminaris/exportar_pdf.html'
    llistaSolicituds =  Solicitud.objects.filter(assignat=True)
    context = {'llistaSolicituds': llistaSolicituds}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="llistaAssignacioProjecte.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('Error amb la impressora pdf <pre>' + html + '</pre>')
    return response