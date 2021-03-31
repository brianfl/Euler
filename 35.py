def is_prime(number):
    counter = 0
    for i in range(2, int(number**.5)+1):
        if number % i == 0:
            counter += 1
    if counter == 0:
        return True
    return False

circle_tracker = 2 # for 2 and 5. Which are skipped later

def chopper(number):
    s = str(number)
    tracker = 0
    all_rotations = []

    while tracker != len(s):
        s = s[1:] + s[0]
        all_rotations.append(int(s))
        tracker += 1
    
    return all_rotations

for i in range(2, 1000000+1):
    s = str(i)
    if not('0' in s or '2' in s or '4' in s or '5' in s or '6' in s or '8' in s):
        # If any one of these are in the number, eventually they will be at the end of the rotation.
        # Therefore not all the rotations can be prime. So we can skip these and speed up the program by a lot.
        count = 0
        rot_list = chopper(i)
        for j in rot_list:
            if is_prime(j):
                count += 1
        if count == len(rot_list):
            circle_tracker += 1
    
print(circle_tracker) #55