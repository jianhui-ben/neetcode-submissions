class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        
        for heights[i], we need to find its left and right boundary
        which is the nearest height smaller than heights[i]

        we can use a monotonic increasing stack
        when heights[i] < stack[-1], we need to pop stack[-1]
        index i is the right boundary then
        we need to store the left boundary into the stack[-1] somehow
        
        
        each stack element store (start index of the current height, current height)

        add a boundary on two sides:
        [0,7,1,7,2,2,4, 0]

        [(0, 0), (1, 7)]
        1 <= 7 so pop out (1, 7) -> [(0, 0), (1, 1)] and record (2 - 1) * 7 = 7
        [(0, 0), (1, 1), (3, 7)]
        2 <= 7 so pop out (3, 7) -> [(0, 0), (1, 1), (3, 2)] and record (4 - 3) * 7 = 7
        2 <= 2 so pop out (3, 2) -> [(0, 0), (1, 1), (3, 2)] and record (5 - 3) * 2 = 4
        [(0, 0), (1, 1), (3, 2), (6, 4)]
        0 < 4 so pop out (6, 4) -> [(0, 0), (1, 1), (3, 2)] and record (7 - 6) * 4 = 4
        0 < 2 so pop out (3, 2) -> [(0, 0), (1, 1)] and record (7 - 3) *2 = 8 
        ....
        time: O(n)
        space: O(n)

        heights = [0] + heights + [0]
        stack = []
        out = 0
        for i, height in enumerate(heights):
            if not stack or height > stack[-1][1]:
                stack.append((i, height))
            else:
                while stack and stack[-1][1] >= height:
                    leftBoundary, lastMaxHeight = stack.pop()
                    out = max(out, (i - leftBoundary) * lastMaxHeight)
                stack.append((leftBoundary, height))
        return out

        one optimization is to only store the index, instead of a tuple in
        """

        heights = [0] + heights + [0]
        stack = []
        out = 0
        for i, height in enumerate(heights):
            if not stack or height > stack[-1][1]:
                stack.append((i, height))
            else:
                while stack and stack[-1][1] >= height:
                    leftBoundary, lastMaxHeight = stack.pop()
                    out = max(out, (i - leftBoundary) * lastMaxHeight)
                stack.append((leftBoundary, height))
        return out



        