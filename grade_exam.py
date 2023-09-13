def grade_exam():
    # Read the correct answers from a list
    correct_answers = ['B', 'D', 'A', 'A', 'B', 'A', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']
    # Read the student's answers from a student_answers text file
    with open('student_answers.txt', 'r') as file:
        student_answers = file.read().splitlines()
    # Extract the answers from each line in student_answers.txt
    answers_only = [answer.split('.')[1].strip() for answer in student_answers]
    print('answers =', answers_only)
    # Grading the student's exam
    num_correct = 0
    incorrect_indices = []
    correct_indices = []  # List to store question numbers with correct answers
    for i in range(len(correct_answers)):
        if answers_only[i] == correct_answers[i]:
            num_correct += 1
            correct_indices.append(i + 1)
        else:
            incorrect_indices.append(i + 1)

    print("Results:")
    print("--------")
    print("Total number of correctly answered questions:", num_correct)
    print("Total number of incorrectly answered questions:", len(incorrect_indices))
    print("Question numbers with incorrect answers:", incorrect_indices)
    # Display the question numbers with correct answers
    print("Question numbers with correct answers:", correct_indices)
    # Check if the student passed or failed
    if num_correct >= 15:
        print("Congratulations! You passed the exam.")
    else:
        print("Sorry, you failed the exam.")

grade_exam()
