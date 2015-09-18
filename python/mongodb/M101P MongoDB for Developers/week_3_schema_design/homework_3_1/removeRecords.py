
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.school
students = db.students


def find():

    print "find, reporting for duty"

    query = {'scores.type': 'homework'}

    try:

        cursor = students.find(query)
        # cursor = cursor.limit(1)

        #cursor = cursor.sort('student_id', pymongo.ASCENDING).skip(4).limit(1)
        
        cursor = cursor.sort([('_id',pymongo.ASCENDING),('scores.score',pymongo.ASCENDING)])



    except:
        print "Unexpected error:", sys.exc_info()[0]

    test=0
    for doc in cursor:
            #print doc
            #if test<3:
            print doc
            #grades.remove(doc)
            if doc['scores'][2]['type']==doc['scores'][3]['type']:
                if doc['scores'][2]['score'] < doc['scores'][3]['score']:
                    #print doc['scores'][2]
                    doc['scores'].pop(2)
                else:
                    #print doc['scores'][3]
                    doc['scores'].pop(3)
                students.update({'_id':doc['_id']},doc)
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

