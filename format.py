#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program shows formatting output


def main():
    # this function shows formatting output

    # input
    value = float(input("Enter a value ($): "))

    # process
    # nill

    # output
    print("")
    print("The cost is: ${:,.2f}".format(value))

    print("\nDone.")


if __name__ == "__main__":
    main()
