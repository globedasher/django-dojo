from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db.models import Count

from ..users.models import User
from .models import Poke

def index(request):
    if not 'id' in request.session:
        messages.error(request, "Please login first.")
        return redirect(reverse('login:index'))
    else:

        p = Poke.objects.annotate(Count('id'))
        print(p.count)
        
        pokes = Poke.objects.filter(
                    poked__id=request.session['id']
                ).exclude(
                    pointy_end_id=request.session['id']
                ).annotate(
                    poking=Count('pointy_end'))

        #print(pokes[0].pointy_end.name)
        try:
            print(pokes[0].poking__count)
        except:
            pass

        all_users = User.objects.exclude(id=request.session['id'])

        poked_total = Poke.objects.annotate(
                    counted_end=Count('poked'))


        context = { 
                'all_users': all_users, 
                'pokes': pokes, 
                'poked_total': poked_total,
                }
        return render(request, 'poke/index.html', context)

def new(request, user_id):
    if not 'id' in request.session:
        messages.error(request, "Please login first.")
        return redirect(reverse('login:index'))
    else:
        pointy_end = User.objects.get(id=request.session['id'])
        poked = User.objects.get(id=user_id)
        Poke.objects.create(poked=poked, pointy_end=pointy_end)
        messages.success(request, "You've poked a user!")
        return redirect(reverse('poke:index'))
