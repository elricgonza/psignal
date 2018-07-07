from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from polls.models import Question, Choice
import os.path
from django.db import connection

from django.conf import settings
from django.db.utils import ConnectionHandler


@receiver(post_save, sender=Question)
@receiver(post_save, sender=Choice)
def model_post_save(sender, **kwargs):
    print('Grabadez: {}'.format(kwargs['instance'].__dict__))
    print('******************************************')
    print(kwargs['instance'].question_text)
    print('********************************************')

    with connection.cursor() as cursor:
        cursor.execute(
        "insert into question (id, question_text, usr) values (1, 'oso', 'I')"
        )
        cursor.commit()
        cursor.close()


    '''
    private_connections = ConnectionHandler(settings.DATABASES)
    #db = router.db_for_write(model)
    new_conn = private_connections[db]
    new_conn.enter_transaction_management()
    new_conn.managed(True)
    new_cur = new_conn.cursor()
    new_cur.execute(
        "insert into question (id, question_text, usr) values (1, 'oso', 'I')"
    )
    new_conn.commit()
    new_conn.close()
    '''


    '''
    cursor = connection.cursor()
    #    "insert into question (id, question_text, usr) values (1, 'oso', 'I')"
    #    "select question_text from polls_question where id=2"
    cursor.execute(
        "insert into question (id, question_text, usr) values (1, 'oso', 'I')"
    )
    #row = cursor.fetchone()
    cursor.close
    #print (row[0])
    print ('-------new insert----')
    '''


