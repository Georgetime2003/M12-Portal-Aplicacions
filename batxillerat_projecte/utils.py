from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required,permission_required
from .models import Solicitud

# vista per generar un pdf amb el llistat d'alumnes i seminari assignat
@login_required
@permission_required('batx_seminaris.gestio_professor',raise_exception=True)
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
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response