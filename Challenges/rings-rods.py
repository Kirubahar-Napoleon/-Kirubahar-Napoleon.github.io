class Solution:
    def countPoints(self, rings: str) -> int:
        rod = [set() for _ in range(10)]
        Iter = len(rings)
        for i in range (0, Iter, 2):
            color = rings[i]
            rodnum = int(rings[i+1])
            rod[rodnum].add(color)
        return sum(len(s)==3 for s in rod)

