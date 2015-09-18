# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import numpy
import random
import pylab

''' 
Begin helper code
'''
random.seed(0)

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """
    pass
        

'''
End helper code
'''

#
# PROBLEM 2
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        # TODO
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        # TODO
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        # TODO
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        # TODO
        if random.random() < self.clearProb:
            return True
        else:
            return False

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        # TODO
        if random.random() <= float(self.maxBirthProb) * (1 - float(popDensity)):
            return SimpleVirus(float(self.maxBirthProb), float(self.clearProb))
        else:
            raise NoChildException


class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        # TODO
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        # TODO
        return self.viruses
        

    def getMaxPop(self):
        """
        Returns the max population.
        """
        # TODO
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """

        # TODO
        return len(self.viruses)


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """

        # TODO
        temp_viruses=self.viruses[:]
        for vir in temp_viruses:
            if vir.doesClear()==True:
                self.viruses.remove(vir)
        
        temp_viruses=self.viruses[:]
        currPopDen = float(self.getTotalPop())/float(self.getMaxPop())        
        for vir in self.viruses:
            try:
                simVir=vir.reproduce(currPopDen)
                self.viruses.append(simVir)
                
            except NoChildException:
                pass
        return self.getTotalPop()                
                
"""
v1 = SimpleVirus(1.0, 0.0)
print "SimpleVirus(1.0, 0.0) : v1.doesClear() : ",v1.doesClear()
print "SimpleVirus(1.0, 0.0) : v1.doesClear() : ",v1.doesClear()
print "SimpleVirus(1.0, 0.0) : v1.doesClear() : ",v1.doesClear()
print "SimpleVirus(1.0, 0.0) : v1.doesClear() : ",v1.doesClear()
print "SimpleVirus(1.0, 0.0) : v1.doesClear() : ",v1.doesClear()
print "SimpleVirus(1.0, 0.0) : v1.doesClear() : ",v1.doesClear()
print "SimpleVirus(1.0, 0.0) : v1.doesClear() : ",v1.doesClear()
print "SimpleVirus(1.0, 0.0) : v1.doesClear() : ",v1.doesClear()
print "SimpleVirus(1.0, 0.0) : v1.doesClear() : ",v1.doesClear()
print "SimpleVirus(1.0, 0.0) : v1.doesClear() : ",v1.doesClear()


v2 = SimpleVirus(0.0, 0.0)
print "SimpleVirus(0.0, 0.0) : v2.doesClear() : ",v2.doesClear()
print "SimpleVirus(0.0, 0.0) : v2.doesClear() : ",v2.doesClear()
print "SimpleVirus(0.0, 0.0) : v2.doesClear() : ",v2.doesClear()
print "SimpleVirus(0.0, 0.0) : v2.doesClear() : ",v2.doesClear()
print "SimpleVirus(0.0, 0.0) : v2.doesClear() : ",v2.doesClear()
print "SimpleVirus(0.0, 0.0) : v2.doesClear() : ",v2.doesClear()
print "SimpleVirus(0.0, 0.0) : v2.doesClear() : ",v2.doesClear()
print "SimpleVirus(0.0, 0.0) : v2.doesClear() : ",v2.doesClear()
print "SimpleVirus(0.0, 0.0) : v2.doesClear() : ",v2.doesClear()
print "SimpleVirus(0.0, 0.0) : v2.doesClear() : ",v2.doesClear()


viruses = [SimpleVirus(0.48, 0.9), SimpleVirus(0.4, 0.42), SimpleVirus(0.59, 0.52), SimpleVirus(0.94, 0.22), SimpleVirus(0.08, 0.44), SimpleVirus(0.42, 0.83), SimpleVirus(0.74, 0.72) ]
P1 = Patient(viruses, 120)
for i in range(100):
    P1.update()
    #print P1.getTotalPop()
print P1.getTotalPop()

virus = SimpleVirus(1.0,1.0)
patient = Patient([virus], 100)
for i in range(100):
    patient.update()
print patient.getTotalPop()


virus = SimpleVirus(1.0, 0.0)
patient = Patient([virus], 100)
for i in range(100):
    patient.update()
print patient.getTotalPop()

"""

#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """

    # TODO
    simpleViruses = []
    for i in range(numViruses):
        simpleViruses.append(SimpleVirus(maxBirthProb, clearProb))
        
    perVirPop=[]
    for i in range(numTrials):
        p1 = Patient(simpleViruses, maxPop)
        pv=[]
        for j in range(300):
            p1.update()
            pv.append(float(p1.getTotalPop()))
        perVirPop.append(pv)
        
    
    #print perVirPop
    l2=[]
    for i in range(len(perVirPop[0])):
        l2.append(float(sum(map(lambda x : x[i], perVirPop)))/numTrials)

    #print l2
    
    pylab.plot(l2)
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend()
    pylab.show()

