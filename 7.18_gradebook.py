"""Gradebook class using nested lists to store grades"""

from collections import OrderedDict


class Gradebook(object):

    def __init__(self, course_name, grades):

        self.course_name = course_name
        self.grades = grades

    def display_message(self):
        """Display a welcome message to the Gradebook user"""

        print "\n################################################"
        print "Welcome to the grade book for \n%s!\n" % self.course_name

    def get_minimum(self):
        """Find minimum grade"""

        # original:
        # low_grade = self.grades[0][0]

        # for student, grade in enumerate(self.grades):
        #     for grade in self.grades[student]:
        #         if grade < low_grade:
        #             low_grade = grade


        # more pythonic:
        # low_grade = self.grades[0][0]

        # for row in self.grades:
        #     if min(row) < low_grade:
        #         low_grade = min(row)

        # with list comprehension:
        # low_grade = min([min(row) for row in self.grades])

        # with generator-expression:
        low_grade = min(min(row) for row in self.grades)

        return low_grade

    def get_maximum(self):
        """Find the maximum grade"""

        # original:
        # high_grade = self.grades[0][0]

        # for student, grade in enumerate(self.grades):
        #     for grade in self.grades[student]:
        #         if grade > high_grade:
        #             high_grade = grade

        # more pythonic:
        # for row in self.grades:
        #     if max(row) > high_grade:
        #         high_grade = max(row)

        # with generator expression:
        high_grade = max(max(row) for row in self.grades)
        return high_grade

    def get_average(self, r):
        """Determine average grade for test"""

        # original:
        # initialize total to a float to retain float for average calculation
        # total = 0.00

        # for grade in self.grades[r]:
        #     total += grade

        # concise:
        total = float(sum(self.grades[r]))

        return total/(len(self.grades[r]))

    def output_bar_chart(self):
        """Output a bar chart showing overall grade distribution"""

        print "\nOverall grade distribution:"

        frequency = OrderedDict()
        frequency = {n: 0 for n in range(0, 11)}

        # original:
        # for each student's grades
        # for each grade, increment appropriate frequency
        for grades in self.grades:
            for grade in grades:
                frequency[grade/10] = frequency.get(grade/10) + 1

        # for each frequency, print bar chart
        for key, value in frequency.items():
            star = "*" * value
            if key == 10:
                print "%5d:" % 100, star
            else:
                print "%02d-%02d: " % (key * 10, key * 10 + 9) + star

        print "\n"

    def output_grades(self):
        """Output the contents of the grades list"""

        print "The grades are:\n"
        print "            ",

        # create column heading for each of the tests
        for test in self.grades[0]:
            print "Test %d  " % (test + 1),
        print "Average"

        # create rows/columns of text representing array grades
        for index, students in enumerate(self.grades):
            print "Student %2d" % (index + 1),
            for grade in students:
                print "%8d" % grade,

            # call get_average to caclulate student's average grade; pass row
            # of grades as the argument to get_average
            average = self.get_average(index)
            print "%9.2f" % average

    def process_grades(self):
        """Perform various operations on the grade data"""

        self.output_grades()

        # Call methods get_maximum and get_minimum
        print "\nHighest grade in grade book is %d" % self.get_maximum()
        print "Lowest grade in grade book is %d" % self.get_minimum()

        self.output_bar_chart()


def main():
    grades = [
        [87, 96, 70],
        [68, 87, 90],
        [94, 100, 90],
        [100, 81, 82],
        [83, 65, 85],
        [78, 87, 65],
        [85, 75, 83],
        [91, 94, 100],
        [76, 72, 84],
        [87, 93, 73]
    ]
    my_gradebook = Gradebook("Math", grades)
    my_gradebook.display_message()
    my_gradebook.process_grades()

if __name__ == '__main__':
    main()
