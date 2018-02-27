from setuptools import find_packages, setup

setup(
    name='django-service-locator',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/alexescalonafernandez/django-service-locator.git',
    license='MIT',
    author='Alexander Escalona Fernández',
    author_email='alexescalonafernandez@gmail.com',
    setup_requires=['setuptools-markdown', 'service-locator', 'django'],
    description='Django application that allows the use of a light implementation of the service locator pattern.',
    long_description_markdown_filename='README.md',
    classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.4',
            'Topic :: Pattern Design :: Service Locator',
        ],
)
