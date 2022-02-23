import json
import pandas as pd
from pdgs_generation import *
from pymongo import MongoClient
import psycopg2

# sinks = ['WebSocket', 'Storage', 'SQLTransaction', 'IDBTransaction', 'IDBObjectStore', 'IDBFactory', 'openDatabase', 'transaction', 'sessionStorage', 'sendBeacon', 'localStorage', 'port2', 'Database', 'port1', 'toDataURL', 'indexedDB', 'postMessage', 'IDBDatabase', 'responseText', 'send', 'fetch', 'XMLHttpRequest', 'MessageEvent', 'MessageChannel', 'createObjectStore', 'MessagePort', 'src']
Array_att = ["ArrayExpression", "ObjectExpression"]
If_att = ["ConditionalExpression", "LogicalExpression", "BinaryExperssion", "SwitchCase"]

array_API = []
if_API = []
df_API = []
sink_API = []
idList = []
idObjList = []
sink_flag = False

def iterate_node(node, sttList):
    
    if node is None:
        return node
    if node.is_leaf():
        return node
    else:
        for child in node.get_children():
            if child.is_statement():
                sttList.append(child)
            iterate_node(child, sttList)
         
def iterate_node_name(node):
    
    if node is None:
        return node
    if node.is_leaf():
        return node
    else:
        for child in node.get_children():
            if "name" in child.get_attributes():
                print(child.get_attributes()["name"])
            iterate_node_name(child)         
   
def iterate_node_st(node, dataflow):
    
    if node is None:
        return node
    if node.is_leaf():
        return node
    else:
        for child in node.get_children():
            if len(child.data_dep_parents) > 0 or len(child.data_dep_children) > 0:
                dataflow.append(child)

            iterate_node_st(child, dataflow)


def search_API_st(node, offset, api):
    if node is None:
        return node
    if node.is_leaf():
        return node
    else:
        for child in node.get_children():
            if child.data_dep_parents or child.data_dep_children:
                dataflow.append(child)

            search_API_st(child, offset, api)

def iterate_stt(node, flag):
    if node is None:
        return node
    if node.is_leaf():
        return node
    else:
        for child in node.get_children():
            if "name" in child.get_attributes():
                # print(child.get_attributes()["name"])
                for sink in sinks:
                    if sink.lower() == child.get_attributes()["name"].lower():
                        # print("SINK: "+str(child.get_attributes()["name"]))
                        flag.append(True)
                        return node

            iterate_stt(child, flag)


def get_dataflow_stt(node):
    psd_node = node
    while not psd_node.is_statement():
        # print("psd_node.get_name()"+str(psd_node.get_name()))
        # for i in psd_node.get_parent().get_children():
            # print("psd_node.get_parent().get_children()"+str(i.get_name()))
        psd_node = psd_node.get_parent()
    # print("STATEMENT: psd_node.get_name()"+str(psd_node.get_name()))
    # print("STATEMENT:"+str(psd_node.get_id()))
    return psd_node

def search_dataflow(apiList, dataflow):
    # Find every data flow dependency associated with
    # the parent statement
    # print("len(apiList[0].data_dep_parents)"+str(len(apiList[0].data_dep_parents)))
    # print("len(apiList[0].data_dep_children)"+str(len(apiList[0].data_dep_children)))
    for i in apiList[0].data_dep_parents:
        # print("get_dataflow_stt(i.get_id_begin()"+str(get_dataflow_stt(i.get_id_begin()).get_id()))
        # print("get_dataflow_stt(i.get_id_end())"+str(get_dataflow_stt(i.get_id_end()).get_id()))
        # print(apiList[0].get_id())
        # If the parent statements of two nodes on the data flow dependency 
        # are not the same parent statement of given feature, we consider 
        # the parent statements have data flow to the parent statement of
        # the given feature and add them to dataflow
        if get_dataflow_stt(i.get_id_begin()).get_id() != apiList[0].get_id():
            # print("PRENT CHECK IF")
            dataflow.append(get_dataflow_stt(i.get_id_begin()))
        elif get_dataflow_stt(i.get_id_end()).get_id() != apiList[0].get_id():
            # print("PRENT CHECK ELIF")
            dataflow.append(get_dataflow_stt(i.get_id_end()))
        # print("Data Dep parents: Begin(Name/ID):"+str(i.get_id_begin().get_name()) +"/"+str(i.get_id_begin().get_id())+ " End(Name/ID): " + str(i.get_id_end().get_name()) + "/" + str(i.get_id_end().get_id()))

    for i in apiList[0].data_dep_children:
        # print(i)
        if get_dataflow_stt(i.get_id_begin()).get_id() != apiList[0].get_id():
            # print("CHILD CHECK IF")
            dataflow.append(get_dataflow_stt(i.get_id_begin()))
        elif get_dataflow_stt(i.get_id_end()).get_id() != apiList[0].get_id():
            # print("CHILD CHECK ELIF")
            dataflow.append(get_dataflow_stt(i.get_id_end()))
        # print("Data Dep children: Begin(Name/ID):"+str(i.get_id_begin().get_name())+"/"+str(i.get_id_begin().get_id()) + " End(Name/ID): " + str(i.get_id_end().get_name()) + "/" + str(i.get_id_end().get_id()))

