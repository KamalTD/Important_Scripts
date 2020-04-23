
'''
script edit Clarisse Preferences samples :: Edit > Preferences

'''

import ix

#Color_Management :

ix.application.get_prefs(ix.api.AppPreferences.MODE_APPLICATION).set_bool_value("color_management", "use_ocio_config_file", True)


ix.application.get_prefs(ix.api.AppPreferences.MODE_APPLICATION).set_bool_value("color_management", "auto_detect_color_space", True)



ix.application.get_prefs(ix.api.AppPreferences.MODE_APPLICATION).set_string_value("color_management", "ocio_config_file", "C:/config.ocio")


ix.application.get_prefs(ix.api.AppPreferences.MODE_APPLICATION).set_preset_value("color_management", "scene_color_space", "ACES|ACES - ACEScg")


ix.application.get_prefs(ix.api.AppPreferences.MODE_APPLICATION).set_preset_value("color_management", "default_display_color_space", "Output|Output - sRGB")


#Clarisse Command Port :


ix.application.get_prefs(ix.api.AppPreferences.MODE_APPLICATION).set_bool_value("command_port", "enabled",True)

ix.application.get_prefs(ix.api.AppPreferences.MODE_APPLICATION).set_long_value("command_port", "port",55000)

#=================================================================================================================
#=================================================================================================================
#=================================================================================================================

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

#=================================================================================================================
#=================================================================================================================
#=================================================================================================================   
    
"""
  form all texture nodes in the scene get attribute and name
"""
  
import ix

objectList = ix.api.OfObjectArray() # the item that will contain all our objects

ix.application.get_factory().get_all_objects("ProjectItem", objectList) # this function fill the objectList

for i in range(objectList.get_count()):



    if objectList[i].is_kindof("TextureStreamedMapFile") == True or objectList[i].is_kindof("TextureMapFile") or objectList[i].is_kindof("TextureMap"):

        
        
        obj_full_name =  objectList[i].get_full_name()
        
        obj_attr = objectList[i].get_attribute("filename").get_string()

        print obj_name , ":" , obj_attr
        

################################################################################################### 
#get scene variables, Ex:'_renderPath'  
ix.application.get_factory().get_vars().get("_renderPath").get_string()

  
  
