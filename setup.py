from setuptools import setup, find_packages


setup(
    name="djangocms-ckeditor-font",
    version="0.1.0",
    url='http://github.com/ichag/djangocms-ckeditor-font',
    license='MIT',
    description="A plugin to incorporate Font Family and Sizes into djangocms-text-ckeditor",
    long_description=open('README.rst').read(),
    author='Max Hellwig',
    author_email='mx.hellwig@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    include_package_data=True,
    zip_safe=False,
)
