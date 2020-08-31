def get_node_outputs(node_path):
    
    """
      Get all node outputs and return it 
    """
    
    item = ix.get_item(node_path)

    obj_array = ix.api.OfItemArray(1)
    obj_array[0] = item
    item_outputs = ix.api.OfItemVector()

    ix.application.get_factory().get_items_outputs(obj_array, item_outputs, False)

    node_outputs = []
    for item_ in range(item_outputs.get_count()):

        for i in range(item_outputs[item_].get_attribute_count()):

            attr= item_outputs[item_].get_attribute(i)

            if attr.get_texture():

                if str(attr.get_texture()) == item.get_full_name():

                    #attrs[attr] = target_node.get_full_name()
                    node_outputs.append(attr)
    return node_outputs


def get_node_inputs(node_path):

    item = ix.get_item(node_path)

    obj_array = ix.api.OfItemArray(1)
    obj_array[0] = item
    item_inputs = ix.api.OfItemVector()
 
    node_inputs = []
    

    for i in range(item.get_attribute_count()):

        attr= item.get_attribute(i)

        if attr.get_texture():

            node_inputs.append(attr)

    return node_inputs


print get_node_inputs("project://material_node")
print get_node_outputs("project://texture_node")
