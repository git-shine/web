# About
em..........a test subject of Django
## Tips
No.1 venv环境中start.py脚本中 stop 和 reload 不生效，待排查
N0.2 使用uwsgi后django admin 静态文件不生效：
     新建一个自定义目录 ---> 修改setting.py文件添加STATIC_ROOT参数（值为刚才新建目录的绝对路径，STATIC_URL请勿修改）---> 使用命令：python manage.py collectstatic 迁移静态文件 ---> 修改nginx配置文件，指定location块的的static处理规则(alias 到刚才的自定义目录) ---> reload nginx和uwsgi
N0.3 nginx + uwsgi使用时nginx配置：include uwsgi_params模块；指定连接uwsgi超时时间；指定uwsgi_pass对应uwsgi的sock路径以接收动态请求。
