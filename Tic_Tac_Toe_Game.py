import simpleguitk as simplegui
#import simplegui
p1=True
p2=False
l=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
play=True
win1=False
win2=False
tie=False

def full():
    global l
    if(' ' in l):
        return False
    else:
        return True

def check():
    global l,win1,win2,play,tie
    if(l[0]==l[1]==l[2]=='O' or l[0]==l[3]==l[6]=='O' or l[3]==l[4]==l[5]=='O' or l[6]==l[7]==l[8]=='O' or
      l[1]==l[4]==l[7]=='O' or l[2]==l[5]==l[8]=='O' or l[0]==l[4]==l[8]=='O' or l[2]==l[4]==l[6]=='O'):
        win1=True
        play=False
        
    elif(l[0]==l[1]==l[2]=='X' or l[0]==l[3]==l[6]=='X' or l[3]==l[4]==l[5]=='X' or l[6]==l[7]==l[8]=='X' or
      l[1]==l[4]==l[7]=='X' or l[2]==l[5]==l[8]=='X' or l[0]==l[4]==l[8]=='X' or l[2]==l[4]==l[6]=='X'):
        win2=True
        play=False
        
    elif(full()):
        tie=True
        play=False
        
def restart():
    global l,p1,p1,play,win1,win2,tie
    p1=True
    p2=False
    l=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    play=True
    win1=False
    win2=False
    tie=False
    
def click(p):
    global p1,p2,a,b,pos1,pos2
    
    if(p[0]>=150 and p[0]<=250 and p[1]>=200 and p[1]<=270 and l[0]==' '):
        if(p1==True):
            l[0]='O'
            p2=True
            p1=False
        elif(p2==True):
            l[0]='X'
            p1=True
            p2=False
            
    if(p[0]>250 and p[0]<=350 and p[1]>=200 and p[1]<=270 and l[1]==' '):
        if(p1==True):
            l[1]='O'
            p2=True
            p1=False
        elif(p2==True):
            l[1]='X'                    
            p1=True
            p2=False
        
    if(p[0]>350 and p[0]<=450 and p[1]>=200 and p[1]<=270 and l[2]==' '):
        if(p1==True):
            l[2]='O'
            p2=True
            p1=False
        elif(p2==True):
            l[2]='X'
            p1=True
            p2=False
        
    if(p[0]>=150 and p[0]<=250 and p[1]>270 and p[1]<=340 and l[3]==' '):
        if(p1==True):
            l[3]='O'
            p2=True
            p1=False
        elif(p2==True):
            l[3]='X'
            p1=True
            p2=False
        
    if(p[0]>250 and p[0]<=350 and p[1]>270 and p[1]<=340 and l[4]==' '):
        if(p1==True):
            l[4]='O'
            p2=True
            p1=False
        elif(p2==True):
            l[4]='X'
            p1=True
            p2=False
        
    if(p[0]>350 and p[0]<=450 and p[1]>270 and p[1]<=340 and l[5]==' '):
        if(p1==True):
            l[5]='O'
            p2=True
            p1=False
        elif(p2==True):
            l[5]='X'
            p1=True
            p2=False
        
    if(p[0]>=150 and p[0]<=250 and p[1]>340 and p[1]<=410 and l[6]==' '):
        if(p1==True):
            l[6]='O'
            p2=True
            p1=False
        elif(p2==True):
            l[6]='X'
            p1=True
            p2=False
        
    if(p[0]>250 and p[0]<=350 and p[1]>340 and p[1]<=410 and l[7]==' '):
        if(p1==True):
            l[7]='O'
            p2=True
            p1=False
        elif(p2==True):
            l[7]='X'
            p1=True
            p2=False
        
    if(p[0]>350 and p[0]<=450 and p[1]>340 and p[1]<=410 and l[8]==' '):
        if(p1==True):
            l[8]='O'
            p2=True
            p1=False
        elif(p2==True):
            l[8]='X'
            p1=True
            p2=False
    check()    
    
            
def draw(canvas):
    global l,p1,p2,play,win1,win2,tie
    if(play==True):
        canvas.draw_line([150,270],[450,270],3,'White')
        canvas.draw_line([150,340],[450,340],3,'White')
        canvas.draw_line([250,200],[250,410],3,'White')
        canvas.draw_line([350,200],[350,410],3,'White')
        canvas.draw_text(l[0],[180,260],30,'white')
        canvas.draw_text(l[1],[280,260],30,'white')
        canvas.draw_text(l[2],[380,260],30,'white')
        canvas.draw_text(l[3],[180,330],30,'white')
        canvas.draw_text(l[4],[280,330],30,'white')
        canvas.draw_text(l[5],[380,330],30,'white')
        canvas.draw_text(l[6],[180,410],30,'white')
        canvas.draw_text(l[7],[280,410],30,'white')
        canvas.draw_text(l[8],[380,410],30,'white')
        if(p1==True):
            canvas.draw_text("Player 1",[160,130],50,'Red')
       
        elif(p2==True):
            canvas.draw_text("Player 2",[160,130],50,'Blue')

    elif(play==False):
        if(win1==True):
            canvas.draw_text('Player 1 Wins!!!',[60,310],40,'Red')
            
        elif(win2==True):
            canvas.draw_text('Player 2 Wins!!!',[60,310],40,'Blue')
            
        elif(tie==True):
            canvas.draw_text('Ohh Its Tie!!!',[90,310],40,'Yellow')
            
            
    
frame=simplegui.create_frame("tictac",600,600)
frame.set_mouseclick_handler(click)
frame.add_button("Restart",restart)
frame.set_draw_handler(draw)
frame.start()
