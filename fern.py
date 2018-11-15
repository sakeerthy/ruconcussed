import tobii_research as tr

def getEyetracker():
	eye_trackers = tr.find_all_eyetrackers()
	if len(eye_trackers) > 0:
		return eye_trackers[0]
	else:
		return 0

print(getEyetracker())