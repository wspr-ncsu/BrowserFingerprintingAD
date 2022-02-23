from pymongo import MongoClient
from pdgs_generation import *
from FPstatic import *
import psycopg2


double_checked_list = []   

# connect to Postgres
insert_con = psycopg2.connect(
    database="manual",
    user="jane_doe",
    password="never_gonna_give_you_up",
    host="localhost",
    port="5432",
)

with insert_con.cursor(name="custom_cursor") as cursor:
    cursor.itersize = 1000  # chunk size
    query = "SELECT * FROM locality_result;"
    cursor.execute(query)
    
    # Iterate every API sequence per execution context
    for script_name,content, sinkapis, features in cursor:      
        double_checked_flag = []
        apiList = []
        sinkList = []
        dataflow = []
        pdg_flag = False
        for feature in features:
            start,api = feature.split(",")
            if api not in double_checked_list:
                # print(api)
                # if api == "HTMLInputElement.defaultValue" or api == "HTMLInputElement.disabled" or api == "HTMLInputElement.files" or api == "HTMLInputElement.type" or api == "HTMLInputElement.value":
                    # print("QWE")
                pdg_flag = True
                break
                
        if pdg_flag:
            # remove file content
            open('/tmp/exp.js', 'w').close()
            # write content of current url js code
            with open("/tmp/exp.js", 'a') as jsfile:
                print(content, file=jsfile)

            pdg = get_data_flow('/tmp/exp.js', benchmarks=dict())
        
            # print("Number of Features: "+str(len(features)))
            # print("Features: "+str((features)))
            # For every feature we got from locality algorithm
            if pdg:
                sinkapis_set = list(set(sinkapis))
                for s in sinkapis_set:
                    # print(s)
                    s_start,s_api = s.split(",")
                    snk = s_api.split(".")[1]
                    search_API(pdg, int(s_start), content[int(s_start):int(s_start)+30], snk, sinkList)
                
                for feature in features:
                    double_checked_flag = []
                    apiList = []
                    dataflow = []
                    sttList = []
                    start,api = feature.split(",")
                    fea = api.split(".")[1]

                    # if api not in double_checked_list:
                    # if api == "HTMLInputElement.defaultValue" or api == "HTMLInputElement.disabled" or api == "HTMLInputElement.files" or api == "HTMLInputElement.type" or api == "HTMLInputElement.value":
                    #     print("------------------------------")
                    #     print(script_name)
                    #     print(feature)
                    #     print(set(features))
                    #     print(set(sinkapis))
                    #     print(content[int(start):int(start)+30])
                    #     print(content[int(start)-30:int(start)+30])
                    if api not in double_checked_list:
                        # We need to find their corresponding parent statement
                        # The parent statement is stored in apiList
                        search_API(pdg, int(start), content[int(start):int(start)+30], fea, apiList)                        
                        # If there is only one parent statement per one feature
                        # which is the correct case
                        if len(apiList) == 1:
                            # print(apiList[0].get_name())
                            # print(apiList[0].get_id())
                            # print(apiList[0].get_attributes())
                            prev_dataflow = len(set(dataflow))
                            # Find dataflows connect to the parent statement in apiList
                            # and store them in dataflow
                            search_dataflow(apiList, dataflow)
                            # print("1 st prev_dataflow "+str(prev_dataflow))
                            # print("len(dataflow)"+str(len(dataflow)))
                            # print("len(set(dataflow)) "+str(len(set(dataflow))))
                            # print(set(dataflow))
                            # for i in dataflow:
                            #     print(i.get_id())
                            
                            # iterate_node(pdg, sttList)
                            # print("len(set(sttList)): "+str(len(set(sttList))))
                            while prev_dataflow != len(set(dataflow)):
                                dataflowset = list(set(dataflow))
                                prev_dataflow = len(dataflowset)
                                # print("prev_dataflow "+str(prev_dataflow))
                                for i in dataflowset:
                                    apiList[0] = i
                                    search_dataflow(apiList, dataflow)
                                    # print("len(set(dataflow)) "+str(len(set(dataflow))))
                            # print("set(dataflow)): "+str(len(set(dataflow))))
                            dataflowset = list(set(dataflow))
                            # print("len(set(dataflowset)) "+str(len(set(dataflowset))))
                            # print(set(dataflowset))
                            # for i in dataflowset:
                            #     print(i.get_name())
                            #     iterate_node_name(i)
                            # print("len(sinkapis): " + str(len(sinkapis)))
                            # print("len(sinkList): " + str(len(sinkList)))
                            # print(sinkList)
                            
                            for i in sinkList:
                                # print(i.get_name())
                                # print(i.get_attributes())
                                # print(i)
                                # print(dataflowset)
                                if i in dataflowset:
                                    # print("HAHAHAHAHA")
                                    # print(i.get_name())
                                    # print(i.get_attributes())
                                    # iterate_node_name(i)
                                    double_checked_list.append(api)
                            
                            # for i in dataflowset:
                            #     iterate_stt(i,double_checked_flag)
                            #     # print(double_checked_flag)
                            # if True in double_checked_flag:
                            #     double_checked_list.append(api)
                        elif len(apiList) > 1:
                            # for i in apiList:
                            #     print("------------------------")
                            #     print(i.get_attributes())
                            #     print(i.get_name())
                            #     for j in i.get_children():
                            #         print(j.get_attributes())
                            #         for k in j.get_children():
                            #             print(k.get_attributes())
                            #             for z in k.get_children():
                            #                 print(z.get_attributes())
                            print(script_name)
                            print(feature)
                            print(set(features))
                            print(set(sinkapis))
                            print(content[int(start):int(start)+30])
                            print(content[int(start)-30:int(start)+30])
                            print("ERROR!!!!!!!!!!!!!!!!!")
                        else:
                            print(script_name)
                            print(feature)
                            print(set(features))
                            print(set(sinkapis))
                            print(content[int(start):int(start)+30])
                            print(content[int(start)-30:int(start)+30])
                            print("ERROR!!!!!!!!!!!!!!!!!ELSE")
        
        # print(len(double_checked_list))
        # print(len(set(double_checked_list)))
        # print("Features: "+str((features)))
        print("Double Checked list: "+str(set(double_checked_list)))
        