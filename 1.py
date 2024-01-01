def get_numbers(line):

    num_dict = {
        'one':'1','two':'2','three':'3','four':'4','five':'5',
        'six':'6','seven':'7','eight':'8','nine':'9'
        }

    nums = []
    for key, val in num_dict.items():
        ix = 0
        while ix < len(line) and line.find(key,ix)>-1:
            nums.append((line.find(key, ix), val))
            ix = (line.find(key, ix) + len(key)-1)

    return nums

def get_calibration(lines):

    count = 0
    for line in lines:
        line_nums = []
        nums = get_numbers(line)
        if nums:
            for num in nums:
                line_nums.append(num)

        for ix, char in enumerate(line):
            if char.isdigit():
                line_nums.append((ix, char))

        values = sorted(line_nums, key=lambda tup:tup[0])

        if len(values) == 1:
            count += int(values[0][1] + values[0][1])
        else:
            count += int(values[0][1] + values[-1][1])

    return count

def main():

    with open("inputs/1.txt") as f:
        calibration_document = f.read()

    lines = calibration_document.split()

    print(get_calibration(lines))

if __name__ == '__main__':
    main()