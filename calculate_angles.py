#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: Dec. 12, 2022
# a program that calculates the angles of a right
# angle triangle given the side lengths


import math


# function that asks the user if they want to play again
def play_again():
    while True:
        # getting user input
        yes_no = input("Do you want to play again? (y/n)")
        # they want to play again
        if yes_no.lower() == "y":
            return True
        # they don't want to play again
        if yes_no.lower() == "n":
            return False
        # user input invalid
        print("please make sure your input is valid.")


# function that calculates an unknown angle given the opposite and the hypotenuse
def calc_angles(opposite, hypotenuse):
    opp_over_hyp = opposite / hypotenuse
    angle_theta = math.asin(opp_over_hyp) * 57.2958
    return angle_theta


def error_checking(user_input):
    # try catch
    try:
        user_input_fl = float(user_input)
    # input is invalid
    except Exception:
        print("Input invalid! Please enter a valid number!")
        return 0
    # user input is valid
    else:
        # user input is not positive
        if user_input_fl < 1:
            print("Side length must be at least 1 unit long!")
            return 0
        # user input is positive
        else:
            return user_input_fl


def main():
    while True:
        print()
        # user input for the first leg
        leg_1_str = input("Enter the length of one of the legs (no units): ")
        if error_checking(leg_1_str) != 0:
            leg_1_fl = error_checking(leg_1_str)
        # user input is valid
        else:
            if play_again():
                continue
            break
        # user input for the other leg
        leg_2_str = input("Enter the length of the other leg (no units): ")
        if error_checking(leg_2_str) != 0:
            leg_2_fl = error_checking(leg_2_str)
        # user input is invalid
        else:
            if play_again():
                continue
            break
        # user input for the hypotenuse
        hypotenuse_str = input("Enter the length of the hypotenuse (no units): ")
        if error_checking(hypotenuse_str) != 0:
            hypotenuse_fl = error_checking(hypotenuse_str)
            # hypotenuse is not the longest side
            if hypotenuse_fl < leg_1_fl or hypotenuse_fl < leg_2_fl:
                print("The hypotenuse needs to be the longest side!")
                if play_again():
                    continue
                break
            # all input is valid
            else:
                theta_1 = calc_angles(leg_1_fl, hypotenuse_fl)
                theta_2 = calc_angles(leg_2_fl, hypotenuse_fl)
                print()
                print(
                    f"The angle opposite to the side with {leg_1_str}units is {theta_1:.2f}° and the angle opposite to the side with {leg_2_str}units is {theta_2:.2f}°."
                )
                if play_again():
                    continue
                break
        # user input is invalid
        else:
            if play_again():
                continue
            break


if __name__ == "__main__":
    main()
