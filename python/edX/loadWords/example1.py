import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())

xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

print len(xVals),len(yVals),len(wVals),len(zVals),len(tVals),
pylab.figure()
pylab.title('Heads/Tails Ratios')
pylab.xlabel('Number of Flips')
pylab.ylabel('Heads/Tails')
pylab.plot(xVals)
print xVals 
#pylab.plot(range(1000),yVals)
#pylab.plot(range(1000),wVals)
#pylab.plot(range(1000),zVals)
#pylab.plot(range(1000),tVals)
#pylab.plot(xVals, zVals)
#pylab.plot(sorted(xVals), sorted(yVals))

pylab.show()