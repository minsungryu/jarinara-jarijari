# -*- coding: utf-8 -*-

import random
import math
from collections import namedtuple

class SeatGenerator:
    DIRECTION = 4
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    OverflowedTeam = namedtuple('Team', 'team4 team5')
    Point = namedtuple('Point', 'x y')

    def __init__(self, number_of_seats, number_of_teams, seat_column):
        self.number_of_seats = number_of_seats
        self.number_of_teams = number_of_teams
        self.seat_column = seat_column
        self.seat_row = int(math.floor(self.number_of_seats / self.seat_column))

    def rand(self, max):
        return random.randrange(0, max)

    def inRange(self, point):
        return 0 <= point.x < self.seat_column and 0 <= point.y < self.seat_row

    def toDeskNumber(self, point):
        return 1 + point.x + (point.y * self.seat_column)

    def shuffleSeats(self):
        self.seats = dict()

        # 2인 자리를 랜덤하게 결정
        seat_pivot = self.Point(self.rand(self.seat_column), self.rand(self.seat_row))
        self.seats[seat_pivot] = 0

        # 경우의 수를 검사
        while True:
            self.teams = range(1, 2) + range(3, 9)
            # 4조와 5조의 상대 위치를 결정(0번은 4조의 방향, 1번은 5조의 방향)
            direction = self.OverflowedTeam(self.rand(self.DIRECTION), self.rand(self.DIRECTION))

            if len(set(direction)) is 1:
                continue

            findFlag = True
            team = 4
            for _direction in direction:
                team_point = self.Point(seat_pivot.x + self.dx[_direction], seat_pivot.y + self.dy[_direction])

                if not self.inRange(team_point):
                    findFlag = False
                    break

                self.seats[team_point] = team
                del(self.teams[2])
                team += 1

            if findFlag:
                break
        
        # 나머지 랜덤 배치
        random.shuffle(self.teams)
        while len(self.seats) < self.number_of_seats:
            rand_seat = self.Point(self.rand(self.seat_column), self.rand(self.seat_row))

            if rand_seat in self.seats:
                continue
            
            if not self.inRange(rand_seat):
                continue 
            
            self.seats[rand_seat] = self.teams.pop()

        result = [ [-1, -1, -1, -1], [-1, -1, -1, -1] ]
        for position in self.seats:
            result[position.y][position.x] = self.seats[position]

        return result