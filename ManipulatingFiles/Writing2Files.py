
#declaring the first variable to store what is going to be written in to the file
test_string = "first text to be written to the file\n"

test_file = open("test_file.txt","w+")
test_file.write(test_string)
print("write operation complete")
test_file.close()

test_file = open("test_file.txt", "r")
print(test_file.read())
test_file.close()

#appending to the end of the above file
test_file = open("test_file.txt","a+")
test_string_2 = "second text to be written\n"

test_file.write(test_string_2)

#using loop to read contents of a file
test_file = open("test_file.txt","r")
i = 1
for f in test_file:
    print("the ",i,"st line is --> ",f)
    i+=1