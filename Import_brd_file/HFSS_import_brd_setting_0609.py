# ----------------------------------------------
# Script for OPPO Couple Inductor
# Script Recorded by ANSYS Electronics Desktop Version 2020.2.0
# 7:39:12  May, 2021
# ----------------------------------------------
from win32com import client
import os
import shutil
from pathlib import Path
import time
import initial
import import_design_setting

import_brd_file = r"D:\Test\Dest20210604\Dom_test.brd"
# device_x = 1.6
# device_y = 1.6
interface, module_name = initial.init_HFSS(import_brd_file)

path_list= os.path.split(import_brd_file)
project_name = path_list[1].split(".")[0]
design_name = project_name
layout_name = project_name + ".aedt"
layout_path = os.path.join(path_list[0],layout_name)
aedb_name = project_name + ".aedb"
adeb_path = os.path.join(path_list[0],aedb_name)
aedb_path = Path(adeb_path).as_posix()
xml_name = project_name + ".xml"
xml_path = os.path.join(path_list[0],xml_name)
xml_path = Path(xml_path).as_posix()
hfss_name = "HFSS_"+project_name+".aedt"
hfss_path = os.path.join(path_list[0],hfss_name)
hfss_path = Path(hfss_path).as_posix() 

oAnsoftApp = client.Dispatch(interface)
oDesktop = oAnsoftApp.GetAppDesktop()
oDesktop.RestoreWindow()
oTool = oDesktop.GetTool(module_name)
oTool.ImportExtracta(import_brd_file, adeb_path, xml_path)
oProject = oDesktop.SetActiveProject(project_name)
oDesign = oProject.SetActiveDesign(design_name)
oEditor = oDesign.SetActiveEditor("Layout")

import_design_setting.import_brd_trans2(oEditor)

