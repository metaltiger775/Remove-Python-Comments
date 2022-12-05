import os
import sys

file_name = input("Enter the file name: ")
file = open(file_name, "r")
file_data = file.read()
file.close()
file_data = file_data.split("\n")
new_file_data = []

for line in file_data:
    if line.strip().startswith("#"):
        continue

    new_file_data.append(line)

new_file_data = "\n".join(new_file_data)
file = open(file_name, "w")
file.write(new_file_data)
file.close()

print("Comments removed from the file!")