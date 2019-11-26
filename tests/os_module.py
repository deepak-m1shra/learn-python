import os, sys

print(os.getcwd())

os.chdir("c:/deepak")
print(os.getcwd())

# os.mkdir('dir_from_python')
os.listdir(os.getcwd())
# os.remove('dir_from_python')

# exception handling

try:
    1/"a"
except ZeroDivisionError:
    print("something went wrong")
    print(sys.exc_info()[0])
except TypeError:
    print("Issue with the type bro!!!")
    print(sys.exc_info()[0])
else:
    print("All is well")
finally:
    print("no matter what this will execute always")


