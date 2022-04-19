def minion_game(word):
    a = 1
    x =0
    b = []
    Kevin = []
    Stuart = []
    for i in word:
        for j in range(65,91):
            if ord(i) == j:
                x += 1
    if x == len(word):
        while(a != len(word)):
            for i in range(len(word)):
                c = word[i:a+i]
                if len(c) != a:
                    break
                b.append(c)
            a += 1
        b.append(word)
        for i in b:
            if i[0] == 'A' or i[0] == 'E' or i[0] == 'I' or i[0] == 'O' or i[0] == 'U':
                Kevin.append(i)
            else:
                Stuart.append(i)
        if len(Kevin) > len(Stuart):
            print(f'Kevin {len(Kevin)}')
        elif len(Kevin) == len(Stuart):
            print("Draw")
        else:
            print(f'Stuart {len(Stuart)}')
minion_game('BANANA')
