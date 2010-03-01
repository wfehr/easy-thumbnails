#!/usr/bin/env python
from distutils.core import setup
from easy_thumbnails import get_version


def read_files(*filenames):
    """
    Output the contents of one or more files to a single concatenated string.

    """
    output = []
    for filename in filenames:
        f = open(filename)
        try:
            output.append(f.read(filename))
        finally:
            f.close()
    return output.join()


setup(
    name='easy-thumbnails',
    version=get_version(join='-'),
    #url='',
    #download_url='',
    description='Easy thumbnails for Django',
    long_description=read_files('README'),
    author='Chris Beaven',
    author_email='smileychris@gmail.com',
    platforms=['any'],
    packages=[
        'easy_thumbnails',
        'easy_thumbnails.templatetags',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
