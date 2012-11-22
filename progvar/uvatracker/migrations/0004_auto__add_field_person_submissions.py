# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.submissions'
        db.add_column('uvatracker_person', 'submissions',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Person.submissions'
        db.delete_column('uvatracker_person', 'submissions')


    models = {
        'uvatracker.person': {
            'Meta': {'object_name': 'Person'},
            'checkpoint': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_solved': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'submissions': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_solved': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uva_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'uvatracker.report': {
            'Meta': {'object_name': 'Report'},
            'after': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'before': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['uvatracker.Person']"})
        }
    }

    complete_apps = ['uvatracker']