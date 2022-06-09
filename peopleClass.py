
class Person:
    def __init__(self, first_name, last_name, gender, age, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return self.age
        
    def get_gender(self):
        return self.gender

people_list=[]


with open('people.txt', 'r') as f:
    lines=f.readlines()
    print(lines)

people=[]
  
for x in lines:
    info = x.split(',')
    p = Person(info[0],info[1],info[2],info[3],info[4],info[5])
    people.append(p)

female, male = [], []

for a_person in people:
    if a_person.get_gender()=="Male":
        male.append(a_person)
    else:
        female.append(a_person)

young, old = [],[]

for a_person in people:
    if int(a_person.get_age()) >= 50:
        old.append(a_person)
    else:
        young.append(a_person)
