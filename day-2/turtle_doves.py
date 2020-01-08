import json


def run_intcode(intcode):
    start = 0
    finish = 4
    while finish <= len(intcode):
        current = intcode[start:finish]
        if current[0] == 99:
            finish = len(intcode) + 1
            return intcode
        if current[0] == 1:
            intcode[current[3]] = intcode[current[1]] + intcode[current[2]]
            start += 4
            finish = start + 4
            continue
        if current[0] == 2:
            intcode[current[3]] = intcode[current[1]] * intcode[current[2]]
            start += 4
            finish = start + 4
            continue

    return intcode


with open('./intcode.json', 'r') as f:
    raw = f.read()
    original = json.loads(raw)

    for noun in range(100):
        for verb in range(100):
            intcode = original[:]

            intcode[1] = noun
            intcode[2] = verb

            result = run_intcode(intcode)

            if result[0] == 19690720:
                print(result[0])
                print(100 * noun + verb)
            verb += 1
        noun += 1
