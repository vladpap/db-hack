from datacenter.models import Schoolkid, Mark, Subject
from datacenter.models import Lesson, Commendation, Chastisement
from random import choice


def get_child(child_full_name):
    childs = Schoolkid.objects.filter(
        full_name__contains=child_full_name)
    if not childs:
        print(f'Такого ученика нет: {child_full_name}')
        return None
    elif len(childs) > 1:
        print(f'Учеников с именем {child_full_name} несколько, уточни имя')
        return None

    return childs.first()


def fix_marks(child_full_name):
    child = get_child(child_full_name)
    if not child:
        return
    child_marks = Mark.objects.filter(schoolkid=child.id, points__lte=3)
    for child_mark in child_marks:
        child_mark.points = 5
        child_mark.save()


def remove_chastisements(child_full_name):
    child = get_child(child_full_name)
    if not child:
        return
    chastisements = Chastisement.objects.filter(
        schoolkid=child)
    chastisements.delete()


def create_commendation(child_full_name, lesson):
    child = get_child(child_full_name)
    if not child:
        return
    subjects = Subject.objects.filter(
        title=lesson,
        year_of_study=child.year_of_study)
    if not subjects:
        print(f'Такого предмета нет: {lesson}')
        return
    subject = subjects.first()

    all_commendations = [
        'Молодец!', 'Отлично!', 'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!', 'Великолепно!', 'Прекрасно!',
        'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!',
        'Очень хороший ответ!', 'Талантливо!', 'Я поражен!',
        'Ты сегодня прыгнул выше головы!', 'Уже существенно лучше!',
        'Потрясающе!', 'Замечательно!', 'Прекрасное начало!',
        'Так держать!', 'Ты на верном пути!', 'Здорово!',
        'Это как раз то, что нужно!', 'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!',
        'Ты растешь над собой!', 'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!'
    ]

    lesson = Lesson.objects.filter(
        year_of_study=child.year_of_study,
        group_letter=child.group_letter,
        subject=subject.id).first()
    Commendation.objects.create(
        text=choice(all_commendations),
        created=lesson.date,
        schoolkid=child,
        subject=subject,
        teacher=lesson.teacher)


def a123():
    print('Yess')
