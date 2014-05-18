# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Readers.login'
        db.delete_column('bibliotheca_readers', 'login')

        # Deleting field 'Readers.password'
        db.delete_column('bibliotheca_readers', 'password')

        # Deleting field 'Readers.is_blocked'
        db.delete_column('bibliotheca_readers', 'is_blocked')

        # Adding field 'Readers.user'
        db.add_column('bibliotheca_readers', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, unique=True, to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Readers.login'
        db.add_column('bibliotheca_readers', 'login',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Readers.password'
        db.add_column('bibliotheca_readers', 'password',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Readers.is_blocked'
        db.add_column('bibliotheca_readers', 'is_blocked',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Readers.user'
        db.delete_column('bibliotheca_readers', 'user_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'bibliotheca.authors': {
            'Meta': {'object_name': 'Authors'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'bibliotheca.books': {
            'ISBN': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Meta': {'object_name': 'Books'},
            'category_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Categories']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_pages': ('django.db.models.fields.IntegerField', [], {}),
            'original_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'published_date': ('django.db.models.fields.DateTimeField', [], {}),
            'publisher_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Publishers']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'bibliotheca.books_authors': {
            'Meta': {'object_name': 'Books_Authors'},
            'author_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Authors']"}),
            'book_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Books']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bibliotheca.books_categories': {
            'Meta': {'object_name': 'Books_Categories'},
            'book_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Books']"}),
            'category_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Categories']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bibliotheca.borrowings': {
            'Meta': {'object_name': 'Borrowings'},
            'book_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Books']"}),
            'date_since': ('django.db.models.fields.DateTimeField', [], {}),
            'date_to': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reader_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Readers']"})
        },
        'bibliotheca.categories': {
            'Meta': {'object_name': 'Categories'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_main_category': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'top_category_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'bibliotheca.news': {
            'Meta': {'object_name': 'News'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'text_body': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'bibliotheca.publishers': {
            'Meta': {'object_name': 'Publishers'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'bibliotheca.readers': {
            'Meta': {'object_name': 'Readers'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        },
        'bibliotheca.reservations': {
            'Meta': {'object_name': 'Reservations'},
            'book_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Books']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reader_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Readers']"}),
            'reservation_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'bibliotheca.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'book_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Books']"}),
            'books_available': ('django.db.models.fields.IntegerField', [], {}),
            'books_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'books_reserved': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'ordering': "('name',)", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bibliotheca']