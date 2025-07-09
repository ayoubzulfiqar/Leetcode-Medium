def arrange_by_gender(people_list):
    males = []
    females = []
    other_genders = []

    for person in people_list:
        gender = person.get('gender')
        if isinstance(gender, str):
            gender_lower = gender.lower()
            if gender_lower == 'male':
                males.append(person)
            elif gender_lower == 'female':
                females.append(person)
            else:
                other_genders.append(person)
        else:
            other_genders.append(person)

    return males + females + other_genders

if __name__ == "__main__":
    sample_people_data = [
        {'name': 'Alice', 'gender': 'Female'},
        {'name': 'Bob', 'gender': 'Male'},
        {'name': 'Charlie', 'gender': 'Male'},
        {'name': 'Diana', 'gender': 'Female'},
        {'name': 'Eve', 'gender': 'female'},
        {'name': 'Frank', 'gender': 'male'},
        {'name': 'Grace', 'gender': 'Non-binary'},
        {'name': 'Heidi', 'gender': None},
        {'name': 'Ivan', 'gender': 'Male'}
    ]

    arranged_table = arrange_by_gender(sample_people_data)
    print(arranged_table)