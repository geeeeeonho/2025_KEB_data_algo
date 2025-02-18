import random

low=1
high=100
answer = random.randint(low, high)
chance = 7
log_list=[]


def do_half(low, high):
    global guess
    guess= (high+low)//2
    log_list.append(str(guess))


while chance != 0:
    do_half(low, high)
    if guess == answer:
        print(f'You win. Answer is {answer}')
        break
    elif guess > answer:
        chance = chance - 1
        print(f'{guess} is bigger. Chance left : {chance}')
        high=guess-1
    else:
        chance = chance - 1
        print(f'{guess} is lower. Chance left : {chance}')
        low=guess+1
else:
    print(f'You lost. Answer is {answer}')

with open('guess.txt','w') as fp:
    for i in log_list:
        fp.write(i)
        fp.write('  ')
print('txt 파일 작성 완료')