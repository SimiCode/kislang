#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import logging

def xwrite(filename, data):
    if len(data)<1:
        open(filename, 'w').close()
    else:
        if type(data) is list:
            with open(filename, 'w') as dx:
                data = [l+"\n" for l in data]
                dx.writelines(data)

        elif type(data) is str:
            with open(filename, 'w') as dx:
                data = data+"\n"
                dx.write(data)

        elif type(data) is dict:
            with open(filename, 'w') as dx:
                data = [l+"\n" for l in data]
                dx.writelines(data)


def xappend(filename, data):
    if type(data) is list:
        with open(filename, "ab") as dx:
            data = [l+"\n" for l in data]
            dx.writelines(data)

    elif type(data) is str:
        with open(filename, "ab") as dx:
            data = data+"\n"
            dx.write(data)

    elif type(data) is dict:
        with open(filename, "ab") as dx:
            data = [l+"\n" for l in data]
            dx.writelines(data)

    else:
        print(type(data))


def xread(filename):
    with open(filename, 'r') as dx:
        rl = dx.readlines()
        rl = [l.strip() for l in rl]
    return rl


def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


#xwrite("rd.txt", ['data', "dt"])
#xappend("flagged.txt", "dafef")
#print(xread("rd.txt"))