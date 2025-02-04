#!/usr/bin/env python3

import os
import rospkg
import numpy as np
from roboticstoolbox.robot.ERobot import ERobot


class xarm7(ERobot):
    """
    Class that imports a UR10 URDF model
    ``UR3()`` is a class which imports a Universal Robotics UR310 robot
    definition from a URDF file.  The model describes its kinematic and
    graphical characteristics.
    .. runblock:: pycon
        >>> import roboticstoolbox as rtb
        >>> robot = rtb.models.URDF.UR10()
        >>> print(robot)
    Defined joint configurations are:
    - qz, zero joint angle configuration, 'L' shaped configuration
    - qr, vertical 'READY' configuration
    .. codeauthor:: Jesse Haviland
    .. sectionauthor:: Peter Corke
    """

    def __init__(self):

        links, name, urdf_string, urdf_filepath = self.URDF_read(
            "xarm_description/urdf/xarm7.urdf.xacro"
        )

        super().__init__(
            links,
            name=name.upper(),
            manufacturer="UFACTORY",
            urdf_string=urdf_string,
            urdf_filepath=urdf_filepath,
        )

        self.addconfiguration("qz", np.array([0, 0, 0, 0, 0, 0, 0]))
        # self.addconfiguration("qr", np.array([np.pi, 0, 0, 0, np.pi / 2, 0]))


if __name__ == "__main__":
    print(f"hello")

    # print(__file__)
    robot = xarm7()
    print(robot)