"""
Script to Get all folder and file names and store it in txt file in the same directory

"""
import os



def get_files(dir = None,mark = None,*args):

    """
    dir     :: directory to get data from EX: D:/Movies/

    mark    :: Start every new line with this mark

    *args   :: File Extensions

    """
    
    if True:
        
        out_file = open(dir + "file_Crawler.txt","w")
        
        for root , dirs, files in os.walk(dir, topdown=True):
            
            dirs.sort()
            
            if "/" in root:
                
                root = root.replace("/","\\")
                
            folder_name = root.split("\\")

            out_file.write("===================== %s =====================\n\n" %folder_name[-1::][0])

            for file in sorted(files):

                for arg in args:

                    if file.endswith(arg):
                        

                        out_file.write("%s %s\n\n" %(mark,file))
                        

                        
        out_file.close()

     
        


# Example ================================

get_files("D:/Movie/", "*-",   "mp4",   "mkv")


