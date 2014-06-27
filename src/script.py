#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Jun 23, 2014

@author: keisano1
'''


def main():
    parameters = {"Name":"Test", "Npoints":6 , "components":5}
    blocks = [""]*4
    with open("test_format.frm", "r") as f:
        for line in f:
            if line.startswith('#'):
                block = int(line[1])
            elif line.startswith('£'):
                if containsOptionalParameters(line, parameters):
                    clean_line = createCleanLine(line, parameters) 
                    blocks[block] += clean_line
            elif containsParameters(line, parameters):
                clean_line = createCleanLine(line, parameters) 
                blocks[block] += clean_line
            #elif line.startswith('\\'):
                #blocks[block] += line
                    
    with open("save_test.py", 'w') as f:
        i = 0
        for block in blocks:
            f.write("'Block #"+str(i)+"'\n")
            f.write(block)
            f.write('\n\n')
            i += 1
            
def createFromFormat(blocks, format_file, parameters):
    f = format_file
    for line in f:
        if line.startswith('#'):
            block = int(line[1])
        elif line.startswith('£'):
            if containsOptionalParameters(line, parameters):
                clean_line = createCleanLine(line, parameters) 
                blocks[block] += clean_line
                print "1 wrote " + clean_line
        elif getParameters(line):
            clean_line = createCleanLine(line, parameters) 
            blocks[block] += clean_line
            print "2 wrote " + clean_line
        else:
            blocks[block] += line
            print "3 wrote " + line
    
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
        if containsParameters(string[start:end], parameters):
            blocks.append(string[start:end])
        start = string.find('$', end+1) +1
    string = string.replace(string[i:end+1], '')
    if len(blocks) < 1:
        rcomma = string.rfind(',')
        string = string[:rcomma] + string[rcomma+1:]
    for block in blocks:
        rbracket = string.find(')')
        if block == blocks[0]:
            string = string[:rbracket]+ block + string[rbracket:]
        else:
            string = string[:rbracket]+ ", " + block + string[rbracket:]
    return string
    

def containsParameters(string, parameters):
    for parameter in getParameters(string):
        if parameters.has_key(parameter):
            return True
    return False

def containsOptionalParameters(string, parameters):
    for parameter in getOptionalParameters(string):
        if parameters.has_key(parameter):
            return True
    return False
    
def getParameters(string):
    parameters = []
    start = string.find('%') + 1
    while start:
        end = string.find('%', start)
        parameters.append(string[start:end])
        start  = string.find('%', end + 1) + 1 
    return parameters

def getOptionalParameters(string):
    parameters = []
    start_opt = string.find('$') + 1
    while start_opt:
        end_opt = string.find('$', start_opt)
        start = string.find('%', start_opt, end_opt) + 1
        end = string.rfind('%', start_opt, end_opt+1)
        parameters.append(string[start:end])
        start_opt  = string.find('$', end_opt) + 1
    print parameters 
    return parameters

if __name__ == "__main__":
    main()