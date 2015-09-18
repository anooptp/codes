# 6.00.2x Problem Set 4

import time
import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        

from multiprocessing import Pool
from functools import partial

def testsim(numTrials,injectTime,clinic):
    results=[]
    simpool = Pool()        
    clinic_p = partial(clinic,injectTime)
    results=simpool.map(clinic_p,xrange(numTrials))
    simpool.close()
    simpool.join()
    # use results list to compute 
    # endPop, minPop, maxPop and avgPop
    return end1,avg1,min1,max1

def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    # TODO
    #ceil(10*log(number of Samples))
    for i in range(4):
        pylab.subplot(4,1,i+1)
        pylab.plot(something)
    pylab.show()


#simulationDelayedTreatment(100)


def simulationDelayedTreatmentCopy(numTrials):    

    InjectTimes=(0,100,200,300) # change this for pset
    start=time.clock() #get the start time
    fig = pylab.figure()
    for count,InjectTime in enumerate(InjectTimes):

        endPopList,avg1,min1,max1 = testsim(numTrials,InjectTime,arkham)        
        cured=0
        for x in endPopList:
            if x <= 50: cured+=1
        pcured = 100*cured/float(len(TotalPopList))
        print 'Inject:',InjectTime,' Cured:',cured,'=',str(pcured)+'%'
        #print endPopList

        PopMax = max(endPopList)
        PopMin = min(endPopList)
        bins= int(PopMax-PopMin) or 1  
        bins = 20 if bins >1 else bins 

        pylab.subplot(4,2,1+count*2)
        title = 'Injected at: '+str(InjectTime)+' Cured: '+str(pcured)+'%'
        pylab.title(title )
        pylab.hist(TotalPopList, bins)

        ax = pylab.subplot(4,2,2+count*2)
        ax.yaxis.tick_right()
        pylab.title("Virus Growth")
        pylab.plot( avg1,color='b',lw=1,label="Virus Pop")
        pylab.plot( min1,color='g',lw=1,label="Min Virus Pop")
        pylab.plot( max1,color='r',lw=1,label="Max Virus Pop")

    stop=time.clock() - start # how long did this all take
    simtext=str(numTrials)+' trials in ' + str(round(stop,2))+'s'
    fig.text(0.5, 0.96, simtext, ha='center', va='center') 
    fig.text(0.3, 0.03, 'Final total virus pop', ha='center', va='center')
    fig.text(0.7, 0.03, 'Timesteps', ha='center', va='center')   
    fig.text(0.97, 0.5, 'Average Virus Population', ha='center', va='center', rotation=270)
    fig.text(0.03, 0.5, 'Number of Trials', ha='center', va='center', rotation='vertical')
    pylab.tight_layout(pad=2.4,h_pad=0.6,w_pad=0.4)    
    pylab.show()
    
simulationDelayedTreatmentCopy(2)

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
