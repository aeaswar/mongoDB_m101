use blog
db.posts.aggregate([
	{$project: {c_author:"$comments.author"}},
	{$unwind:"$c_author"},
	{$group:
	  {_id:"$c_author",
	   "count":{$sum:1}
	  }
	},
	{$sort:{"count":-1}},
	{"$limit":10}
])
