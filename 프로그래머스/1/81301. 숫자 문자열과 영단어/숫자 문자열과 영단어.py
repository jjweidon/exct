import re

def solution(s):
    mapper = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    words = re.findall(r"[0-9]|zero|one|two|three|four|five|six|seven|eight|nine", s)
    for i, word in enumerate(words):
        if word in mapper:
            words[i] = mapper[word]
    
    return int(''.join(words))
    