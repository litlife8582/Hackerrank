# Initialize an empty dictionary to store student marks
student_marks = {}

# Read the number of students
n = int(input("Enter the number of students: "))

# Read each student's name and their scores
for _ in range(n):
    line = input("Enter the student's name and scores: ").split()
    name = line[0]
    scores = list(map(float, line[1:]))
    student_marks[name] = scores

# Query a student's name
query_name = input("Enter the student's name to query: ")

# Calculate the average score for the queried student
if query_name in student_marks:
    query_scores = student_marks[query_name]
    average_score = sum(query_scores) / len(query_scores)
    print(f"{query_name}'s average score is: {average_score:.2f}")
else:
    print(f"No records found for student: {query_name}")