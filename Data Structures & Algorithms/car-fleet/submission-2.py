from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(key=lambda x: x[0], reverse=True) ## sort by postion descending
        cars = deque(cars)
        out = 0

        def car_can_catch(car_1_pos, car_1_speed, car_2_pos, car_2_speed):
            return ((target - car_1_pos) / car_1_speed) >= ((target - car_2_pos) / car_2_speed)
        
        while len(cars) > 1:
            car_1, car_2 = cars.popleft(), cars.popleft()
            car_1_pos, car_1_speed = car_1[0], car_1[1]
            car_2_pos, car_2_speed = car_2[0], car_2[1]

            if not car_can_catch(car_1_pos, car_1_speed, car_2_pos, car_2_speed):
                ## then car_2 never catch to car_1
                out += 1
                cars.appendleft((car_2_pos, car_2_speed))
            else:
                ## if two cars can merge
                cars.appendleft((car_1_pos, car_1_speed))

        return out + len(cars)