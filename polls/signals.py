from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from polls.models import Question, Choice
from django.db import connection


@receiver(post_save, sender=Question)
def model_post_save(sender, **kwargs):
    if kwargs.get('created', False):
        action_is= 'new'
    else:
        action_is= 'update'

    print('SAVED: {}'.format(kwargs['instance'].__dict__))
    print('******************************************')
    print(kwargs['instance'].question_text) + '--->' +  action_is
    print('********************************************')

    with connection.cursor() as cursor:
        try:
            '''
            # inserta valores directamente
            sql = "insert into public.question (id, question_text, usr) values (%s, %s, %s)"
            cursor.execute (sql, (
                kwargs['instance'].id,
                kwargs['instance'].question_text,
                kwargs['instance'].id
                )
            )
            '''
            # get valores from f
            cursor.callproc('f_question', [kwargs['instance'].id])
            results = cursor.fetchone()
            print(results)
            print('===========')
            print(results[0])
            print(results[1])
            print(results[2])
            print('===========')

            sql = "insert into public.question (id, question_text, usr) values (%s, %s, %s)"
            cursor.execute (sql, (
                results[0],
                results[1],
                results[2]
                )
            )

        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)


@receiver(post_delete, sender=Question)
def model_post_delete(sender, **kwargs):
    print('******************************************')
    print ("DELETED: %s" % str(kwargs['instance'].id) + '---' +  kwargs['instance'].question_text )
    print('******************************************')
    with connection.cursor() as cursor:
        try:
            sql = "delete from public.question where id = %s;"
            cursor.execute (sql, (int(kwargs['instance'].id),))
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)

