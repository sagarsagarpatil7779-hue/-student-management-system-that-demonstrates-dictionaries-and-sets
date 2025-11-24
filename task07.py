
# Step 1: Create student records
s001 = {"id": "S001", "name": "Alice", "age": 24, "gender": "Female", "courses": {"Computer Science"}}
s002 = {"id": "S002", "name": "Bob", "age": 28, "gender": "Male", "courses": {"Mathematics"}}
s003 = {"id": "S003", "name": "John", "age": 45, "gender": "Male", "courses": {"Physics"}}
s004 = {"id": "S004", "name": "Gowri", "age": 15, "gender": "Female", "courses": {"Chemistry"}}
s005 = {"id": "S005", "name": "Chaya", "age": 36, "gender": "Female", "courses": {"Botany"}}
 
# Step 2: Store all students in one dictionary
students = {
    "S001": s001,
    "S002": s002,
    "S003": s003,
    "S004": s004,
    "S005": s005
}
 
# Step 3: Add a new course to a student
students["S001"]["courses"].add("Math")
 
# Step 4: Remove a course from a student
students["S002"]["courses"].discard("Mathematics")
 
# Step 5: Add a new student
students["S006"] = {"id": "S006", "name": "Kiran", "age": 22, "gender": "Male", "courses": {"Biology"}}
 
# Step 6: Remove a student
del students["S004"]
 
# Step 7: Print all students
print("All Students:\n")
for sid, info in students.items():
    print("ID:", info["id"])
    print("Name:", info["name"])
    print("Age:", info["age"])
    print("Gender:", info["gender"])
    print("Courses:", info["courses"])