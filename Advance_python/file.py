#Create a Python script to read data from an input file. Perform count lines, extract the first two lines, and write the extracted data into a new file.
file = open("Data.txt", "w")
file.write("Hello, World!")
file.write("\nThis is a text file.")
file.close()

file = open("Data.txt", "r")
file1 = open("Extra.txt", "w")
data = file.read()
file1.write(data)
file.close()
file1.close()

file = open("Data.txt", "r")
lines = file.readlines()
file.close()

count = len(lines)
print(count)
twolines = lines[:2]
print(twolines)
file1 = open("Extra.txt", "w")
for line in twolines:
    file1.write(line)
file1.close()