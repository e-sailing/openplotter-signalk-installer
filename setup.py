#!/usr/bin/env python3

# This file is part of Openplotter.
# Copyright (C) 2019 by sailoog <https://github.com/sailoog/openplotter>
#                     e-sailing <https://github.com/e-sailing/openplotter>
# Openplotter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# any later version.
# Openplotter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Openplotter. If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
from openplotterSignalkInstaller import version

setup (
	name = 'openplotterSignalkInstaller',
	version = version.version,
	description = 'OpenPlotter app to manage Signal K node server installation',
	license = 'GPLv3',
	author="Sailoog",
	author_email='info@sailoog.com',
	url='https://github.com/openplotter/openplotter-signalk-installer',
	packages=['openplotterSignalkInstaller'],
	classifiers = ['Natural Language :: English',
	'Operating System :: POSIX :: Linux',
	'Programming Language :: Python :: 3'],
	include_package_data=True,
	entry_points={'console_scripts': ['signalkPostInstall=openplotterSignalkInstaller.signalkPostInstall:main','signalkPreUninstall=openplotterSignalkInstaller.signalkPreUninstall:main']},
	data_files=[('share/applications', ['openplotterSignalkInstaller/data/openplotter-signalk-installer.desktop']),('share/pixmaps', ['openplotterSignalkInstaller/data/openplotter-signalk-installer.png']),],
	)