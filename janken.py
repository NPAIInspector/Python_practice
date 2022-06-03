from random import randint
import time

hands = ["グー", "チョキ", "パー"]
rules = ["あいこ", "負け( ﾟДﾟ)", "勝ち(>_<)"]
win = 0
lose = 0
draw = 0

print("====じゃんけんスタート(^^)/====")

while True:
    #player
    print("0:グー 1:チョキ 2:パー")
    p = int(input("あなたは何をだす??・・・"))
    print("あなたは、" +hands[p] + "をだす")
    time.sleep(0.9)

    #PC
    m = randint(0,2)
    print("PCは、" +hands[m] + "をだす")
    time.sleep(0.9)

    #勝敗判定
    i = (p - m) % 3
    print(rules[i])
    if i == 0:
        draw = draw + 1
    elif i == 1:
        lose = lose + 1
    else:
        win = win + 1
    time.sleep(0.9)

    #結果を出力する
    print("{}勝/{}負/{}引き分け".format(win, lose, draw))
    if win == 3:
        print("対戦結果は・・・?!?!")
        time.sleep(3)
        print("「3勝で、あなたの勝ち(#^.^#),You win!!」")
        break
    if lose == 3:
        print("対戦結果は・・・?!?!")
        time.sleep(3)
        print("「3勝で、あなたの負け( ﾟДﾟ),Sorry・・!!」")
        break
time.sleep(1)
