# Copyright (C) 2020, 2021, 2022 Collabora Limited
# Author: Guillaume Tucker <guillaume.tucker@collabora.com>
#
# This module is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

import fnmatch
from glob import glob
import os
import setuptools
import kernelci


def _list_files(path, match):
    all_files = []
    for root, _, files in os.walk(path):
        dir_files = []
        for f in fnmatch.filter(files, match):
            dir_files.append(os.path.join(root, f))
        all_files.append((root, dir_files))
    return all_files


setuptools.setup(
    name='kernelci',
    version=kernelci.__version__,
    description="KernelCI core functions",
    author="kernelci.org",
    author_email="kernelci@groups.io",
    url="https://github.com/kernelci/kernelci-core",
    packages=[
        "kernelci",
        "kernelci.cli",
        "kernelci.config",
        "kernelci.lab",
        "kernelci.lab.lava",
        "kernelci.db",
        "kernelci.storage",
    ],
    scripts=[
        'kci',
        'kci_build',
        'kci_test',
        'kci_rootfs',
        'kci_data',
        'kci_bisect',
        'scripts/kci-bisect-lava-v2-callback',
        'scripts/kci-bisect-push-results',
    ],
    long_description=open('README.md', 'rb').read().decode('utf8'),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',  # noqa
        'Operating System :: OS Independent',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Testing',
    ],
    python_requires='>=3.6',
    install_requires=[
        "cloudevents",
        "jinja2",
        "kubernetes",
        "pyelftools",
        "pytest",
        "pyyaml",
        "requests",
    ],
    extras_require={
        'dev': [
            'pycodestyle',
            'pylint',
        ]
    }
)
