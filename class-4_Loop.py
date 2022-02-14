# n = 5
# for i in range(1, n+1):
#     print(i, end=" ")
# n = int(input("Please enter number: "))
# for i in range(1, n+1):
#     for e in range(1, i+1):
#         print(e, end=" ")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# #################### Factorial
n = int(input("Please enter number: "))
nf = 1
for i in range(1, n+1):
    nf = i * nf

print(f"{n} թվի ֆակտորիալը հավասար է {nf}-ի։")
print("*".center(32, '='))

# n! = 1*2*3*4*5*...*(n - 2)(n - 1)n
# 1! = 1
# 3! = 1 * 2 * 3 = 6
# ################# Պարզ թվի դեպքում YES, այլապես No
# n = int(input("Please enter number: "))
x = 0
for i in range(1, n+1):
    d = n % i
    if d == 0:
        x = x + 1
print(f"Բաժանարարների քանակը {x}")
if x > 2:
    print("Պարզ թիվ չէ։ Ունի 2-ից ավել բաժանարար։")
else:
    print("Պարզ թիվ է։")
# ########################

