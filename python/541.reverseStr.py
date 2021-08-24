class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        t = list(s)
        for i in range(0, len(t), 2 * k):
            t[i: i + k] = reversed(t[i: i + k])
        return "".join(t)

    def reverseStrOptimize(self, s: str, k: int) -> str:
        return ''.join(''.join(reversed(list(t[:k])))+t[k:] for t in iter(s[i:i+2*k] for i in range(0, len(s), 2*k)))