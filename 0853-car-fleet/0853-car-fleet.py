class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        fleets = 0
        while len(time) > 1:
            lead = time.pop()
            if lead < time[-1]:
                fleets += 1
            else:
                time[-1] = lead
        return fleets + bool(time)