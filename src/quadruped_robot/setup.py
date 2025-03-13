from setuptools import find_packages, setup

package_name = "quadruped_robot"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="wwd9861",
    maintainer_email="wwd9861@naver.com",
    description="quadruped_robot_control",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "leg_control = quadruped_robot.leg_control:main",
        ],
    },
)
