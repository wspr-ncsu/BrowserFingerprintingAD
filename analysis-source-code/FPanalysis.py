from pymongo import MongoClient

import sys
import local_cal
import psycopg2
import csv
import json
from script import Script
from sklearn.cluster import DBSCAN
from pdgs_generation import *
from FPstatic import *

# attributes from major papers in browser FP(https://docs.google.com/spreadsheets/d/1jH24h0DJUUTw-s6gOzIk_SPE93BswMfJg5uXUZJvacs/edit#gid=0)
attributes = [
    "Navigator.languages",
    "Window.sessionStorage",
    "Window.localStorage",
    "Navigator.appName",
    "Element.getBoundingClientRect",
    "Navigator.mimeTypes",
    "Navigator.doNotTrack",
    "HTMLElement.offsetHeight",
    "Screen.availHeight",
    "Screen.availWidth",
    "Screen.height",
    "Navigator.product",
    "Navigator.productSub",
    "Screen.pixelDepth",
    "Navigator.vendorSub",
    "Screen.colorDepth",
    "Navigator.appCodeName",
    "Navigator.vendor",
    "Screen.availLeft",
    "Screen.width",
    "Screen.availTop",
    "Navigator.appVersion",
    "Navigator.userAgent",
    "Navigator.javaEnabled",
    "Navigator.platform",
    "Navigator.language",
    "Navigator.cookieEnabled",
    "HTMLElement.offsetWidth",
    "Navigator.plugins",
]

new_attributes = [
    "Navigator.languages",
    "Navigator.appName",
    "Navigator.mimeTypes",
    "Navigator.doNotTrack",
    "Navigator.hardwareConcurrency",
    "Navigator.getBattery",
    "Navigator.javaEnabled",
    "Navigator.platform",
    "Navigator.language",
    "Navigator.cookieEnabled",
    "Navigator.plugins",
    "Navigator.productSub",
    "Navigator.vendorSub",
    "Navigator.appCodeName",
    "Navigator.vendor",
    "CanvasRenderingContext2D.fillText",
    "CanvasRenderingContext2D.arc",
    "CanvasRenderingContext2D.fill",
    "WebGLRenderingContext.canvas",
    "WebGL2RenderingContext.canvas",
    "WebGL2RenderingContext.getParameter",
    "WebGL2RenderingContext.getExtension",
    "OfflineAudioContext.createOscillator",
    "OfflineAudioContext.createDynamicsCompressor",
    "DynamicsCompressorNode.connect",
    "OscillatorNode.frequency",
    "AudioParam.setValueAtTime",
    "Screen.height",
    "Screen.pixelDepth",
    "Screen.colorDepth",
    "Screen.width",
    "Screen.orientation",
    "Geolocation.getCurrentPosition",
    "Geolocation.watchPosition",
    "Window.devicePixelRatio",
]

sinks = ['Window.sessionStorage', 'MessagePort.postMessage', 'WebSocket.send', 'ServiceWorker.postMessage', 'Window.localStorage', 'Window.openDatabase', 'XMLHttpRequest.send', 'IDBObjectStore.put', 'RTCDataChannel.send', 'Client.postMessage', 'Window.postMessage', 'Window.indexedDB', 'Navigator.sendBeacon', 'DedicatedWorkerGlobalScope.postMessage', 'IDBObjectStore.add', 'Worker.postMessage', 'Document.cookie']


Block_list = [
    "HTML",
    "DOM",
    "Document",
    "Tree",
    "Range",
    "NamedNodeMap."
]

