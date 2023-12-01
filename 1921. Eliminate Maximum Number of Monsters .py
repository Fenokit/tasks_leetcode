# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        """
        Finds the maximum number of monsters killed.
        """
        total_steps = [el / speed[index_el] for index_el, el in enumerate(dist)]
        total_steps.sort()

        for index, el in enumerate(total_steps):
            if index >= el:
                return index
        return len(total_steps)


if __name__ == '__main__':
    dist = list(map(int, input().split()))
    speed = list(map(int, input().split()))
    a = Solution()
    print(a.eliminateMaximum(dist, speed))
