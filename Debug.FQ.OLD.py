#!/usr/bin/python


# #################################################################
#
#
# -----------------------------------------------------------------
#
#
#
# -----------------------------------------------------------------
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# ###########################################################################
# to do

# reporting
# counters


import os
import sys
import time




def usage():
    print("""
Name: FQ.py 
Called as: FQ.py <file_in> <start> <end> <pattern1> <pattern2> ...<patternN>
Input: <file_in> : full path to file
       <start>      : integer
       <end>        : integer
       <pattern.>   : string
""")



# script time param
def script_time_param():
    # Name: time parameter
    # Function: script_time_param
    # Input: None
    # Output: string with formatted time
    # Usage: print (script_time_param) or a = script_time_param
    return time.strftime("%c")


# script params
def script_path_param(string1, vocal = 'yes'):
    '''
    Name: script_path_param
    Function: script_path_param(string1, vocal = 'yes')
    Input: script_path_param(sys.argv[0])  
    Output: [ T | F ]
    Usage: Precaches basic script parameters
    Notes: None
    '''
    #import sys
    #import os
    #Called as: script_path_param(sys.argv[0])
    
    try:
        script_name = os.path.basename(string1)
        script_dir = os.path.dirname(os.path.realpath(string1))
        script_full = script_dir + script_name
    except:
        print("Error loading script parameters. Possible problem with os module")
    
    if vocal != 'yes': 
        return ( script_name, script_dir, script_full )
    else:
        print("Script name: " + str(script_name))
        print("Script directory: " + str(script_dir))
        print("Script full: " + str(script_full))
        print ('Script started at: ' + time.strftime("%c"))
        return True


# isinteger
def typecheck(input, type):
    '''
    Name: typecheck
    Function: typecheck(input, type)
    Input:  * data
            * type = type definition:
                        int, 
                        string | str,
                        list,
                        dict,
                        tuple,
                        defaultdict,
                        array
    Output: [ T | F ]
    Usage: Checks data type against a specific type.
    Notes: None
    
    '''
    return isinstance(input, type)

       
        
# file exists
def fileexists(filepath):
  '''
  Function: filexists
  Description: Checks for existence of file
  Input: filepath (or raw string of it)
  Output: Boolean
  Usage: if filexists(file_in):...
  Notes: Depending on system may need to 
  conver to raw string with r'file_in.
  '''
  import os.path
  if os.path.exists(filepath):
    return True
  else:
    return False

    
# timer
def timing_val(func):
    '''
    Author: p.doulgeridis
    Name: timing_val
    Function: timing_val(func)
    Input: none, decorator function
    Output: prints elapsed time of execution
    Usage: @timing_val over function declaration
    Notes: wrapper timing function.
    '''
    def wrapper(*arg, **kw):
        
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        print ('%r (%r, %r) %0.9f sec' % \
              (func.__name__, arg, kw, t1-t2))
        return (t2 - t1), res
    return wrapper 
    
    
def calcoffsetsub(sub_start, sub_length):
    '''
    Name: Calculates awk/bash style offset
    Function: calcoffsetsub
    Input: start, end
    Output: start, length for python
    Usage: calcoffsetsub(2, 10)
    Notes: None
    '''
    start_int = int(sub_start)
    length_int = int(sub_length)
    
    start_real = start_int - 1
    end_real = start_real + length_int
    
    return (start_real, end_real)


def parsearguments(list_in):
    '''
    Name: parsearguments
    Function: parsearguments(list_in)
    Input: sys.argv
    Output: <list> - arguments past the 3rd.
    Usage: parsearguments(sys.argv)
    Notes: None, script specific.
    '''
    out_list = []

    for index, argument in enumerate(sys.argv):
        if index > 3:
            out_list.append(argument)

    return out_list



# chk_args_type
def chck_args_type(string):
    '''
    Function : chck_args_type(string)
    Description: Checks the content of parameters
    Input: sys.argv
    Output: STDOUT print
    Called as chck_args_type(sys.argv)
    '''
    for i in range(len(string)):
        if i == 0:
            print "Arguments for script: %s" % sys.argv[0]
        else:
            print "%d. argument: %s" % (i,sys.argv[i])
    print("\n")
    
    return 0

def script_end():
    import time
    print("\n" + "Script ended at: " + time.strftime("%c"))   
    
@timing_val
def parse_file(file_in, filter_list_in):
    
    counter = 0
    count_found = 0
    file_ot = str(file_in) + ".filterpy"
    out_file = open(file_ot, 'w')
    
    with open(file_in, 'r') as f:
        for i, line in enumerate(f):
            fixed_line = line.rstrip()
            #print(fixed_line[calcoffsetsub(sub_start, sub_length)[0]:calcoffsetsub(sub_start, sub_length)[1]])
            key = fixed_line[calcoffsetsub(sub_start, sub_length)[0]:calcoffsetsub(sub_start, sub_length)[1]]
            #print(key)
        
            if key in filter_list:
                count_found += 1
                out_file.write(line)
                
        print("Read: " + str(i) + " lines.")
        print("Found: " + str(count_found) + " matches.")
                
# #######################################################
# Initial checks

# Parse non optinal parameters.
try:
    file_in = sys.argv[1]
    sub_start = sys.argv[2]
    sub_length = sys.argv[3]
    sub_pat = sys.argv[4]
except:
    print("Error: Parameter parsing. Terminating script")
    sys.exit(1)


# Check for existence of input file
if not fileexists(file_in):
    print("\n" + "Provided file could not be detected. Terminating")
    usage()
    sys.exit(1)

# Typecheck the next two positional parameters against int
if not typecheck(int(sub_start), int):
    print("\n" + "Provided number is not an integer. Terminating")
    usage()
    sys.exit(1)

if not typecheck(int(sub_length), int):
    print("\n" + "Provided number is not an integer. Terminating")
    usage()
    sys.exit(1)    
    
    
    
# ########################################################    
# Script Start
print("Initial controls successful. Launching script...")
print("\n")


# print script parameters
script_path_param(sys.argv[0])
print("\n")


# product filter_list from arguments                
filter_list = parsearguments(sys.argv)
print("\n")


# check args type - on screen report                
chck_args_type(sys.argv)
print("\n")


# Call main work - time it.
parse_file(file_in, filter_list)

            
# ##########################################################
# Script end
script_end()