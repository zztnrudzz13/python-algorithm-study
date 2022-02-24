# str_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
# split_list = []
# anagram_list = []
#
# for str in str_list:
#     split_str = sorted(list(str))
#     if split_str in split_list:
#         num = split_list.index(split_str)
#         anagram_list[num].append(str)
#         print(split_list.index(split_str))
#     else:
#         split_list.append(split_str)
#         anagram_list.append([])
#         anagram_list[-1].append(str)
#         print(split_list)
#         print(anagram_list)


class Solution(object):
    def groupAnagrams(self, strs):
        split_list = []
        anagram_list = []
        for str in strs:
            split_str = sorted(list(str))
            if split_str in split_list:
                num = split_list.index(split_str)
                anagram_list[num].append(str)
            else:
                split_list.append(split_str)
                anagram_list.append([])
                anagram_list[-1].append(str)
        return anagram_list

