
# Iterators implement iter and next methods
list_a = [1, 2, 4, 5, 6, 7, 8, 8, 8, 1212]
my_iter = iter(list_a)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter))

input_str = "This is a string"
print(input_str[::-1])
count = len(input_str)

for i in input_str:
    print(input_str[count-1], end='')
    count = count - 1

print("######################")
# Generator are a special way to generate an iterator [Used to create iterations]
# Generator to reverse a string


def rev_str(str_input):
    length = len(str_input)
    for j in range(length - 1, -1, -1):
        yield str_input[j]


for ch in (rev_str("this is some string")):
        print(ch, end='')