# attributes for new added APIs
# Buffer_attrs = ['CanvasRenderingContext2D.rotate', 'HTMLAnchorElement.relList', 'Performance.timing', 'Permissions.query', 'Window.getComputedStyle', 'Navigator.permissions', 'BatteryManager.charging', 'History.pushState', 'Navigator.maxTouchPoints', 'ServiceWorkerContainer.register', 'WebGLLoseContext.loseContext', 'Window.orientation', 'HTMLCanvasElement.height', 'TextMetrics.width', 'Window.setTimeout', 'PerformanceTiming.navigationStart', 'MediaQueryList.addListener', 'IDBRequest.result', 'HTMLInputElement.value', 'CanvasRenderingContext2D.clearRect', 'Window.matchMedia', 'Headers.append', 'HTMLAnchorElement.search', 'Crypto.subtle', 'PluginArray.length', 'Navigator.connection', 'CanvasRenderingContext2D.measureText', 'Window.document', 'CanvasRenderingContext2D.createImageData', 'Window.location', 'BatteryManager.dischargingTime', 'BatteryManager.level', 'DOMRect.height', 'Window.webkitRequestFileSystem', 'IDBFactory.open', 'CSSStyleSheet.insertRule', 'CustomElementRegistry.define', 'Event.timeStamp', 'Window.screen', 'Performance.mark', 'URLSearchParams.get', 'Location.protocol', 'Window.requestIdleCallback', 'Location.port', 'UnderlyingSourceBase.start', 'URL.searchParams', 'Response.json', 'CanvasRenderingContext2D.save', 'IntersectionObserverEntry.isIntersecting', 'Window.devicePixelRatio', 'Location.hostname', 'WebGL2RenderingContext.createShader', 'HTMLStyleElement.sheet', 'Window.outerHeight', 'HTMLAnchorElement.href', 'Window.self', 'HTMLAnchorElement.hash', 'HTMLAnchorElement.protocol', 'HTMLIFrameElement.name', 'HTMLCanvasElement.width', 'Window.window', 'HTMLAnchorElement.hostname', 'Location.host', 'WebGL2RenderingContext.bufferData', 'CSSRuleList.length', 'WebGL2RenderingContext.createProgram', 'IntersectionObserver.unobserve', 'Storage.key', 'Window.clearTimeout', 'MediaStream.removeTrack', 'Location.toString', 'Window.onpagehide', 'Navigator.serviceWorker', 'MutationObserver.disconnect', 'PermissionStatus.state', 'Window.atob', 'CanvasRenderingContext2D.beginPath', 'HTMLInputElement.type', 'IDBTransaction.objectStore', 'IntersectionObserverEntry.target', 'CanvasRenderingContext2D.moveTo', 'HTMLLinkElement.href', 'HTMLElement.dataset', 'UnderlyingSourceBase.cancel', 'Storage.length', 'Performance.measure', 'Storage.getItem', 'CSSStyleDeclaration.setProperty', 'SQLTransaction.executeSql', 'UnderlyingSourceBase.pull', 'MutationRecord.type', 'Location.ancestorOrigins', 'Window.scrollY', 'Window.performance', 'Element.matches', 'CanvasRenderingContext2D.quadraticCurveTo', 'HTMLCollection.length', 'Window.event', 'Event.currentTarget', 'Location.origin', 'DOMTokenList.remove', 'URL.search', 'Window.parent', 'Response.ok', 'Response.status', 'Window.frames', 'Navigator.geolocation', 'Window.clearInterval', 'Window.btoa', 'NodeList.length', 'URLSearchParams.getAll', 'Window.customElements', 'PerformanceTiming.domComplete', 'NetworkInformation.downlink', 'Geolocation.watchPosition', 'MediaQueryList.matches', 'Navigator.getUserMedia', 'DOMTokenList.add', 'Window.setInterval', 'HTMLCanvasElement.getContext', 'Window.WebKitCSSMatrix', 'Location.search', 'Storage.removeItem', 'IDBObjectStore.put', 'TextMetrics.fontBoundingBoxAscent', 'CustomElementRegistry.get', 'Iterator.next', 'BatteryManager.chargingTime', 'Navigator.share', 'Window.innerWidth', 'Window.history', 'PerformanceTiming.connectStart', 'Location.href', 'Window.top', 'Location.pathname', 'Crypto.getRandomValues', 'FormData.append', 'Window.crypto', 'WebGL2RenderingContext.createBuffer', 'CanvasRenderingContext2D.bezierCurveTo', 'URL.pathname', 'DOMRect.width', 'WebGL2RenderingContext.bindBuffer', 'Window.cancelAnimationFrame', 'HTMLInputElement.form', 'CanvasRenderingContext2D.stroke', 'Window.requestAnimationFrame', 'Window.webkitMediaStream', 'Performance.now', 'IntersectionObserver.observe', 'MimeTypeArray.length', 'MutationRecord.target', 'HTMLAnchorElement.port', 'WebGLRenderingContext.getParameter', 'WebSocket.readyState', 'HTMLImageElement.complete', 'Performance.clearMarks', 'Document.evaluate', 'History.length', 'DOMTokenList.contains', 'HTMLAnchorElement.host', 'Storage.setItem', 'Window.pageXOffset', 'IntersectionObserverEntry.intersectionRatio', 'Window.innerHeight', 'CanvasRenderingContext2D.lineTo', 'MutationObserver.observe', 'Window.opener', 'HTMLAnchorElement.pathname', 'CanvasRenderingContext2D.restore', 'Window.pageYOffset', 'Window.navigator', 'HTMLIFrameElement.contentWindow', 'URL.origin', 'CSSStyleSheet.cssRules', 'Location.hash', 'HTMLMetaElement.name', 'CSSStyleDeclaration.getPropertyValue', 'DOMTokenList.supports', 'CSSStyleDeclaration.cssText', 'CanvasRenderingContext2D.fillRect', 'Navigator.onLine']
# Buffer_attrs = ['URLSearchParams.get', 'Response.json', 'Response.status', 'Location.href', 'BatteryManager.dischargingTime', 'Location.protocol', 'WebGL2RenderingContext.createBuffer', 'Window.setTimeout', 'CanvasRenderingContext2D.measureText', 'BatteryManager.chargingTime', 'URL.searchParams', 'DOMTokenList.remove', 'TextMetrics.fontBoundingBoxAscent', 'Event.timeStamp', 'Window.top', 'Storage.removeItem', 'WebGL2RenderingContext.bindBuffer', 'MimeTypeArray.length', 'Navigator.serviceWorker', 'Location.hash', 'WebGLLoseContext.loseContext', 'WebGL2RenderingContext.createProgram', 'Window.screen', 'Geolocation.watchPosition', 'URL.search', 'Location.search', 'Storage.getItem', 'BatteryManager.level', 'Window.atob', 'Navigator.permissions', 'Window.btoa', 'DOMTokenList.supports', 'PluginArray.length', 'Navigator.maxTouchPoints', 'Window.innerWidth', 'CanvasRenderingContext2D.lineTo', 'HTMLStyleElement.sheet', 'ServiceWorkerContainer.register', 'CanvasRenderingContext2D.beginPath', 'CanvasRenderingContext2D.fillRect', 'Location.toString', 'HTMLAnchorElement.relList', 'Storage.setItem', 'Crypto.getRandomValues', 'Window.document', 'Iterator.next', 'DOMTokenList.add', 'CanvasRenderingContext2D.stroke', 'HTMLMetaElement.name', 'Response.ok', 'WebGL2RenderingContext.bufferData', 'Navigator.geolocation', 'CanvasRenderingContext2D.quadraticCurveTo', 'SQLTransaction.executeSql', 'Event.currentTarget', 'BatteryManager.charging', 'Window.innerHeight', 'Window.WebKitCSSMatrix', 'HTMLAnchorElement.pathname', 'Window.devicePixelRatio', 'TextMetrics.width', 'CanvasRenderingContext2D.moveTo', 'CSSRuleList.length', 'Performance.now', 'URL.pathname', 'Window.location', 'Location.pathname', 'Window.navigator', 'CanvasRenderingContext2D.bezierCurveTo', 'CanvasRenderingContext2D.rotate', 'NetworkInformation.downlink', 'HTMLAnchorElement.hostname', 'Navigator.connection', 'WebGL2RenderingContext.createShader', 'MutationObserver.disconnect', 'MutationRecord.target', 'HTMLAnchorElement.port', 'CSSStyleDeclaration.setProperty', 'URLSearchParams.getAll', 'MutationObserver.observe', 'CSSStyleSheet.insertRule', 'CSSStyleSheet.cssRules', 'Location.host', 'Window.outerHeight', 'Location.origin', 'MutationRecord.type', 'Location.hostname', 'NodeList.length', 'HTMLAnchorElement.href', 'Window.self', 'HTMLCanvasElement.getContext', 'Navigator.onLine', 'Window.clearTimeout']
# Buffer_attrs = []
# attributes for new added non-standard APIs
non_std = []

