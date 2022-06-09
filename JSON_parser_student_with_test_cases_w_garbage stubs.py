#############################
# JSON parser
# Note: Can parse any JSON values which includes:
#       true/false, null, numbers, objects, arrays, strings
#
#       parse_value(ds) is the entry point,
#       can only parse a single value, in order to parse multiple values, either
#       place the values into an array or an object OR you can call the
#       function multiple times to send each value in one at a time.
#       This parser will stop when a trailing space, '," or end of string is
#       encountered
#       
#############################
    
# parse_value(ds)
# This is a function used to parse JSON values
# Input: ds
#   ds: data stream (in string format)
# Output: ret_val, ret_str
#   ret_val: (will be type casted to the correct type: int, float, Null, list,
#             dictionary)
#   ret_str: the new ds after parsing the value
#           Example #1:
#               if you call parse_value('"abc", 1, null')
#               ret_val should equal to the string: abc
#               and ret_str should equal to the string: ', 1, null'
#
#           Example #2:
#               if you call parse_value(' "abc" ')
#               ret_val should equal to the string: abc
#               and ret_str should equal to the string: ' '
#                   which is the last character in the string ' "abc" '
#           Exmaple #3:
#               See the last case of Test case#1 below
#               print(parse_value(' true , false, null'))
#
#           if end of the string is reached, then return None instead
#              
# Note: to signify the end of key/value stream, just check for the following chars
#   ", :, ","
# Note: does not raise exception on JSON errors, if an invalid JSON data is
#       sent it, this parser will return None
def parse_value(ds):

    ds=remve_leading_spaces(ds)

    if ds[0]=='[':
        # start of a list
        ret_val=parse_array(ds)
    elif ds[0]=='{':
        # start of a dictionary
        ret_val=parse_object(ds)
    elif ds[0]=='"':
        # start of a string
        ret_val=ds[1:ds[1:].find('"')]
        ret_str=ds[ds[1:].find('"')+1:]
        
    elif len(ds)>=4 and ds[:4]=='null':
        ret_val=None
        ret_str=ds[4:]

    elif len(ds)>=4 and ds[:4]=='true':
        ret_val=True
        ret_str=ds[4:]  
        
    elif ds[0] in "-0123456789":
        end_pos....
        ret_val=int(ds[:end_pos])

        ret_val=float(ds[:end_pos])
        
        ret_str=ds[...]
    
    return ret_val, ret_str # remove this line to implement parse_value(ds)

def parse_array(ds):
    if ds[0]!='[':
        print("Exception error!!!")

    some_list=[]

    while ...:
    ret_val, ds=parse_value(ds[1:])
    some_list.append(ret_val)

    if ds[]==']':
        return some_list, ds


###############################################
# Test cases
###############################################

print("Testing simple data values\n")

print("1. Test true/false/none")
print(parse_value('false'))
print(parse_value(' false '))
print(type(parse_value(' false ')[0]))

print(parse_value('true'))
print(parse_value(' true '))
print(type(parse_value(' true ')[0]))
      
print(parse_value('null'))
print(parse_value(' null '))
print(type(parse_value(' null ')[0]))

print(parse_value(' true , false, null'))

print("\n2. Test strings")
print(parse_value('"abc"'))
print(parse_value(' "abc" '))
print(type(parse_value(' "abc" ')[0]))

print("\n3. Test ints")
print(parse_value('123'))
print(parse_value('-123'))
print(type(parse_value(' -123 ')[0]))

print("\n4. Test floats")
print(parse_value('1.23'))
print(parse_value('0.23'))
print(parse_value('-1e1'))
print(parse_value('-1e-5'))
print(parse_value(' -1E-5 '))
print(type(parse_value(' -1e-5 ')[0]))

##
##print("\n5. Test arrays")
##print(parse_value('[1,2.0, -1, -1e-10 , "abc",null,true,false]'))
##print(type(parse_value('[ 1,2.0, -1, -1e-10 , "abc"  , null, true,false ] ')[0]))
##
##print("\n6. Test nested arrays")
##print(parse_value('  [1,2.0, -1, [-1e-10, 1.5e1]  , "abc" ,null,true,false]  '))
##print(type(parse_value('  [1,2.0, -1, [-1e-10, 1.5e1]  , "abc" ,null,true,false]  ')[0][1]))
##
##print("\n7. Test objects")
##print(parse_value('{"LeagueID" : 0 ,  "PerMode":"PerGame","StatCategory": null}'))
##print(type(parse_value('{"LeagueID" : 0 ,  "PerMode":"PerGame","StatCategory": null}')[0]))
##
##print("\n8. Test objects with arrays")
##print(parse_value('{"LeagueID" : [0,1,2.0] ,  "PerMode":"PerGame","StatCategory": null}'))
##print(type(parse_value('{"LeagueID" : [0,1,2.0] ,  "PerMode":"PerGame","StatCategory": null}')[0]['LeagueID']))
##
##print("\n9. Test objects with arrays and objects")
##print(parse_value('{"LeagueID" : [0,1,2.0] ,  "PerMode":{"a": 1, "b":0.12e3},"StatCategory": null}'))
##print(type(parse_value('{"LeagueID" : [0,1,2.0] ,  "PerMode":{"a": 1, "b":0.12e3},"StatCategory": null}')[0]['LeagueID']))
##print(type(parse_value('{"LeagueID" : [0,1,2.0] ,  "PerMode":{"a": 1, "b":0.12e3},"StatCategory": null}')[0]['PerMode']))
##
##print("\n10. Final test, large mixed types")
##print(parse_value('{"resource":"leagueleaders","parameters":{"LeagueID":"00","PerMode":"PerGame","StatCategory":"PTS","Season":"2018-19","SeasonType":"Regular Season","Scope":"S","ActiveFlag":null},"resultSet":{"name":"LeagueLeaders","headers":["PLAYER_ID","RANK","PLAYER","TEAM","GP","MIN","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","FTM","FTA","FT_PCT","OREB","DREB","REB","AST","STL","BLK","TOV","PTS","EFF"],"rowSet":[[201935,1,"James Harden","HOU",18,36.800000,9.200000,20.900000,0.438000,4.100000,11.300000,0.363000,8.200000,9.900000,0.827000,0.700000,5.000000,5.700000,8.800000,2.300000,0.600000,5.700000,30.700000,28.800000],[201142,2,"Kevin Durant","GSW",23,35.700000,10.600000,20.600000,0.513000,1.500000,4.500000,0.340000,7.500000,8.000000,0.930000,0.500000,7.400000,7.900000,6.100000,0.900000,1.100000,3.300000,30.100000,32.300000],[2544,3,"LeBron James","LAL",22,34.800000,10.200000,19.700000,0.520000,2.200000,5.900000,0.372000,5.500000,7.700000,0.710000,1.000000,6.800000,7.800000,6.600000,1.300000,0.900000,3.500000,28.100000,29.500000],[203076,4,"Anthony Davis","NOP",19,37.500000,9.600000,19.500000,0.493000,0.800000,2.500000,0.340000,7.700000,9.500000,0.807000,3.500000,9.200000,12.700000,4.600000,1.500000,2.700000,2.400000,27.800000,35.300000  ]  ,  [203954,5,  "Joel Embiid","PHI"  ,  24,34.100000,8.900000,18.900000,0.472000,1.300000,4.200000,0.307000,8.400000,10.500000,0.794000,2.300000,11.000000,13.400000,3.500000,  0.500000,2.000000,  3.000000,27.500000,31.700000  ]  ] } }'))
##
