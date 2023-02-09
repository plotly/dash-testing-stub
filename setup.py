import io
from setuptools import setup


main_ns = {}
exec(open("dash_testing_stub/_version.py", encoding="utf-8").read(), main_ns)

setup(
    name="dash-testing-stub",
    version=main_ns["__version__"],
    author="Philippe Duval",
    author_email="philippe@plot.ly",
    license="MIT",
    description="Package installed with dash[testing] for optional loading of pytest dash plugin.",
    long_description=io.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://plotly.com/dash",
    packages=["dash_testing_stub"],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Dash",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ]
)
