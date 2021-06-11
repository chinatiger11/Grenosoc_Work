# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2020.2.0
# 22:22:03  May, 2021
# ----------------------------------------------
# import win32api
# import win32con
from win32com import client
import string

oAnsoftApp = client.Dispatch('AnsoftHfss.HfssScriptInterface')
oDesktop = oAnsoftApp.GetAppDesktop()
oDesktop.RestoreWindow()
oDesktop.OpenProject(r"C:\Users\Tigerhwa\Desktop\test\HFSS_oppo_couple_inductor_20210510_1600.aedt")
oProject = oDesktop.SetActiveProject("HFSS_oppo_couple_inductor_20210510_1600")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")

# win32api.keybd_event(17,0,0,0)  
# win32api.keybd_event(65,0,0,0)  

oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"Mode:="		, "Axis/Position",
		"OriginX:="		, "-0.8mm",
		"OriginY:="		, "-0.4mm",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS1"
	])

# list_of_bodies=[]
# for i in range(60):
#     tuple_of_bodies = oEditor.GetBodyNamesByPosition(
#     [
#     "NAME:Parameters",
#     "XPosition:=","0.0mm",
#     "YPosition:=","0.0mm",
#     "ZPosition:=",str(i*0.01)+"mm",
#     ])
#     temp_list = list(tuple_of_bodies)
#     list_of_bodies.extend(temp_list)
# list_of_bodies = list(set(list_of_bodies))
# str1 = ",".join(list_of_bodies)


num_bodies = oEditor.GetNumObjects()
list_of_bodies=set()
for i in range (num_bodies):
    list_of_bodies.add(oEditor.GetObjectName(i))

oEditor.Split(
    [
    "NAME:Selections",
    "Selections:="		, str1,
    "NewPartsModelFlag:="	, "Model"
	],
	[
		"NAME:SplitToParameters",
		"SplitPlane:="		, "YZ",
		"WhichSide:="		, "PositiveOnly",
		"ToolType:="		, "PlaneTool",
		"ToolEntityID:="	, -1,
		"SplitCrossingObjectsOnly:=", False,
		"DeleteInvalidObjects:=", True
	])