# Vendor prefix
vendor_prefix = ["webkit", "moz", "ms", "o"]

# frequency table
frq_table = dict()

all_api = 0

        
def api_printer(ori, ori_name):
    f = open("manual.txt", "w")
    if str(ori["origin"]) == str(ori_name):
        f.write(str(ori["origin"]) + "_____" + str(ori_name))
        for feature in ori["features"]:
            f.write(str(feature) + "\n")
    f.close()


def search(api):
    # connect to MongoDB
    client = MongoClient()
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client["test_db"]
    collection = db["rawAPIs"]

    # websites in database
    for website in collection.find():
        # origins in websites
        for origin in website["origins"]:
            api_list = []
            # js features in origins
            for feature in origin["apis"]:
                # if str(api).lower() in str(feature).lower():
                #     print(str(feature))
                api_list.append(feature)
            if len(api_list) != len(set(api_list)):
                print("qwe")


# determine whether the input origin is doing fingerprinting
# based on suspicious FP APIs
def isFP_seed(ori_list):
    for feature in ori_list:
        if (str(feature) in new_attributes):
            return True
    return False

def isFP_sink(ori_list):
    for feature in ori_list:
        if (str(feature) in sinks):
            return True
    return False

def get_sink(api_tuple):
    sink_list = []
    for feature in api_tuple:
        api = feature[0].split(",")[1]
        if api in sinks:
            sink_list.append(feature[0])
    return sink_list
            
    
