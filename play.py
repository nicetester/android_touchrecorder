#!/usr/bin/python
import sys
import os

def trim(s):
    return str(int(s))

def h2d(s):
    h = int(s, 16)
    return str(h)

#deprecated
def compose_cmd(args):
    return "sendevent /dev/input/event1 " + compose_point(args)

def compose_point(args):
    try:
        args[0] = trim(args[0])
        args[1] = h2d(args[1])
        args[2] = h2d(args[2])
        return args[0] + " " + args[1] + " " + args[2]
    except IndexError:
        return ""

#deprecated
def touch(line):
    args = line.split()
    cmd = compose_cmd(args)
    #os.system(cmd)
    return cmd

def touch_point(line):
    args = line.split()
    point = compose_point(args)
    return point

def push_points():
    os.system("adb push points.txt /")

def play():
    os.system("adb shell \"toolbox hongbosb\"")

if __name__ == '__main__':
    file = open("log.txt")
    points_file = open("points.txt", "w")
    line = file.readline().rstrip()
    while line != "":
        point = touch_point(line)
        points_file.write(point + "\n")
        line = file.readline().rstrip()
    points_file.close()

    push_points()
    play()
