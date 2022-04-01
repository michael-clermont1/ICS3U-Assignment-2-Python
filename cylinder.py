#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Feb 2022
# This program calculates the surface area of a cylinder

import math


def main():
    # this function calculates the circumference

    # input
    radius = int(input("Enter the radius of the cylinder (mm): "))
    height = int(input("Enter the height of the cylinder (mm): "))

    # process
    surface_area = 2 * math.pi * radius * height + 2 * math.pi * (radius**2)

    # output
    print("")
    print(
        "The surface area for the cylinder with a radius of {0} and height of {1} is {2} mm².".format(
            radius, height, surface_area
        )
    )

    print("\nDone.")


if __name__ == "__main__":
    main()
