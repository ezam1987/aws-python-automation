from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Emmamnuel Alvarez',
    author_email='emmanuel1787@gmail.com',
    description='Webotron 80 is a tool to deploy static websites to AWS.',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/ezam1987/aws-python-automation/edit/master/01-webotron',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
