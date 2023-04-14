import bpy
from bpy.props import (EnumProperty, StringProperty, BoolProperty)
from bpy.types import (PropertyGroup, Operator)
import os

class AutoTexProperties(bpy.types.PropertyGroup):
    
    gltf_Node : bpy.props.BoolProperty(
        name="Add glTF Node",
        description="Create a GLB/GLTF Output node, connect AO or ORM red channel to it for Ambient Occlusion",
        default=False
    )
    texCoord : bpy.props.BoolProperty(
        name="Add Texture Coord",
        description="Add Texture Coordinate node with mapping",
        default=False
    )
    displacement : bpy.props.BoolProperty(
        name="Add Displacement",
        description="Add a Displacement node, connect to material output",
        default=False
    )
    image_file_type: bpy.props.EnumProperty(
        name="Image File Type",
        description="Select the image file type",
        items=(
            (".jpg", "JPEG", ""),
            (".png", "PNG", ""),
            (".bmp", "BMP", ""),
            (".tga", "Targa", "")
        ),
        default=".jpg"
    )
    
    apply_to: bpy.props.EnumProperty(
        name="Apply To",
        description="Select the option to apply to",
        items=(
            ("SELECTED", "Selected", ""),
            ("ALL_ATTACHED", "All Attached", ""),
            ("ALL_VISIBLE", "All Visible", ""),
        ),
        default="SELECTED"
    )
    node_structure: bpy.props.EnumProperty(
        name="Node Structure",
        description="Select the node structure",
        items=(
            ("ORM_GLB", "ORM - GLB", ""),
            ("BLENDER_BSDF", "Blender (BSDF)", ""),
            #("PBR_METALLIC_ROUGHNESS", "PBR (Metallic Roughness)", ""),
            #("DOCUMENT_CHANNELS_NORMAL_AO_NO_ALPHA", "Document Channels + Normal + AO (No Alpha)", ""),
            #("DOCUMENT_CHANNELS_NORMAL_AO_WITH_ALPHA", "Document Channels + Normal + AO (With Alpha)", ""),
        ),
        default="ORM_GLB"
    )
        # Add two new StringProperty properties for texture names
    normal_map: bpy.props.StringProperty(
        name="Normal Map",
        default="_Normal"
    )
    base_color: bpy.props.StringProperty(
        name="Base Color",
        default="_Color"
    )
    texturePath: bpy.props.StringProperty(
        name="Path",
        default = "/Textures"
    )

        
