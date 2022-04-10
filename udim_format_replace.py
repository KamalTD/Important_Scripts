#Replace '%(UDIM)d' to '<UDIM>' in houdini arnold solaris stage

import hou
def collect_nodes(parent_node, filter=["image"]):
    
    fileName = None
    result = []
    if parent_node != None:
        for n in parent_node.children():
            t = str(n.type().name())
            if t != None:
                for filter_item in filter:
                    if (t.find(filter_item) != -1):
                        if n not in result:
                            result.append(n)
    return result
  
node = hou.node("/stage")
collect_mtl = collect_nodes(node,['materiallibrary'])
for mtl in collect_mtl:
    collect_net = collect_nodes(mtl,['arnold_materialbuilder'])
    for network in collect_net:
    
        collect_image = collect_nodes(network,['image'])
        for image in collect_image:
            print(image.name())
            file_name = image.parm('filename').eval()
            image.parm('filename').set(file_name.replace("%(UDIM)d","<UDIM>"))
        
