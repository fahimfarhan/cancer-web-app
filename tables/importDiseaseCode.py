from django.http import HttpResponse

from tables.models import DiseaseCode
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


def import_disease_code(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CODE_PATH = BASE_DIR+'/diseaseCode.txt'
    MEANING_PATH = BASE_DIR+'/diseaseCodeMeaning.txt'
    try:
        with open(CODE_PATH, "r") as f:
            code = []
            for line in f:
                code.append(line.rstrip('\n'))
                # print(line.rstrip('\n'))
        f.close()
        with open(MEANING_PATH, "r") as f:
            meaning = []
            for line in f:
                meaning.append(line.rstrip('\n'))
                # print(line.rstrip('\n'))
                # print(len(array2))
        f.close()

        i = 0
        while i < len(code):
            # print(array1[i]+' '+array2[i])
            a = DiseaseCode(code=code[i], meaning=meaning[i])
            a.save()
            i = i + 1
            # print(i)
        print('HAPPY! :D')
    except:
        print("Shit!")
        return HttpResponse('<h1>shit!</h1>')
    return HttpResponse('<h1>ok!</h1>')