from setuptools import setup


setup(	name = 'spotlightpy',
		version = 0.1,
		description = 'Extract Images from Microsoft Spotlight(WinX only) Porject',
		classifiers = [
		"Development Status :: 3 - Alpha",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3 :: Only",
		"Operating System :: Microsoft :: Windows",
		],
		keywords = 'spotlight Microsoft Windows10 HDImages',
		url = 'https://github.com/joshikunal94/spotlightpy',
		author = 'Kunal Joshi',
		author_email = 'joshikunal16@gmail.com',
		license = 'MIT',
		packages = ['spotlightpy'],
		install_requires = [
							'pillow',
							],
		include_package_data = True,
		zip_safe = False	)