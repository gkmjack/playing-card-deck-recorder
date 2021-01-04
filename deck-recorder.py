ranks = ['3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K', 'A', '2']

tokens = {
    '0' : 'X',
    '1' : 'A',
    '2' : '2',
    '3' : '3',
    '4' : '4',
    '5' : '5',
    '6' : '6',
    '7' : '7',
    '8' : '8',
    '9' : '9',
    '/' : 'J',
    '*' : 'Q',
    '-' : 'K',
}
deck = {}

def reset():
    # deck = {rank : 4 for rank in ranks}
    for rank in ranks:
        deck[rank] = 4
    print('Reset')
    display()

def display():
    print('---- BEGIN ----')
    spacing = '  '
    line_rank  = ''
    line_count = ''
    line_notif = ''
    for rank in deck:
        line_rank = line_rank + rank + spacing
        line_count = line_count + str(deck[rank]) + spacing
        if deck[rank] == 4:
            line_notif = line_notif + '#' + spacing
        else:
            line_notif = line_notif + ' ' + spacing
    print(line_rank)
    print(line_count)
    print(line_notif)
    print('----  END  ----')

def parse(str):
    batch = {}
    parsed_tokens = ''
    for rank in ranks:
        batch[rank] = 0
    for char in str:
        assert(char in tokens)
        token = tokens[char]
        parsed_tokens += token
        batch[token] += 1
    print(parsed_tokens)
    return batch

def subtract(batch):
    for rank in ranks:
        deck[rank] -= batch[rank]
        assert(deck[rank] >= 0)

def loop():
    message = 'Accept tokens 0123456789/*- or empty line for reset: '
    while(True):
        print()
        cmd = input(message)
        if cmd == '':
            reset()
        else:
            batch = parse(cmd)
            subtract(batch)
            display()

if __name__ == '__main__':
    reset()
    loop()
