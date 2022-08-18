import setuptools

setuptools.setup(name='firebase-authentication',
                 version='0.0.1',
                 description='Firebase Authentication Helper',
                 long_description=open('README.md').read().strip(),
                 author='Package Author',
                 author_email='yunus.kayalidere@gmail.com',
                 url='http://wwww.github.com/deduble/firebase-authentication.git',
                 install_requires=['firebase-admin'],
                 license='MIT License',
                 zip_safe=False,
                 keywords='firebase authentication',
                 classifiers=['Packages', 'Authentication', 'Firebase'])