

# s = pattern start  ( passed from wrapper ) 
# l = pattern length ( start from wrapper )
#BEGIN {
#
#	print pat ;
#
#
#}





{ 


if  ( substr($0,s,l)==pat ) 
{  
	print $0 
}

	
}