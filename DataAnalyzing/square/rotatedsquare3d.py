import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D

vertices = np.array([[-1,-1,0], [1,-1,0], [1,1,0], [-1,1,0]])
edges = [(0,1), (1,2), (2,3), (3,0)]

root = tk.Tk()
root.title("Rotate Square 3D")
root.geometry("600x600")

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection='3d')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def rotate(angle, axis):
    rad = np.radians(angle)
    c, s = np.cos(rad), np.sin(rad)
    if axis == 'x':
        return np.array([[1,0,0],[0,c,-s],[0,s,c]])
    elif axis == 'y':
        return np.array([[c,0,s],[0,1,0],[-s,0,c]])
    else:  # z
        return np.array([[c,-s,0],[s,c,0],[0,0,1]])

def update(val=None):
    ax.clear()

    rotated = vertices.copy()
    rotated = rotated @ rotate(z_slider.get(), 'z').T
    rotated = rotated @ rotate(y_slider.get(), 'y').T
    rotated = rotated @ rotate(x_slider.get(), 'x').T

    for edge in edges:
        ax.plot3D(rotated[edge,0], rotated[edge,1], rotated[edge,2], 'b-', linewidth=2)
    ax.scatter(rotated[:,0], rotated[:,1], rotated[:,2], c='r', s=50)
    
    ax.set_xlim([-2,2])
    ax.set_ylim([-2,2])
    ax.set_zlim([-2,2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    canvas.draw()

control = tk.Frame(root)
control.pack(side=tk.BOTTOM, pady=10)

frame_x = tk.Frame(control)
frame_x.pack()
tk.Label(frame_x, text='X:', width=5).pack(side=tk.LEFT)
x_slider = tk.Scale(frame_x, from_=-180, to=180, orient='horizontal', command=update, length=300)
x_slider.pack(side=tk.LEFT)

frame_y = tk.Frame(control)
frame_y.pack()
tk.Label(frame_y, text='Y:', width=5).pack(side=tk.LEFT)
y_slider = tk.Scale(frame_y, from_=-180, to=180, orient='horizontal', command=update, length=300)
y_slider.pack(side=tk.LEFT)

frame_z = tk.Frame(control)
frame_z.pack()
tk.Label(frame_z, text='Z:', width=5).pack(side=tk.LEFT)
z_slider = tk.Scale(frame_z, from_=-180, to=180, orient='horizontal', command=update, length=300)
z_slider.pack(side=tk.LEFT)

def reset():
    x_slider.set(0)
    y_slider.set(0)
    z_slider.set(0)

tk.Button(control, text='Reset', command=reset, width=10).pack(pady=5)

update()
root.mainloop()