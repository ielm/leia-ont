from setuptools import setup, find_packages

setup(
    name="LEIAOntology",
    version="1.3.1",
    packages=find_packages(),
    install_requires=[
        "Flask==1.0.2",
        "Flask-Cors==3.0.9",
        "Flask-SocketIO==3.3.1",
        "pymongo==4.6.3",
        "boto3==1.7.6",
    ],
    author="Ivan Leon",
    author_email="i.leonmaldonado@gmail.com",
    description="LEIA Ontology Service and API",
    keywords="ontology",
    project_urls={
        "Documentation": "https://app.nuclino.com/LEIA/Knowledge/",
        "Source Code": "https://bitbucket.org/leia-rpi/leiaontology/src/master/",
    },
)