def pre_proc(apis):
    real_apis = []
    only_apis = []
    
    for i in apis:
        idx = i.index(",")+1
        api = i[idx:]
        only_apis.append(api)
        real_apis.append(i[1:])
    
    return only_apis,real_apis

def FPstatic():
    # connect to MongoDB
    client = MongoClient()
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client["intermedia1"]
    collection = db["codeset1"]

    error_count = 0

    for i in collection.find():
        actual_code = str(i["code"])
        # remove file content
        open('/tmp/exp.js', 'w').close()
        # write content of current url js code
        with open("/tmp/exp.js", 'a') as jsfile:
            print(actual_code, file=jsfile)

        pdg = get_data_flow('/tmp/exp.js', benchmarks=dict())
        iterate_node(pdg)
        # if pdg:
        #     if "ERROR" in pdg.stdout.decode():
        #         print("validation failed")
        #     else:
        #         iterate_node(pdg)
        # print(collection[key])
        # print(collection.find()[key])
        # break


def FPLocal(filter):

    apis = []
    count = 0
    fp_api = []
    global all_api
    non_std_table = dict()
    flag_script = False
    std_api = FPIdldata()
    total_api = []
    tmp_api = []
    sink_api = []
    Buffer_attrs = []

    print(len(sinks))
    # connect to MongoDB
    # client = MongoClient()
    # client = MongoClient("mongodb://127.0.0.1:27017")
    # db = client["intermedia1"]
    # collection = db["codeset1"]

    try:
        # connect to Postgres
        con = psycopg2.connect(
            database="experiment2",
            user="jane_doe",
            password="never_gonna_give_you_up",
            host="localhost",
            port="5432",
        )
        # connect to Postgres
        insert_con = psycopg2.connect(
            database="manual",
            user="jane_doe",
            password="never_gonna_give_you_up",
            host="localhost",
            port="5432",
        )
        
        insert_cursor = insert_con.cursor()
        with con.cursor(name="custom_cursor") as cursor:
            cursor.itersize = 1000  # chunk size
            query = "SELECT * FROM script;"
            cursor.execute(query)
            # Iterate every API sequence per execution context
            for script_name,script_id,ori_name,dom_name,content,features in cursor:                
                # print("features: "+str(features))
                only_apis,real_apis = pre_proc(features)

                api_uni = list(set(only_apis))
                # If given API sequence has at least one 
                # fingerprinting related API
                if isFP_seed(api_uni) and isFP_sink(api_uni):
                    for api in real_apis:
                        element = api[api.index(",")+1:]
                        if (
                            (element in new_attributes) or (element in Buffer_attrs)
                        ):
                            apis.append([api, 1, 1])
                        else:
                            apis.append([api, 0, 0])

                    local_cal.sum_ones(apis)
                    
                    local_cal.cal_local(apis)
                    
                    sink_api = get_sink(apis)
                    # print(sink_api)
                    
                    # First filter is based on API's weight
                    # Second filter is based on WebIDL
                    # exp = len(only_apis) ** (1.0 / 3.0)
                    if len(sink_api) > 0:
                        for i in apis:
                            if i[1] > 0 and i[2] == 2 and i[0][i[0].index(",")+1:] in std_api and i[0][i[0].index(",")+1:] not in sinks:
                                total_api.append(i[0])
                                tmp_api.append(i[0])
                                    # print(i[0])
                                # if "HTMLMetaElement.content" in i[0] or "HTMLMetaElement.name" in i[0] or "Node.appendChild" in i[0] or "NodeList.item" in i[0] or "NodeList.length" in i[0]:
                                #     print("--------------------------------")
                                #     print(i)
                                #     print(dom_name)
                                #     print(script_name)
                                #     print(content[:200])
                                #     print(set(tmp_api))
                                #     print(set(sink_api))
                                #     print(apis)  
                                                        

                        # if len(tmp_api) > 0:
                        #     print("--------------------------------")
                        #     print(script_name)
                        #     print(content[:200])
                        #     print(set(sink_api)) 
                        #     print(set(tmp_api))
                        #     insert_cursor.execute("INSERT INTO locality_result(script_name, code, sink, APIs) VALUES (%s, %s, %s, %s)",(script_name,content,sink_api,tmp_api))
                        #     insert_con.commit()
                    # print(msg)
                    # print(apis)
                    # print("TOTAL: "+str(total_api))    
                    sink_api.clear()      
                    apis.clear()
                    tmp_api.clear()
            
                # break
        
        
        # print("Unknonw data: "+str(un_data))    
        # print("Unknonw: "+str(unknown)+" correct: "+str(correct)+" wrong: "+str(wrong))
        # accuracy = correct*1.0 / (total - unknown)
        # accuracy = 0

        # print("Number of unique standard suspicious FP API: " + str(len(api_block)))
        # # print("List of unique standard suspicious FP API: " + str(api_block))
        print("Number of standard suspicious unique Buffer FP API: " + str(len(set(Buffer_attrs))))
        print("List of standard suspicious Buffer FP API: " + str(set(Buffer_attrs)))
        # print("Number of new non-standard suspicious FP API: " + str(len(non_std_uni_new)))
        # # print("List of new non-standard suspicious FP API: " + str(non_std_uni_new))
        # print("Number of all non-standard suspicious unique FP API: " + str(len(set(non_std))))
        # print("Number of all non-standard suspicious FP API: " + str(len(non_std)))
        # # print("List of all non-standard suspicious FP API: " + str(set(non_std)))
        # print("Accuracy of Number of unique standard suspicious FP API:" + str(round(accuracy, 2)))
        # # print frequency table in order
        # # print(sorted(frq_table.items(), key=lambda x: x[1], reverse=True))
        # t_api = list(set(total_api))
        print("Number of standard suspicious total unique Buffer FP API: " + str(len(total_api)))
        print("List of standard suspicious total Buffer FP API: " + str(total_api))
        print("Count: "+str(count))
        buff = []
        for i in total_api:
            buff.append(i[i.index(",")+1:])
        Buffer_attrs += list(set(buff))
        total_api.clear()
        print("Number of standard suspicious unique Buffer FP API: " + str(len(set(Buffer_attrs))))
        print("List of standard suspicious Buffer FP API: " + str(set(Buffer_attrs)))
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        insert_cursor.close()
        insert_con.close()


