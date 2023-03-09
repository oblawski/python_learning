universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(list_of_universities):
    """return lists of students and tuition"""
    students = []
    tuition_fees = []
    for university in list_of_universities:
        students.append(university[1])
        tuition_fees.append(university[2])
    return students, tuition_fees


def mean(value):
    """return mean value in the list 'value' """
    return sum(value) / len(universities)


def median(value):
    """return median value in the list 'value' """
    value.sort()
    if len(value) % 2 == 0:
        n = ((len(value) / 2) + (len(value) / 2) + 1) / 2
    else:
        n = int((len(value) / 2))
    return value[n]


print("*" * 22)
print(f"Total students: {sum(enrollment_stats(universities)[0]):,}")
print(f"Total tuition: ${sum(enrollment_stats(universities)[1]):,}")
print()
print(f"Student mean: {mean(enrollment_stats(universities)[0]):,.2f}")
print(f"Student median: {median(enrollment_stats(universities)[0]):,}")
print()
print(f"Tuition mean: ${mean(enrollment_stats(universities)[1]):,.2f}")
print(f"Tuition median: ${median(enrollment_stats(universities)[1]):,}")
print("*" * 22)