from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse

from django.template.loader import get_template

from xhtml2pdf import pisa
# Create your views here.

def about(request):
    return render(request, 'About us.html')

def contact(request):
    return render(request, 'Contact us.html')

def home(request):
    return render(request, 'index.html')

def create(request):
    return render(request, 'form.html')

def testing(request):
    if request.method == 'POST':
        details = {
            'name' : request.POST.get('name'),
            'email' : request.POST.get('email'),
            'phone' : request.POST.get('phone'),
            'designation' : request.POST.get('designation'),
            'github' : request.POST.get('github'),
            'linkedin' : request.POST.get('linkedin'),
            'summary' : request.POST.get('summary'),
            'schoolname' : request.POST.get('schoolname'),
            'schoolperc' : request.POST.get('schoolperc'),
            'schoolyop' : request.POST.get('schoolyop'),
            'collegename' : request.POST.get('collegename'),
            'collegeperc' : request.POST.get('collegeperc'),
            'collegeyop' : request.POST.get('collegeyop'),
            'ugname' : request.POST.get('ugname'),
            'course' : request.POST.get('course'),
            'special' : request.POST.get('special'),
            'ugperc' : request.POST.get('ugperc'),
            'ugyop' : request.POST.get('ugyop'),
            'pgname' : request.POST.get('pgname'),
            'pgcourse' : request.POST.get('pgcourse'),
            'pgspecial' : request.POST.get('pgspecial'),
            'pgperc' : request.POST.get('pgperc'),
            'pgyop' : request.POST.get('pgyop'),
            'pjtitle1' : request.POST.get('pjtitle1'),
            'pjsummary1' : request.POST.get('pjsummary1'),
            'pjlink1' : request.POST.get('pjlink1'),
            'pjtitle2' : request.POST.get('pjtitle2'),
            'pjsummary2' : request.POST.get('pjsummary2'),
            'pjlink2' : request.POST.get('pjlink2'),
            'pjtitle3' : request.POST.get('pjtitle3'),
            'pjsummary3' : request.POST.get('pjsummary3'),
            'pjlink3' : request.POST.get('pjlink3'),
            'cftitle1' : request.POST.get('cftitle1'),
            'cflink1' : request.POST.get('cflink1'),
            'cftitle2' : request.POST.get('cftitle2'),
            'cflink2' : request.POST.get('cflink2'),
            'cftitle3' : request.POST.get('cftitle3'),
            'cflink3' : request.POST.get('cflink3'),
            'skillno1' : request.POST.get('skillno1'),
            'skillno2' : request.POST.get('skillno2'),
            'skillno3' : request.POST.get('skillno3'),
            'skillno4' : request.POST.get('skillno4'),
            'hobby1' : request.POST.get('hobby1'),
            'hobby2' : request.POST.get('hobby2'),
            'hobby3' : request.POST.get('hobby3'),
        }
        # return render(request, 'resume.html',{
        #     "details" : details
        # }) 




    template_path = 'resume.html'

    response = HttpResponse(content_type='application/pdf')
    context = {'details' : details}

    response['Content-Disposition'] = 'filename="testing.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response