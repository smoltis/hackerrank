
"""
Student ID → ___1_____2_____3_____4_____5__               
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86  
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5 


Input:
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

Output average score for each student

"""


students, subjects = map(int,input().split())
subject_rows = []
for _ in range(subjects):
    subject_rows.append(map(float,input().split()))

marks_by_student = zip(*subject_rows)
for row in marks_by_student:
    print(sum(row)/len(row))
