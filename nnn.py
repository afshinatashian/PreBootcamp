import json

correct_answers = [
    ("what is the output?", 4),
    ("Is earth flat?", 1),
    ("how much money do they have?", 2)
]

Student_submissions = {
    "Helen": [
        {"what is the output?": 4},
        {"Is earth flat?": 2},
        {"how much money do they have?": 3}
    ],
    "Hana": [
        {"what is the output?": 3},
        {"Is earth flat?": 1},
        {"how much money do they have?": 3}
    ],
    "Helma": [
        {"what is the output?": 4},
        {"Is earth flat?": 1},
        {"how much money do they have?": 2}
    ],
}

result = list()
for student in Student_submissions.items():
    # print(student)
    d = dict()
    d['name'] = student[0]
    d['correct'] = 0
    d['wrong'] = 0

    for v in student[1]:
        # print(v)
        i = 0
        if list(v.items())[0][1] == correct_answers[i][1]:
            d['correct'] += 1
            i += 1
        else:
            d['wrong'] += 1
            i += 1

    result.append(d)

# print(result)

res = dict()
for student in result:
    # print(student)
    percent = ((3*student['correct']) - student['wrong']) / ((student['correct'] + student['wrong']) * 3)
    res[student['name']] = percent


f = open('names_marks.txt', 'w', encoding='UTF-8')
# json.dump(res)
# or
f.write(str(res))
f.close()
