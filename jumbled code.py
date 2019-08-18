import random 
def choose(): 
    words = ['rainbow', 'computer', 'science', 'programming', 
             'mathematics', 'player', 'condition', 'reverse', 
             'water', 'board', 'world'] 
  
    pick = random.choice(words) 
  
    return pick 
  
  
def jumble(word): 
    random_word = random.sample(word, len(word)) 
  
    jumbled = ''.join(random_word) 
    return jumbled 
  
  
def thank(p1n,p1): 
    print(p1n, 'Your score is :', p1) 
    print('Thanks for playing...') 
  
  

  
  
# Function for playing the game. 
def play(): 
    # enter player1 and player2 name 
    p1name = input("player 1, Please enter your name :") 
  
    # variable for counting score. 
    pp1 = 0

    # variable for counting score. 
    turn = 1
    c=0
  
    # keep looping 
    while True: 
  
        # choose() function calling 
        picked_word = choose() 
  
        # jumble() fucntion calling 
        qn = jumble(picked_word) 
        print("jumbled word is :", qn) 
  
       
           
            # player1 turn 
        print(p1name, 'Your Turn.') 
  
        ans = input("what is in your mind? ") 
  
            # checking ans is equal to picked_word or not 
        if ans == picked_word: 
  
                # incremented by 1 
            pp1 += 1
            print('Your score is :', pp1) 
        else:
            if turn<5:
                print("Better luck next time...correct word is :", picked_word)
                print("turn",turn)
                turn +=1
            else:
                print("out of turn")
                print("exiting the game")
                break
          
      
        c = int(input("press 1 to continue and 0 to quit :"))
              
        if c == 0: 
                    # thank() function calling 
            thank(p1name,pp1) 
            break
  
  
  
 
if __name__ == '__main__': 
      
    # play() function calling 
    play() 
