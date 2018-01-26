class Solution:
    def removeDuplicates(self, nums):
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                count += 1
                nums[count] = nums[i]
        return nums

    def strStr(self, haystack, needle):
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

    def findSubstring(self, s, words):
        result_list, word_map = [], {}
        for word in words:
            word_map[word] = word_map.get(word, 0) + 1
        word_len = len(words[0])
        for i in range(len(s)-len(words)*word_len+1):
            j, count = i, len(words)
            tmp = word_map.copy()
            while tmp.get(s[j:j+word_len], 0) > 0:
                tmp[s[j:j+word_len]] -= 1
                j += word_len
                count -= 1
            if count == 0:
                result_list.append(i)
        return result_list

    def lengthOfLongestSubstring(self, s):
        max_len, i = 0, 0
        while i < len(s) - max_len:
            lo, hi = i, len(s)
            while lo+1 < hi:
                next_index = s.find(s[lo], lo+1, hi)
                if next_index != -1:
                    hi = next_index
                lo += 1
            max_len = max(max_len, hi-i)
            i += 1
        return max_len

    def generate_permutation(self, nums):
        result_list = []

        def back_trace(i):
            if i == len(nums)-1:
                result_list.append(nums.copy())
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                back_trace(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        back_trace(0)
        return result_list

    def nextPermutation(self, nums):
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        for k in range(i, (len(nums)+i) // 2):
                            nums[k], nums[len(nums)-1+i-k] = nums[len(nums)-1+i-k], nums[k]
                        break
                break
        else:
            nums.reverse()
        return nums


if __name__ == "__main__":
    solution = Solution()
    print(solution.nextPermutation([3, 5, 4, 2, 1]))