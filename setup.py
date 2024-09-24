from setuptools import setup, find_packages

with open("README.md", "r") as file:
    lstr_long_prescription = file.read()

setup(
    name="resume_filter_API",  # Project name
    version="1.0.0",  # Version number
    description="A Python project for the API EndPoints",
    long_description=lstr_long_prescription,  # Add this to include the long description
    long_description_content_type="text/markdown",  # Ensure it's treated as markdown
    author="Dipa Kamble",
    author_email="",
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=[  # Dependencies
        'numpy',
        'pandas', 'configparser', 'fastapi', 'uvicorn', 'mysql-connector-python'
    ],
)
