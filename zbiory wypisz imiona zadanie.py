array1 = ["Anna", "Adam", "Bartosz", "Kasia", "Kamil"]
array2 = ["Anna", "Bartosz", "Marta", "Ola"]
array3 = ["Bartosz", "Marta", "Tomek", "Wojtek", "Zuza"]

# zamiana tablic na zbiory
setA = set(array1)
setB = set(array2)
setC = set(array3)

# część wspólna zbiorów A i B
commonAB = setA.intersection(setB)
print("Imiona w zbiorze A i B:", commonAB)

# część wspólna zbiorów A, B i C
commonABC = commonAB.intersection(setC)
print("Imiona w zbiorze A, B i C:", commonABC)

# imiona w zbiorze C, ale nie ma ich w zbiorze A
onlyC = setC.difference(setA)
print("Imiona tylko w zbiorze C:", onlyC)

# imiona w zbiorze B, ale nie ma ich w zbiorze A i C
onlyB = setB.difference(setA.union(setC))
print("Imiona tylko w zbiorze B:", onlyB)

# imiona, które występują w przynajmniej jednym ze zbiorów
anySet = setA.union(setB, setC)
print("Imiona przynajmniej w jednym zbiorze:", anySet)

# imiona w zbiorze A, ale nie ma ich w sumie zbiorów B i C
onlyA = setA.difference(setB.union(setC))
print("Imiona tylko w zbiorze A:", onlyA)


# wypisz imiona które są:
# - w zbiorze A i B (część wspólna).
# - w zbiorze A i B i C (część wspólna).
# - w zbiorze C, ale nie ma ich w zbiorze A.
# - w zbiorze B, ale nie ma ich w zbiorze A i C.
# - przynajmniej jednym ze zbiorów.
# - w zbiorze A, ale nie ma ich w sumie zbiorów B i C.