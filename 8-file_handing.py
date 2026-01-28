# coding: utf-8 and read file line by line
with open("myfile.txt", "r", encoding='utf8') as file:
    for line in file:
        print(line) 
    