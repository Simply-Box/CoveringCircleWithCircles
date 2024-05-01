import random
import statistics

# Variables for the start condition.
area_r = 30 # Radius of the main circle
ball_r = 15 # Radius of the covering circles
cover_ratio = 0.8 # How much of the circle needs to be covered before stopping the iteration
iterations = 1000 # How many iterations

print(f"{area_r}")
print(f"{ball_r}")

print(f"{cover_ratio}")
print(f"{iterations}")

# Usefull constants
screen_size = area_r * 2
ball_d = ball_r * 2

# Main circle center
big_cx = area_r
big_cy = area_r

# Created the main circle
screen = [[0 for i in range(screen_size)] for j in range(screen_size)]

# Amount of pixles and the nummber of pixles left in the main circle
pixels = [
  0, 0
]

display_chars = [' ', '.', '#']

# Clear screen
def reset():
  for y in range(screen_size):
    for x in range(screen_size):
      screen[y][x] = 0

  pixels[0] = 0
  pixels[1] = 0

# Visual representation of screen
'''
def print_screen():
  for y in range(screen_size):
    print("".join(map(display_chars.__getitem__, screen[y])))
'''

# Calculates if the pixel is inside the main circle
def in_circle(x, y, cx, cy, cr):
  return (x - cx) * (x - cx) + (y - cy) * (y - cy) < cr * cr

# Calculates if the pixel is inside the screen
def in_screen(x, y):
  return 0 <= x < screen_size and 0 <= y < screen_size

# 'Draws' the entire screen
def draw_circle():
  for y in range(screen_size):
    for x in range(screen_size):
      if in_circle(x, y, big_cx, big_cy, area_r):
        screen[y][x] = 1
        pixels[0] += 1

# 'Draws' the main circle, relative_y, center point = [bx, by]
def draw_ball(bx, by):
  for rel_y in range(-ball_r, ball_r + 1):
    for rel_x in range(-ball_r, ball_r + 1):
      y = rel_y + by
      x = rel_x + bx
      if in_screen(x, y) and screen[y][x] == 1 and in_circle(x, y, bx, by, ball_r):
        screen[y][x] = 2
        pixels[1] += 1

# Randomly hitting screen until center point is inside main circle
def draw_random_ball():
  bx = random.randint(0, screen_size - 1)
  by = random.randint(0, screen_size - 1)

  if in_circle(bx, by, big_cx, big_cy, area_r):
    draw_ball(bx, by)
  else:
    draw_random_ball()

# One iteration of dropped circles
def one_iteration():
  reset()
  draw_circle()
  dropped_circles = 0

  while pixels[1] / pixels[0] < cover_ratio:
    draw_random_ball()
    dropped_circles += 1
    # Continuous data of percentage
    #print(f"Dropped balls: {dropped_circles}, Fill ratio: {round(100 * pixels[1] / pixels[0])}%")
  
  # Extra data
  #print_screen()

  return dropped_circles

data = []

for _ in range(iterations):
  data.append(one_iteration())

mean_data = statistics.mean(data)
median_data = statistics.median(data)
min_data = min(data)
max_data = max(data)

# Convenience with readability of output
print("")

print(f"min: {min_data}")
print(f"max: {max_data}")
print(f"median: {median_data}")
print(f"mean: {mean_data}")

print("")

from collections import Counter
counter = Counter(data)

s = []
for d in range(min_data, max_data + 1):
  if d in counter:
    s.append([d, counter[d]])

print("")
print(s)
