index = 0
less_than50 = 0
more_than50 = 0
while index < list_length:
	marks = student_marks[index]
	if marks < 50:
		less_than50 = less_than50 + 1
	else:
		more_than50 = more_than50 + 1
	index = index + 1
print "Marks more than 50: " + str(more_than50)
print "Marks less than 50: " + str(less_than50)
