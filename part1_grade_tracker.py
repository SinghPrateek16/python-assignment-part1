

# PART 1: Python Basics & Control Flow


# Task- 1

# data provided

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# new list to store cleaned data
final_list = []

# looping through each student
for record in raw_students:

    # removing spaces and fixing name format
    full_name = record["name"].strip().title()

    # converting roll number from string to int
    roll_no = int(record["roll"])

    # converting marks string into list of numbers
    marks_list = []
    for num in record["marks_str"].split(", "):
        marks_list.append(int(num))

    # checking if name is valid
    is_valid = True
    for part in full_name.split():
        if not part.isalpha():
            is_valid = False

    # printing result
    if is_valid:
        print("✓ Valid name")
    else:
        print("✗ Invalid name")

    # printing student info
    print("=" * 32)
    print("Student :", full_name)
    print("Roll No :", roll_no)
    print("Marks   :", marks_list)
    print("=" * 32)

    # storing cleaned data
    final_list.append({
        "name": full_name,
        "roll": roll_no,
        "marks": marks_list
    })

# finding student with roll 103
for item in final_list:
    if item["roll"] == 103:
        print(item["name"].upper())
        print(item["name"].lower())


     
✓ Valid name
================================
Student : Ayesha Sharma
Roll No : 101
Marks   : [88, 72, 95, 60, 78]
================================
✓ Valid name
================================
Student : Rohit Verma
Roll No : 102
Marks   : [55, 68, 49, 72, 61]
================================
✓ Valid name
================================
Student : Priya Nair
Roll No : 103
Marks   : [91, 85, 88, 94, 79]
================================
✓ Valid name
================================
Student : Karan Mehta
Roll No : 104
Marks   : [40, 55, 38, 62, 50]
================================
✓ Valid name
================================
Student : Sneha Pillai
Roll No : 105
Marks   : [75, 80, 70, 68, 85]
================================
PRIYA NAIR
priya nair

# Task - 2



student = "Ayesha Sharma"

# list of subjects and marks
subject_list = ["Math", "Physics", "CS", "English", "Chemistry"]
marks_list = [88, 72, 95, 60, 78]

# function to calculate grade
def find_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

# printing each subject with marks and grade

print("\nSubject Wise Marks")
for index in range(len(subject_list)):
    sub_name = subject_list[index]
    score = marks_list[index]
    print(sub_name, ":", score, "Grade =", find_grade(score))

# calculating total marks
total_marks = sum(marks_list)

# calculating average
average_marks = round(total_marks / len(marks_list), 2)

print("\nTotal Marks:", total_marks)
print("Average Marks:", average_marks)

# finding highest and lowest
highest_marks = max(marks_list)
lowest_marks = min(marks_list)

# getting subject name using index
high_sub = subject_list[marks_list.index(highest_marks)]
low_sub = subject_list[marks_list.index(lowest_marks)]

print("Highest:", high_sub, highest_marks)
print("Lowest:", low_sub, lowest_marks)

# While loop for adding new subjects

count_new = 0
while True:
    new_sub = input("Enter new subject (or type done): ")
    if new_sub.lower() == "done":
        break
    try:
        new_marks = int(input("Enter marks (0-100): "))

        if new_marks >= 0 and new_marks <= 100:
            subject_list.append(new_sub)
            marks_list.append(new_marks)
            count_new += 1
        else:
            print("Marks should be between 0 and 100")
    except:
        print("Wrong input! Please enter numbers only")
print("\nNew subjects added:", count_new)

# updated average
new_avg = round(sum(marks_list) / len(marks_list), 2)
print("Updated Average:", new_avg)


     
Subject Wise Marks
Math : 88 Grade = A
Physics : 72 Grade = B
CS : 95 Grade = A+
English : 60 Grade = C
Chemistry : 78 Grade = B

Total Marks: 393
Average Marks: 78.6
Highest: CS 95
Lowest: English 60
Enter new subject (or type done): done

New subjects added: 0
Updated Average: 78.6

# Task - 3


# given data
my_class = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("\nName              | Average | Status")
print("----------------------------------------")

pass_count = 0
fail_count = 0

all_avg = []  # to store all averages

# loop through each student
for entry in my_class:

    name = entry[0]       # getting name
    marks = entry[1]      # getting marks list

    # calculate average
    total = sum(marks)
    avg = total / len(marks)
    avg = round(avg, 2)

    all_avg.append(avg)    # storing average

    # checking pass or fail
    if avg >= 60:
        result = "Pass"
        pass_count += 1
    else:
        result = "Fail"
        fail_count += 1

    # printing row
    print(f"{name:<18} | {avg:^7} | {result}")

# printing pass fail count
print("\nPassed Students:", pass_count)
print("Failed Students:", fail_count)

# finding topper
top_marks = max(all_avg)
top_index = all_avg.index(top_marks)

top_name = my_class[top_index][0]

print("Topper:", top_name, top_marks)

# class average
class_avg = sum(all_avg) / len(all_avg)
class_avg = round(class_avg, 2)

print("Class Average:", class_avg)

     
Name              | Average | Status
----------------------------------------
Ayesha Sharma      |  78.6   | Pass
Rohit Verma        |  61.0   | Pass
Priya Nair         |  87.4   | Pass
Karan Mehta        |  49.0   | Fail
Sneha Pillai       |  75.6   | Pass

Passed Students: 4
Failed Students: 1
Topper: Priya Nair 87.4
Class Average: 70.32


# Task-  4



# given essay
text_data = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# step 1: remove extra spaces
clean_text = text_data.strip()
print("\nClean Text:", clean_text)

# step 2: convert to title case
title_text = clean_text.title()
print("\nTitle Case:", title_text)

# step 3: count 'python'
count_word = clean_text.count("python")
print("\nPython word count:", count_word)

# step 4: replace word
new_text = clean_text.replace("python", "Python 🐍")
print("\nAfter Replacement:", new_text)

# step 5: split into sentences
sentence_list = clean_text.split(". ")
print("\nSentences List:", sentence_list)

# step 6: print sentences one by one
print("\nNumbered Sentences:")
num = 1

for line in sentence_list:

    # adding . if not present
    if not line.endswith("."):
        line = line + "."

    print(num, ".", line)

    num += 1
     
Clean Text: python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.

Title Case: Python Is A Versatile Language. It Supports Object Oriented, Functional, And Procedural Programming. Python Is Widely Used In Data Science And Machine Learning.

Python word count: 2

After Replacement: Python 🐍 is a versatile language. it supports object oriented, functional, and procedural programming. Python 🐍 is widely used in data science and machine learning.

Sentences List: ['python is a versatile language', 'it supports object oriented, functional, and procedural programming', 'python is widely used in data science and machine learning.']

Numbered Sentences:
1 . python is a versatile language.
2 . it supports object oriented, functional, and procedural programming.
3 . python is widely used in data science and machine learning.
