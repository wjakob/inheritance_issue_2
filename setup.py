from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="inheritance_issue_2",
            sources=["inheritance_issue_2.c"],
        ),
    ]
)
