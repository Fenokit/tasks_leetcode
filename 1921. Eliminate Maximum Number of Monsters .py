# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        """
        Finds the maximum number of monsters killed.
        """
        total_steps = [el / speed[index_el] for index_el, el in enumerate(dist)]
        total_steps.sort(reverse=True)
        num = 0
        while True:
            if not total_steps:
                return num if num > 0 else 1
            for x in total_steps:
                if x <= 0:
                    return num if num > 0 else 1
            x = 1
            if len(total_steps) > 1000 and total_steps[-1] > 1000:
                x = 1000
            elif len(total_steps) > 100 and total_steps[-1] > 100:
                x = 100
            elif len(total_steps) > 10 and total_steps[-1] > 10:
                x = 10

            num += x
            total_steps = [y - x for y in total_steps[:-x]]


if __name__ == '__main__':
    dist = list(map(int, input().split()))
    speed = list(map(int, input().split()))
    a = Solution()
    print(a.eliminateMaximum(dist, speed))
