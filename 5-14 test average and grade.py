def main():
    first_test_score = int(input("Enter the first test score: "))
    second_test_score = int(input("Enter the second test score: "))
    third_test_score = int(input("Enter the third test score: "))
    fourth_test_score = int(input("Enter the fourth test score: "))
    fifth_test_score = int(input("Enter the fifth test score: "))
    calc_average = average(first_test_score, second_test_score, third_test_score, fourth_test_score, fifth_test_score)
    print(f"The average is {calc_average:.2f}")
    determine_grade = grade(first_test_score, second_test_score, third_test_score, fourth_test_score, fifth_test_score)
def average(grade1, grade2, grade3, grade4, grade5):
    return (grade1 + grade2 + grade3 + grade4 + grade5) / 5
def grade(grade1, grade2, grade3, grade4, grade5):
    for grade in [grade1, grade2, grade3, grade4, grade5]:
        if grade >= 90 and grade <= 100:
            print("A")
        elif grade >=80 and grade <= 89:
            print("B")
        elif grade >= 70 and grade <=79:
            print("C")
        elif grade >= 60 and grade <= 69:
            print("D")
        elif grade < 60:
            print("F")
main()

