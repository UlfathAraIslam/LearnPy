# set automatically remove duplicates
def second_highest(scores):
    unique = sorted(set(scores),reverse=True) 
    return unique[1] if len(unique) > 1 else None
print(second_highest([88, 92, 92, 75, 100]))