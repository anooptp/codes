import random
import pylab

"""
random.seed(0)
def sampleQuizzes(numTrials = 10001):
    # Your code here
    res=[]
    for i in range(numTrials):
        mid1 = random.choice(range(50,81))
        mid2 = random.choice(range(60,91))
        fin = random.choice(range(55,96))
        res.append((0.25 * float(mid1)) + (0.25 * float(mid2)) + (0.50 * float(fin)))
    
    return float(sum(float(res)))/len(res)
"""

def sampleQuizzes():
    # Your code here
    mid1 = random.choice(range(50,81))
    mid2 = random.choice(range(60,91))
    fin = random.choice(range(55,96))
    return (0.25 * float(mid1) + 0.25 * float(mid2) + 0.50 * float(fin))


def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the final score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    res=[]
    for i in range(numTrials):
        res.append(sampleQuizzes())
    return res

random.seed(0)
def plotQuizzes():
    # Your code here
    res=generateScores(10000)
    
    pylab.hist(res, bins=7)
    
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    
    pylab.show()

plotQuizzes()