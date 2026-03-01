"""
Student Mark Analysis
------------------------
1. Average by student and subject
2. Highest and Lowest per subject
3. Overall class topper
4. Pass count per subject
5. Which subject is difficult
6. Ranking Students

"""

import numpy as np

# Random mark generation fro 30 students and 5 subjects
np.random.seed(25)
marks = np.random.randint(10, 101, size=(30, 5))
print("Marks array: ", marks)

# Average by subject
average_by_subject = np.mean(marks, axis=0)
print("Average by marks: ", average_by_subject.astype(int))

# Average by Marks
average_by_marks = np.mean(marks, axis=1)
print("Average by marks: ", average_by_marks.astype(int))

# Highest per subject
highest_per_subject = np.max(marks, axis=0)
print("Highest per subject: ", highest_per_subject)

# Lowest per subject
lowest_per_subject = np.min(marks, axis=0)
print("Lowest per subject: ", lowest_per_subject)

# Class topper
total_marks = np.sum(marks, axis=1)
topper = np.max(total_marks)
topper_student_index = np.argmax(total_marks)
print("Class Topper mark: ", topper)
print("Class Topper index: ", topper_student_index)

#pass count per subject
# pass_mark = np.array([marks[marks>=40]])
# pass_mark_count = len(pass_mark)
# print("pass_mark_count", pass_mark_count)

pass_mark = marks >=40
print("Pass mark: ", pass_mark)
pass_count_by_subject = np.sum(pass_mark, axis=0)
print("Pass mark count: ", pass_count_by_subject)

#Difficult Subject = Low average mark
difficult_subject = np.argmin(average_by_subject)
print("Difficult Subject: ", difficult_subject)


#rank
rank = np.argsort(-total_marks)
rank_des = np.argsort(total_marks)
print("Rank by index: ", rank)
print("Rank by index: ", rank_des)

for mark in range(len(rank)):
    print(f"Rank {mark+1}: Student {rank[mark]}")
    
top_5 = rank[:5]
print("Top 5: ", top_5)
