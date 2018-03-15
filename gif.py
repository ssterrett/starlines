import matplotlib.pyplot as plt
import numpy as np
import math
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

r1 = 1
r2 = 2*r1

def star2(T1,T2):
    N = 1000
    cm = T1*T2
    ang = np.linspace(0,2*math.pi,N)
    sin = np.sin(ang)
    cos = np.cos(ang)
    plt.plot(np.cos(ang), np.sin(ang))
    plt.plot(r2*np.cos(ang), r2*np.sin(ang))
    plt.axis('equal')
    for i in range(N):
        plt.plot([cos[(i*T1)%N], r2*cos[(i*T2)%N]], [sin[(i*T1)%N], r2*sin[(i*T2)%N]], 'k', linewidth = .1)
    plt.axis('off')
    plt.title('N1 = %s N2 = %s'%(T1,T2))
    plt.savefig((r'\pics\%s.png'%(T2)), format = 'png', bbox_inches='tight')
    plt.show()

  primes = np.array([])
  for num in range(1,100):
      for i in range(2,num):
          if (num%i) == 0:
              break
          else:
              primes = np.append(primes, num
filenames = np.array([])
for i in primes:
    star2(1,int(i))
    name = str(int(i)) + '.png'
    filenames = np.append(filenames,name)

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('all.gif', images, duration = .5)
