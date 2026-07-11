class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))

        # Sort cars from closest to the target to farthest
        cars.sort(reverse=True)

        stack = []

        for pos, spd in cars:
            time_to_target = (target - pos) / spd

            # A larger time means this car cannot catch the fleet ahead
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)

            # Otherwise, it catches the fleet ahead and joins it

        return len(stack)