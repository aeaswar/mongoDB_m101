import pymongo
import sys

# establish a connection to the server, and use it to get a handle on the scores collection.
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database and the scores collection.
db=connection.school
students = db.students
     

def drop_hw(scores):
	try:
                hw_scores = [score for score in scores if score[u"type"] == u"homework"]
                lowest = min( [score[u"score"] for score in hw_scores])
                return [score for score in scores \
                        if (score[u"type"] != u"homework") \
                        or (score[u"type"] == u"homework" and score[u"score"] != lowest)]

	except Exception as e:
        	print "Delete Exception:", type(e), e
		


def update_scores(coll, doc_id, new_scores):
	try:
		coll.update( {"_id": doc_id}, {"$set": {"scores": new_scores} } )        
        
	except Exception as e:
        	print "Unexpected error while updating:", type(e), e

def main(argv):
        try:
                cursor = students.find( {"scores.type": "homework"} )

        except Exception as e:
                print "Unexpected error while finding:", type(e), e

        for doc in cursor:
                id = doc["_id"]
                scores = doc["scores"]
                updated_scores = drop_hw(scores)
                update_scores(students, id, update_scores)
                print "updated doc %s:\n   scores:%s\n   new scores: %s" % (id, scores, update_scores)

if __name__ == "__main__":
        main(sys.argv[1:])
