import pyglet
import time
import sys

mus1 = pyglet.resource.media('src/I_am_ghoul.mp3')
mus2 = pyglet.resource.media('src/amogus.mp3')


def ghoul():
    mus1.play()
    time.sleep(18)
    print('Я')
    time.sleep(1.7)
    print('Гуль')
    time.sleep(2)
    x = 1000
    while x > 0:
        print(x, '-7=', x - 7, sep='')
        x -= 7
        time.sleep(0.04)


if __name__ == '__main__':
    if input('Гуль? Y|N \n').upper() == 'Y':
        ghoul()
    else:
        time.sleep(3)
        print('ච AMOGUS ච')
        mus2.play()
    input('Для завершения нажмите любую клавишу... ')
    sys.exit()

pyglet.app.run()
