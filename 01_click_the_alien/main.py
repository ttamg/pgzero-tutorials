import random

bobby = Actor('alien_swim_1.png')
bobby.topright = 0, 10
bobby.swim_phase = 0
bobby.hurt = False

WIDTH = 712
HEIGHT = 508


def draw():
  screen.fill((40, 6, 53))
  bobby.draw()


def update():
  # Move to the right
  bobby.left += 1

  # Scroll around screen
  if bobby.left > WIDTH:
    bobby.right = 0
    bobby.top = random.randint(0, 300)

  # Swim
  if not bobby.hurt:
    bobby.swim_phase += 1
    if bobby.swim_phase < 10:
      bobby.image = 'alien_swim_1.png'
    else:
      bobby.image = 'alien_swim_2.png'
      if bobby.swim_phase > 25:
        bobby.swim_phase = 0


def on_mouse_down(pos):
  if bobby.collidepoint(pos):
    print("Good shot!")
    set_alien_hurt()
  else:
    print("You missed me!")


def set_alien_hurt():
  print("Eek!")
  # sounds.ouch.play()
  bobby.hurt = True
  bobby.image = 'alien_hurt'
  clock.schedule_unique(set_alien_normal, 1.0)


def set_alien_normal():
  bobby.hurt = False
