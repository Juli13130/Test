import random

mf1_nombre = ("Ichi")
mf2_nombre = ("Ni")
mf3_nombre = ("San")

#nom_A = input("n1")
prob_A = int(input("proA"))

#nom_B = input("n2")
prob_B = int(input("proB"))

#nom_C = input("n3")
prob_C = int(input("proC"))

while prob_A + prob_B + prob_C != 100:
    print(prob_A + prob_B + prob_C, "?")
    prob_A = int(input("p1"))
    prob_B = int(input("p2"))
    prob_C = int(input("p3"))

numran = random.randint(0,100)
print("se rolleo un dado de:",  numran)

if numran >= 0 and numran < prob_A:
    print(mf1_nombre)
elif numran >= prob_A and numran < prob_B + prob_A:
    print(mf2_nombre)
else: ### necesitamos listas para literalmente todo si quieren buen codigo
     print(mf3_nombre)