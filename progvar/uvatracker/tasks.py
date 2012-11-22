from djcelery import celery
from django.core.mail import send_mail, EmailMultiAlternatives


from uvatracker.models import Person

import urllib2
import simplejson

   
@celery.task(name='uvatracker.tasks.update_data')
def update_data():
    persons = Person.objects.all().order_by('total_solved')
    
    for person in persons:
        print person
        req = urllib2.Request( "http://uhunt.felix-halim.net/api/ranklist/"+str(person.uva_id)+"/0/0" , None, {} )
        opener = urllib2.build_opener()
        try:
            f = opener.open(req)
            print( "finished loading json for ", person )
            s = simplejson.load(f)
            
            person.username = s[0]['username']
            person.name = s[0]['name']
            person.total_solved = s[0]['ac']
            person.submissions = s[0]['nos']
            person.save()
            print person.total_solved
        except:
            pass
        
    update_data.delay()
     
