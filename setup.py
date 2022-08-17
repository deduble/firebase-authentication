import setuptools
from packagename.version import Version


setuptools.setup(name='firebase-authentication',
                 version=Version('1.0.0').number,
                 description='Firebase Authentication Helper',
                 long_description=open('README.md').read().strip(),
                 author='Package Author',
                 author_email='yunus.kayalidere@gmail.com',
                 url='http://wwww.github.com/deduble/firebase-authentication.git',
                 py_modules=['firebase_authentication'],
                 install_requires=['firebase-admin'],
                 license='MIT License',
                 zip_safe=False,
                 keywords='firebase authentication',
                 classifiers=['Packages', 'Authentication', 'Firebase'])