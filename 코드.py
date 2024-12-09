import turtle
t = turtle.Turtle()
t.shape('turtle')
import random as rd

def circle():  ##처음에 원을 만들기 위한 함수
    t.up()
    t.goto(0,-100)
    t.down()
    t.circle(100)
    t.up()
    t.goto(0,0)
    


def t_move(): ##거북이가 전방향 무작위로 움직이게하는 함수
    dirct = rd.randint(0, 360)
    t.setheading(dirct)
    t.fd(20)
    

   


def myMain(): ##거북이가 원 밖으로 나갔는지, 얼마나 이동했는지 보는 함수
    i=0
    circle()
    while True :
        t_move()
        i = i +20
        x, y = t.position()
        
        if (x**2 + y**2) >= 100**2 :
            break
    print('총 거리 합:',i)

        
        
myMain()  ##함수 출력 시작
