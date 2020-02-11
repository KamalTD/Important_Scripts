"""
    select all Texture Nodes in the scene

"""

import ix

item_List = ix.api.OfObjectArray() # Make empty object list

ix.application.get_factory().get_all_objects("ProjectItem", item_List) # assign all scene nodes to item_List

selection = []

for i in range(item_List.get_count()):

    """
        filter all items in the scene , add just "TextureStreamedMapFile,TextureMapFile,TextureMap" to selection list

    """



    if item_List[i].is_kindof("TextureStreamedMapFile") == True or item_List[i].is_kindof("TextureMapFile") or item_List[i].is_kindof("TextureMap"):

        """
            Check if the node is Texture Node

        """




        selection.append(item_List[i]) # append to selection list



ix.application.get_selection().set_selection('global','Global',selection[0] ) # select first item in selection list



for sel in range(len(selection)-1):

    """
    range(len(selection)-1) to extract first item in the selection list that already selected and append the rest of items to this one

    """


    ix.application.get_selection().add_item('global',selection[sel+1],'Global') # select all items
