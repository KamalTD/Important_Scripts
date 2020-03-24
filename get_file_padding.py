#this function is to get padding from the end of a file and return "file name and padding(frame number)"

def get_padding(file = ""):
  
    
    file = file.split(".")[0]
    
    file_name = file

    list = []

    for char in file:

        list.append(char)

    list.reverse()

    digit_count = 0
    
    
    
    for num in list:
    
        try:
        
            int(num)
            
            digit_count += 1
            
            
        except:
        
            break

    return digit_count,file_name

#Ex:
padding,file = get_padding("Black_Smoke_Seed01_1835.vdb")
