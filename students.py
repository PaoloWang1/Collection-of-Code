students=[ {'name':'Tommy',
            'homework':[70,80,88,79],
            'quiz':[88,78,50],
            'test':[75,68]},
           {'name':'Alex',
            'homework':[90,98,87,97],
            'quiz':[95,89,91],
            'test':[88,90]},
           {'name':'Jason',
            'homework':[50,89,71,82],
            'quiz':[71,87,70],
            'test':[78,81]}]
highest_test = 0
lowest_quiz = 100
lowest_hw = 100
lowest_hw_name = ""
lowest_hw_name = ""
highest_test_name = ""
average = 0
for x in range(3):
    for y in range(len(students[x]["homework"])):
        average += students[x]["homework"][y]
    average = average/4
    if average < lowest_hw:
        lowest_hw = average
        lowest_hw_name = students[x]["name"]
    average = 0

    for z in range(len(students[x]["quiz"])):
        average += students[x]["quiz"][z]
    average = average/4
    if average < lowest_quiz:
        lowest_quiz = average
        lowest_quiz_name = students[x]["name"]
    average = 0
    for c in range(len(students[x]["test"])):
        average += students[x]["test"][c]
    average = average/4
    if average > highest_test:
        highest_test = average
        highest_test_name = students[x]["name"]
    average = 0

print("lowest homework average: ", str(lowest_hw_name))
print("lowest quiz average: ", str(lowest_quiz_name))
print("highest test average: ", str(highest_test_name))


