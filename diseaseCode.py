from tables.models import DiseaseCode

with open("diseaseCode.txt", "r") as f:
    code = []
    for line in f:
        code.append(line.rstrip('\n'))
        # print(line.rstrip('\n'))
f.close()
with open("diseaseCodeMeaning.txt", "r") as f:
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
