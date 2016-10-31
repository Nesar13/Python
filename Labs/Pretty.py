# Modify me!


from Shapes import *
def main():
    turtle.speed(0)
    face = Circle(Vector(0, 0), 200, 'yellow')
    face.render()
    left_eye = Circle(Vector(-60, 50), 40, 'black')
    left_eye.render()  
    right_eye = Circle(Vector(60, 50), 40, 'black')
    right_eye.render()
    mouth = Circle(Vector(0, -150), 50, 'red')
    mouth.render()
    rect = Rectangle(25,50,Vector(0,0),'blue')
    rect.render()
    turtle.done()

if __name__ == '__main__':
    main()