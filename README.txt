# -!- coding: utf-8 -!-

# 这是我尝试进行构建的第一个python包

# 配置文件的优先级 setup.py < MANIFEST.in < setup.cfg

#创建.pypirc
# windows的用户文件夹目录为：
# C:\Users\Administrator\.pypirc
# .pypirc内容：
#
# [distutils]
# index-servers = pypi
#
# [pypi]
# username: 用户名
# password: 密码

#python setup.py register

#本地打包
#python setup.py sdist build
#python setup.py bdist_wheel --universal

#上传到pypi
#python setup.py sdist upload
#python setup.py bdist_wheel upload


#或者使用twine上传,先安装twine
# pip install twine
#

rm -rf src/hello_python_demo_demo.egg-info dist build &&  python setup.py sdist build && python setup.py bdist_wheel --universal
twine upload dist/*