random.seed(0)

#simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)

#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """

        # TODO
        SimpleVirus.__init__(self,maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb
        

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        # TODO
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        # TODO
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        
        # TODO
        if drug in self.resistances:
            return self.resistances[drug]


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        # TODO
        resistant = True
        for al in activeDrugs:
            if self.isResistantTo(al):
                resistant = True
            else:
                resistant = False
                break
        if resistant:
            if random.random() < float(self.maxBirthProb) * (1 - popDensity):
                child_resistances = dict(self.resistances)
                for i in self.resistances:
                    if random.random() <= (1-self.mutProb):
                        child_resistances[i]=True
                    else:
                        child_resistances[i]=False
                return ResistantVirus(self.maxBirthProb, self.clearProb, child_resistances, self.mutProb)
            else:
                raise NoChildException
        else:
            raise NoChildException
            

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """

        # TODO
        Patient.__init__(self, viruses, maxPop)
        self.drugs = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """

        # TODO
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        # TODO
        return self.drugs


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """

        # TODO
        count=0
        flag=0
        for virus in self.viruses:
            for drug in drugResist:
                if virus.isResistantTo(drug):
                    flag=1
                else:
                    flag=0
                    break
            if flag==1:
                count+=1
                flag=0
                
        return count


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """

        # TODO
        virusList = self.viruses[:]
        

        for virus in virusList:
            if virus.doesClear():
                self.viruses.remove(virus) 
        
        
        popDensity = float(self.getTotalPop())/self.getMaxPop()
    
        virusList = self.viruses[:]
        for virus in virusList:
            try:                
                self.viruses.append(virus.reproduce(popDensity, self.getPrescriptions()))
            except NoChildException:
                pass
    
        return self.getTotalPop()  


#
# PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    # TODO
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses)]    
    
    perVirPop=[]
    resistVirPop=[]
    
    for i in range(numTrials):
        p1 = TreatedPatient(viruses, maxPop)
        pv=[]
        rg=[]
        for j in range(150):
            p1.update()
            pv.append(float(p1.getTotalPop()))
            rg.append(float(p1.getResistPop(['guttagonol'])))
        
        p1.addPrescription('guttagonol')

        for j in range(150):
            p1.update()
            pv.append(float(p1.getTotalPop()))
            rg.append(float(p1.getResistPop(['guttagonol'])))
        perVirPop.append(pv)
        resistVirPop.append(rg)

    
    totPop=[]
    for i in range(len(perVirPop[0])):
        totPop.append(float(sum(map(lambda x : x[i], perVirPop)))/numTrials)
    #print totPop 
    resistPop=[]
    for i in range(len(resistVirPop[0])):
        resistPop.append(float(sum(map(lambda x : x[i], resistVirPop)))/numTrials)
    #print resistPop
    #print l2
    pylab.plot(totPop, 'b-', label = "Total Pop")
    pylab.plot(resistPop, 'r-', label = "Resistance Pop")
    #pylab.plot(l2)
    pylab.title("ResistantVirus simulation")
    pylab.xlabel("time step")
    pylab.ylabel("# viruses")
    pylab.legend()
    pylab.show()

        
#simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 100)



def simulationWithDrug_ps4(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    # TODO
    #viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses)]    
    
    perVirPop=[]
    resistVirPop=[]
    
    delays=[300, 150, 75, 0]
    pop = [[] for i in range(4)]
    popPercentage = []
    
    
    for num in range(numTrials):
        for index,delay in enumerate(delays):
            viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses)]
            patient = TreatedPatient(viruses, maxPop)
            for j in range(150):
                patient.update()
                
            patient.addPrescription('guttagonol')

            for j in range(delay+150):
                if j==delay:
                    patient.addPrescription('grimpex')#Is this fuc right?
                patient.update()
            pop[index].append(float(patient.getTotalPop()))
        print "loop :",num
    for index,delay in enumerate(delays):
        pylab.subplot(4,1,index+1)
        pylab.hist(pop[index])
    pylab.show()
    
    countList = []
    for index,delay in enumerate(delays):
        count = 0
        for each_trial in pop[index]:
            if each_trial > 50:
                count += 1
        countList.append([delay,(1.0-float(count)/float(len(pop[index])))*100.0])
    
    print pop
    print countList




simulationWithDrug_ps4(100, 1000, 0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005, 110)