def FPLocalItr(times):
    for i in range(int(times)):
        FPLocal(1/3)
        # FPLocal(20,0)
    # FPLocal(15,0)
    # FPLocal(20,0)


def FPIdldata():
    std_api = []
    with open("idldata.json") as f:
        data = json.load(f)

    for i in data:
        if data[str(i)] is not None:
            if "members" in data[str(i)]:
                for ele in data[str(i)]["members"]:
                    std_api.append(str(i) + "." + str(ele))
            else:
                for ele in data[str(i)].values():
                    std_api.append(str(i) + "." + str(ele))
    # print(len(set(std_api)))
    # print(len((std_api)))
    # print((set(std_api)))
    return std_api

def FPmongo():
    # connect to MongoDB
    client = MongoClient()
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client["oracle"]
    apis = db["apis"]

    # Transfer oracle from Mongodb to here
    oracle = dict()
    for i in apis.find():
        oracle[i["name"]] = i["fp"]

    return oracle

def FPfreq():

    # connect to MongoDB
    client = MongoClient()
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client["experiment2"]
    collection = db["js_api_features"]

    freq = dict()
    fp_table = dict()
    x = collection.find()
    ori = []
    count = []
    total = []
    name = []
    top100 = 0
    t100_1000 = 0
    t1k_5k = 0
    t5k_10k = 0
    error = 0
    webs,alexa = Alexa()
    for i in x:
        # print(i)
        # fp_table[str(i["name"])] = 0
        if i["featureOrigins"]:
            # print(i["featureOrigins"][0]["origin"])
            ori.append(i["featureOrigins"][0]["origin"])
        # else:
        #     print(i)
        # ori.append(i["featureOrigins"][0]["origin"])
    print(len(ori))
    # return
    try:
        # connect to Postgres
        con = psycopg2.connect(
            database="experiment",
            user="jane_doe",
            password="never_gonna_give_you_up",
            host="localhost",
            port="5432",
        )

        with con.cursor(name="custom_cursor") as cursor:
            cursor.itersize = 10000  # chunk size
            query = "SELECT * FROM origin;"
            cursor.execute(query)

            for key, value in cursor:
                api_uni = list(set(value))
                total.append(key)
                for i in api_uni:
                    if "DeprecatedStorageQuota" in i:
                        print(key)
                    if isFP(api_uni):
                        count.append(key)
                    # for i in fp_table:
                    #     if i in api_uni:
                    #         fp_table[i] += 1
                            # if i == "Window.onpointerout":
                            #     print(key)
                        
        for i in ori:
            buffer = i[8:]
            if buffer[0:3] == "www":
                name.append(buffer[4:])
                # print(buffer[4:])
            else:
                name.append(buffer)

        # print(name)

        # for i in name:
        #     try:
        #         if int(alexa[i]) <= 100:
        #             # print(i,alexa[i])
        #             top100 += 1
        #         elif int(alexa[i]) <= 1000:
        #             t100_1000 += 1
        #         elif int(alexa[i]) <= 5000:
        #             t1k_5k += 1
        #         elif int(alexa[i]) <= 10000:
        #             t5k_10k += 1
        #         else:
        #             error += 1
        #     except KeyError:
        #         count += 1
        # print(sorted(fp_table.items(), key=lambda x: x[1], reverse=True))
        
        # print("Number of FP websites: "+str(len(set(count))))
        # print(set(count))
        # print("Total Number of FP origins: "+str(len((total))))
        # print("Total Number of uni FP origins: "+str(len(set(total))))
        # print(set(total))
        print("Intersction: "+str(len(list(set(name) & set(webs)))))
        # print("Intersction: "+str((list(set(name) - set(webs)))))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def Alexa():
    alexa = dict()
    websites = []
    easylist = open('top-1m.csv')
    with easylist as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            alexa[row[1]] = row[0]
            websites.append(row[1])
    return websites,alexa


