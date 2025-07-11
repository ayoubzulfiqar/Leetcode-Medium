class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def get_average_score(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

class ClassPerformance:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise TypeError("Only Student objects can be added.")

    def get_class_average(self):
        if not self.students:
            return 0.0
        total_average_scores = 0.0
        for student in self.students:
            total_average_scores += student.get_average_score()
        return total_average_scores / len(self.students)

    def get_student_performance(self):
        performance_data = []
        for student in self.students:
            performance_data.append({
                "name": student.name,
                "average_score": student.get_average_score()
            })
        return performance_data