def search_API(node, offset, content_30, feature, api):
    range = []
    if node is None:
        return node
    if node.is_leaf():
        return node
    else:
        for child in node.get_children():
            # print(child.get_attributes()["range"])
            # print(child.get_attributes())
            # for key in child.get_attributes()["range"]:
            #     print(key)
            #     range.append(child.get_attributes()["range"][key])
            if isinstance(child.get_attributes()["range"], dict):
                for key in child.get_attributes()["range"]:
                    range.append(child.get_attributes()["range"][key])
                
                if range[0] <= offset and range[1] > offset:
                    # print("Range: "+str(child.get_attributes()["range"]))
                    # print("ATT: "+str(child.get_attributes()))
                        
                    if range[0] == offset and "name" in child.get_attributes():
                        # print("Range: "+str(range))
                        # print(str(child.get_attributes()))
                        # print("NAME: "+str(child.get_attributes()["name"]))
                        if child.get_attributes()["name"] == feature:
                            api.append(get_dataflow_stt(child))
                        
                    search_API(child, offset, content_30, feature, api)
                elif range[0] == offset + 1:
                    # print(child.get_attributes())
                    if "name" in child.get_attributes():
                        diff = len(child.get_attributes()["name"])
                        if child.get_attributes()["name"] == content_30[1:1+diff]:
                            # print("q")
                            # print(content_30[1:1+diff])
                            api.append(get_dataflow_stt(child))
                    else:
                        for i in child.get_children():
                            # print(i.get_attributes())
                            if "name" in i.get_attributes():
                                diff = len(i.get_attributes()["name"])
                                if i.get_attributes()["name"] == content_30[1:1+diff]:
                                    # print("w")
                                    # print(content_30[1:1+diff])
                                    api.append(get_dataflow_stt(i))
                        
            elif isinstance(child.get_attributes()["range"], list):
                if child.get_attributes()["range"][0] <= offset and child.get_attributes()["range"][1] > offset:
                    # print("Range: "+str(child.get_attributes()["range"]))
                    # print("ATT: "+str(child.get_attributes()))
                    
                    # for j in child.get_children():
                    #     print(j.get_attributes())
                            
                    if child.get_attributes()["range"][0] == offset and "name" in child.get_attributes():
                        # print("Range: "+str(child.get_attributes()["range"]))
                        # print("NAME: "+str(child.get_attributes()["name"]))
                        if child.get_attributes()["name"] == feature:
                            api.append(get_dataflow_stt(child))
                    
                    search_API(child, offset, content_30, feature, api)
                elif child.get_attributes()["range"][0] == offset + 1:
                    # print("OBFUSCATION")
                    if "name" in child.get_attributes():
                        diff = len(child.get_attributes()["name"])
                        if child.get_attributes()["name"] == content_30[1:1+diff]:
                            # print("e")
                            # print(content_30[1:1+diff])
                            api.append(get_dataflow_stt(child))
                    elif "value" in child.get_attributes() or "raw" in child.get_attributes():
                        # print("IWANT")
                        if "value" in child.get_attributes() and isinstance(child.get_attributes()["value"], str):
                            # print("kankan")
                            diff = len(child.get_attributes()["value"])
                            if child.get_attributes()["value"] == content_30[1:1+diff]:
                                api.append(get_dataflow_stt(child))
                        if "raw" in child.get_attributes() and isinstance(child.get_attributes()["raw"], str):
                            # print("kan")
                            diff = len(child.get_attributes()["raw"])
                            if child.get_attributes()["raw"] == content_30[1:1+diff] and get_dataflow_stt(child) not in api:
                                api.append(get_dataflow_stt(child))
                    else:
                        for i in child.get_children():
                            # print(i.get_attributes())
                            if "name" in i.get_attributes():
                                diff = len(i.get_attributes()["name"])
                                if i.get_attributes()["name"] == content_30[1:1+diff]:
                                    # print("r")
                                    # print(content_30[1:1+diff])
                                    api.append(get_dataflow_stt(i))
                            elif "value" in i.get_attributes() or "raw" in i.get_attributes():
                                # print("IWANT")
                                if "value" in i.get_attributes() and isinstance(i.get_attributes()["value"], str):
                                    # print("kankan")
                                    diff = len(i.get_attributes()["value"])
                                    if i.get_attributes()["value"] == content_30[1:1+diff]:
                                        
                                        api.append(get_dataflow_stt(i))
                                if "raw" in i.get_attributes() and isinstance(i.get_attributes()["raw"], str):
                                    # print("kan")
                                    diff = len(i.get_attributes()["raw"])
                                    if i.get_attributes()["raw"] == content_30[1:1+diff] and get_dataflow_stt(i) not in api:
                                        
                                        api.append(get_dataflow_stt(i))
        
            else:
                print("ERROR!!!!!!")

