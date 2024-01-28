class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s2 = s
        s1 = p
        hashstore = {}
        found = {}
        for c in s1:
            hashstore[c] = hashstore.get(c, 0) + 1
        startIndex = 0
        maxLen = 0
        matched = 0
        matchedList = []
        for window_end in range(len(s2)):
            right_char = s2[window_end]

            if right_char in hashstore:
                hashstore[right_char] -= 1

                if hashstore[right_char] == 0:
                    matched += 1

                if matched == len(hashstore):
                    matchedList.append(startIndex)

            if window_end >= len(s1) - 1:
                left_char = s2[startIndex]

                if left_char in hashstore:
                    if hashstore[left_char] == 0:
                        matched -= 1
                    hashstore[left_char] += 1

                startIndex += 1

        return matchedList