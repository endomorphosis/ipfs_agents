from setuptools import setup

setup(
	name='ipfs_accelerate',
	version='0.0.1',
	packages=[
        'ipfs_accelerate',
	],
	install_requires=[
        'ipfs_transformers@git+https://github.com/endomorphosis/ipfs_transformers.git',
        'ipfs_model_manager@git+https://github.com/endomorphosis/ipfs_model_manager.git',
        'transformers',
		'torch',
        'torchvision',
        'numpy',
        'torchtext',
		'urllib3',
		'requests',
		'boto3',
        'toml',
        'websocket-client',
        'trio',
        'multiaddr',
	]
)