# if __name__ == '__main__':
#     n = int(input())
#     if 2 <= n <= 10:
#         student_marks = {}
#         for i in range(n):
#             name, *line = input().split()
#             print(*line)
#             scores = list(map(float, line))
#             if len(scores) == 3:
#                 student_marks[name] = scores
#         query_name = input()
#         marks = student_marks[query_name]
#         total = 0.0
#         for mark in marks:
#             if 0 <= mark >=100:
#                 total += mark
#         print(f"{total/len(marks):.2f}")

# if __name__ == '__main__':
#     n = int(input())
#     if 2 <= n <= 10:
#         student_marks = {}
#         for i in range(n):
#             name, *line = input().split()
#             scores = list(map(float, line))
#             all_valid = all(0 <= score >= 100 for score in scores)
#             if all_valid and len(scores) == 3:
#                 student_marks[name] = scores
#             else:
#                 break
#         query_name = input()
#         marks = student_marks[query_name]
#         total = 0.0
#         for mark in marks:
#             total += mark
#         print(f"{total / len(marks):.2f}")

if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 10:
        student_marks = {}
        for i in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            valid_list = []
            for score in scores:
                if score <= 100 and score >= 0 :
                    valid_list.append(score)
            if len(valid_list) == 3:
                student_marks[name] = valid_list
        query_name = input()
        marks = student_marks[query_name]
        total = 0.0
        for mark in marks:
            total += mark
        print(f"{total / len(marks):.2f}")