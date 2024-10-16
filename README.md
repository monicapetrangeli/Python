# Python
# after class exercise - lecture 3
For the exercises of lecture 3 four classes were created; student, course, registration and grade.

Course Class:
  The Course class contains as attributes its name, course type, a dictionary of students enrolled in the course and a dictionary of grades given in the course.
  Dictionaries were used for both students and grades as it allows to store for students both the student object(key) and its id(value) to then connected to the grades dictionary containing student ids(keys) and grades(values).

Student Class:
  The Student class contains as attributes its name, id and a list of courses enrolled. A list was chosen as a student is not able to enroll into a course already present within its courses list due to the if statement in the enroll_course method and therefore repetitions could not occur.

Registration Class:
  The Registration class is defined by a dictionary containing the students registered and a set of courses registered.
  when a student is enrolled in a course both attributed of the Registration class are updated as well as the corresponding course's dictionary of students and the student's list of courses. Equally, when a course is dropped the above mentioned values are updated to esnure compatability between classes.

Grade Class:
  The Grade class has been designed as a single dictionary containing all grades for all students and courses. this was done so that all grades of a student could be accessed from the single object 'grade'.
  When adding a grade a student id is required that will be used as key for the first dictionary, its value will be a second dictionary containg the course(key) and grade(value). This structure enables us to add courses' grades to a single original key (the student id).
  When calculating the GPA a for loop has been created to iterate over all grades present for a specific student id, add them together and then divide them by the number of courses the student is enrolled in. 
