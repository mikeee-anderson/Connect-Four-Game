class GameBoard:
    def __init__(self, size):
        self.size = size
        self.num_disks = [0] * size
        self.items = [[0] * size for i in range(size)]
        self.points = [0] * 2

    def num_free_positions_in_column(self, column):
        return self.size - self.num_disks[column]

    def game_over(self):
        return all(self.num_disks[column] == self.size for column in range(self.size))

    def display(self):
        for row in range(self.size - 1, -1, -1):
            for col in range(self.size):
                if self.items[col][row] == 0:
                    print(" ", end=" ")
                elif self.items[col][row] == 1:
                    print("o", end=" ")
                else:
                    print("x", end=" ")
            print()

        print("-" * (self.size * 2 - 1))
        print(" ".join(str(i) for i in range(self.size)))
        print(f"Points player 1: {self.points[0]}")
        print(f"Points player 2: {self.points[1]}")

    def num_new_points(self, column, row, player):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        new_points = 0

        for dx, dy in directions:
            count = 1
            for i in range(1, 4):
                x, y = column + i * dx, row + i * dy
                if 0 <= x < self.size and 0 <= y < self.size and self.items[x][y] == player:
                    count += 1
                else:
                    break
            for i in range(1, 4):
                x, y = column - i * dx, row - i * dy
                if 0 <= x < self.size and 0 <= y < self.size and self.items[x][y] == player:
                    count += 1
                else:
                    break
            if count >= 4:
                new_points += count - 3  # Count all possible 4-in-a-row combinations

        return new_points

    def add(self, column, player):
        if column < 0 or column >= self.size or self.num_disks[column] >= self.size:
            return False

        row = self.num_disks[column]
        self.items[column][row] = player
        self.num_disks[column] += 1

        new_points = self.num_new_points(column, row, player)
        self.points[player - 1] += new_points

        return True

    def free_slots_as_close_to_middle_as_possible(self):
        middle = (self.size - 1) / 2
        free_slots = [col for col in range(self.size) if self.num_free_positions_in_column(col) > 0]
        return sorted(free_slots, key=lambda x: (abs(x - middle), x))

    def column_resulting_in_max_points(self, player):
        max_points = 0
        best_column = -1
        free_slots = self.free_slots_as_close_to_middle_as_possible()

        for column in free_slots:
            row = self.num_disks[column]
            points = self.num_new_points(column, row, player)

            if points > max_points:
                max_points = points
                best_column = column
            elif points == max_points and best_column == -1:
                best_column = column

        if best_column == -1:
            best_column = free_slots[0] if free_slots else 0

        return (best_column, max_points)


class FourInARow:
    def __init__(self, size):
        self.board = GameBoard(size)

    def move_human_player(self, player_number):
        valid_input = False
        while not valid_input:
            try:
                column = int(input("Please input slot: "))
            except ValueError:
                print("Input must be an integer in the range 0 to ", self.board.size - 1)
            else:
                if column < 0 or column >= self.board.size:
                    print("Input must be an integer in the range 0 to ", self.board.size - 1)
                elif self.board.add(column, player_number + 1):
                    valid_input = True
                else:
                    print("Column ", column, "is already full. Please choose another one.")

    def move_ai_player(self, player_number):
        # Choose move which maximises new points for computer player
        (best_column, max_points) = self.board.column_resulting_in_max_points(2)
        if max_points > 0:
            column = best_column
        else:
            # if no move adds new points choose move which minimises points opponent player gets
            (best_column, max_points) = self.board.column_resulting_in_max_points(1)
            if max_points > 0:
                column = best_column
            else:
                # if no opponent move creates new points then choose column as close to middle as possible
                column = self.board.free_slots_as_close_to_middle_as_possible()[0]
        self.board.add(column, player_number + 1)
        print("The AI chooses column ", column)

    def play(self):
        print("*****************NEW GAME*****************")
        self.board.display()
        player_number = 0
        print()
        while not self.board.game_over():
            print("Player ", player_number + 1, ": ")
            if player_number == 0:
                self.move_human_player(player_number)
            else:
                self.move_ai_player(player_number)
            self.board.display()
            player_number = (player_number + 1) % 2
        if (self.board.points[0] > self.board.points[1]):
            print("Player 1 (circles) wins!")
        elif (self.board.points[0] < self.board.points[1]):
            print("Player 2 (crosses) wins!")
        else:
            print("It's a draw!")


game = FourInARow(6)
game.play()