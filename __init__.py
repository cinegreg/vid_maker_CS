#!/usr/bin/python
import libs
import functions
import json
import time

datafile = "data/videourls2mod.csv"

if __name__ == "__main__":
	vidlist = []
	videos = libs.getCSV(datafile)


	#write code to loop, and also write code to skip non https items

	vidmod = videos #[0:2]
	
	for this_vid in vidmod:
		time.sleep(5)
		vid = {}

		print this_vid
		data, misc = functions.getVideoData(this_vid[0])
		if len(this_vid[2]) == 0:
			data, misc = functions.getVideoData(this_vid[0])
			vid["title"] = data["description"]
		else:
			vid["title"] = this_vid[2]
		vid["description"] = data["description"]

		categories, connections = libs.splitCategoriesConnections(this_vid[1])

		vid["categories"] = categories
		vid["connections"] = connections
		vid["URL"] = libs.getYTID(this_vid[0])
		vid["preview"] = 'https://img.youtube.com/vi/'+vid["URL"]+'/mqdefault.jpg'
		vid["meta"] = ["free", "youtube"] 

		vidlist.append(vid)


	with open('videos.json', 'w') as outfile:
		json.dump(vidlist, outfile)












		#for k in vid:
		#	print str(k)+": "+str(vid[k])
		#print vid


		#print videos[0][0]
		#write code to put vid dict in list...then put list out as JSON

		
