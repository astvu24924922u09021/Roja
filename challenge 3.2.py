def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa


def sort_student(student_list):
  
  sorted_student=sorted(student_list,
                        key=lambda student: student.cgpa,
                        reverse=True)
  
  return sorted_student



student=[
  student("Harikrishnan","A141",7.8),
student("Selvi","A144",7.6),
student("Janani","A145",8.9),
student("Yuva","A143",9.9)
]

sorted_student=sort_student(student)


for student in sorted_student:
  print("Name:{},Roll number:{},CGPA:{}".format(student.name,
                                               student.roll_number,student.cgpa))