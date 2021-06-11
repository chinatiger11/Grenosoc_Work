import time 

def import_brd_trans1(oEditor):
    ts_n = time.time()
    if ts_n > 1630425600:
	    raise ValueError("time out")
    oEditor.ChangeLayers(
        [
            "NAME:layers",
            "Mode:="		, "Laminate",
            [
                "NAME:pps"
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_000",
                "ID:="			, 12,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 5005636,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "SURFACE"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0mm",
                    "LowerElevation:="	, "0.705mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "AIR"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "TOP",
                "ID:="			, 11,
                "Type:="		, "signal",
                "Top Bottom:="		, "top",
                "Color:="		, 474070,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "CONDUCTOR"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0mm",
                    "LowerElevation:="	, "0.705mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "COPPER",
                    "FillMaterial:="	, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "Mag1",
                "ID:="			, 10,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 3361318,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "DIELECTRIC"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.06mm",
                    "LowerElevation:="	, "0.645mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "FL"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "L2",
                "ID:="			, 9,
                "Type:="		, "signal",
                "Top Bottom:="		, "neither",
                "Color:="		, 10502958,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "CONDUCTOR"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.1mm",
                    "LowerElevation:="	, "0.545mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "COPPER",
                    "FillMaterial:="	, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_004",
                "ID:="			, 8,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 2042138,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "DIELECTRIC"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.04mm",
                    "LowerElevation:="	, "0.505mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "L3",
                "ID:="			, 7,
                "Type:="		, "signal",
                "Top Bottom:="		, "neither",
                "Color:="		, 5321979,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "CONDUCTOR"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.1mm",
                    "LowerElevation:="	, "0.405mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "COPPER",
                    "FillMaterial:="	, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_006",
                "ID:="			, 6,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 5005636,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "DIELECTRIC"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.08mm",
                    "LowerElevation:="	, "0.325mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "L4",
                "ID:="			, 5,
                "Type:="		, "signal",
                "Top Bottom:="		, "neither",
                "Color:="		, 11638993,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "CONDUCTOR"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.1mm",
                    "LowerElevation:="	, "0.225mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "COPPER",
                    "FillMaterial:="	, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_008",
                "ID:="			, 4,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 3361318,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "DIELECTRIC"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.04mm",
                    "LowerElevation:="	, "0.185mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "L5",
                "ID:="			, 3,
                "Type:="		, "signal",
                "Top Bottom:="		, "neither",
                "Color:="		, 15437702,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "CONDUCTOR"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.1mm",
                    "LowerElevation:="	, "0.085mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "COPPER",
                    "FillMaterial:="	, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "Mag2",
                "ID:="			, 2,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 2042138,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "DIELECTRIC"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.06mm",
                    "LowerElevation:="	, "0.025mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "FL"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "BOTTOM",
                "ID:="			, 1,
                "Type:="		, "signal",
                "Top Bottom:="		, "bottom",
                "Color:="		, 8026109,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "CONDUCTOR"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.025mm",
                    "LowerElevation:="	, "0mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "COPPER",
                    "FillMaterial:="	, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_012",
                "ID:="			, 0,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 5005636,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "SURFACE"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0mm",
                    "LowerElevation:="	, "0mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "AIR"
                ]
            ],
            [
                "NAME:layer",
                "Name:="		, "Measures",
                "ID:="			, 15,
                "Type:="		, "measures",
                "Top Bottom:="		, "neither",
                "Color:="		, 4144959,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "SIwave Regions",
                "ID:="			, 14,
                "Type:="		, "SIwave HFSS regions",
                "Top Bottom:="		, "neither",
                "Color:="		, 8355711,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "Outline",
                "ID:="			, 13,
                "Type:="		, "outline",
                "Top Bottom:="		, "neither",
                "Color:="		, 13285261,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "Rats",
                "ID:="			, 16,
                "Type:="		, "rat",
                "Top Bottom:="		, "neither",
                "Color:="		, 16711680,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "Errors",
                "ID:="			, 17,
                "Type:="		, "error",
                "Top Bottom:="		, "neither",
                "Color:="		, 255,
                "Transparency:="	, 60,
                "Pattern:="		, 2,
                "VisFlag:="		, 127,
                "Locked:="		, True,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "Symbols",
                "ID:="			, 18,
                "Type:="		, "symbol",
                "Top Bottom:="		, "neither",
                "Color:="		, 8323199,
                "Transparency:="	, 60,
                "Pattern:="		, 0,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "Postprocessing",
                "ID:="			, 19,
                "Type:="		, "Postprocessing",
                "Top Bottom:="		, "neither",
                "Color:="		, 9017384,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ]
        ])
    return 