# ts_n = time.time()
# if ts_n > 1622276620:
# 	raise ValueError("time out")
oModule = oDesign.GetModule("SolveSetups")
oModule.Add(
	[
		"NAME:HFSS Setup 1",
		[
			"NAME:Properties",
			"Enable:="		, "true"
		],
		"CustomSetup:="		, False,
		"AutoSetup:="		, False,
		"SliderType:="		, "Balanced",
		"SolveSetupType:="	, "HFSS",
		"PercentRefinementPerPass:=", 30,
		"MinNumberOfPasses:="	, 2,
		"MinNumberOfConvergedPasses:=", 2,
		"UseDefaultLambda:="	, False,
		"UseMaxRefinement:="	, False,
		"MaxRefinement:="	, 1000000,
		"SaveAdaptiveCurrents:=", True,
		"SaveLastAdaptiveRadFields:=", True,
		"ProdMajVerID:="	, -1,
		"ProjDesignSetup:="	, "",
		"ProdMinVerID:="	, -1,
		"Refine:="		, False,
		"Frequency:="		, "10GHz",
		"LambdaRefine:="	, True,
		"MeshSizeFactor:="	, 10,
		"QualityRefine:="	, True,
		"MinAngle:="		, "15deg",
		"UniformityRefine:="	, False,
		"MaxRatio:="		, 2,
		"Smooth:="		, False,
		"SmoothingPasses:="	, 5,
		"UseEdgeMesh:="		, False,
		"UseEdgeMeshAbsLength:=", False,
		"EdgeMeshRatio:="	, 0.1,
		"EdgeMeshAbsLength:="	, "1000mm",
		"LayerProjectThickness:=", "0meter",
		"UseDefeature:="	, True,
		"UseDefeatureAbsLength:=", False,
		"DefeatureRatio:="	, 1E-06,
		"DefeatureAbsLength:="	, "0mm",
		"InfArrayDimX:="	, 0,
		"InfArrayDimY:="	, 0,
		"InfArrayOrigX:="	, 0,
		"InfArrayOrigY:="	, 0,
		"InfArraySkew:="	, 0,
		"ViaNumSides:="		, 6,
		"ViaMaterial:="		, "copper",
		"Style25DVia:="		, "Mesh",
		"Replace3DTriangles:="	, True,
		"LayerSnapTol:="	, "1e-05",
		"ViaDensity:="		, 0,
		"HfssMesh:="		, True,
		"Q3dPostProc:="		, False,
		"UnitFactor:="		, 1000,
		"Verbose:="		, False,
		"NumberOfProcessors:="	, 0,
		"SmallVoidArea:="	, -4E-12,
		"HealingOption:="	, 1,
		"InclBBoxOption:="	, 1,
		"ModelType:="		, 0,
		[
			"NAME:AuxBlock"
		],
		"DoAdaptive:="		, True,
		"Color:="		, [			"R:="			, 0,			"G:="			, 0,			"B:="			, 0],
		[
			"NAME:AdvancedSettings",
			"AccuracyLevel:="	, 2,
			"GapPortCalibration:="	, True,
			"ReferenceLengthRatio:=", 0.25,
			"RefineAreaRatio:="	, 4,
			"DRCOn:="		, False,
			"FastSolverOn:="	, False,
			"StartFastSolverAt:="	, 3000,
			"LoopTreeOn:="		, True,
			"SingularElementsOn:="	, False,
			"UseStaticPortSolver:="	, False,
			"UseThinMetalPortSolver:=", False,
			"ComputeBothEvenAndOddCPWModes:=", False,
			"ZeroMetalLayerThickness:=", 0,
			"ThinDielectric:="	, 0,
			"UseShellElements:="	, False,
			"SVDHighCompression:="	, False,
			"NumProcessors:="	, 1,
			"UseHfssIterativeSolver:=", False,
			"UseHfssMUMPSSolver:="	, True,
			"RelativeResidual:="	, 1E-06,
			"EnhancedLowFreqAccuracy:=", False,
			"OrderBasis:="		, -1,
			"MaxDeltaZo:="		, 2,
			"UseRadBoundaryOnPorts:=", False,
			"SetTrianglesForWavePort:=", False,
			"MinTrianglesForWavePort:=", 100,
			"MaxTrianglesForWavePort:=", 500,
			"numprocessorsdistrib:=", 1,
			"CausalMaterials:="	, True,
			"enabledsoforopti:="	, True,
			"usehfsssolvelicense:="	, False,
			"ExportAfterSolve:="	, False,
			"ExportDir:="		, "",
			"CircuitSparamDefinition:=", False,
			"CircuitIntegrationType:=", "FFT",
			"DesignType:="		, "Generic",
			"MeshingMethod:="	, "Phi",
			"EnableDesignIntersectionCheck:=", True,
			"BroadbandFreqOption:="	, "AutoMaxFreq",
			"BroadbandMaxNumFreq:="	, 5,
			"UseAdvancedDCExtrap:="	, False
		],
		[
			"NAME:CurveApproximation",
			"ArcAngle:="		, "30deg",
			"StartAzimuth:="	, "0deg",
			"UseError:="		, False,
			"Error:="		, "0meter",
			"MaxPoints:="		, 8,
			"UnionPolys:="		, True,
			"Replace3DTriangles:="	, True
		],
		[
			"NAME:Q3D_DCSettings",
			"SolveResOnly:="	, True,
			[
				"NAME:Cond",
				"MaxPass:="		, 10,
				"MinPass:="		, 1,
				"MinConvPass:="		, 1,
				"PerError:="		, 1,
				"PerRefine:="		, 30
			],
			[
				"NAME:Mult",
				"MaxPass:="		, 1,
				"MinPass:="		, 1,
				"MinConvPass:="		, 1,
				"PerError:="		, 1,
				"PerRefine:="		, 30
			],
			"Solution Order:="	, "Normal"
		],
		[
			"NAME:AdaptiveSettings",
			"DoAdaptive:="		, True,
			"SaveFields:="		, False,
			"SaveRadFieldsOnly:="	, False,
			"MaxRefinePerPass:="	, 30,
			"MinPasses:="		, 1,
			"MinConvergedPasses:="	, 1,
			"AdaptType:="		, "kSingle",
			"Basic:="		, True,
			[
				"NAME:SingleFrequencyDataList",
				[
					"NAME:AdaptiveFrequencyData",
					"AdaptiveFrequency:="	, "1MHz",
					"MaxDelta:="		, "0.005",
					"MaxPasses:="		, 20,
					"Expressions:="		, []
				]
			],
			[
				"NAME:BroadbandFrequencyDataList",
				[
					"NAME:AdaptiveFrequencyData",
					"AdaptiveFrequency:="	, "5GHz",
					"MaxDelta:="		, "0.005",
					"MaxPasses:="		, 20,
					"Expressions:="		, []
				],
				[
					"NAME:AdaptiveFrequencyData",
					"AdaptiveFrequency:="	, "10GHz",
					"MaxDelta:="		, "0.005",
					"MaxPasses:="		, 20,
					"Expressions:="		, []
				]
			],
			[
				"NAME:MultiFrequencyDataList",
				[
					"NAME:AdaptiveFrequencyData",
					"AdaptiveFrequency:="	, "2.5GHz",
					"MaxDelta:="		, "0.005",
					"MaxPasses:="		, 20,
					"Expressions:="		, []
				],
				[
					"NAME:AdaptiveFrequencyData",
					"AdaptiveFrequency:="	, "5GHz",
					"MaxDelta:="		, "0.005",
					"MaxPasses:="		, 20,
					"Expressions:="		, []
				],
				[
					"NAME:AdaptiveFrequencyData",
					"AdaptiveFrequency:="	, "10GHz",
					"MaxDelta:="		, "0.005",
					"MaxPasses:="		, 20,
					"Expressions:="		, []
				]
			]
		]
	])
