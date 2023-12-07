import random

n = input('最小値（整数）を決めてください\n')
m = input('最大値（整数）を決めてください\n')
n = int(n)
m = int(m)

if n > m:
    print('最大値は最小値以下にしてください')
else:
    target = random.randint(n,m)
    switch = 0
    print('先ほどの二つの数字の範囲からランダムに数字が選ばれます。当ててみてください')
    while switch == 0:
        selectNum = int(input('何と予想しますか？\n'))
        
        if selectNum == target:
            print('正解です！！')
            switch = 1
        else:
            print('不正解です。')
