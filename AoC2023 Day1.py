import re

file = open("Day1 input.txt", "r")
lines = file.readlines()
file.close()


def sum_calibration_value(part2):
    sum_calibration = 0
    substring_pattern = r'\b(one|two|three|four|five|six|seven|eight|nine)'
    substring_pattern_1 = r"one"
    substring_pattern_2 = r"two"
    substring_pattern_3 = r"three"
    substring_pattern_4 = r"four"
    substring_pattern_5 = r"five"
    substring_pattern_6 = r"six"
    substring_pattern_7 = r"seven"
    substring_pattern_8 = r"eight"
    substring_pattern_9 = r"nine"

    word_to_digit = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    for line in lines:
        line = line.strip()
        if part2:
            matches = re.findall(substring_pattern, line)
            # matches += re.findall(substring_pattern_2, line)
            # matches += re.findall(substring_pattern_3, line)
            # matches += re.findall(substring_pattern_4, line)
            # matches += re.findall(substring_pattern_5, line)
            # matches += re.findall(substring_pattern_6, line)
            # matches += re.findall(substring_pattern_7, line)
            # matches += re.findall(substring_pattern_8, line)
            # matches += re.findall(substring_pattern_9, line)

            for match in matches:
                line = line[:line.find(match)] + word_to_digit[match] + line[line.find(match) + 1:]
        numbers = re.findall(r"\d", line)
        sum_calibration += (int(numbers[0] + numbers[-1]))
    return sum_calibration


print(sum_calibration_value(False))
print(sum_calibration_value(True))

# wrong answers
# 46619
# 45939
# 45969
# 46040
# 45980
# 54569
# 54558
# 54208
# 55327
# 54588
