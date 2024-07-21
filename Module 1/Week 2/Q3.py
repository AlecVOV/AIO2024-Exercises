"""
Question 3: Couting words from a text file
- Logic: 
1) Open a file => Read all the files, then add a split() function to split the content into words
2) Add a for loop to lower all the words into lower case
3) counting all the word into a for loop and write it inot a dictionary

"""

with open('C:/Users/Admin/Desktop/AIO2024 Log/Excercise/AIO2024-Exercises/Module 1/Week 2/data.txt', 'r') as file:
    document = file.read()

    words = document.split()

    words = [word.lower() for word in words]

    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    print(counter)