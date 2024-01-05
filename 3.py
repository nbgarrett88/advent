def find_special_chars(line):
    return set([x for x in line if not x.isnumeric()])

def remove_special_chars(line):
    
    for char in find_special_chars(line):
        if not char == '.':
            line = line.replace(char,'.')

    return line

def get_scan_index(line):

    scan_ixs = {}
    nums = []
    ixs = []

    for ix, x in enumerate(line):
        if x.isnumeric():
            nums.append(x)
            ixs.append(ix)
            
            if len(ixs) > 1:
                if ixs[-1]-ixs[-2]>1:
                    scan_ixs[(''.join(nums[:-1])),ixs[0]] = ixs[:-1]
                    nums = nums[-1:]
                    ixs = ixs[-1:]
    if ixs:
        scan_ixs[(''.join(nums)),ixs[0]] = ixs
            
    return scan_ixs

def scan_window(lines, i, num, ix):
    
    pos = [-1,0,1]

    for j in range(len(pos)):
        for k in range(len(pos)):
            if not lines[i+pos[j]][ix+pos[k]].isnumeric():
                if not lines[i+pos[j]][ix+pos[k]] == '.':
                    return int(num[0])
    return 0

def score_rows(lines):

    score = 0
    for i in range(1, len(lines)):

        scan_ixs = get_scan_index(remove_special_chars(lines[i]))
        
        for num, ixs in scan_ixs.items():
            for ix in ixs:
                if ix < len(lines[i])-1:
                    if scan_window(lines, i, num, ix) == 0:
                        continue
                    else:
                        score += scan_window(lines, i, num, ix)
                        break
    return score

def main():

    with open("inputs/3.txt") as f:
        engine_schematic = f.read()

    pad = '.' * len(engine_schematic.split('\n')[0])
    engine_schematic = pad + '\n' + engine_schematic + '\n' + pad
    
    lines = engine_schematic.split('\n')
          
    print(score_rows(lines))
        
if __name__ == '__main__':
    main()