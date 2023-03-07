from django.http import HttpResponse
from django.template import loader
from django.core.files import File
from CoRal import settings

import random


def index(request):
    template = loader.get_template('index.html')
    with open(settings.TEXT_ROOT / "texts.txt", 'r', encoding="utf-8") as f:
        django_file = File(f)
        transcriptions = django_file.readlines()

    transcriptions = [line.rstrip() for line in transcriptions]

    random.shuffle(transcriptions)

    content = {
        "transcriptions": transcriptions[:150],
    }

    return HttpResponse(template.render(content, request))