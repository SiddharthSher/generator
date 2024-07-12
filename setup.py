from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Siddharth',
    author_email='s.sherkhane09@gmail.com',
    install_requires=["Openai","langChain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
    )

