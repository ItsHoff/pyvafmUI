#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Jun 23, 2014

@author: keisano1

Module that handles the script creation.

The script will be first saved as a list of strings
and the file creation is handled by the main window.
The blocks will be written in in order but content inside
the blocks can be in any order.

The required format:
    # at the start of the line followed by number 0-4
      to start a new block.
    %Parameter% to signal a parameter, these will be
      replaced by the corresponding values from parameters
      dictionary.
    $$ to signal an optional parameter anything inside these
      will not be written if the parameter is missing.
      example: $parameter = '%Parameter%'$
    ££ to signal optional line, these lines will not be written
      if no OPTIONAL parameters are contained inside.
      example: £%name%.Configure($parameter = %Parameter%$)£
"""
# TODO: Make this cleaner
# TODO: Handle invalid formats


def createFromFormat(blocks, format_file, parameters):
    """Clean format_file lines and insert the right parameters.
    After cleaning append the line to the right block.
    """
    f = format_file
    for line in f:
        # set the current block
        if line.startswith('#'):
            # TODO: handle not setting a block
            block = int(line[1])
        elif line.startswith('£'):
            if containsSetOptionalParameters(line, parameters):
                clean_line = createCleanLine(line, parameters)
                blocks[block] += clean_line
        elif getParameters(line):
            clean_line = createCleanLine(line, parameters)
            blocks[block] += clean_line
        else:
            blocks[block] += line


def createCleanLine(line, parameters):
    if getOptionalParameters(line):
        print "cleaning optionals"
        line = cleanOptionalBlocks(line, parameters)
    for label, value in parameters.iteritems():
        replaced = '%'+label+'%'
        line = line.replace(replaced, str(value))
    line = line.replace('£', '')
    line = line.replace('$', '')
    return line


def cleanOptionalBlocks(string, parameters):
    blocks = []
    start = string.find('$') + 1
    i = start-1
    while start:
        end = string.find('$', start)
        if containsSetParameters(string[start:end], parameters):
            blocks.append(string[start:end])
        start = string.find('$', end+1) + 1
    string = string.replace(string[i:end+1], '')
    if len(blocks) < 1:
        rcomma = string.rfind(',')
        string = string[:rcomma] + string[rcomma+1:]
    for block in blocks:
        rbracket = string.find(')')
        if block == blocks[0]:
            string = string[:rbracket] + block + string[rbracket:]
        else:
            string = string[:rbracket] + ", " + block + string[rbracket:]
    return string


def containsParameters(string):
    found = string.find('%')
    if found != -1:
        return True
    else:
        return False


def containsSetParameters(string, parameters):
    for parameter in getParameters(string):
        if parameter in parameters:
            return True
    return False


def containsSetOptionalParameters(string, parameters):
    for parameter in getOptionalParameters(string):
        if parameter in parameters:
            return True
    return False


def getParameters(string):
    parameters = []
    start = string.find('%') + 1
    while start:
        end = string.find('%', start)
        parameters.append(string[start:end])
        start = string.find('%', end + 1) + 1
    return parameters


def getOptionalParameters(string):
    parameters = []
    start_opt = string.find('$') + 1
    while start_opt:
        end_opt = string.find('$', start_opt)
        start = string.find('%', start_opt, end_opt) + 1
        end = string.rfind('%', start_opt, end_opt+1)
        parameters.append(string[start:end])
        start_opt = string.find('$', end_opt) + 1
    print parameters
    return parameters
