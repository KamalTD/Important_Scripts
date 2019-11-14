
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
