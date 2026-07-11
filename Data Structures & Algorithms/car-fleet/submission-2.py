class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        fleet = []

        for position, speed in cars:
            time_to_target = (target - position) / speed
            if not fleet or time_to_target > fleet[-1]:
                fleet.append(time_to_target)

        return len(fleet)

