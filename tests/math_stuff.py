import math

print(math.asin(1))
print(math.ceil(1.333))
print(math.floor(1.9999))
print(math.pi)

f = open("test.txt")
for line in f:
    print(line)
f.close()

#write the file

# f = open("test.txt", "a")
# f.write("\n\n\nanother line from python\n\n\n")
# f.write("one more line from python")
#
# f.close()
#
# f = open("test.txt")
#
# for line in f:
#     print(line)


with open("test1.txt", 'w', encoding='UTF-8') as f:
    f.write("first line\n")
    f.write("second line \n")
    f.write("third line \n")

read_file = open("test1.txt", 'r')

for line in read_file:
    print(line)
