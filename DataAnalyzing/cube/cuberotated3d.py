import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D

v = np.array([
    [-1,-1,-1], [1,-1,-1], [1,-1,1], [-1,-1,1],
    [-1,1,-1], [1,1,-1], [1,1,1], [-1,1,1]
])

edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]

root = tk.Tk()
root.title("Cube Rotator")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack()

def rot(ang, axis):
    r = np.radians(ang)
    c, s = np.cos(r), np.sin(r)
    if axis=='x': return np.array([[1,0,0],[0,c,-s],[0,s,c]])
    if axis=='y': return np.array([[c,0,s],[0,1,0],[-s,0,c]])
    return np.array([[c,-s,0],[s,c,0],[0,0,1]])

def update(a):
    ax.clear()
    r = v.copy()
    r = r @ rot(z.get(),'z').T
    r = r @ rot(y.get(),'y').T
    r = r @ rot(x.get(),'x').T
    
    for e in edges:
        ax.plot3D([r[e[0]][0],r[e[1]][0]], 
                  [r[e[0]][1],r[e[1]][1]], 
                  [r[e[0]][2],r[e[1]][2]], 'b-')
    
    ax.scatter(r[:,0], r[:,1], r[:,2], c='r')
    ax.set_xlim(-2,2); ax.set_ylim(-2,2); ax.set_zlim(-2,2)
    canvas.draw()

x = tk.Scale(root, from_=-180, to=180, orient='horizontal', command=update)
x.pack()
y = tk.Scale(root, from_=-180, to=180, orient='horizontal', command=update)
y.pack()
z = tk.Scale(root, from_=-180, to=180, orient='horizontal', command=update)
z.pack()

tk.Button(root, text='Reset', command=lambda: (x.set(0), y.set(0), z.set(0))).pack()

update(0)
root.mainloop()