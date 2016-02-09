import pymongo
import sys

# establish a connection to the server, and use it to get a handle on the scores collection.
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database and the scores collection.
db=connection.students
grades = db.grades
     
def find():
	query = {'type':'homework'}

	try:
		cursor = grades.find(query)

		cursor = cursor.sort([('student_id', pymongo.ASCENDING), ('score', pymongo.DESCENDING)])        
        
	except Exception as e:
        	print "Unexpected error:", type(e), e

	student_id = 0
	for doc in cursor:
		
		print doc

find()