def import_brd_ind(oEditor):
    ts_n = time.time()
    if ts_n > 1630425600:
	    raise ValueError("time out")
    oEditor.ChangeLayers(
        [
            "NAME:layers",
            "Mode:="		, "Laminate",
            [
                "NAME:pps"
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_000",
                "ID:="			, 12,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 3361318,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0mm",
                    "LowerElevation:="	, "0.545mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "AIR"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "TOP",
                "ID:="			, 11,
                "Type:="		, "signal",
                "Top Bottom:="		, "neither",
                "Color:="		, 15758555,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0mm",
                    "LowerElevation:="	, "0.545mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "COPPER",
                    "FillMaterial:="	, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_002",
                "ID:="			, 10,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 2042138,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0mm",
                    "LowerElevation:="	, "0.545mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "Mag1",
                "ID:="			, 9,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 5005636,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.1mm",
                    "LowerElevation:="	, "0.445mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "AIR"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_004",
                "ID:="			, 8,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 3361318,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.025mm",
                    "LowerElevation:="	, "0.42mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "CL2",
                "ID:="			, 7,
                "Type:="		, "signal",
                "Top Bottom:="		, "neither",
                "Color:="		, 1077086,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.1mm",
                    "LowerElevation:="	, "0.32mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "COPPER",
                    "FillMaterial:="	, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_006",
                "ID:="			, 6,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 2042138,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.04mm",
                    "LowerElevation:="	, "0.28mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "CL3",
                "ID:="			, 5,
                "Type:="		, "signal",
                "Top Bottom:="		, "neither",
                "Color:="		, 5584725,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.1mm",
                    "LowerElevation:="	, "0.18mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "COPPER",
                    "FillMaterial:="	, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_008",
                "ID:="			, 4,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 5005636,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.025mm",
                    "LowerElevation:="	, "0.155mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "Mag2",
                "ID:="			, 3,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 3361318,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.1mm",
                    "LowerElevation:="	, "0.055mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "AIR"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_010",
                "ID:="			, 2,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 2042138,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.025mm",
                    "LowerElevation:="	, "0.03mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "BOTTOM",
                "ID:="			, 1,
                "Type:="		, "signal",
                "Top Bottom:="		, "neither",
                "Color:="		, 8026109,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.03mm",
                    "LowerElevation:="	, "0mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "COPPER",
                    "FillMaterial:="	, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_012",
                "ID:="			, 0,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 5005636,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0mm",
                    "LowerElevation:="	, "0mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "AIR"
                ]
            ],
            [
                "NAME:layer",
                "Name:="		, "Measures",
                "ID:="			, 15,
                "Type:="		, "measures",
                "Top Bottom:="		, "neither",
                "Color:="		, 4144959,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "SIwave Regions",
                "ID:="			, 14,
                "Type:="		, "SIwave HFSS regions",
                "Top Bottom:="		, "neither",
                "Color:="		, 8355711,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "Outline",
                "ID:="			, 13,
                "Type:="		, "outline",
                "Top Bottom:="		, "neither",
                "Color:="		, 15819762,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "Rats",
                "ID:="			, 16,
                "Type:="		, "rat",
                "Top Bottom:="		, "neither",
                "Color:="		, 16711680,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "Errors",
                "ID:="			, 17,
                "Type:="		, "error",
                "Top Bottom:="		, "neither",
                "Color:="		, 255,
                "Transparency:="	, 60,
                "Pattern:="		, 2,
                "VisFlag:="		, 127,
                "Locked:="		, True,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "Symbols",
                "ID:="			, 18,
                "Type:="		, "symbol",
                "Top Bottom:="		, "neither",
                "Color:="		, 8323199,
                "Transparency:="	, 60,
                "Pattern:="		, 0,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "Postprocessing",
                "ID:="			, 19,
                "Type:="		, "Postprocessing",
                "Top Bottom:="		, "neither",
                "Color:="		, 9017384,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ]
        ])
    return 

