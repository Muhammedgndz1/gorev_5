from setuptools import setup

package_name = 'turtlefollow'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author_email='emred@example.com',
    description='Package for turtle creation and following in TurtleSim',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_creation_service = turtlefollow.turtle_creation_service:main',
            'turtle_follow_service = turtlefollow.turtle_follow_service:main',
        ],
    },
)

