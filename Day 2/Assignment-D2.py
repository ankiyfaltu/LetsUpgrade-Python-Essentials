# List and 5 of its functions
rudy = ['judy with Mr.moody in a coach', 12/7, 25, 'on a Train No.', 'blabla']
rudy.append(2525)  # adds data in list
ina = rudy.count(25)  # Counts occurence of particular data in list
inb = rudy.index(25)  # Gives the index of data
rudy.insert(inb, 'at a berth numbner')  # inserts an element before the given index
rudy.remove('blabla')  # Removes an element from the list
print(rudy)

# Dictionary and 5 of its functions
tom = {'Name': 'Rumpelstiltskin', 'KnownAs': 'Tom Tit Tot', 'From': 'Germany'}
size_of_tom = tom.__sizeof__()  # gives size of dictionary in bytes
copy_of_tom = tom.copy()  # Creats a shallow copy of dictionary
tom.items()  # gives items in a dictionary
tom.values()  # Gives all the values of dictionary
tom.get('From', 'not present')  # Gives the value of key if present in dictionary, else will return 'not present'
print(tom)

# Sets and its functions
age_of_class_A = {50, 35, 42, 56, 28, 32, 27, 34, 26}
age_of_class_B = {28, 27, 26, 25, 24, 50}
age_of_class_B.add(20)  # adds an element in set
difference_bw_AB = age_of_class_A.difference(age_of_class_B)  # gives difference between 2 Sets
intersection_of_AB = age_of_class_A.intersection(age_of_class_B)   # returns intersection of 2 Sets
intersection_of_AB.discard(50)  # Discards an element from Sets
union_of_AB = age_of_class_B.union(age_of_class_A)  # returns union of given sets

