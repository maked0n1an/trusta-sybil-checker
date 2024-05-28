
with open('trusta_sybils.txt', 'r') as file: 
    SYBIL_ADDRESSES = [row.strip() for row in file]

with open('addresses.txt', 'r') as file:
    OWN_ADDRESSES = [row.strip() for row in file]

def main():
    addresses_as_sybil = []
    
    for sybil in SYBIL_ADDRESSES:
        if sybil in OWN_ADDRESSES:
            addresses_as_sybil.append(f'{sybil}\n')
    
    if len(addresses_as_sybil) == 0:
        print('Sybils not found')
    else:
        print('Sybils are found, processing them to \'found_sybils.txt\'')
        with open('found_sybils.txt', 'w') as file:        
            file.writelines(addresses_as_sybil)

if __name__ == '__main__':
    main()