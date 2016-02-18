from math import sqrt

# NOTE: This is the book implementation
# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs,person1,person2):
    # Get the list of shared_items
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    # if they have no ratings in common, return 0
    if len(si)==0: return 0

    # Add up the squares of all the differences
    sum_of_squares=sum(
        [
            pow(
                prefs[person1][item]
                -
                prefs[person2][item]
            ,2)
            for item in prefs[person1] if item in prefs[person2]
        ]
    )

    return 1/(1+sum_of_squares)

# NOTE: This is my implementation
def get_euclidean_distance(person1, person2):
    no_common_items = True
    for key, value in person1.items():
        if key in person2:
            no_common_items = False
            break

    # Return 0 if person 1 and 2 have no common items
    if no_common_items:
        return 0

    sum_of_squares = 0
    for key, value in person1.items():
        if key in person2:
            sum_of_squares += pow(person1[key] - person2[key], 2)

    return 1/(1+sqrt(sum_of_squares))
