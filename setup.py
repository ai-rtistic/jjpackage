from setuptools import setup, find_packages

setup(name='jjpackage-test', # 패키지 명

version='1.0.0',

description='Test Package',

author='airtistic',

author_email='blacwhit28@gmail.com',

url='https://github.com/airtistic/jjpackage-test',

license='MIT', # MIT에서 정한 표준 라이센스

py_modules=['packageTest'], # 패키지에 포함되는 모듈

python_requires='>=3',

install_requires=[], # 패키지 사용을 위해 필요한 추가 설치 패키지

packages=['packageTest'] # 패키지가 들어있는 폴더들

)