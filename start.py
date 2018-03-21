#!/usr/bin/env python
#coding=utf-8

#######################################
## use age: python start.py env action
#######################################
import os
import sys

try:
    #脚本路径
    pwd = sys.path[0]
    #指定应用环境
    env = sys.argv[1]
    #指定执行动作，start reload stop
    action = sys.argv[2]
    if env == "dev":
        from hello_world.dev import *
    elif env == "product":
        from hello_world.product import *
    else:
        print "请指定应用环境参数，dev | product"
    if action == "start":
        os.system("cd %s; uwsgi --ini %s" %(pwd, config))
    elif action == "stop":
        os.system("cd %s; uwsgi --reload Logs/uwsgi.pid" %(pwd))
    elif action == "reload":
        os.system("cd %s; uwsgi --stop Logs/uwsgi.pid" %(pwd))
    else:
        print "请指定执行动作参数，start | stop | reload"
except Exception as e:
    print "="*30
    print "ERROR：请输入正确的启动参数！Use: python start.py env action\n环境参数：dev | product\n启动参数：start | reload | stop"
