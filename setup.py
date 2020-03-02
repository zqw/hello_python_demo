from setuptools import setup, find_packages

setup(
    name="hello_python",
    version="1.0",
    description="安装hello_python的学习测试项目",
    author="zhaoqiangwei",
    author_email="zhaoqiangwei@qq.com",
    url="https://www.baidu.com",
    # python解释器，sitepackages里面的最顶层文件

    # python解释器，sitepackages里面的模块
    package_dir={
        '': 'src',
    },
    # packages=["module1","module2", "module1.scripts", ],
    packages = find_packages(where="src", exclude=["module2"], include=["module1", "module1.*"]),
    py_modules=["hello_python1_top1", "hello_python1_top2"],

    # python解释器，scripts的文件
    scripts = ["src/scripts/hello_python_script1.py", ],

    ext_modules=[],
    ext_package=[],
    # python解释器，最外层的文件,这个里面无法用正则表达式
    data_files=[
        ('hello_python_bm', ['src/data/bm/b1.txt', 'src/data/bm/b2.txt']),
        ('hello_python_cfg', ['src/data/cfg/data.cfg']),
        ('hello_python_sh', ['src/data/sh/shell1.sh'])
                ],
    requires = ["request", "six"],

)