
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
grades = db.grades


def find():

    print "find, reporting for duty"

    query = {'type': 'homework'}

    try:

        cursor = grades.find(query)
        # cursor = cursor.limit(1)

        #cursor = cursor.sort('student_id', pymongo.ASCENDING).skip(4).limit(1)
        
        cursor = cursor.sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])



    except:
        print "Unexpected error:", sys.exc_info()[0]

    test=0
    for doc in cursor:
        print doc
        #if test%2==0:
            #grades.remove(doc)
        #test+=1


def find_one():

    print "find one, reporting for duty"
    query = {'student_id':10}
    
    try:
        doc = scores.find_one(query)
        
    except:
        print "Unexpected error:", sys.exc_info()[0]

    
    print doc


find()

