def solution_part1(input_file):
  file = open(input_file, "r")
  result = 0

  for line in file:
    digits = [char for char in line if char.isdigit()]
    result += int(digits[0] + digits[-1])

  return result


def solution_part2(input_file):
  file = open(input_file, "r")
  result = 0
  numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

  for line in file:
    digits = []

    for i, char in enumerate(line):
      if char.isdigit():
        digits.append(char)

      for j, value in enumerate(numbers):
        if line[i:].startswith(value):
          digits.append(str(j + 1))

    result += int(digits[0] + digits[-1])

  return result


input_file = "day1/day1_input.txt"
print(f"Result Part 1: {solution_part1(input_file)}")
print(f"Result Part 2: {solution_part2(input_file)}")
