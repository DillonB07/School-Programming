# import re as regex

# email = input("Enter your email: ")

# valid = regex.search(r"^[\w-\.]+@([\w-]+\.)+[\w-]{2,10}$", email)

# print(valid)


# import re as regex


# def email_validator(em):

#     valid = regex.search(r"^[\w-\.]+@([\w-]+\.)+[\w-]{2,10}$", em)
#     return valid


# email = input("Enter your email: ")

# print(email_validator(email))




email = input("Enter your email: ")

if email.find("@") == -1:
    print("Email must include @ symbol")
elif email.find(".") == -1:
    print("Email must include . symbol")
else:
    print("Email is valid")
