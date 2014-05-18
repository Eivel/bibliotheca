# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Warehouse.book_id'
        db.delete_column('bibliotheca_warehouse', 'book_id_id')

        # Adding field 'Warehouse.book'
        db.add_column('bibliotheca_warehouse', 'book',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Books'], default=0),
                      keep_default=False)

        # Deleting field 'Reservations.reader_id'
        db.delete_column('bibliotheca_reservations', 'reader_id_id')

        # Adding field 'Reservations.reader'
        db.add_column('bibliotheca_reservations', 'reader',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Readers'], default=0),
                      keep_default=False)

        # Deleting field 'Books.publisher_id'
        db.delete_column('bibliotheca_books', 'publisher_id_id')

        # Deleting field 'Books.category_id'
        db.delete_column('bibliotheca_books', 'category_id_id')

        # Adding field 'Books.publisher'
        db.add_column('bibliotheca_books', 'publisher',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Publishers'], default=0),
                      keep_default=False)

        # Adding field 'Books.category'
        db.add_column('bibliotheca_books', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Categories'], default=0),
                      keep_default=False)

        # Deleting field 'Borrowings.book_id'
        db.delete_column('bibliotheca_borrowings', 'book_id_id')

        # Deleting field 'Borrowings.reader_id'
        db.delete_column('bibliotheca_borrowings', 'reader_id_id')

        # Adding field 'Borrowings.reader'
        db.add_column('bibliotheca_borrowings', 'reader',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Readers'], default=0),
                      keep_default=False)

        # Adding field 'Borrowings.book'
        db.add_column('bibliotheca_borrowings', 'book',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Books'], default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Warehouse.book_id'
        db.add_column('bibliotheca_warehouse', 'book_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Books'], default=0),
                      keep_default=False)

        # Deleting field 'Warehouse.book'
        db.delete_column('bibliotheca_warehouse', 'book_id')

        # Adding field 'Reservations.reader_id'
        db.add_column('bibliotheca_reservations', 'reader_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Readers'], default=0),
                      keep_default=False)

        # Deleting field 'Reservations.reader'
        db.delete_column('bibliotheca_reservations', 'reader_id')

        # Adding field 'Books.publisher_id'
        db.add_column('bibliotheca_books', 'publisher_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Publishers'], default=0),
                      keep_default=False)

        # Adding field 'Books.category_id'
        db.add_column('bibliotheca_books', 'category_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Categories'], default=0),
                      keep_default=False)

        # Deleting field 'Books.publisher'
        db.delete_column('bibliotheca_books', 'publisher_id')

        # Deleting field 'Books.category'
        db.delete_column('bibliotheca_books', 'category_id')

        # Adding field 'Borrowings.book_id'
        db.add_column('bibliotheca_borrowings', 'book_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Books'], default=0),
                      keep_default=False)

        # Adding field 'Borrowings.reader_id'
        db.add_column('bibliotheca_borrowings', 'reader_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliotheca.Readers'], default=0),
                      keep_default=False)

        # Deleting field 'Borrowings.reader'
        db.delete_column('bibliotheca_borrowings', 'reader_id')

        # Deleting field 'Borrowings.book'
        db.delete_column('bibliotheca_borrowings', 'book_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
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
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Categories']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_pages': ('django.db.models.fields.IntegerField', [], {}),
            'original_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'published_date': ('django.db.models.fields.IntegerField', [], {}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Publishers']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'bibliotheca.borrowings': {
            'Meta': {'object_name': 'Borrowings'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Books']"}),
            'date_since': ('django.db.models.fields.DateTimeField', [], {}),
            'date_to': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reader': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Readers']"})
        },
        'bibliotheca.categories': {
            'Meta': {'object_name': 'Categories'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'top_category': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['bibliotheca.Categories']"})
        },
        'bibliotheca.news': {
            'Meta': {'object_name': 'News'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
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
            'address_aptno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'reader': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Readers']"}),
            'reservation_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'bibliotheca.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliotheca.Books']"}),
            'books_available': ('django.db.models.fields.IntegerField', [], {}),
            'books_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'books_reserved': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bibliotheca']