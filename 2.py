def parse_record(record):
    
    record = record.split(': ')
    game = record[0].split(' ')[1]

    cubes_seen = []
    for samples in record[1:]:
        for reveals in samples.split('; '):
            for cubes in reveals.split(', '):
                cubes_seen.append(cubes)
    
    return game, cubes_seen

def check_cubes(game, cubes_seen):
    check = {
        'red': 12,
        'green': 13,
        'blue': 14
    }  
    
    for reveal in cubes_seen:
        num, color = reveal.split(' ')
        
        if check[color] >= int(num):
            win = True
        else:
            win = False
            break

    if win:
        return int(game)
    else:
        return 0
    
log = {}
def find_max_cubes(game, cubes_seen):
    dict = {}
    for reveal in cubes_seen:
        num, color = reveal.split(' ')
        if color in dict:
            if int(num) > dict[color]:
                dict[color] = int(num)
        else:
            dict[color] = int(num)
    log[int(game)] = dict
    
    return log

def score_log(log):
    score = 0
    for val in log.values():
        power = 1
        for val2 in val.values():
            power *= val2
        score += power

    return score

def main():

    with open("inputs/2.txt") as f:
        game_records = f.read()

    records  = game_records.split('\n')

    sum = 0
    for record in records:
        game, cubes_seen = parse_record(record)
        sum += check_cubes(game, cubes_seen)
        log = find_max_cubes(game, cubes_seen)

    print(sum, score_log(log))

if __name__ == '__main__':
    main()