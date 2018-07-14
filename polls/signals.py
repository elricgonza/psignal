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
            sql = "insert into public.question (id, question_text, usr) values (%s, %s, %s)"
            cursor.execute (sql, (
                kwargs['instance'].id,
                kwargs['instance'].question_text,
                kwargs['instance'].id
                )
            )
            '''
            print('<<<kwargs')
            print(kwargs['instance'].id)
            print(kwargs['instance'].question_text)
            print('>>>')
            #cursor.callproc('f_question', [kwargs['instance'].id])

            sql = 'select * from f_question(%s)'
            some_id= 16
            #cursor.execute(sql, ([16]))  #no invoca funciones?
            #cursor.callproc('f_question', [16])
            '''
create or replace function f_question(
    id int
    ) returns table (
        id int,
            question_text varchar(50),
                usr int
                ) language sql as $$
                    select id, question_text, id*2 from question where id=$1;
                    $$;

                    --select * from f_question(16);

            '''


            cursor.execute("select * from question;")
            results = cursor.fetchall()
            while True:
                if not results:
                    print '---NO hay ROWS---'
                    break
                for result in results:
                    print 'hay ROW'
                    break
            print('////////ret')
            print(results)
            #print(cursor.fetchone()[0])
            #print(cursor.fetchone()[1])
            #print(cursor.fetchone()[2])
            print('////////')

            '''
            sql = "insert into public.question (id, question_text, usr) values (%s, %s, %s)"
            cursor.execute (sql, (
                results.id,
                results.question_text,
                results.id
                )
            )
            '''

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

