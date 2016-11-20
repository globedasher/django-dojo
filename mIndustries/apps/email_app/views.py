from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Email

def index(request):
    all_emails = Email.objects.all()
    context = { 'all_emails': all_emails }
    return render(request, "email_app/index.html", context)

def submit(request):

    # The following Tuple will have a Boolean at index 0 to indicate if the
    # email_address given is valid. Index 1 will either contain an error
    # message as a string or an email object.
    tuple_return = Email.objects.register(request.POST['email_address'])

    #print(request.POST['email_address'])
    print(tuple_return)

    if tuple_return[0] == True:

        print(tuple_return[1].id)
        messages.success(request, "The email address you entered " 
                + str(tuple_return[1].email_address) 
                + " is a VALID email address! Thank you !")

        all_emails = Email.objects.all()
        context = { 'email': tuple_return[1], 'all_emails': all_emails }
        return render(request, "email_app/success.html", context)

    if tuple_return[0] == False:
        messages.error(request, "Email incorrect")
        return redirect(reverse('email:index'))
