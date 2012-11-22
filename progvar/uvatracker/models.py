from django.db import models
import datetime
# Create your models here.

class Person(models.Model):
    uva_id = models.PositiveIntegerField()
    #overall_rank = models.PositiveIntegerField()
    username = models.CharField( max_length=255 )
    name = models.CharField( max_length=255 )
    initial_solved = models.IntegerField( default=0 )
    total_solved = models.IntegerField(default=0)
    last_updated = models.DateTimeField( auto_now_add=True )
    submissions = models.IntegerField(default=0)
    checkpoint = models.IntegerField( default=0)
    
    def __unicode__(self):
        return self.name+"/"+self.username
        
    def get_last_update(self):
        return self.last_updated.strftime("%m/%d/%Y")
        
    def accuracy(self):
        val = 10000* float(self.total_solved)/self.submissions
        val = int(val)
        
        return float(val)/100
        
    def getProgress(self):
        return self.total_solved-self.checkpoint
        
    def save( self, *args, **kwargs):
        if self.pk == None:
            pass
        else:
            dayToday = datetime.datetime.now().strftime("%A")
            dayLastUpdate = self.last_updated.strftime("%A")
            diff = datetime.datetime.now()-self.last_updated.replace(tzinfo=None)
            if dayLastUpdate == 'Saturday':
                if diff.days >= 7:
                    delta = self.total_solved - self.checkpoint
                    report = Report( person=self, before=self.checkpoint, after=self.total_solved)
                    report.save()
                    self.checkpoint = self.total_solved
                self.last_updated = datetime.datetime.now()
                    
            else:
                self.checkpoint = self.total_solved
                self.last_updated = datetime.datetime.now() 
        return super(Person, self).save(*args, **kwargs)
                
class Report( models.Model ):
    person = models.ForeignKey(Person)
    before = models.IntegerField(default=0)
    after = models.IntegerField(default=0)
