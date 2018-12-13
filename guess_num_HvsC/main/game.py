from random import randint
import time

SLEEP_TIME = 1

class Judge(object):
    """此类包括如下功能:
    1.信息输入提示.
    2.对给定的数字，进行比对、返回结果。
    3.在2的基础上，给出是大还是小的文字提示。
    """
    def __init__(self):
        self.uper_num = 100
        self.lower_num = 1
        self.right_num = randint(self.lower_num, self.uper_num)
        super(Judge, self).__init__()
        # self.arg = arg

    def give_judge(self, guess_num):
        if self.right_num == guess_num:
            # 正确则返回
            time.sleep(SLEEP_TIME)
            print("裁判:数字正确 !")
            return 1

        elif guess_num > self.right_num:
            # 偏大 则更改上限
            time.sleep(SLEEP_TIME)
            print("裁判:数字过大 !")
            self.uper_num = min(self.uper_num, guess_num - 1)
            return 0

        elif guess_num < self.right_num:
            # 偏小 则更改下限
            time.sleep(SLEEP_TIME)
            print("裁判:数字过小 !")
            self.lower_num = max(self.lower_num, guess_num + 1)
            return 0
        pass

    def give_message(self, flag):
        if flag == 1:
            print("correct!")
            pass
        elif flag == 0:
            print("wrong!")
        elif flag == -1:
            print(f"请在输入一个1-100之间的整数。")

            # print(f"请在{self.lower_num}与{self.uper_num}中给出你所猜的数。")
            pass

class Human(object):
    """docstring for Human."""
    def guess(self):
        num = input("> ")
        num = int(num)
        return num
        pass

class Computer(object):
    """docstring for Computer."""
    def guess(self):
        num = randint(judger.lower_num, judger.uper_num)
        print(f"电脑:{num}.")
        return num
        pass

judger = Judge() # 提示范围。
human = Human()
computer = Computer()

round = 0 # round 0 belongs to computer, round 1 to human
flag = 0
print("欢迎进入人机对抗猜数字游戏。")
while flag != 1:
    round = round + 1
    if round % 2:
        # human's turn
        time.sleep(SLEEP_TIME)
        print("\n---你的回合---")

        time.sleep(SLEEP_TIME)
        judger.give_message(-1)

        time.sleep(SLEEP_TIME)
        flag = judger.give_judge(human.guess())
        # 若正确，则结束，否则，换轮。
    else:
        # computer's turn
        time.sleep(SLEEP_TIME)
        print("\n---电脑回合---")

        time.sleep(SLEEP_TIME)
        judger.give_message(-1)

        time.sleep(SLEEP_TIME)
        flag = judger.give_judge(computer.guess())

if round % 2:
    print("恭喜获胜!!")
else:
    print("你输了!!")
