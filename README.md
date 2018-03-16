# starlines
### Visualize the relationship between two rotating points as they complete a full period. 
I saw a [tweet](https://twitter.com/markdoczy/status/901986301808861184) a while back that drew lines between the Earth and Venus every certain amount of time and let it run for "8 years."
Though the orbits were wildly out of scale, it made a really pretty picture.
I decided to take a look at what the relationships look like for a wide variety of of periods. 

I made a Jupyter Notebook that is hosted on [binder](https://mybinder.org) so you can interact with it right from your browser:
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/ssterrett/starlines/master?filepath=starlines.ipynb)

The refresh rate is pretty slow since you have to draw 1000 lines. 
I couldn't find an easy way to draw all the lines with one command so it loops through all points (send me a pull request if you do!). 
In the mean time, enjoy this gif of the prime numbers less than 100!

![alt text](https://github.com/ssterrett/starlines/blob/master/all.gif)

This repo also has the code I used to generate the primes gif. You will have to change the filepath in plt.savefig() to your own directory. 
