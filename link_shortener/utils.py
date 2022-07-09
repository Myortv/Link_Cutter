from random import choice

from django.core.exceptions import ObjectDoesNotExist

from .models import Link


chars = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-'
    )


def get_url():

    # не лучший скрипт, если будет заполняться база данных
    # то будет слишком много времени уходить на перебор неподходящих вариантов
    # в таком случае имеет смысл заменить этот скрипт на более акутальный
    # сейчас это фактически просто перебор с помощью грубой силы
    # однако из-за того что значений которые хеш может иметь, не имеет
    # смысла делать более сложный скрипт сейчас

    hash = ''
    while True:
        for i in range(0,32):
            hash = f'{hash}{choice(chars)}'
        try:
            Link.objects.get(hashed_url=hash)
        except ObjectDoesNotExist:
            break

    return hash
