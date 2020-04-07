"""
    This script prevent dosen't allow openinig more than one same script at the same time .



    How it works:
    
    *- check if the "file" that ends with "police for example" exists in the temp folder .
    
         - if the "file" exists it will not run.
         
         - if the "file" dosen't exist it will be created and run the "code_to_run" function.   

"""

import os
import tempfile
import sys
from PyQt4.QtGui import QWidget,QApplication,QLabel


class window(QLabel):
    def __init__(self):
        super(window, self).__init__()
        self.setText("Hello!! you can't run more of me :)")
        self.show()





def run_checker():

    """
    Check the file exist in temp ,

    Or create it if not exists

    :return: file_exist

    """

    temp_path = str(tempfile.gettempdir())

    file_exist = False

    for dirs , root,files in os.walk(temp_path):

        for file in files:

            if file.endswith("police"):

                file_exist = True

                break

        break


    return file_exist



def code_to_run():
    """
    Open window if it can

    :return:
    """

    file_exist = run_checker()

    if file_exist == False:

        mk_temp_file = tempfile.NamedTemporaryFile(mode='w+b',suffix="police")


        app= QApplication(sys.argv)

        window_ = window()

        sys.exit(app.exec_())

    else:

        print "I can't run more than once at the same time"





code_to_run()


