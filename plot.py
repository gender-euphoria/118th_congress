from astropy.io import ascii

data = ascii.read('members.csv', header_start=0, data_start=1)
print(data)
print(set(data['Party']))
print(set(data['Sex']))
print(set(data['Race']))

# TODO: make conda env file
#       fill out rest of members
#       plots :)
