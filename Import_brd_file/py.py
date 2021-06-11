# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2020.2.0
# 22:09:54  May, 2021
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("HFSS_oppo_couple_inductor_20210519_1850")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateObjectFromEdges(
	[
		"NAME:Selections",
		"Selections:="		, "BOTTOM_L3,BOTTOM_L1,BOTTOM_L2,BOTTOM",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:Parameters",
		[
			"NAME:BodyFromEdgeToParameters",
			"Edges:="		, [331]
		],
		[
			"NAME:BodyFromEdgeToParameters",
			"Edges:="		, [144]
		],
		[
			"NAME:BodyFromEdgeToParameters",
			"Edges:="		, [230]
		],
		[
			"NAME:BodyFromEdgeToParameters",
			"Edges:="		, [44]
		]
	], 
	[
		"CreateGroupsForNewObjects:=", False
	])
oEditor.SweepAlongVector(
	[
		"NAME:Selections",
		"Selections:="		, "BOTTOM_L3_ObjectFromEdge1,BOTTOM_L1_ObjectFromEdge1,BOTTOM_L2_ObjectFromEdge1,BOTTOM_ObjectFromEdge1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:VectorSweepParameters",
		"DraftAngle:="		, "0deg",
		"DraftType:="		, "Round",
		"CheckFaceFaceIntersection:=", False,
		"SweepVectorX:="	, "0mm",
		"SweepVectorY:="	, "0mm",
		"SweepVectorZ:="	, "-0.1mm"
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AutoIdentifyPorts(
	[
		"NAME:Faces", 
		2924, 
		2931, 
		2938, 
		2945
	], False, 
	[
		"NAME:ReferenceConductors", 
		"Rectangle1"
	], "1", True)
oModule.EditDiffPairs(
	[
		"NAME:EditDiffPairs",
		[
			"NAME:Pair1",
			"PosBoundary:="		, "BOTTOM_L3_T1",
			"NegBoundary:="		, "BOTTOM_L1_T1",
			"CommonName:="		, "Comm1",
			"CommonRefZ:="		, "25ohm",
			"DiffName:="		, "Pri",
			"DiffRefZ:="		, "100ohm",
			"IsActive:="		, True,
			"UseMatched:="		, False
		],
		[
			"NAME:Pair2",
			"PosBoundary:="		, "BOTTOM_L2_T1",
			"NegBoundary:="		, "BOTTOM_T1",
			"CommonName:="		, "Comm2",
			"CommonRefZ:="		, "25ohm",
			"DiffName:="		, "Sec",
			"DiffRefZ:="		, "100ohm",
			"IsActive:="		, True,
			"UseMatched:="		, False
		]
	])
oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditSetup("HFSS_Setup_1", 
	[
		"NAME:HFSS_Setup_1",
		"SolveType:="		, "Broadband",
		[
			"NAME:MultipleAdaptiveFreqsSetup",
			"Low:="			, "1MHz",
			"High:="		, "30MHz"
		],
		"MaxDeltaS:="		, 0.001,
		"MaximumPasses:="	, 20,
		"MinimumPasses:="	, 2,
		"MinimumConvergedPasses:=", 2,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"BasisOrder:="		, -1,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, True,
		"Target:="		, 0.1,
		"UseMaxTetIncrease:="	, False,
		"PortAccuracy:="	, 2,
		"UseABCOnPort:="	, False,
		"SetPortMinMaxTri:="	, False,
		"UseDomains:="		, False,
		"UseIterativeSolver:="	, False,
		"SaveRadFieldsOnly:="	, True,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True,
		"IE Solver Accuracy:="	, "Balanced"
	])
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport(" L", "Terminal Solution Data", "Rectangular Plot", "HFSS_Setup_1 : Sweep_1", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["im(Zt(Pri,Pri))/(2*pi*freq)*1e9","im(Zt(Sec,Sec))/(2*pi*freq)*1e9"]
	])
oModule.CreateReport(" Q", "Terminal Solution Data", "Rectangular Plot", "HFSS_Setup_1 : Sweep_1", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["im(Zt(Pri,Pri))/re(Zt(Pri,Pri))","im(Zt(Sec,Sec))/re(Zt(Sec,Sec))"]
	])

oModule.CreateReport("R", "Terminal Solution Data", "Rectangular Plot", "HFSS_Setup_1 : Sweep_1", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["re(Zt(Pri,Pri))","re(Zt(Sec,Sec))"]
	])


import win32api
import win32con
 
win32api.keybd_event(17,0,0,0)  
win32api.keybd_event(65,0,0,0)  