import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
 
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_title("Ernest and Kernest travel to the moon!")
 
moon_pos = np.array([50.0, 90.0])
ernest_pos = np.array([40.0, 25.0])
kernest_pos = np.array([50.0, 25.0])
 
ernest_dot, = ax.plot(*ernest_pos, 'ro', ms=10, label="Ernest's Rocket")
kernest_dot, = ax.plot(*kernest_pos, 'go', ms=10, label="Kernest's Rocket")
moon_dot, = ax.plot(*moon_pos, 'o', color='yellow', ms=15, label="Moon")
ax.legend(loc='upper right')
 
status_text = ax.text(50, 5, "", ha='center', fontsize=13, fontweight='bold')
countdown_text = ax.text(50, 50, "", ha='center', fontsize=36, fontweight='bold', color='red')
 
speed = 0.5
countdown = [3]
launched = [False]
frame_count = [0]
 
def move_toward(pos, target, spd):
    d = np.linalg.norm(target - pos)
    if d < spd:
        return target.copy(), True
    return pos + (target - pos) / d * spd, False
 
def separate(a, b, min_dist=3.0):
    d = np.linalg.norm(b - a)
    if d < min_dist and d > 0:
        push = (b - a) / d * 0.3
        a -= push
        b += push
    return a, b
 
def update(frame):
    global ernest_pos, kernest_pos
 
    if not launched[0]:
        cd = countdown[0] - frame_count[0] // 30
        if cd > 0:
            countdown_text.set_text(str(cd))
        else:
            countdown_text.set_text("Launch!")
            if frame_count[0] > 30 * 4:
                countdown_text.set_text("")
                launched[0] = True
        frame_count[0] += 1
        return ernest_dot, kernest_dot, countdown_text, status_text
 
    ernest_pos, e_done = move_toward(ernest_pos, moon_pos, speed)
    kernest_pos, k_done = move_toward(kernest_pos, moon_pos, speed)
    ernest_pos, kernest_pos = separate(ernest_pos, kernest_pos)
 
    ernest_dot.set_data([ernest_pos[0]], [ernest_pos[1]])
    kernest_dot.set_data([kernest_pos[0]], [kernest_pos[1]])
 
    if e_done and k_done:
        status_text.set_text("both rockets reached the moon!")
    elif e_done:
        status_text.set_text("ernest hit the moon!")
    elif k_done:
        status_text.set_text("kernest hit the moon!")
    else:
        status_text.set_text("succesfull launch!")
 
    return ernest_dot, kernest_dot, countdown_text, status_text
 
ani = animation.FuncAnimation(fig, update, frames=300, interval=50, blit=True)
plt.tight_layout()
plt.show()