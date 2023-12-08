def solution_part1(input_file):
  file = open(input_file, "r")
  result = 0
  max_red = 12
  max_green = 13
  max_blue = 14

  for line in file:
    game_name, game = line.split(": ")
    game_id = int(game_name.split()[1])
    rounds = game.split("; ")
    game_possible = True

    for round in rounds:
      cubes = round.split(", ")
      for cube in cubes:
        num = int(cube.split()[0])
        color = cube.split()[1].replace("\n", "")

        if (
            color == "red" and num > max_red or
            color == "green" and num > max_green or
            color == "blue" and num > max_blue
          ):
          game_possible = False

    if game_possible == True:
      result += game_id

  return result


def solution_part2(input_file):
  file = open(input_file, "r")
  result = 0

  for line in file:
    game = line.split(": ")[1]
    rounds = game.split("; ")
    min_red = 0
    min_green = 0
    min_blue = 0

    for round in rounds:
      cubes = round.split(", ")

      for cube in cubes:
        num = int(cube.split(" ")[0])
        color = cube.split(" ")[1].replace("\n", "")

        if color == "red" and num > min_red:
          min_red = num

        elif color == "green" and num > min_green:
          min_green = num

        elif color == "blue" and num > min_blue:
          min_blue = num

    result += min_red * min_blue * min_green

  return result


input_file = "day2/day2_input.txt"
print(f"Result Part 1: {solution_part1(input_file)}")
print(f"Result Part 2: {solution_part2(input_file)}")
