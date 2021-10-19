# I made this because I was so annoyed at always having manually change
# keys when playing songs on the guitar. Now it is a lot easier!

from collections import deque


def rotate(key):
    # Creates the order of a key
    keys = deque('ABCDEFG')
    while True:
        keys.rotate(1)
        if keys[0] == key:
            break
    return keys


def change_key(current_key, change_to, *args):
    '''
    This function takes the current key, the key you want to change to, and
    the specific chords you want changed to the new key and returns those
    new chords in an output that looks nice.
    '''
    new_chords = []
    curr_key = rotate(current_key)
    change_to = rotate(change_to)
    for i in [*args]:
        position = curr_key.index(i[0])
        if len(i) == 1:
            new_chords.append(change_to[position])
        else:
            new_chords.append(change_to[position]+i[1])
    return f'Old Chords:{[*args]}\nNew Chords:{new_chords}'

''' 
Example:
print(change_key('A', 'D', 'Am', 'A', 'B7', 'C'))
Output:
Old Chords:['Am', 'A', 'B7', 'C']
New Chords:['Dm', 'D', 'E7', 'F']
'''