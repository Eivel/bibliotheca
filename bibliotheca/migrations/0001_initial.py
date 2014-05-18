# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Readers'
        db.create_table('bibliotheca_readers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('login', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_blocked', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('bibliotheca', ['Readers'])

        # Adding model 'Publishers'
        db.create_table('bibliotheca_publishers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('bibliotheca', ['Publishers'])

        # Adding model 'Categories'
        db.create_table('bibliotheca_categories', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('top_category_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('bibliotheca', ['Categories'])

        # Adding model 'Books'
        db.create_table('bibliotheca_books', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publisher_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Publishers'])),
            ('category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Categories'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('original_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ISBN', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('published_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('number_of_pages', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bibliotheca', ['Books'])

        # Adding model 'Borrowings'
        db.create_table('bibliotheca_borrowings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reader_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Readers'])),
            ('book_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Books'])),
            ('date_since', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_to', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('bibliotheca', ['Borrowings'])

        # Adding model 'Authors'
        db.create_table('bibliotheca_authors', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('bibliotheca', ['Authors'])

        # Adding model 'Books_Authors'
        db.create_table('bibliotheca_books_authors', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Authors'])),
            ('book_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Books'])),
        ))
        db.send_create_signal('bibliotheca', ['Books_Authors'])

        # Adding model 'Books_Categories'
        db.create_table('bibliotheca_books_categories', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Categories'])),
            ('book_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Books'])),
        ))
        db.send_create_signal('bibliotheca', ['Books_Categories'])

        # Adding model 'Warehouse'
        db.create_table('bibliotheca_warehouse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Books'])),
            ('books_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('books_available', self.gf('django.db.models.fields.IntegerField')()),
            ('books_reserved', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('bibliotheca', ['Warehouse'])

        # Adding model 'News'
        db.create_table('bibliotheca_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('modification_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, null=True)),
            ('text_body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bibliotheca', ['News'])

        # Adding model 'Reservations'
        db.create_table('bibliotheca_reservations', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reader_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Readers'])),
            ('book_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Books'])),
            ('reservation_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('bibliotheca', ['Reservations'])


    def backwards(self, orm):
        # Deleting model 'Readers'
        db.delete_table('bibliotheca_readers')

        # Deleting model 'Publishers'
        db.delete_table('bibliotheca_publishers')

        # Deleting model 'Categories'
        db.delete_table('bibliotheca_categories')

        # Deleting model 'Books'
        db.delete_table('bibliotheca_books')

        # Deleting model 'Borrowings'
        db.delete_table('bibliotheca_borrowings')

        # Deleting model 'Authors'
        db.delete_table('bibliotheca_authors')

        # Deleting model 'Books_Authors'
        db.delete_table('bibliotheca_books_authors')

        # Deleting model 'Books_Categories'
        db.delete_table('bibliotheca_books_categories')

        # Deleting model 'Warehouse'
        db.delete_table('bibliotheca_warehouse')

        # Deleting model 'News'
        db.delete_table('bibliotheca_news')

        # Deleting model 'Reservations'
        db.delete_table('bibliotheca_reservations')


    models = {
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'top_category_id': ('django.db.models.fields.IntegerField', [], {})
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
            'is_blocked': ('django.db.models.fields.BooleanField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '12'})
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
        }
    }

    complete_apps = ['bibliotheca']