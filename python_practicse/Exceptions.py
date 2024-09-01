# Exceptions: it is used to handle errors by displaying a message to the user
try:
    with open("Exceptions.py") as file:
        print("file is opened")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didnt enter a valid age ")
else:
    print("No exceptions were thrown")
# finally:  # finally clause is always excecuted and is mainly used to free the external resources
 #   file.close()
 # another method
# with statement: used to release external resources automatically
