# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

# logs_digit = list(filter(lambda x: x[-1].isdigit() == True, logs))
# logs_alpha = list(filter(lambda x: x[-1].isalpha() == True, logs))
#
# new_logs_alpha = []
# result_logs_alpha = []
# for i in range(len(logs_alpha)):
#     new_logs_alpha.append(logs_alpha[i].split(maxsplit=1))
#     new_logs_alpha.sort(key=lambda x: (x[1], x[0]))
#
# for i in range(len(new_logs_alpha)):
#     result_logs_alpha.append(' '.join(new_logs_alpha[i]))
#
# print(result_logs_alpha + logs_digit)


class Solution(object):
    def reorderLogFiles(self, logs):
        logs_digit = list(filter(lambda x: x[-1].isdigit() == True, logs))
        logs_alpha = list(filter(lambda x: x[-1].isalpha() == True, logs))

        new_logs_alpha = []
        result_logs_alpha = []
        for i in range(len(logs_alpha)):
            new_logs_alpha.append(logs_alpha[i].split(' ', 1))
            new_logs_alpha.sort(key=lambda x: (x[1], x[0]))

        for i in range(len(new_logs_alpha)):
            result_logs_alpha.append(' '.join(new_logs_alpha[i]))

        return result_logs_alpha + logs_digit