import statistics
def view_grade():
  student= ['Musa', 'Adeola', 'Khalid','yemi','cardozo','yaradua', 'wale', 'kemi', 'ghandhishow','elon']
  Grade=[24,26,27,28, 20,18,21,25,30,15]
  gradebook=list(zip(student, Grade))
  average_grade= statistics.mean(Grade)
  highest_grade= max(Grade)
  lowest_grade= min(Grade)
  Grade_maxi_mini= (highest_grade, lowest_grade)
  reverse_name=student[::-1]

  value= {"Grade book ": gradebook, 
          "Average Grade" : average_grade, 
          "Highest and lowest grade": Grade_maxi_mini, "student name ":student,"half reversed name" :reverse_name[0:5]}
  return value
stud= ['Musa', 'Adeola', 'Khalid','yemi','cardozo','yaradua', 'wale', 'kemi', 'ghandhishow','elon']
grd=[24,26,27,28, 20,18,21,25,30,15]
value= view_grade ()

print((value))
  
