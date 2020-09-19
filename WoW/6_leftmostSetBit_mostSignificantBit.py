#Author	:	Bhavya Singh
#Date	:	23-May-2020
#Name	:	First set bit from left/ Most significant set bit


#PROBLEM:

Given a number, find the most significant bit number which is set bit and which is in power of two


#CODE

def leftmost_set_bit( n ):
    
    # Below steps set bits after 
    # MSB (including MSB)
    
    n |= n>>1
    n |= n>>2
    n |= n>>4
    n |= n>>8
    n |= n>>16
    
    # Increment n by 1 so that 
    # there is only one set bit 
    # which is just before original 
    # MSB.
    
    n += 1
    
    # Return original MSB after shifting.
    
    return (n >> 1)