def FPratio():

    ratio = dict()
    std = []
    extra = add_attrs + WebGL_attrs + WebGL2_attrs + Canvas_attrs + Geo_attrs + RTC_attrs + Speech_attrs + Audio_attrs + Network_attrs + Screen_attrs + Battery_attrs
    

    test = []

    print("Length of APIs: "+str(len(std)))
    total = 0
    count = 0
    fp_origin = []
    for element in std:
        ratio[element] = [0,0,0.0]

    try:
        # connect to Postgres
        con = psycopg2.connect(
            database="experiment2",
            user="jane_doe",
            password="never_gonna_give_you_up",
            host="localhost",
            port="5432",
        )

        with con.cursor(name="custom_cursor") as cursor:
            cursor.itersize = 10000  # chunk size
            query = "SELECT * FROM origin;"
            cursor.execute(query)

            for key, value in cursor:
                api_uni = list(set(value))
                flag = isFP(api_uni)
                total += 1
                for i in std:
                    if i in api_uni:
                        if flag:
                            count += 1
                            ratio[i][0] += 1
                            fp_origin.append(key)
                        else:
                            ratio[i][1] += 1
        
        for i in ratio:
            print(i)
            if ratio[i][1] != 0:
                ratio[i][2] = round(float(ratio[i][0])/ratio[i][1],2)
            else:
                ratio[i][2] = 666

        print(sorted(ratio.items(), key=lambda x: x[1][2], reverse=True))
        print("Number of FP websites: "+str(count))
        print("Number of total websites: "+str(total))
        print("Number of FP origin: "+str(len(set(fp_origin))))
        print("List of FP origin: "+str(set(fp_origin)))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def FPcheck():
    total = attributes + add_attrs + WebGL_attrs + WebGL2_attrs + Canvas_attrs + Geo_attrs + RTC_attrs + Speech_attrs + Audio_attrs + Network_attrs + Screen_attrs + Battery_attrs
    std = []

    
    print("Total number of advanced seed before: "+str(len(total)))
    after = []
    idl = FPIdldata()
    for i in total:
        if i in idl:
            after.append(i)
    print("Total number of advanced seed after : "+str(len(after)))
    print("Diff: " + str(set(total) - set(after)))
    print(len(real_std))
    extra = add_attrs + WebGL_attrs + WebGL2_attrs + Canvas_attrs + Geo_attrs + RTC_attrs + Speech_attrs + Audio_attrs + Network_attrs + Screen_attrs + Battery_attrs
    print(extra)
    print("Advanced seed: "+str(len(extra)))
    output = ""
    # for i in extra:
        # output += 

