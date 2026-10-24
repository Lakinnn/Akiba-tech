print("*"*5,"Student Performance Analyzer","*"*5)

students= [
{"name":"Sara","score":45},
{"name":"Ahmed","score":70},
{"name":"Hana","score":95}
]


def validate_score(score):
	if score >=0 and score <= 100:
		return score
	else:
		raise ValueError("Score must between 0 and 100.")
		#return 0<= score <= 100

def calc_grade(score):
	if score < 60:
		return "F"
	elif score <70:
		return "D"
	elif score <80:
		return "C"
	elif score < 90:
		return "B"
	else:
		return "A"


def calc_avgScore(students):
	total = count =0
	for student in students:
		total +=student["score"]
		count+= 1
	if count == 0:
		return 0
	else:
		return total / count

def find_high_and_low(students):
	if len(students)== 0:
		return None, None
	high = students[0]["score"]
	low = students[0]["score"]

	for student in students:
		score= student["score"]
		if score > high:
			high = score
		if score < low:
			low= score

	return high ,low

def count_pass_fail(students):
	passed = failed= 0
	for student in students:
		if student["score"] > 50:
			passed += 1
		else:
			failed += 1
	return passed , failed

def generate_report(students):
	if len(students)== 0:
		return "No students record."

	for student in students:
		if not validate_score(student["score"]):
			return "Invalid score for"+ student["name"]

		avg = calc_avgScore(students)
		high, low = find_high_and_low(students)
		passed, failed = count_pass_fail(students)

	print("\n","======Student Results=====")

	print("Name\tScore\tGrade ")
	for student in students:
			name = student["name"]
			score = student["score"]
			grade =calc_grade(score)

			print(f"{name}\t{score}\t\t{grade}")

	print("\n","===== Summary =====")

	print("Average: ", avg)
	print("Highest score: ",high)
	print("Lowest score: ",low)
	print("Passed students: ",passed)
	print("Faild students: ",failed)

	#challenge - above avg

	above_avg= []
	for studnet in students:
		if student["score"] > avg:
			above_avg.append(student["name"])
		if len(above_avg)== 0:
			print( "No student score above the average")
		else:
			for name in above_avg:
				print("\nStudents who scored above the class average: ",name)
		return above_avg


above_avrg= generate_report(students)





