# name = input("Please enter you name: ")
# age = int(input("Please enter the age: "))
#
# # String Formatting ~ f-strings ( >= python 3.8)
# grating = f"Hello {name}! Next year you will be {age + 1} years old."
# print(grating)
#
# # Old version
# print("Hello {}! Next year you will be {} years old.".format(name, age + 1))

# # String functions
# full_name = "ara voskanyan"
# print(full_name.title())
# print(full_name)
# print(full_name.capitalize())
# print(full_name.upper())
# print(full_name.lower())

# full_name = input("Please enter you fill name: ")
# print((full_name.lower()).title())
#
# # String langth
# print(len(full_name))
# print(full_name.center(32, "="))
# print(full_name.rjust(32, "."))
# print(full_name.ljust(32, "."))
#
# # Տառերի քանակը տրված բառում / տարբերում է մեծատառը և փոքրքտքռը
# print(full_name.count("a"))
# print(type(full_name))  # type for variables

# # Indexing
full_name = "Ara Voskanyan"
# print(full_name[1])
# # # Slicing
# print(full_name[2:6])
# ## Start, Stop, Step
# print(full_name[2:11:2])  ## 2-ից 10 տարածքում գտնվող նիշերի ամեն 2-րդ նիշը
# ## Եթե սկսվում է 0-ից, առաջին թիվը կարելի է չգրել։ Նույնը արվում է նաև վերջի համար
# print(full_name[:6])
# print(full_name[3:])
# ## Վերջին նիշը ընտրելը
# print(full_name[-1])
# print(full_name[9:2:-1]) # ## Թարս հերթականությամբ
# print(full_name[::-1]) # Revers
# print(full_name[-9:-2])

# ### SubString
print(full_name.find("a"))
print(full_name.find("a", 3)) # ## 3-րդից հետո կսկսի փնտրել
print(full_name.find("z"))  # ## Եթե չկա, ապա արդյունքը -1 է
print(full_name.index("a"))
print(full_name.index("a", 3))
print(full_name.index("z"))  # ## Եթե չկա, ապա index() արդյունքը error է




