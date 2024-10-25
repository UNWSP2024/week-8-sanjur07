def get_courses():
    courses = {}
    print("Enter course ID and course name pairs. Type 'done' when finished.")

    while True:
        course_id = input("Enter course ID (e.g, COS 2005): ").strip()
        if course_id.lower() == 'done':
            break
        course_name = input("Enter course name (e.g., Pyhton Programming): ").strip()
        courses[course_id] = course_name
    return courses

def display_courses_by_subject(courses):
    subject_code = input("\nEnter a subject code to search for (e.g., COS): ").strip().upper()
    print(f"\nCourses for subject '{subject_code}':")

    found_courses = False
    for course_id, course_name in courses.items():
        print(f"{course_id}: {course_name}")
        found_courses = True
    
    if not found_courses:
        print(f"No courses found for subject '{subject_code}'.")

'''Define Function get_courses:

Initialize an empty dictionary courses to store course ID and course name pairs.
Prompt user to enter course ID and course name pairs.
Loop:
Prompt user for course_id.
If course_id is 'done', exit loop.
Prompt user for course_name.
Add course_id and course_name to courses dictionary.
Return the courses dictionary.
Define Function display_courses_by_subject:

Prompt user for a subject_code.
Display a message indicating the courses for this subject_code.
Initialize a found_courses flag as False.
Loop through each course_id, course_name in courses dictionary:
If course_id starts with subject_code:
Print course_id and course_name.
Set found_courses to True.
If found_courses is False:
Print message that no courses were found for subject_code.
Main Program:

Call get_courses and store the result in courses.
Call display_courses_by_subject with courses.'''