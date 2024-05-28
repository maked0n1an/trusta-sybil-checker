
with open('trusta_sybils.txt', 'r') as file: 
    SYBIL_ADDRESSES = [row.strip() for row in file]

with open('addresses.txt', 'r') as file:
    OWN_ADDRESSES = [row.strip() for row in file]

def main():
    addresses_as_sybil = []
    
    for sybil in SYBIL_ADDRESSES:
        if sybil in OWN_ADDRESSES:
            addresses_as_sybil.append(f'{sybil}\n')
    
    sybil_len = len(addresses_as_sybil)
    
    if sybil_len == 0:
        print('Sybils not found')
    else:        
        message = f'Total: {sybil_len} sybil wallet(s)'
        
        print(
            f'Sybils are found, processing them to "found_sybils.txt"'
        )
        print(message)
        
        with open('found_sybils.txt', 'w') as file:
            file.write(message)   
            file.writelines(addresses_as_sybil)
            
if __name__ == '__main__':
    main()