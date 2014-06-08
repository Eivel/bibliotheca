from bibliotheca.models import *
from datetime import datetime, timedelta
from django.core.mail import EmailMessage
from django_cron import CronJobBase, Schedule

class remindofBorrowings(CronJobBase):
    RUN_EVERY_MINS = 2

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'bibliotheca.cron.remindofBorrowings'

    def do(self):
        last_week = datetime.today() - timedelta(days=7)
        borrowings = Borrowings.objects.filter(date_to__gte=last_week)

        for b in borrowings:
            try:
                remainders = MailRemainder.objects.get(borrowing=b)
            except MailRemainder.DoesNotExist:
                html_msg = 'Witaj, ' + b.reader.user.first_name + ' ' + b.reader.user.last_name + '!<br><br>Niedługo dobiega termin oddania książki <b>' + b.book.title + '</b>.<br>' +\
                           'Termin oddania upływa dnia ' + b.date_to.strftime('%d.%m.%Y') + '. Nieoddanie książki w terminie będzie wiązało się z dodatkowymi kosztami.<br><br>Pozdrawiamy, Bibliotheca'
                msg = EmailMessage('Przypomnienie o oddaniu wypożyczonej książki', html_msg, 'bibliotheca.mia@gmail.com', [b.reader.user.email])
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send()

                rem = MailRemainder(borrowing=b, sent_mails=1)
                rem.save()

        three_days = datetime.today() - timedelta(days=3)
        reservations = Reservations.objects.filter(reservation_date__lte=three_days)

        for r in reservations:
            ware = Warehouse.objects.get(book=r.book)
            ware.books_reserved -= 1
            ware.books_available += 1
            ware.save()
            r.delete()

            html_msg = 'Witaj, ' + r.reader.user.first_name + ' ' + r.reader.user.last_name + '!<br><br>Ponieważ minęły trzy dni od podjęcia przez Ciebie rezerwacji książki <b>' + r.book.title + '</b>, jesteśmy zmuszeni ją anulować.<br>' +\
                           'Jeżeli chcesz, możesz ją ponownie zarezerwować w systemie, jeśli jest dostępna.<br><br>Pozdrawiamy, Bibliotheca'
            msg = EmailMessage('Anulowanie rezerwacji', html_msg, 'bibliotheca.mia@gmail.com', [r.reader.user.email])
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()
