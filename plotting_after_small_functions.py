from matplotlib.pyplot import *
from numpy import *

t = arange(0,1,0.01)
y1 = sin(2*pi*t)

def myplot(t, y, fignum=1, myxlabel='Time (sec.)', \
           myylabel='', clear=True):
    figure(fignum)# create or activate figure
    if clear:
        clf()#clear figure
    plot(t,y)
    if myxlabel:
        xlabel(myxlabel)
    if myylabel:
        ylabel(myylabel)


myplot(t, y1, myylabel='$y_1(t)$')
#savefig('fig1.png',dpi=200)

y2 = 1.5*cos(3*pi*t)

myplot(t, y2, myylabel='$y(t)$', fignum=1, \
       clear=False)
#savefig('fig2.png',dpi=200)

show()
