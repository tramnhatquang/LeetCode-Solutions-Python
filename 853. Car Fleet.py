class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Sort cars by the start positions pos
        # Loop on each car from the end to the beginning
        # Calculate its time needed to arrive the target
        # cur records the current biggest time (the slowest)

        # If another car needs less or equal time than cur,
        # it can catch up this car fleet.

        # If another car needs more time,
        # it will be the new slowest car,
        # and becomes the new lead of a car fleet.

        # calculate the needed times for each car to arrive at the target in the
        times = [float(target - p)/s for p, s in sorted(zip(position, speed))]

        curr_time = res = 0
        for time in times[::-1]:
            if time > curr_time:
                res += 1  # increase the car fleet
                curr_time = time

        return res

        # time: O(n log n) for sorting, O(n) in the loop, TC is O(n log n), n is length of pos
        # space: O(n)