def has_dataflow(node):
    if len(node.data_dep_parents) == 0:
        print("NO data flow parents")
    for i in node.data_dep_parents:
        print("Data Dep parents: Begin(Name/ID):"+str(i.get_id_begin().get_name()) +"/"+str(i.get_id_begin().get_id())+ " End(Name/ID): " + str(i.get_id_end().get_name()) + "/" + str(i.get_id_end().get_id()))
    if len(node.data_dep_children) == 0:
        print("NO data flow children")
    for i in node.data_dep_children:
        print("Data Dep children: Begin(Name/ID):"+str(i.get_id_begin().get_name())+"/"+str(i.get_id_begin().get_id()) + " End(Name/ID): " + str(i.get_id_end().get_name()) + "/" + str(i.get_id_end().get_id()))

def conn_feature_pdg(features, dataflow, apiList):
    for i in features:
        counter = 0
        offset,feature = i.split(",")
        feature_len = len(feature)-feature.index(".")
        start = int(offset)
        end = int(offset)+feature_len-1
        print(start)
        for j in dataflow:
            print("j: "+str(j.get_attributes()))
            api_node = []
            search_API(j, start, api_node)
            if api_node:
                apiList.append(j)
                break

def has_dataflow_nb(node, api_node):
    if node.get_parent():
        for child in node.get_parent().get_children():
            api_node.append({child.get_id():child.get_value()})
            # print_node(child)
            # print("Name: "+str(child.get_name()))
            # print("Attributes: "+str(child.get_attributes()))
            # if len(child.data_dep_parents) == 0:
            #     print("NO data flow parents")
            # for i in child.data_dep_parents:
            #     print("Data Dep parents: Begin(Name/ID):"+str(i.get_id_begin().get_name()) +"/"+str(i.get_id_begin().get_id())+ " End(Name/ID): " + str(i.get_id_end().get_name()) + "/" + str(i.get_id_end().get_id()))
            # if len(child.data_dep_children) == 0:
            #     print("NO data flow children")
            # for i in child.data_dep_children:
            #     print("Data Dep children: Begin(Name/ID):"+str(i.get_id_begin().get_name())+"/"+str(i.get_id_begin().get_id()) + " End(Name/ID): " + str(i.get_id_end().get_name()) + "/" + str(i.get_id_end().get_id()))


def iterate_dfnode(node, ids, idmap):
    if node is None:
        return node
    if node.is_leaf():
        return node
    else:
        for child in node.get_children():
            searchDF(child,ids,idmap)
            iterate_dfnode(child, ids, idmap)

def iterate_sink_node(node):
    global sink_flag

    if node is None:
        return node
    if node.is_leaf():
        return node
    else:
        for child in node.get_children():
            for i in sinks:
                if str(getAttName(child)).lower() in i.lower():
                    sink_flag = True
            iterate_sink_node(child)

def print_node(node):
    children_detail = []

    print("Name: "+str(node.get_name()))
    print("ID: "+str(node.get_id()))
    print("Attributes: "+str(node.get_attributes()))
    print("GET_Attributes: "+str(getAttName(node)))
    for i in node.data_dep_parents:
        print("Data Dep parents: Begin(Name/ID):"+str(i.get_id_begin().get_name()) +"/"+str(i.get_id_begin().get_id())+ " End(Name/ID): " + str(i.get_id_end().get_name()) + "/" + str(i.get_id_end().get_id()))
    for i in node.data_dep_children:
        print("Data Dep children: Begin(Name/ID):"+str(i.get_id_begin().get_name())+"/"+str(i.get_id_begin().get_id()) + " End(Name/ID): " + str(i.get_id_end().get_name()) + "/" + str(i.get_id_end().get_id()))
    print("Body: "+str(node.get_body()))
    print("Body list: "+str(node.get_body_list()))
    print("Parent: "+str(node.get_parent()))
    print("Parent detail: "+str(node.get_parent().get_name()))
    print("Children: "+str(node.get_children()))
    for i in node.get_children():
        children_detail.append(i.get_name())
    print("Children detail: "+str(children_detail))
    print("Literal: "+str(node.literal_type()))
    print("Data Depend: "+str(node.get_data_dependencies()))
    print("Control Depend: "+str(node.get_control_dependencies()))
    print("Statement Depend: "+str(node.get_statement_dependencies()))
    print("-----------------------------------------------------------")

