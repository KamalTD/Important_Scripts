"""
Maya

set time line range based on object animation keyframes range

"""

import maya.cmds as cmds

sel = cmds.ls(sl=True)

time_range = cmds.keyframe( '%s'%sel[0], time=(1,10000000), query=True, timeChange=True)



mini = min(time_range)
maxi = max(time_range)



#for key in reversed(range(int(mini),int(maxi)+1)):
	
#	cmds.keyframe(time=(key,key),timeChange=key+1001)


cmds.playbackOptions(min=mini,max=maxi)
