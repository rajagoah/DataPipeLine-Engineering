#####
#writing in to the file
str = ("this is delhi \n", "this is paris \n", "this is new york \n")

test_file = open("test_file.txt","w+")
test_file.write("hello \n")
test_file.writelines(str)

#returning the cursor to the start of the file
test_file.seek(0)

#reading the content of the file
print(test_file.read(20))

#returning the cursor to the start of the file
test_file.seek(0)
print(test_file.readline())
test_file.seek(0)
print(test_file.readline(50))

#returning the cursor to the start of the file
test_file.seek(0)
print(test_file.readlines(50))
