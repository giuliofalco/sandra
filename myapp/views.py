
import json

from django.conf import settings
from django.shortcuts import render


LINGUE_SUPPORTATE = ("it", "de", "en")


def home(request):
    lang = request.GET.get("lang", "it")

    if lang not in LINGUE_SUPPORTATE:
        lang = "it"

    percorso_traduzioni = settings.BASE_DIR / "traduzioni.json"

    with open(percorso_traduzioni, "r", encoding="utf-8") as file:
        traduzioni = json.load(file)

    context = {"lang": lang}

    for chiave, lingue in traduzioni.items():
        context[chiave] = lingue[lang]

    return render(request, "myapp/index.html", context)

