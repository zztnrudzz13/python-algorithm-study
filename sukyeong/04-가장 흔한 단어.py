import re

# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]

# paragraph = "a, a, a, a, b,b,b,c, c"
# banned = ['a']
#
# paragraph = paragraph.lower()
# paragraph = re.sub('[^a-z]+', ' ', paragraph)
#
#
# paragraph_list = paragraph.split()
# paragraph_no_banned_list = list(filter(lambda x: x not in banned, paragraph_list))
#
# # 중복 요소 세기
# count = {}
# for i in paragraph_no_banned_list:
#     try: count[i] += 1
#     except: count[i] = 1
#
# result = max(count, key=count.get)
# print(result)

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-z]+', ' ', paragraph)

        paragraph_list = paragraph.split()
        paragraph_no_banned_list = list(filter(lambda x: x not in banned, paragraph_list))

        # 중복 요소 세기
        count = {}
        for i in paragraph_no_banned_list:
            try:
                count[i] += 1
            except:
                count[i] = 1

        result = max(count, key=count.get)
        return result

