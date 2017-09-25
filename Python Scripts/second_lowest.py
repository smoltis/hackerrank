def find_second_lowest_score(students):
    scores = sorted(set([s[1] for s in students]))
    return scores[0] if len(scores) == 1 else scores[1]

if __name__ == '__main__':
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    score = find_second_lowest_score(students)
    names = sorted([name[0] for name in filter(lambda x: x[1]==score, students)])
    print(*names, sep='\n')