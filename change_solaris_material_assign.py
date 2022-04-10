#Add astric(*) to 'primatives parameter' in all material assign node in solaris stage
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
collect_mtl = collect_nodes(node,['assignmaterial'])
for mtl in collect_mtl:
    matl_count = mtl.parm('nummaterials').eval()
    
    for network in range(1,matl_count+1):

        
        prim = mtl.parm('primpattern{}'.format(network)).eval().split("*")[1]
        mtl.parm('primpattern{}'.format(network)).set("*{}".format(prim))
        
