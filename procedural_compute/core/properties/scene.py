###########################################################
# Blender Addon for Procedural Cloud-based Design Tools
# Copyright (C) 2020, Procedural Compute
# License : procedural compute license
# Version : 1.2
# Web     : compute.procedural.build
###########################################################


import bpy
from procedural_compute.core.utils.selectUtils import makeTuples

##############


class BM_SCENE_ODS(bpy.types.PropertyGroup):
    mainMenu: bpy.props.EnumProperty(
        name="mainMenu",
        items=makeTuples(["SunPath", "CFD", "Radiance", "Energy"]),
        description="Procedural Compute menu categories"
    )


bpy.utils.register_class(BM_SCENE_ODS)

##############
# Point from Scene to ODS variables
bpy.types.Scene.ODS = bpy.props.PointerProperty(type=BM_SCENE_ODS)