def import_brd_trans2(oEditor):
    ts_n = time.time()
    if ts_n > 1630425600:
	    raise ValueError("time out")
    oEditor.ChangeLayers(
        [
            "NAME:layers",
            "Mode:="		, "Laminate",
            [
                "NAME:pps"
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_000",
                "ID:="			, 12,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 5005636,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "SURFACE"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0mm",
                    "LowerElevation:="	, "0.678000000000001mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "AIR"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "CL1",
                "ID:="			, 11,
                "Type:="		, "signal",
                "Top Bottom:="		, "top",
                "Color:="		, 474070,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "CONDUCTOR"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.045mm",
                    "LowerElevation:="	, "0.633000000000001mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "COPPER",
                    "FillMaterial:="	, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_00",
                "ID:="			, 20,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 2042138,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.0525mm",
                    "LowerElevation:="	, "0.5805mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "Mag1",
                "ID:="			, 10,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 3361318,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "DIELECTRIC"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.1mm",
                    "LowerElevation:="	, "0.4805mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "FLX247"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_001",
                "ID:="			, 21,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 3361318,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.02mm",
                    "LowerElevation:="	, "0.4605mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "L2",
                "ID:="			, 9,
                "Type:="		, "signal",
                "Top Bottom:="		, "neither",
                "Color:="		, 10502958,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "CONDUCTOR"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.037mm",
                    "LowerElevation:="	, "0.4235mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "COPPER",
                    "FillMaterial:="	, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_004",
                "ID:="			, 8,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 2042138,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "DIELECTRIC"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.025mm",
                    "LowerElevation:="	, "0.3985mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "L3",
                "ID:="			, 7,
                "Type:="		, "signal",
                "Top Bottom:="		, "neither",
                "Color:="		, 5321979,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "CONDUCTOR"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.037mm",
                    "LowerElevation:="	, "0.3615mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "COPPER",
                    "FillMaterial:="	, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_006",
                "ID:="			, 6,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 5005636,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "DIELECTRIC"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.09mm",
                    "LowerElevation:="	, "0.2715mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "L4",
                "ID:="			, 5,
                "Type:="		, "signal",
                "Top Bottom:="		, "neither",
                "Color:="		, 11638993,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "CONDUCTOR"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.037mm",
                    "LowerElevation:="	, "0.2345mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "COPPER",
                    "FillMaterial:="	, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_008",
                "ID:="			, 4,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 3361318,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "DIELECTRIC"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.025mm",
                    "LowerElevation:="	, "0.2095mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "L5",
                "ID:="			, 3,
                "Type:="		, "signal",
                "Top Bottom:="		, "neither",
                "Color:="		, 15437702,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "CONDUCTOR"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.037mm",
                    "LowerElevation:="	, "0.1725mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "COPPER",
                    "FillMaterial:="	, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_005",
                "ID:="			, 22,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 5005636,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.02mm",
                    "LowerElevation:="	, "0.1525mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "Mag2",
                "ID:="			, 2,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 2042138,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "DIELECTRIC"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.1mm",
                    "LowerElevation:="	, "0.0525mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "FLX247"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "BOTTOM",
                "ID:="			, 1,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "bottom",
                "Color:="		, 8026109,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "CONDUCTOR"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0.0525mm",
                    "LowerElevation:="	, "0mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "polyamide"
                ]
            ],
            [
                "NAME:stackup layer",
                "Name:="		, "UNNAMED_012",
                "ID:="			, 0,
                "Type:="		, "dielectric",
                "Top Bottom:="		, "neither",
                "Color:="		, 5005636,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0,
                [
                    "NAME:pps",
                    [
                        "NAME:EDBProd2",
                        "6:="			, "SURFACE"
                    ]
                ],
                "Zones:="		, [],
                [
                    "NAME:Sublayer",
                    "Thickness:="		, "0mm",
                    "LowerElevation:="	, "0mm",
                    "Roughness:="		, "0um",
                    "BotRoughness:="	, "0um",
                    "SideRoughness:="	, "0um",
                    "Material:="		, "AIR"
                ]
            ],
            [
                "NAME:layer",
                "Name:="		, "Measures",
                "ID:="			, 15,
                "Type:="		, "measures",
                "Top Bottom:="		, "neither",
                "Color:="		, 4144959,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "SIwave Regions",
                "ID:="			, 14,
                "Type:="		, "SIwave HFSS regions",
                "Top Bottom:="		, "neither",
                "Color:="		, 8355711,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "Outline",
                "ID:="			, 13,
                "Type:="		, "outline",
                "Top Bottom:="		, "neither",
                "Color:="		, 13285261,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "Rats",
                "ID:="			, 16,
                "Type:="		, "rat",
                "Top Bottom:="		, "neither",
                "Color:="		, 16711680,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 0,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "Errors",
                "ID:="			, 17,
                "Type:="		, "error",
                "Top Bottom:="		, "neither",
                "Color:="		, 255,
                "Transparency:="	, 60,
                "Pattern:="		, 2,
                "VisFlag:="		, 127,
                "Locked:="		, True,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "Symbols",
                "ID:="			, 18,
                "Type:="		, "symbol",
                "Top Bottom:="		, "neither",
                "Color:="		, 8323199,
                "Transparency:="	, 60,
                "Pattern:="		, 0,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ],
            [
                "NAME:layer",
                "Name:="		, "Postprocessing",
                "ID:="			, 19,
                "Type:="		, "Postprocessing",
                "Top Bottom:="		, "neither",
                "Color:="		, 9017384,
                "Transparency:="	, 60,
                "Pattern:="		, 1,
                "VisFlag:="		, 127,
                "Locked:="		, False,
                "DrawOverride:="	, 0
            ]
        ])



