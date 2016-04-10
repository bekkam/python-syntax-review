from collections import OrderedDict


class Gradebook(object):
    """Gradebook class to store list of test grades"""

    def __init__(self, course_name, grades):
        """Two argument constructor initializes course_name and grades list"""

        self.course_name = course_name
        self.grades = grades

    def display_message(self):
        """Display a welcome message to the Gradebook user"""

        print "\n################################################"
        print "Welcome to the grade book for \n%s!\n" % self.course_name

    def get_minimum(self):
        """Find minimum grade"""

        low_grade = self.grades[0]

        for grade in self.grades:
            if grade < low_grade:
                low_grade = grade

        return low_grade

    def get_maximum(self):
        """Find the maximum grade"""

        high_grade = self.grades[0]

        for grade in self.grades:
            if grade > high_grade:
                high_grade = grade

        return high_grade

    def get_average(self):
        """Determine average grade for test"""

        total = 0

        for grade in self.grades:
            total += grade

        return total/len(self.grades)

    def output_bar_chart(self):
        """Output a bar chart showing grade distribution"""

        print "Grade distribution:"

        frequency = OrderedDict()
        frequency = {n: 0 for n in range(0, 11)}

        # for each grade, increment appropriate frequency
        for grade in self.grades:
            frequency[grade/10] = frequency.get(grade/10) + 1

        # for each frequency, print bar chart
        for key, value in frequency.items():
            star = "*" * value
            if key == 10:
                print "100: " + star
            else:
                print "%d - %d: " % (key * 10, key * 10 + 9) + star

        print "\n"

    def output_grades(self):
        """Output the contents of the grades list"""

        for grade, index in enumerate(self.grades):
            print "Student %d:  %d" % (index + 1, self.grades[grade])

    def process_grades(self):
        """Perform various operations on the grade data"""

        self.output_grades()

        # Get the average
        print "\nClass average is %d" % self.get_average()

        # Call methods get_maximum and get_minimum
        print "Lowest grade is %d\nHighest grade is %d\n" % (self.get_minimum(), self.get_maximum())

        self.output_bar_chart()


def main():
    grades = [87, 68, 94, 55, 83, 78, 85, 91, 76, 87]
    my_gradebook = Gradebook("Math", grades)
    my_gradebook.display_message()
    my_gradebook.process_grades()

if __name__ == '__main__':
    main()
