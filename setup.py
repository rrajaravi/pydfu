from setuptools import setup

def readme():
    return open('README.md', 'r').read()

def requirements():
    with open('requirements.txt', 'r') as f:
        return f.readlines()

setup(
    name = 'pydfs',
    packages = ['pydfs'],
    version = '0.1',
    long_description= readme(),
    description = "Disk and File system query",
    author='rrajaravi',
    author_email='r.rajaravi@gmail.com',
    url='https://github.com/rrajaravi/pydfs.git',
    license="MIT",
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
    ],
    install_requires=requirements(),
    test_suite="tests",
    scripts=['bin/pydfs']
)
