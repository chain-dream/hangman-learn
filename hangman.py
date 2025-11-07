import random
word_list = [
    "apple", "banana", "grape", "orange", "melon",
    "cat", "dog", "fish", "tiger", "lion",
    "car", "train", "plane", "boat", "truck"
]
#0-14
list_downline = []
downline = ""
#这两是用来处理'---'的list和变量
input_letter =""
#第一次输入的字母
check_part = []
#用来检查的list
the_distance_of_death = 7
#游戏剩余次数
random_choice = word_list[random.randint(0,14)]#固定选中词
def hand_graph():
    if the_distance_of_death == 7:
        print(''' 
  +---+
  |   |
      |
      |
      |
      |
=========
''')
    elif the_distance_of_death == 6:
        print('''  
  +---+              
  |   |
  O   |
      |
      |
      |
=========''')
    elif the_distance_of_death == 5:
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========

''')
    elif the_distance_of_death == 4:
        print(''' 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''')
    elif the_distance_of_death == 3:
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''')
    elif the_distance_of_death == 2:
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''')
    elif the_distance_of_death == 1:
        print(''' 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''')


win = 0
def win_function():
    global win
    
    if "-" in list_downline:
        win = 0
    else:
        win = 1 



inside = 0#状态：输入的字母到底在不在选中的单词里
k = 0 #先把小k留着
def sentence():
    global inside
    global k
    check_part = list(random_choice)#把选中的单词拆成单个字母
    for k in range(length):
        if input_letter == check_part[k]:
                #判断这个字母到底在不在里面
            inside = 1
            return k
            
            
           

        else:
            inside = 0
                        
#这个函数的作用是判断字母是否猜对并且返回字母在选中单词中的位置    
def output():
    global input_letter
    global the_distance_of_death
    if inside == 1:
        global downline
        downline = ""    
        list_downline[k] = input_letter
        win_function()
        
        if win == 1:
            print("You win! The word is:", random_choice)
            return 
    
        for i in range(length):
            downline += list_downline[i]
             
        print(f"You guess a right letter, please continue ! \n{downline}") 
        print(f"You still have {the_distance_of_death} times's chances.\n")
        print(f"Please input a letter to continue guess: \n{downline}")
        input_letter = str(input())
    
    elif inside == 0: 
        hand_graph()
        print("You guess a wrong letter.Someone is going to die.......")
        the_distance_of_death -= 1
        print(f"You still have {the_distance_of_death} times's chances.\n")
        print(f"Please input a letter to continue guess: \n{downline}")
        input_letter = str(input())
        
#这个函数在接受了返回的位置以后把字母插进去并打印



#int main(){    
length = len(random_choice)
#这里可以加一条限制输入letter长度的命令防止瞎搞
for i in range(length):
    list_downline.append("-")
for j in range(length):
    downline += list_downline[j]

print(f"Please input a letter to guess the word: {downline}") 
input_letter = str(input())


while win != 1 and the_distance_of_death != 0:
    if the_distance_of_death == 1:
        print("Hang man died!!!\n game over!")
        hand_graph()
        break
    else:
        sentence()
        output()

#}
     


