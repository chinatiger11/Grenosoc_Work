# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2020.2.0
# 15:31:04  6月 01, 2021
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("HFSS_oppo_couple_inductor_20210510_1600")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
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
oEditor.Split(
	[
		"NAME:Selections",
		"Selections:="		, "BOTTOM,BOTTOM_L1,BOTTOM_L2,BOTTOM_L3,BOTTOM_t_fill,L2,L2_t_fill,L3,L3_t_fill,L4,L4_t_fill,L5,L5_t_fill,Mag1,Mag2,TOP,TOP_L1,TOP_L2,TOP_L3,UNNAMED_004,UNNAMED_006,UNNAMED_008,via_10,via_11,via_12,via_13,via_14,via_9,Mag_via",
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
