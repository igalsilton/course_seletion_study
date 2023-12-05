# In this code I try to use new Python futures that I am learning and try to make best design as possible


class Course:

    def __init__(self, course_name, course_credit, course_id):
        self.course_name = course_name
        self.course_credit = course_credit
        self.course_id = course_id
        self.year = self.find_course_year()
        self.course_semester = self.find_course_semester()
        self.prerequisite = None

    def set_prerequisite(self, p_course):
        self.prerequisite = p_course

    def find_course_year(self):
        x = self.course_id/100
        return int(x)

    def find_course_semester(self):
        if self.course_id % 2 == 0:
            return 2
        else:
            return 1

    def find_technical_course(self):
        x = str(self.course_id)
        first_num = x[1]
        return int(first_num)

    def find_pre(self):
        if self.prerequisite is None:
            return 'None'
        else:
            return self.prerequisite.course_name

    def __str__(self):
        return 'Course:{:s}\nCourse ID:{:d}\nCredit:{:d}\nCourse Year:{:d}\nCourse Semester:{:d}\nCourse Prerequisite:{:s}\n\n'\
            .format(self.course_name, self.course_id, self.course_credit, self.year, self.course_semester, self.find_pre())


class TechnicalElectiveCourse(Course):

    def __init__(self, course_name, course_credit, course_id, threshold_credit):
        super().__init__(course_name, course_credit, course_id)
        self.threshold_credit = threshold_credit

    def is_eligible(self, num_gpa):
        if self.threshold_credit > num_gpa:
            return True
        else:
            return False

    def __str__(self):
        return 'Threshold Credit:{:.2f}\n{:s}'.format(self.threshold_credit, super().__str__())


class Student:

    def __init__(self, student_id, student_name, gpa):
        self.student_id = student_id
        self.student_name = student_name
        self.gpa = gpa
        self.credit_limit_for_this_semester = 20
        self.gpa_check_for_credit_limit()
        self.passed_courses = []
        self.semester_courses = []

    def get_passed_courses(self):
        w = ' '
        for x in self.passed_courses:
            a = str(x)
            w = w + a

        return w

    def gpa_check_for_credit_limit(self):
        if self.gpa > 2.5:
            self.credit_limit_for_this_semester = 30

    def set_passed_courses(self, passed_course):
        self.passed_courses.append(passed_course)

    def count_credits_per_semester(self):
        total_credits_per_semester = 0
        for x in self.semester_courses:
            total_credits_per_semester += x.course_credit

        return total_credits_per_semester

    def add_course(self, obj_1):

        if self.count_credits_per_semester() + obj_1.course_credit > self.credit_limit_for_this_semester:
            print('You dont have enough credit')
            return

        if obj_1.prerequisite is not None:
            if obj_1.prerequisite not in self.passed_courses:
                print('you have to take prerequsite class')
                return

        if obj_1.find_technical_course() == 5:
            if obj_1.is_eligible(self.gpa) == True:
                print('Not eligible for technical course')
                return

        self.semester_courses.append(obj_1)


    def get_str_semester_courses(self):
        get_courses_str = ' '
        for x in self.semester_courses:
            a = str(x)
            get_courses_str = get_courses_str + a

        return get_courses_str

    def __str__(self):
        return 'Studen ID:{:d}\nStudent Name:{:s}\nStudent GPA:{:.2f}\n'\
               'Credit Limit For This Semester:{:d}\n\nPassed Courses:\n{}\n\nSemester Courses:\n{}'\
            .format(self.student_id, self.student_name, self.gpa, self.credit_limit_for_this_semester, self.get_passed_courses(), self.get_str_semester_courses())



student_1 = Student(111, 'igal', 3.0)

c_113 = Course('CS 113', 8, 113)
c_114 = Course('CS 114', 6, 114)
c_114.set_prerequisite(c_113)
c_154 = TechnicalElectiveCourse('CS 154', 7, 154, 2.5)
c_221 = Course('CS 221', 7, 221)
c_225 = Course('CS 225', 3, 225)
c_225.set_prerequisite(c_113)


list_of_c = [c_113, c_114, c_154, c_221, c_225]

while True:
    print('CLASS LIST: c_113 (1), c_114 (2), c_154 (3), c_221 (4), c_225 (5)')
    w = input('(A)dd Class, (P)assed, (B)reak, (D)isplay:')
    if w == 'A':
        add_course = int(input('Add Course Num:'))
        add_course = add_course - 1
        student_1.add_course(list_of_c[add_course])

    elif w == 'P':
        passed_course = int(input('Passed Course:'))
        passed_course = passed_course - 1
        student_1.set_passed_courses(list_of_c[passed_course])

    elif w == 'D':
        print(student_1)

    elif w == 'B':
        print(student_1)
        break