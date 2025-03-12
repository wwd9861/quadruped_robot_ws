cmake_minimum_required(VERSION 3.8)
project(quadruped_robot_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY meshes launch urdf DESTINATION share/${PROJECT_NAME})

ament_package()

