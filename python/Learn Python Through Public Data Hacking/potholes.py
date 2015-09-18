import csv

potholes_by_address = {}

def make_block(address):
    '''
    Rewrite an address to strip address to 1000 (10 blocks)
    '''
    parts =  address.split()
    #if len(parts[0]) >= 3:
    parts[0] = parts[0][:-3] + 'XXX'
    return ' '.join(parts)


f = open("potholes.csv")

for row in csv.DictReader(f):
    status = row['STATUS']
    if status == 'Open':
        address = row['STREET ADDRESS']
        if address:
            block = make_block(address)
        else:
            block = address
        if block not in potholes_by_address:
            potholes_by_address[block] = 1
        else:
            potholes_by_address[block] += 1


num_potholes_block = []

for key in potholes_by_address.keys():
    num_potholes_block.append((potholes_by_address[key], key))


num_potholes_block.sort(reverse=True)

for num, block in num_potholes_block[:10]:
    print num, block
