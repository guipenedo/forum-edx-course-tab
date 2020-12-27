"""Setup for python judge XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='forum-edx-course-tab',
    version='0.1',
    description='link para o forum do afterschool',
    packages=[
        'forumcoursetab',
    ],
    entry_points={
        'openedx.course_tab': [
            'forumcoursetab = forumcoursetab:ForumCourseTab',
        ]
    },
    package_data=package_data("forumcoursetab"),
)
