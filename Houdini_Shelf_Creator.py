#execfile("<Path>/install.py")
"""
        Mahmoud Kamal 4/2/2020

            Houdini Shelf Creator

// Create New shelf "Houdini Tools" in "shelf_set_1" if not exists ,

// and if it exists will Create New Tool "Setup Assets" on it

// label= "Setup Assets" :: the label for this tool

// script = 'import sys\nsys.path.append("<Path>/")\nimport Houdini_Setup_Assets\nreload(Houdini_Setup_Assets) #execfile("<Path>/Houdini_Setup_Assets.py")' :: the script that contain in this tool



"""
import hou
"""
    Get the shelf set "Create and Refine
"""
shelf_set = hou.shelves.shelfSets()["shelf_set_1"]

#=============

"""
 Define "Setup Asset Tool" :

     name="Setup_Assets"

     label="Setup Assets"

     script='import sys\nsys.path.append("<Path>/")\nimport Houdini_Setup_Assets\nreload(Houdini_Setup_Assets) #execfile("<Path>/Houdini_Setup_Assets.py")'

     language= Python

      icon="<Path>/icon.jpg"

"""

setup_asset_tool = hou.shelves.newTool(file_path=None, name="Setup_Assets", label="Setup Assets",
                                       script='import sys\nsys.path.append("<Path>/")\nimport Houdini_Setup_Assets\nreload(Houdini_Setup_Assets) #execfile("<Path>/Houdini_Setup_Assets.py")',
                                       language=hou.scriptLanguage.Python, icon="<Path>/icon.jpg")


"""
    Now check if Tools is not exist Create It

"""

if "Tools" not in hou.shelves.shelves(): # check if Tools is not exist Create It

    """
       Define Trend Tools Shelf
    """

    Tools_Shelf = hou.shelves.newShelf(name="Tools", label="Tools")


    shelves_list = list(shelf_set.shelves()) # Get the shelves and assign it to  list

    shelves_list.append(Tools_Shelf) # Append Trend_Tools_Shelf to the shelves list

    shelf_set.setShelves(shelves_list)

else: # If it exist get it

    Tools_Shelf = hou.shelves.shelves()["Tools"]

Tools_Shelf.setTools((setup_asset_tool,)) # add setup_asset_tool to Tools_Shelf