oModule.AddSweep("HFSS Setup 1", 
	[
		"NAME:Sweep 1",
		[
			"NAME:Properties",
			"Enable:="		, "true"
		],
		[
			"NAME:Sweeps",
			"Variable:="		, "Sweep 1",
			"Data:="		, "LIN 0Hz 1MHz 100kHz LIN 1.5MHz 30MHz 500kHz",
			"OffsetF1:="		, False,
			"Synchronize:="		, 0
		],
		"GenerateSurfaceCurrent:=", False,
		"SaveRadFieldsOnly:="	, False,
		"FastSweep:="		, True,
		"ZoSelected:="		, False,
		"SAbsError:="		, 0.005,
		"ZoPercentError:="	, 1,
		"GenerateStateSpace:="	, False,
		"EnforcePassivity:="	, True,
		"PassivityTolerance:="	, 0.0001,
		"UseQ3DForDC:="		, False,
		"ResimulateDC:="	, False,
		"MaxSolutions:="	, 250,
		"InterpUseSMatrix:="	, True,
		"InterpUsePortImpedance:=", True,
		"InterpUsePropConst:="	, True,
		"InterpUseFullBasis:="	, True,
		"AdvDCExtrapolation:="	, False,
		"MinSolvedFreq:="	, "0.01GHz",
		"CustomFrequencyString:=", "",
		"AllEntries:="		, False,
		"AllDiagEntries:="	, False,
		"AllOffDiagEntries:="	, False,
		"MagMinThreshold:="	, 0.01
	])
oModule.ExportToHfss("HFSS Setup 1", hfss_path)
time.sleep(1)
# oDesktop.CloseProject(project_name)
# oDesktop.QuitApplication()
shutil.rmtree(aedb_path)






# oAnsoftApp = client.Dispatch('AnsoftHfss.HfssScriptInterface')
# oDesktop = oAnsoftApp.GetAppDesktop()
# oDesktop.RestoreWindow()
# hfss_path =  hfss_path.replace("/","\\")
# hfss_open_path = str(hfss_path)
time.sleep(3)
oDesktop.OpenProject(hfss_path)
oProject = oDesktop.SetActiveProject("HFSS_"+project_name)
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "airbox"
	])

oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-4mm",
		"YStart:="		, "-4mm",
		"ZStart:="		, "0.778mm",
		"Width:="		, "8mm",
		"Height:="		, "8mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0.9,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])			
