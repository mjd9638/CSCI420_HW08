"""
filename: HW08_Dortz_Program_832.py
author: Michael Dortz (mjd9638)
description: finds the largest fraction by using Axially aligned gradient
accent
"""

import BirdBathFunc_CH_cls420 as bb
import time as tt


def get_value(roll, tilt, twist):
    """
    returns the fraction of the sphere that is held in the birdbath given the
    dimension values
    :param roll: the degree of roll
    :param tilt: the degree of tilt
    :param twist: the degree of twist
    :return: the fraction of sphere that is the birdbath
    """
    bb_value = bb.BirdBathFunc_CH_cls420(roll, tilt, twist)
    return bb_value


def axially_aligned_search(min_val, max_val,
                           curr_max, roll, tilt, twist, degree, count):
    """
    performs the axially aligned search algo for the birdbath function. The
    search function starts by finding the starting fraction given the starting
    roll, tilt and twist dimensions, then recursively finds the max fraction
    with the degree
    :param min_val: minimum value of the dimensions
    :param max_val: maximum value of the dimensions
    :param curr_max: current known maximum of function
    :param roll: roll dimension value of curr_max
    :param tilt: tilt dimension value of curr_max
    :param twist: twist dimension value of curr_max
    :param degree: magnitude of degree change for a dimension
    :return: optimized value of bird bath
    """

    # if the current known maximum is -1
    if curr_max == -1:
        # get the current max, as search algo just started
        curr_max = get_value(roll, tilt, twist)

    # set temporary max and dimensions to current's values
    temp_max = curr_max
    temp_dim = [roll, tilt, twist]

    """
    print("\t\tFinding better max for roll = " + str(round(roll, 3)) + ", tilt = " +
          str(round(tilt, 3)) + ", twist = " + str(round(twist, 3)) + " with a degree of " +
          str(degree) + " (" + str(curr_max) + ")")
    """
    # if the new roll is >= minimum value
    if roll - degree >= min_val:
        # get value of fraction with roll - degree
        roll_minus = get_value(roll - degree, tilt, twist)
        # if this value is better than the temp value
        if roll_minus > temp_max:
            # set temp max and dimensions to roll - degree's values
            temp_max = roll_minus
            temp_dim = [roll - degree, tilt, twist]

    # if the new roll is <= maximum value
    if roll + degree <= max_val:
        # get value of fraction with roll + degree
        roll_plus = get_value(roll + degree, tilt, twist)
        # if this value is better than the temp value
        if roll_plus > temp_max:
            # set temp max and dimensions to roll + degree's values
            temp_max = roll_plus
            temp_dim = [roll + degree, tilt, twist]

    # if the new tilt is >= minimum value
    if tilt - degree >= min_val:
        # get value of fraction with tilt - degree
        tilt_minus = get_value(roll, tilt - degree, twist)
        # if this value is better than the temp value
        if tilt_minus > temp_max:
            # set temp max and dimensions to tilt - degree's values
            temp_max = tilt_minus
            temp_dim = [roll, tilt - degree, twist]

    # if the new tilt is <= maximum value
    if tilt + degree <= max_val:
        # get value of fraction with tilt + degree
        tilt_plus = get_value(roll, tilt + degree, twist)
        # if this value is better than the temp value
        if tilt_plus > temp_max:
            # set temp max and dimensions to tilt + degree's values
            temp_max = tilt_plus
            temp_dim = [roll, tilt + degree, twist]

    # if the new twist is >= minimum value
    if twist - degree >= min_val:
        # get value of fraction with twist - degree
        twist_minus = get_value(roll, tilt, twist - degree)
        # if this value is better than the temp value
        if twist_minus > temp_max:
            # set temp max and dimensions to twist - degree's values
            temp_max = twist_minus
            temp_dim = [roll, tilt, twist - degree]

    # if the new twist is <= maximum value
    if twist + degree <= max_val:
        # get value of fraction with twist + degree
        twist_plus = get_value(roll, tilt, twist + degree)
        # if this value is better than the temp value
        if twist_plus > temp_max:
            # set temp max and dimensions to twist + degree's values
            temp_max = twist_plus
            temp_dim = [roll, tilt, twist + degree]

    count += 1

    # if the temporary max is greater than the current max
    if temp_max > curr_max:
        """
        print(str(count) + "\t\tFound better max at    roll = " + str(round(temp_dim[0], 3)) +
              ", tilt = " + str(round(temp_dim[1], 3)) + ", twist = " +
              str(round(temp_dim[2], 3)) + " with a degree of " + str(degree) +
              " (" + str(temp_max) + ")")
          """
        # find max value around the temp dimensions
        # return the best value and dimensions
        return [temp_max, temp_dim[0], temp_dim[1], temp_dim[2], count, False]
        # return axially_aligned_search(min_val, max_val, temp_max, temp_dim[0],
        #                               temp_dim[1], temp_dim[2], degree, count)
    # else no new max was found
    else:
        # enough searching, it's done
        print(str(count) + "\t\tNo better max than     roll = " + str(round(roll, 3)) +
              ", tilt = " + str(round(tilt, 3)) + ", twist = " +
              str(round(twist, 3)) + " with a degree of " + str(degree) +
              " (" + str(temp_max) + ")")

        # return the best value and dimensions
        return [curr_max, roll, tilt, twist, 0, True]