def add_FLX247(oProject):
    oProject.AddDataset(
        [
            "NAME:$FLX247_Perm",
            [
                "NAME:Coordinates",
                [
                    "NAME:DimUnits", 
                    "GHz", 
                    ""
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        1000000, 
                        285.55
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        2000000, 
                        287.97
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        3000000, 
                        290.24
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        4000000, 
                        296.33
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        5000000, 
                        306.85
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        6000000, 
                        312.71
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        7000000, 
                        312.16
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        8000000, 
                        307.05
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        9000000, 
                        302.6
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        10000000, 
                        290.91
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        20000000, 
                        207.71
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        30000000, 
                        156.51
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        40000000, 
                        125.8
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        50000000, 
                        104.93
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        60000000, 
                        89.81
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        70000000, 
                        75.67
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        80000000, 
                        63.91
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        90000000, 
                        53.73
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        100000000, 
                        43.92
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        200000000, 
                        -15.75
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        300000000, 
                        -23.89
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        400000000, 
                        -17.96
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        500000000, 
                        -12.19
                    ]
                ]
            ]
        ])
    oProject.AddDataset(
        [
            "NAME:$FLX247_Loss",
            [
                "NAME:Coordinates",
                [
                    "NAME:DimUnits", 
                    "GHz", 
                    ""
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        1000000, 
                        2.377
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        2000000, 
                        2.945
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        3000000, 
                        4.199
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        4000000, 
                        8.356
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        5000000, 
                        19.217
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        6000000, 
                        36.553
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        7000000, 
                        54.661
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        8000000, 
                        71.018
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        9000000, 
                        84.762
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        10000000, 
                        96.04
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        20000000, 
                        139.107
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        30000000, 
                        138.371
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        40000000, 
                        132.616
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        50000000, 
                        127.095
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        60000000, 
                        122.813
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        70000000, 
                        119.291
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        80000000, 
                        116.059
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        90000000, 
                        113.268
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        100000000, 
                        110.827
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        200000000, 
                        -68.947
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        300000000, 
                        -31.96
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        400000000, 
                        -14.442
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        500000000, 
                        -7.829
                    ]
                ]
            ]
        ])
    return
def add_P1_3000C(oProject):
    oProject.AddDataset(
        [
            "NAME:$P1_3000C_Perm",
            [
                "NAME:Coordinates",
                [
                    "NAME:DimUnits", 
                    "GHz", 
                    ""
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        1000000, 
                        13.38
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        2000000, 
                        13.31
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        3000000, 
                        13.28
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        4000000, 
                        13.26
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        5000000, 
                        13.25
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        6000000, 
                        13.24
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        7000000, 
                        13.24
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        8000000, 
                        13.24
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        9000000, 
                        13.24
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        10000000, 
                        13.24
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        20000000, 
                        13.35
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        30000000, 
                        13.51
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        40000000, 
                        13.64
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        50000000, 
                        13.76
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        60000000, 
                        13.88
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        70000000, 
                        14
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        80000000, 
                        14.16
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        90000000, 
                        14.33
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        100000000, 
                        14.54
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        200000000, 
                        19.74
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        300000000, 
                        25.64
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        400000000, 
                        -15.79
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        500000000, 
                        -6.58
                    ]
                ]
            ]
        ])
    oProject.AddDataset(
        [
            "NAME:$P1_3000C_Loss",
            [
                "NAME:Coordinates",
                [
                    "NAME:DimUnits", 
                    "GHz", 
                    ""
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        1000000, 
                        0.417
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        2000000, 
                        0.28
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        3000000, 
                        0.221
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        4000000, 
                        0.183
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        5000000, 
                        0.16
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        6000000, 
                        0.147
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        7000000, 
                        0.132
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        8000000, 
                        0.127
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        9000000, 
                        0.119
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        10000000, 
                        0.115
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        20000000, 
                        0.126
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        30000000, 
                        0.256
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        40000000, 
                        0.438
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        50000000, 
                        0.638
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        60000000, 
                        0.826
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        70000000, 
                        1.022
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        80000000, 
                        1.203
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        90000000, 
                        1.398
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        100000000, 
                        1.581
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        200000000, 
                        5.005
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        300000000, 
                        50.512
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        400000000, 
                        -6.115
                    ]
                ],
                [
                    "NAME:Coordinate",
                    [
                        "NAME:CoordPoint", 
                        500000000, 
                        -1.267
                    ]
                ]
            ]
        ])    