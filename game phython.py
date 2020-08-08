#all jumbled words
que=['adhn','npe','irha','yee','sace','anf','mite','oty','rapep','lewot','tighl']
#all correct words
ans=['hand','pen','hair','eye','case','fan','time','toy','paper','towel','light']
#begin function to show rules etc
def begin():
    print('WELCOME TO THE WIZ COMPETITION')
    print('rules: \n 1.give it a try. \n 2.if right it will get ten points.\n 3.if wrong you will lose 10 points')
    choice=input("\n press any key to continue: ")
def game():
    score=0
    life=2
    i=0
    while(life !=0 and i<len(que)):
        x=input(que[i])
        if(x==ans[i]):
            score=score+10
            print('RIGHT ANSWER')
            print('new score=',score)
        else:
            life=life-1
            print('wrong answer \n you loss a life')
        i=i+1
    else:
        print("\n\GAME OVER")
        print("final score= ",score)
        next=input("\n\n Do you want to play again? press Y for yes any key for no:")
        if(next=='Y' or next=='y'):
          play()
        else:
          exit()
def play():
    begin()
    game()
play()    
          
            
