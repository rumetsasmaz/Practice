def calculate_average(notes):
    total_score = 0 

    for entry in notes:
        for score in entry.values():
            total_score += score
    return total_score / len(notes)

notes = [

    {"Jack": 85},
    {"Jill": 92},
    {"John": 78}
]

print(calculate_average(notes))