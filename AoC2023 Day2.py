file = open("Day2 input.txt", "r")
lines = file.readlines()
file.close()


def game_possible(max_red, max_green, max_blue):
    sum2 = 0
    sum_game_numbers = 0
    for line in lines:
        parts = line.split(":")
        game_number = parts[0].split(" ")[1]

        parts = parts[1].split(";")

        red = 0
        blue = 0
        green = 0

        for part in parts:

            rounds = part.split(",")
            for round in rounds:
                round = round.strip()
                number, color = round.split(" ")
                number = int(number)

                if "green" in round:
                    if number > green:
                        green = number

                elif "red" in round:
                    if number > red:
                        red = number

                elif "blue" in round:
                    if number > blue:
                        blue = number

        if blue <= max_blue and red <= max_red and green <= max_green:
            sum_game_numbers += int(game_number)

        sum2 = sum2 + (blue * red * green)

    return sum_game_numbers, sum2


print(game_possible(12, 13, 14))
