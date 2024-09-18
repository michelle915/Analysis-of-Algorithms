def feedDog(hunger_level, biscuit_size):
    satisfied_dogs = 0
    hunger_level.sort()
    biscuit_size.sort()

    dog, biscuit = 0, 0

    while dog < len(hunger_level) and biscuit < len(biscuit_size):
        # This biscuit can satisfy the current dog
        if biscuit_size[biscuit] >= hunger_level[dog]:
            satisfied_dogs += 1
            dog += 1

        # Current biscuit cannot satisfy the current dog. Try the next biscuit
        biscuit += 1

    return satisfied_dogs

print(feedDog([1,2,3], [1,1]))  # satisfied dogs = 1
print(feedDog([2, 1], [1,3,2])) # satisfied dogs = 2