def FPaccuracy():
    total = []

    tt = attributes + add_attrs + WebGL_attrs + WebGL2_attrs + Canvas_attrs + Geo_attrs + RTC_attrs + Speech_attrs + Audio_attrs + Network_attrs + Screen_attrs + Battery_attrs
    
    test2 = []
    
    # connect to MongoDB
    client = MongoClient()
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client["oracle"]
    collection = db["apis"]

    correct = 0
    wrong = 0
    total_fp = []
    print(len(test))
    for i in test:
        x = collection.find({"name": str(i)})
        for j in x:
            if (j["fp"]):
                correct += 1
                total_fp.append(i)
            else:
                wrong += 1
    # print(total_fp)
    print("Correct: "+str(correct) + " Wrong: "+str(wrong))
    print("Accuracy: "+str(round((correct)*1.0/(correct+wrong),3)))

    
    # Accuracy 300 random APIs

    # want =  add_attrs + WebGL_attrs + WebGL2_attrs + Canvas_attrs + Geo_attrs + RTC_attrs + Speech_attrs + Audio_attrs + Network_attrs + Screen_attrs + Battery_attrs
    # # print(want)

    # db = client["experiment2"]
    # collection = db["js_api_features"]

    # api_list = []
    # ran_list = []
    # count = 0

    # for website in collection.find():
    #     for feature in website["featureOrigins"]:
    #         for i in (feature["features"]):
    #             if "AudioNode" in i:
    #                 print(i)
    #                 print(feature["origin"])
    #         api_list.append(feature)
    # for i in range(0,1000):
    #     ran_list.append(random.randint(0, len(api_list)))
    # print(len(ran_list))
    # print(ran_list)
    # for i in enumerate(ran_list):
    #     if (api_list[i[1]]) not in total and (api_list[i[1]]) not in tt and count < 100:
    #         print(str(i[0]) + "      "+str(api_list[i[1]]))
    #         count += 1


