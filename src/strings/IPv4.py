



def int32_to_ip(int32):
    """
    Take the following IPv4 address: 128.32.10.1
    This address has 4 octets where each octet is a single byte 
    (or 8 bits).
    
    1st octet 128 has the binary representation: 10000000
    2nd octet 32 has the binary representation: 00100000
    3rd octet 10 has the binary representation: 00001010
    4th octet 1 has the binary representation: 00000001
    So 128.32.10.1 == 10000000.00100000.00001010.00000001
    
    Because the above IP address has 32 bits, we can represent it as the 
    
    unsigned 32 bit number: 2149583361
    Complete the function that takes an unsigned 32 bit number and returns
    a string representation of its IPv4 address.
    
    """
    # your code here
    binnary = f'{int32:32b}'.strip()

        
    rest = 32 - len(binnary)

    binnary = rest * '0' + binnary

    return ".".join([str(int(binnary[i: i + 8].strip(), 2)) for i in range(0, 32, 8)])


def run_tests():
    int32 = 2149583361
    int32 = 2154959208
    int32 =  10131804 # expecting: 0.154.153.92
    
    def int32_to_ip(int32):
        return '{}.{}.{}.{}'.format(*int32.to_bytes(4, 'big'))
    
    
