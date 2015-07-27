#Question: Given a family tree, find oldest sisters of the given person, oldest sister in the family tree and the oldest ancestor.

#People class
class Person():
    def __init__(self, name, sex, age, parents=None, children=None):
        self.name = name
        self.sex = sex    # 'M' or 'F'
        self.age = age 
        self.parents = set()
        if parents is not None:
            for p in parents:
                self.add_parent(p)

        self.children = set()
        if children is not None:
            for c in children:
                self.add_child(c)

    def add_parent(self, p):
        self.parents.add(p)
        p.children.add(self)

    def add_child(self, c):
        self.children.add(c)
        c.parents.add(self)


#Test Data
# Grandpa, Grandma
#   Daddy, Mommy
#    Son1,Daughter1,Daughter2
#   Uncle1, Aunt1
#     Son2, Daughter3, Son3

#Initialize the Family tree
Grandpa      = Person('Grandpa', 'm', 65)
Grandma      = Person('Grandma', 'f', 69)
Daddy        = Person('Daddy', 'm', 40,[Grandpa,Grandma])
Mommy        = Person('Mommy', 'f', 39)
Son1         = Person('Son1', 'm', 10,[Daddy,Mommy])
Daughter1    = Person('Daughter1', 'f', 15,[Daddy,Mommy])
Daughter2    = Person('Daughter2', 'f', 19,[Daddy])


#Family List
Family = [Grandpa,Grandma,Daddy,Mommy,Son1,Daughter1,Daughter2]

#Q1: find oldest sisters of the given person
def FindOldestSisterFor(person):
    oldest = Person('None', 'm', 0)
    for parent in person.parents:
        #print(parent.name)
        for sibling in parent.children:
            #print (sibling.name)
            if (oldest.age < sibling.age):
                oldest = sibling
    return (oldest.name,oldest.age)

#Q2: Oldest sister in the family tree
def FindOldestSister(Family):
    oldest = -1
    for i in Family:
        if len(i.children) > 1:
            for child in i.children:
                if (child.sex == 'f' and child.age > oldest):
                    oldest = child.age
    return oldest

#Q3: Find Oldest Ancestor
def FindOldestAncestor(Family):
    oldest = -1
    for i in Family:
        if i.age > oldest:
            oldest = i.age
    return oldest
    
name,age = FindOldestSisterFor(Son1)
print("Son1",", Oldest sister is", name , " and age=",age)
print("Age of oldest sister is ", FindOldestSister(Family))
print("Age of oldest ancestor is ", FindOldestAncestor(Family))