def FPSTAnalysis():

    array = []
    if_list = []
    df = []
    sink = []
    url_count = 0
    total = []
    for i in apis.find():
        ori = i["origin"]
        url_count += 1
        array += i["array"].split(",")
        if_list += i["if"].split(",")
        df += i["df"].split(",")
        sink += i["sink"].split(",")
        # print(i["array"].split(","))
        # for j in list(i["array"]):
        #     print(j)
        
    # print(array)    
    total = list(set(array)|set(if_list)|set(df)|set(sink))
    # print(total)
    for j in total:
        # print(''.join(filter(str.isalpha, j)))
        realJ = ''.join(filter(str.isalpha, j))
        for i in std_api:
            
            if realJ.lower() in i.lower():
                std.append(realJ)
                break
    print("Total #: "+str(len(total)))
    print("URL #"+str(url_count))
    # print("Array #: "+str(len(set(array))))
    # # print(array)
    # print("If #: "+str(len(set(if_list))))
    # # print(if_list)
    # print("DF #: "+str(len(set(df))))
    # # print(df)
    # print("Sink #: "+str(len(set(sink))))
    # print(sink)
    print("STD #: "+str(len(std)))
    print(std)
    # print(std)




def main():
    # print(len(dc))
    # print("BEFORE: "+str(len(set(dc))))
    # print("AFTER: "+str(len(set(adc))))
    # dd = []
    # idl = FPIdldata()
    # for i in dc:
    #     if i in idl:
    #         dd.append(i)
    # print("dc: "+str(len(dd)))
    # dd = []
    # for i in adc:
    #     if i in idl:
    #         dd.append(i)
    # print("adc: "+str(len(dd)))
    # for args in sys.argv:
    #     print(str(args))
    if sys.argv[1] == "FPLO":
        FPLocal()
    elif sys.argv[1] == "FPLOI" and sys.argv[2]:
        FPLocalItr(sys.argv[2])
    elif sys.argv[1] == "FPIDL":
        FPIdldata()
    elif sys.argv[1] == "FPFQ":
        FPfreq()
    elif sys.argv[1] == "FPRA":
        FPratio()
    elif sys.argv[1] == "FPCH":
        FPcheck()
    elif sys.argv[1] == "FPST":
        FPstatic()
    elif sys.argv[1] == "FPAC":
        FPaccuracy()
    elif sys.argv[1] == "FPSTA":
        FPSTAnalysis()
    elif sys.argv[1] == "search" and sys.argv[2]:
        search(sys.argv[2])


if __name__ == "__main__":
    main()
