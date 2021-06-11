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

final=[]


for s in Student_submissions.items():

    res = dict()
    res['name'] = s[0]
    res['correct'] = 0
    res['wrong'] = 0

    for value in s[1]:
        count = 0
        if list(value.items()) == correct_answers:
            res['correct'] += 1
            i += 1
        else:
            res['wrong'] += 1
            i += 1

    final.append(res)

result=[]

for student in final:
    percent = ((3*res['correct']) - res['wrong']) / ((res['correct'] + res['wrong']) * 3)
    result[student['name']] = percent