oEditor.CreateRegion(
	[
		"NAME:RegionParameters",
		"+XPaddingType:="	, "Percentage Offset",
		"+XPadding:="		, "150",
		"-XPaddingType:="	, "Percentage Offset",
		"-XPadding:="		, "150",
		"+YPaddingType:="	, "Percentage Offset",
		"+YPadding:="		, "150",
		"-YPaddingType:="	, "Percentage Offset",
		"-YPadding:="		, "150",
		"+ZPaddingType:="	, "Percentage Offset",
		"+ZPadding:="		, "150",
		"-ZPaddingType:="	, "Percentage Offset",
		"-ZPadding:="		, "150"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Region",
		"Flags:="		, "Wireframe#",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "nan ",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignPerfectE(
	[
		"NAME:PerfE1",
		"Objects:="		, ["Rectangle1"],
		"InfGroundPlane:="	, False
	])
oModule.AssignRadiation(
	[
		"NAME:Rad1",
		"Objects:="		, ["Region"],
		"IsFssReference:="	, False,
		"IsForPML:="		, False
	])
oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditSetup("HFSS_Setup_1", 
	[
		"NAME:HFSS_Setup_1",
		"SolveType:="		, "Single",
		"Frequency:="		, "0.03GHz",
		"MaxDeltaE:="		, 0.001,
		"UseMatrixConv:="	, False,
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
import_design_setting.add_FLX247(oProject)
oDefinitionManager = oProject.GetDefinitionManager()
oDefinitionManager.AddMaterial(
	[
		"NAME:FLX247",
		"CoordinateSystemType:=", "Cartesian",
		"BulkOrSurfaceType:="	, 1,
		[
			"NAME:PhysicsTypes",
			"set:="			, ["Electromagnetic"]
		],
		"permeability:="	, "pwl($FLX247_Perm,Freq)",
		"magnetic_loss_tangent:=", "pwl($FLX247_Loss,Freq)"
	])
import_design_setting.add_P1_3000C(oProject)
oDefinitionManager.AddMaterial(
	[
		"NAME:P1_3000C",
		"CoordinateSystemType:=", "Cartesian",
		"BulkOrSurfaceType:="	, 1,
		[
			"NAME:PhysicsTypes",
			"set:="			, ["Electromagnetic"]
		],
		"permeability:="	, "pwl($P1_3000C_Perm,Freq)",
		"magnetic_loss_tangent:=", "pwl($P1_3000C_Loss,Freq)"
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-0.543933982822mm",
		"YPosition:="		, "-0.3mm",
		"ZPosition:="		, "0.445mm",
		"XSize:="		, "1.093933982822mm",
		"YSize:="		, "0.5967949192431mm",
		"ZSize:="		, "-0.29mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Mag_via",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Mag1", 
				"Mag2"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Display Wireframe",
					"Value:="		, False
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Mag1", 
				"Mag2",
				"Mag_via"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 64,
					"G:="			, 0,
					"B:="			, 64
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Mag1", 
				"Mag2",
				"Mag_via"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Transparent",
					"Value:="		, 0.7
				]
			]
		]
	])
oEditor.AssignMaterial(
	[
		"NAME:Selections",
		"AllowRegionDependentPartSelectionForPMLCreation:=", True,
		"AllowRegionSelectionForPMLCreation:=", True,
		"Selections:="		, "Mag1,Mag2,Mag_via"
	], 
	[
		"NAME:Attributes",
		"MaterialValue:="	, "\"P1_3000C\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "nan ",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "L2_t_fill,L3_t_fill,L4_t_fill,L5_t_fill,UNNAMED_00,UNNAMED_001,UNNAMED_004,UNNAMED_005,UNNAMED_006,UNNAMED_008",
		"Tool Parts:="		, "Mag_via"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, True
	])

oProject.Save()	
# shutil.rmtree(aedb_path)
# os.remove(layout_path)
oDesktop.QuitApplication()		