if __name__ == '__main__':
    student = []
    scores = []
    min_student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])

    for i in student:
        scores.append(i[1])

    idx = scores.index(min(scores))
    popped_score = scores.pop(idx)
    popped_student = student.pop(idx)

    for i in range(len(scores)):
        if popped_score == min(scores):
            idx = scores.index(min(scores))
            popped_score = scores.pop(idx)
            popped_student = student.pop(idx)
        else:
            break

    idx = scores.index(min(scores))
    for i in range(len(scores)):
        if scores[idx] == student[i][1]:
            min_student.append(student[i][0])
    min_student.sort()
    for i in min_student:
        print(i+'')
