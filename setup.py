import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description=f.read()
    
    
__version__="1.0.2"

REPO_NAME="Wine-Quality-Prediction-Using-Machine-Learning-and-AWS"
AUTHOR_USER_NAME="Kamran47t6"
SRC_REPO="Wine_Prediction_ML"
AUTHOR_EMAIL="muhammadkamran5862@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Machine Learning project to predict wine quality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

