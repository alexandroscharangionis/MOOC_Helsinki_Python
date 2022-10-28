def oldest_person(people: list):
    oldest = people[0][1]
    for person in people:
        if person[1] <= oldest:
            oldest = person[1]
    for person in people:
        if person[1] == oldest:
            return person[0]
