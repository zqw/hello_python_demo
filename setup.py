from setuptools import setup, find_packages

setup(
    name="hello_python_demo",
    version="1.0",
    description="安装hello_python并打包上传pypi",
    author="zhaoqiangwei",
    author_email="demo@qq.com",
    url="https://github.com/zqw/hello_python",
    license="MIT",
    keywords=["hello_python", "hello_python_demo"],

    # 1.python解释器里的顶级文件夹映射进来的对应目录
    package_dir={
        '': 'src',
    },
    # 2.python解释器，site-packages里面顶级包(package)
    packages = find_packages(where="src", exclude=["module2"], include=["module1", "module1.*"]),
    # 3.python解释器，site-packages里面顶级文件
    py_modules=["hello_python1_top1", "hello_python1_top2"],

    # 4.python解释器，Scripts目录（在site-packageages外面）
    scripts = ["src/scripts/hello_python_script1.py", ],

    # 5.python解释器，c语言相关构建用
    ext_modules=[],
    ext_package=[],

    # 6.python解释器，最外层的文件,这个里面无法用正则表达式
    data_files=[
        ('hello_python_bm', ['src/data/bm/b1.txt', 'src/data/bm/b2.txt']),
        ('hello_python_cfg', ['src/data/cfg/data.cfg']),
        ('hello_python_sh', ['src/data/sh/shell1.sh'])
                ],

    # 7.python解释器，对应的是MANIFEST.in(但是好像也不用设置)
    include_package_data=True,

    requires = [
        'request',
        'six',
        'redis',
        'pytest',
    ],
    install_requires=[
        'enum34;python_version<"3.4"',
        'pywin32 >= 1.0;platform_system=="Windows"',
        'request',
        'six',
        'redis >= 2.10.5',
        'pytest',
    ],
    classifiers = [
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Operating System :: Unix',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
          'Topic :: Software Development'
      ],

)