def max_arg(min_val, max_val, roll, tilt, twist, degree):
    """
    finds the max value of the bird bath function given the starting
    coordinates
    :param min_val: minimum value of the dimensions
    :param max_val: maximum value of the dimensions
    :param roll: the starting roll coordinate
    :param tilt: the starting tilt coordinate
    :param twist: the starting twist coordinate
    :param degree: the change in coordinate for the search
    :return: the max value found given the starting coords, and the dimensions
    of it
    """
    # set max value to -1 for search algo, and make list of current best dims
    max_value = -1
    curr_best = [max_value, roll, tilt, twist, 0, False]
    # while the degree is greater than the minimum it can be
    while degree >= .001:
        # find the best max given the degree
        print("\tFinding best max for roll = " + str(roll) + ", tilt = " + str(tilt)
              + ", twist = " + str(twist) + " with a degree of " + str(degree))
        curr_best = axially_aligned_search(min_val, max_val,
                                           curr_best[0], curr_best[1],
                                           curr_best[2], curr_best[3], degree, curr_best[4])
        print("\tBest max for roll = " + str(roll) + ", tilt = " + str(tilt)
              + ", twist = " + str(twist) + " with a degree of " + str(degree)
              + " is " + str(curr_best[0]))

        if curr_best[5] is True:
            # divide the degree by 10 for a more through search of the max
            degree /= 10
    # return the max value
    return curr_best


def all_max_args(min_val, max_val, increment, degree):
    """
    attempts to find the max value of the birth bath function given the
    minimum and maximum ranges of the dimensions and the degree of change
    to start with
    :param min_val: the minimum value of the range
    :param max_val: the maximum value of the range
    :param increment: the incrementer for each call
    :param degree: the degree of change to start with
    :return: the best max value and its dimensions
    """

    # set
    temp_max = []
    best_max = [0, 0, 0, 0, 0]

    # for each roll increment
    for roll in range(min_val, max_val + 1, increment):
        # for each tilt increment
        for tilt in range(min_val, max_val + 1, increment):
            # for each twist increment
            for twist in range(min_val, max_val + 1, increment):
                # get the max of the starting dimensions
                print("Finding best max for roll = " + str(roll) + ", tilt = "
                      + str(tilt) + ", twist = " + str(twist))
                temp_max = max_arg(min_val, max_val, roll, tilt, twist, degree)
                print("Best max found for roll = " + str(roll) + ", tilt = "
                      + str(tilt) + ", twist = " + str(twist) + " is " +
                      str(temp_max[0]))
                if temp_max[0] > best_max[0]:
                    best_max = temp_max
    print("Best fraction: " + str(best_max[0]))
    print("The roll dimension: " + str(best_max[1]))
    print("The tilt dimension: " + str(best_max[2]))
    print("The twist dimension: " + str(best_max[3]))

def main():

    min_val = -90
    max_val = 90

    all_max_args(min_val, max_val, 90, 1)
    """
    vals = max_arg(-1, -90, -90, -90, 1)
    print("BEST FRACTION: " + str(vals[0]) + "\tROLL: " + str(vals[1]) + ", TILT: " + str(vals[2]) + ", TWIST: " + str(vals[3]))
    vals = max_arg(-1, -90, -90, 90, 1)
    print("BEST FRACTION: " + str(vals[0]) + "\tROLL: " + str(vals[1]) + ", TILT: " + str(vals[2]) + ", TWIST: " + str(
        vals[3]))
    vals = max_arg(-1, -90, 90, -90, 1)
    print("BEST FRACTION: " + str(vals[0]) + "\tROLL: " + str(vals[1]) + ", TILT: " + str(vals[2]) + ", TWIST: " + str(
        vals[3]))
    vals = max_arg(-1, -90, 90, 90, 1)
    print("BEST FRACTION: " + str(vals[0]) + "\tROLL: " + str(vals[1]) + ", TILT: " + str(vals[2]) + ", TWIST: " + str(
        vals[3]))
    vals = max_arg(-1, 90, -90, -90, 1)
    print("BEST FRACTION: " + str(vals[0]) + "\tROLL: " + str(vals[1]) + ", TILT: " + str(vals[2]) + ", TWIST: " + str(
        vals[3]))
    vals = max_arg(-1, 90, -90, 90, 1)
    print("BEST FRACTION: " + str(vals[0]) + "\tROLL: " + str(vals[1]) + ", TILT: " + str(vals[2]) + ", TWIST: " + str(
        vals[3]))
    vals = max_arg(-1, 90, 90, -90, 1)
    print("BEST FRACTION: " + str(vals[0]) + "\tROLL: " + str(vals[1]) + ", TILT: " + str(vals[2]) + ", TWIST: " + str(
        vals[3]))
    vals = max_arg(-1, 90, 90, 90, 1)
    print("BEST FRACTION: " + str(vals[0]) + "\tROLL: " + str(vals[1]) + ", TILT: " + str(vals[2]) + ", TWIST: " + str(
        vals[3]))
    """
    """
    for x in range(min_val, max_val + 1):
        print("X:\t" + str(x))
        for y in range(min_val, max_val + 1):
            print("\tY:\t" + str(y))
            for z in range(min_val, max_val + 1):
                print("\t\tZ:\t" + str(z))
                print("\t\t\t" + str(get_value(x, y, z)))
    """


if __name__ == '__main__':
    start = tt.time()
    main()
    print(tt.time() - start)