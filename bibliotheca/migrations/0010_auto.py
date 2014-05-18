# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field author_id on 'Books'
        db.delete_table(db.shorten_name('bibliotheca_books_author_id'))

        # Adding M2M table for field authors on 'Books'
        m2m_table_name = db.shorten_name('bibliotheca_books_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('books', models.ForeignKey(orm['bibliotheca.books'], null=False)),
            ('authors', models.ForeignKey(orm['bibliotheca.authors'], null=False))
        ))
        db.create_unique(m2m_table_name, ['books_id', 'authors_id'])


    def backwards(self, orm):
        # Adding M2M table for field author_id on 'Books'
        m2m_table_name = db.shorten_name('bibliotheca_books_author_id')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('books', models.ForeignKey(orm['bibliotheca.books'], null=False)),
            ('authors', models.ForeignKey(orm['bibliotheca.authors'], null=False))
        ))
        db.create_unique(m2m_table_name, ['books_id', 'authors_id'])

        # Removing M2M table for field authors on 'Books'
        db.delete_table(db.shorten_name('bibliotheca_books_authors'))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'related_name': "'user_set'", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'symmetrical': 'False', 'blank': 'True'}),
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
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bibliotheca.Authors']", 'symmetrical': 'False'}),
            'category_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Categories']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_pages': ('django.db.models.fields.IntegerField', [], {}),
            'original_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'published_date': ('django.db.models.fields.DateTimeField', [], {}),
            'publisher_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Publishers']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'address_aptno': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'address_city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address_postcode': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'address_street': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address_strno': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
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
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bibliotheca']