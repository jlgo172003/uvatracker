list = [14679, 69883, 69884, 108679, 128454, 140002, 153073, 153451, 69886, 69889, 156740, 164918, 128064, 173885, 187790, 188114, 188550, 153686, 188625, 145723, 176990, 190064,153448]

from uvatracker.models import Person

for i in range(0, len(list)):
    p = Person(uva_id=list[i], username='', name='')
    p.save()
