﻿#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   export_pb.py
@Time    :   2022/03/02 17:49:58
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   导出不同语言的pb文件
'''

# here put the import lib
import subprocess
import os
from tool_define import *
from setting_xml import *
from proto_xml import *

#############################################################################
proto_header = 'syntax = "proto3";'
#############################################################################

@Singleton
class ExportPb(object):
    def __init__(self):
        self.settingXml = ToolSettingXml()
        self.protoXml = ToolProtoXml()
        pass

    # 导出最新proto文件
    def exportProtoFile(self):
        try:
            self.protoXml.readProtocolXml()
            # 根据xml信息生产proto文件
            modules = self.protoXml.getModules()
            protocols = self.protoXml.getProtocols()
            for dirName, dirData in modules.items():
                # 添加引用
                protoMsgs = proto_header+"\n"
                protoMsgs += dirData.package +"\n\n"
                protocolDict = protocols[dirName]
                # if not protocolDict: continue
                for _, protoData in protocolDict.items():
                    # 注释
                    protoDesc = ""
                    descList = protoData.desc.split("\n")
                    for desc in descList:
                        protoDesc += "// "+desc+"\n"
                    protoMsgs += protoDesc
                    # 添加消息
                    protoMsgs += "message " + protoData.name + "{\n"

                    protoContent = ""
                    contentList = protoData.content.split("\n")
                    for content in contentList:
                        protoContent += "   " + content+"\n"
                    protoContent +="}\n\n"

                    protoMsgs += protoContent   
                    pass
                
                # 导出命名
                moduleName = dirData.dirName.split(" ")[1]
                # 获取导出proto路径
                settingXml = ToolSettingXml()
                toolConfig = settingXml.getTool()
                #print("save proto path=", toolConfig['proto'])
                protoFilePath = toolConfig['proto'] +"/"+moduleName+".proto"
                #print("export proto file=", protoFilePath)
                with codecs.open(protoFilePath, "w", 'utf-8', errors='ignore') as f:
                    f.write(protoMsgs)
                    f.flush()
                    pass                
                pass
        except Exception as e:
            print(e)


    def exportProtoBuffer(self):
        try:
            self.exportProtoFile()
            # 根据配置选项导出不同pb
            tmpls = self.settingXml.getTmplsByType(TmplType.PROTO)
            if not tmpls:
                return
            toolConfig = self.settingXml.getTool()
            protocPath = toolConfig['protoc']
            if not protocPath.endswith("/"):
                protocPath = protocPath +"/"
            
            protocExeFile = protocPath+"protoc.exe"
            protocGenGoFile = protocPath+"protoc-gen-go.exe"

            protoDir = toolConfig['proto']  
            if not protoDir: return  
            for config in tmpls:
                for proto in os.listdir(protoDir):
                    if not proto.endswith(".proto"):
                        continue
                    if not config.publish: continue        
                    gen_pb_cmd = ""
                    if config.lang == ProgramLangType.CPP: # cpp
                        gen_pb_cmd = protocExeFile + ' --proto_path=' + \
                            protoDir + ' --cpp_out='+config.publish + " "+proto
                        pass
                    if config.lang == ProgramLangType.LUA: # lua
                        gen_pb_cmd = protocExeFile + ' --proto_path=' + \
                            protoDir + ' -o '+config.publish+"/"+proto[:-6]+".pb" + " "+proto
                        pass
                    if config.lang == ProgramLangType.GO: # go
                        gen_pb_cmd = protocExeFile + ' --proto_path=' + \
                            protoDir + ' --plugin=protoc-gen-go='+ protocGenGoFile + ' --go_out='+config.publish + " "+proto                           
                        pass
                    if config.lang == ProgramLangType.CSHARP: # csharp
                        pass
                    if config.lang == ProgramLangType.PYTHON: #python
                        gen_pb_cmd = protocExeFile + ' --proto_path=' + \
                            protoDir + ' --python_out='+config.publish + " "+proto

                    subprocess.Popen(gen_pb_cmd, shell=True, cwd=os.getcwd())
        except Exception as e:
            print("export pb err, ", e)

   

