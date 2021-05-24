class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''def solveNQueens(self, n: int) -> [[str]]:
        if 1 < n < 9: return
        for i in range(0, n-1):
            for j in range(0, n-1):
       '''

    def isValid(self, s: str) -> bool:
        inner = "([{"
        outer = ")]}"

        for i in range(len(s)):
            if s[i] not in inner: continue
            for j in range(i, len(s)):


        return True

    def longestCommonPrefix(self, strs: [str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            while strs[i] != prefix:
                print("HERE")
                prefix = prefix[0:len(prefix)-1]

        return prefix

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        count = 0
        while head.next is not None:
            count += 1

    def reverse(self, x: int) -> int:
        new = str(abs(x))
        new = new.strip()
        new = new[::-1]
        output = int(new)

        if output >= 2 ** 31 - 1 or output <= -2 ** 31:
            return 0
        elif x < 0:
            return -1 * output
        else:
            return output

    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


test = Solution()

testing = "TESTING"



#print(test.longestCommonPrefix(["flower", "flow", "flight"]))
