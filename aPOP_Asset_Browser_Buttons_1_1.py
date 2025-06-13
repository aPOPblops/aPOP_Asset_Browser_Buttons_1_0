bl_info = {
    "name": "Simple Display Type Buttons",
    "author": "aPOP",
    "version": (1, 1, 0),
    "blender": (4, 4, 0),
    "location": "File Browser Header",
    "description": "Add 3 simple display type buttons",
    "warning": "",
    "doc_url": "",
    "category": "Interface",
}

import bpy
from bpy.types import Operator


class FILEBROWSER_OT_display_list_vertical(Operator):
    """Switch to Vertical List view"""
    bl_idname = "file.display_list_vertical"
    bl_label = "Vertical List"
    bl_description = "Switch to vertical list display type"

    @classmethod
    def poll(cls, context):
        return context.space_data and context.space_data.type == 'FILE_BROWSER'

    def execute(self, context):
        context.space_data.params.display_type = 'LIST_VERTICAL'
        return {'FINISHED'}


class FILEBROWSER_OT_display_list_horizontal(Operator):
    """Switch to Horizontal List view"""
    bl_idname = "file.display_list_horizontal"
    bl_label = "Horizontal List"
    bl_description = "Switch to horizontal list display type"

    @classmethod
    def poll(cls, context):
        return context.space_data and context.space_data.type == 'FILE_BROWSER'

    def execute(self, context):
        context.space_data.params.display_type = 'LIST_HORIZONTAL'
        return {'FINISHED'}


class FILEBROWSER_OT_display_thumbnails(Operator):
    """Switch to Thumbnail view"""
    bl_idname = "file.display_thumbnails"
    bl_label = "Thumbnails"
    bl_description = "Switch to thumbnail display type"

    @classmethod
    def poll(cls, context):
        return context.space_data and context.space_data.type == 'FILE_BROWSER'

    def execute(self, context):
        context.space_data.params.display_type = 'THUMBNAIL'
        context.area.tag_redraw()
        return {'FINISHED'}


def draw_display_buttons(self, context):
    """Add the 3 display buttons to file browser header"""
    if context.space_data and context.space_data.type == 'FILE_BROWSER':
        layout = self.layout
        
        # Get current display type
        current_display = context.space_data.params.display_type
        
        # Add spacer to push buttons towards center
        layout.separator_spacer()
        
        # Create button row
        row = layout.row(align=True)
        
        # Vertical List button
        if current_display == 'LIST_VERTICAL':
            row.operator("file.display_list_vertical", text="", icon='LONGDISPLAY', depress=True)
        else:
            row.operator("file.display_list_vertical", text="", icon='LONGDISPLAY')
        
        # Horizontal List button
        if current_display == 'LIST_HORIZONTAL':
            row.operator("file.display_list_horizontal", text="", icon='SHORTDISPLAY', depress=True)
        else:
            row.operator("file.display_list_horizontal", text="", icon='SHORTDISPLAY')
        
        # Thumbnail button - use correct icon name
        if current_display == 'THUMBNAIL':
            row.operator("file.display_thumbnails", text="", icon='IMGDISPLAY', depress=True)
        else:
            row.operator("file.display_thumbnails", text="", icon='IMGDISPLAY')


def register():
    """Register the add-on"""
    bpy.utils.register_class(FILEBROWSER_OT_display_list_vertical)
    bpy.utils.register_class(FILEBROWSER_OT_display_list_horizontal)
    bpy.utils.register_class(FILEBROWSER_OT_display_thumbnails)
    
    # Use append but with spacer to control positioning
    bpy.types.FILEBROWSER_HT_header.append(draw_display_buttons)


def unregister():
    """Unregister the add-on"""
    bpy.types.FILEBROWSER_HT_header.remove(draw_display_buttons)
    
    bpy.utils.unregister_class(FILEBROWSER_OT_display_thumbnails)
    bpy.utils.unregister_class(FILEBROWSER_OT_display_list_horizontal)
    bpy.utils.unregister_class(FILEBROWSER_OT_display_list_vertical)


# For direct execution/testing in Blender
if __name__ == "__main__":
    try:
        unregister()
    except:
        pass
    register()
    
    print("Simple Display Type Buttons loaded!")
    print("3 buttons added to File Browser header: Vertical List, Horizontal List, Thumbnails")