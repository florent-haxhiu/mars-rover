class Rover:
    def execute(
        self, command: str, obstacles: list[tuple[int, int]] | None = None
    ) -> str:
        x = 0
        y = 0
        direction = 1

        compass_dir = {1: "N", 2: "E", 3: "S", 4: "W"}

        for move in command:
            if move == "M":
                if direction % 4 == 1:
                    y += 1
                elif direction % 4 == 2:
                    x += 1
                elif direction % 4 == 3:
                    y -= 1
                else:
                    x -= 1
            else:
                if move == "R":
                    direction += 1
                else:
                    direction -= 1
            if obstacles:
                for obs in obstacles:
                    if (x, y) == obs:
                        direction %= 4
                        match direction:
                            case 1:
                                y -= 1
                            case 2:
                                x -= 1
                            case 3:
                                y += 1
                            case 4:
                                x += 1
                        return f"Hit: {x}:{y}:{compass_dir[direction]}"

        x %= 10
        y %= 10
        direction %= 4

        return f"{x}:{y}:{compass_dir[direction]}"
