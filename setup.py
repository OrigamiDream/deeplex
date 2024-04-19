from setuptools import find_packages, setup

setup(
    name='deeplex',
    version='0.0.1',
    description='Free DeepL translation with Glossaries',
    url='https://github.com/OrigamiDream/deeplex.git',
    author='OrigamiDream',
    author_email='hello@origamidream.me',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(exclude=[]),
    platforms='any',
    install_requires=[
        'brotli>=1.1.0',
        'aiohttp>=3.9.5',
    ],
    python_requires='>=3.6.0',
    keywords=[
        'machine translation',
        'deepl',
        'free deepl',
        'google translate',
        'free translate',
        'translation',
        'multilingual',
        'mling'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
