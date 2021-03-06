# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Methods.last_used'
        db.add_column('authentication_methods', 'last_used',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 5, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Methods.last_used'
        db.delete_column('authentication_methods', 'last_used')


    models = {
        'authentication.methods': {
            'Meta': {'object_name': 'Methods'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_used': ('django.db.models.fields.DateTimeField', [], {}),
            'method': ('django.db.models.fields.IntegerField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'step': ('django.db.models.fields.IntegerField', [], {}),
            'token': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authentication.Users']"})
        },
        'authentication.users': {
            'Meta': {'object_name': 'Users'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_access': ('django.db.models.fields.DateTimeField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['authentication']