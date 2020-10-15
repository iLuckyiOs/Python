from sys import argv

script, filename = argv

print(f"We are going to erase {filename}")
print("If you don't want that. hit CTRL-C(C)")
print("If you do want that, hit return")

input("?")

print("opening the file")

target = open(filename, 'w')

print ("Truncating the file. GoodBye")

target.truncate()

print("Now I'm going to ask you for three lines")
line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3")
target.write(line1)
target.write(line2)
target.write(line3)


print("Ana finally")

target.close()


