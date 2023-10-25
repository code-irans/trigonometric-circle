import pyxel
import math

angle = 0
radius = 50
speed = 0.05
pause = False
cx = 145
cy = 145

def draw():
    pyxel.cls(pyxel.COLOR_WHITE)
    pyxel.circb(cx, cy, radius, pyxel.COLOR_RED)
    pyxel.line(x, y, cx, cy, pyxel.COLOR_BLACK)
    pyxel.circ(x, y, 5, pyxel.COLOR_DARK_BLUE)
    pyxel.circ(cx, cy, 10, pyxel.COLOR_RED)
    pyxel.text(x + 10, y + 10, f"P({math.cos(angle):.3f},{math.sin(angle):.3f})", pyxel.COLOR_BLACK)
    pyxel.text(cx - 30, 20, f"CIRLCE RADIUS: {radius}", pyxel.COLOR_BLACK)

def update():
    global angle, pause, speed, x, y

    x = math.sin(angle) * radius + cx
    y = math.cos(angle) * radius + cy

    if pyxel.btn(pyxel.KEY_P):
        pause = True

    elif pyxel.btn(pyxel.KEY_R):
        pause = False

    elif pyxel.btn(pyxel.KEY_UP):
        speed += 0.01

    elif pyxel.btn(pyxel.KEY_DOWN):
        speed -= 0.01

    if not pause:
        angle += speed

pyxel.init(300, 300, "Trigonometric circle", display_scale=2)
pyxel.run(update, draw)