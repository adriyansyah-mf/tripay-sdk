from setuptools import setup, find_packages

setup(
    name='tripay-sdk',
    version='0.1.0',
    description='Unofficial SDK for Tripay payment gateway',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='adriyansyahmf',
    author_email='adriyansyahmf0@gmail.com',
    url='https://github.com/adriyansyahmf/tripay-sdk',
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
        'attrs==22.1.0',
        'httpx==0.27.0'
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