def getAttName(node):
    attr = node.get_attributes()
    for i in attr:
        if i == 'name' and len(attr['name']) > 2:
            return attr['name']

def getSiblings(node):
    result = []
    if node.get_parent().get_parent():
        # parent's siblings
        for par in node.get_parent().get_parent().get_children():
            if par.get_name() == "Identifier" and len(par.get_name()) > 2:
                result.append(getAttName(par))
            # node's siblings
            for sib in par.get_children():
                if sib.get_name() == "Identifier" and len(par.get_name()) > 2:
                    result.append(getAttName(sib))
    elif node.get_parent():
        for sib in node.get_parent().get_children():
            if sib.get_name() == "Identifier" and len(sib.get_name()) > 2:
                result.append(getAttName(sib))
    return result
    

def searchArray(node):
    global Array_att, attributes, array_API

    for i in attributes:
        # mark source in tree
        if str(getAttName(node)).lower() in i.lower():
            # if the source is in an array or object array
            for att in Array_att:
                if node.get_parent().get_name() == str(att) or node.get_parent().get_parent().get_name() == str(att):
                    array_API += getSiblings(node)
                    return 
            


def searchIf(node):
    global If_att, attributes, if_API
    
    for i in attributes:
        # mark source in tree
        if str(getAttName(node)).lower() in i.lower():
            # if the source is in an array or object array
            for att in If_att:
                if node.get_parent().get_name() == str(att) or node.get_parent().get_parent().get_name() == str(att):
                    if_API += getSiblings(node)
                    return 
            
def searchSink(node):
    global sinks, sink_API
    for i in sinks:
        # mark sink in tree
        if str(getAttName(node)).lower() in i.lower():
            sink_API += getSiblings(node)
            return 


def searchDF(node, ids, idmap):
    global attributes, sinks, df_API

    for i in attributes:
        # mark source in tree
        if str(getAttName(node)).lower() in i.lower():
            # given node has data flow dependency
            if node.get_id() in ids:
                for dep in idmap:
                    if node.get_id() == dep.get_id_begin().get_id():
                        df_API += getSiblings(dep.get_id_end())
                    elif node.get_id() == dep.get_id_end().get_id():
                        df_API += getSiblings(dep.get_id_begin())
                return 


def remove_known(apis):
    # print("Before remove: "+str(len(apis)))
    for i in list(apis):
        if i is None:
            apis.remove(i)
        else:
            for j in attributes:
                if i.lower() == j.lower():
                    apis.remove(i)
                    break
    # print("After remove: "+str(len(apis)))
    return list(apis)

def main():
    global idList,idObjList, if_API, array_API, df_API, sink_flag, sink_API

    # connect to MongoDB
    client = MongoClient()
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client["intermedia1"]
    collection = db["codeset1"]

    for i in collection.find():
        actual_code = str(i["code"])
        print(i["code"])
        # remove file content
        open('/tmp/exp.js', 'w').close()
        # write content of current url js code
        with open("/tmp/exp.js", 'a') as jsfile:
            print(actual_code, file=jsfile)

        pdg = get_data_flow('/tmp/exp.js', benchmarks=dict())
        iterate_node(pdg)
        print("Finished")
        break


    # with open('/tmp/source_code.json') as f:
    #     data = json.load(f)
    
    # counter = 0
    # for i in data:
    #     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #     print(str(counter)+str(counter)+str(counter)+str(counter)+str(counter)+str(counter)+str(counter)+str(counter)+str(counter))
    #     if_API = []
    #     array_API = []
    #     df_API = []
    #     sink_API = []

    #     idList = []
    #     idObjList = []

    #     sink_flag = False

    #     ori = i['origin'][1:-1]
    #     js = i['code']
    #     # remove content of file from previous urls
    #     open('/tmp/exp.js', 'w').close()
    #     # write content of current url js code
    #     with open("/tmp/exp.js", 'a') as jsfile:
    #         print(js, file=jsfile)

    #     print("Source File Name: "+str((ori)))
    #     # print("Source File: "+str((js)))

    #     pdg = get_data_flow('/tmp/exp.js', benchmarks=dict())

    #     iterate_sink_node(pdg)
    #     # if there is a sink in program
    #     if sink_flag:
    #         print("Check sink flag")
    #         iterate_node(pdg)
            
    #         # print("idList #: "+str(len(idList)))
    #         # print("idObjList #: "+str(len(idObjList)))
    #         iterate_dfnode(pdg, idList, idObjList)

            
    #         print("IF APIs: "+str(remove_known(set(if_API))))
    #         print("ARRAY APIs: "+str(remove_known(set(array_API))))
    #         print("DF APIs: "+str(remove_known(set(df_API))))
    #         print("Sink APIs: "+str(remove_known(set(sink_API))))

    #         counter += 1
    #         # break

if __name__ == "__main__":
    main()