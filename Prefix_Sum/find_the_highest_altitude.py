class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0] * (len(gain) + 1)
        for i, g in enumerate(gain):
            altitudes[i + 1]  = altitudes[i] + g
        return max(altitudes)
