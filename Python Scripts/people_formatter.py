import operator

def person_lister(f):
    def inner(people):
        # complete the function
        people.sort(key=lambda k: int(k[2]))
        return [f(person) for person in people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    #people = [input().split() for i in range(int(input()))]
    people = [
    ['Blossom', 'Michael', '9', 'F'],
    ['Bubbles', 'Kevin', '666666666666666', 'F'],
    ['Buttercup', 'Jake', '4444444444444444444444444444444444444444444444444444444444444444', 'F'],
    ['Michael', 'Blossom', '8888', 'M'],
    ['Kevin', 'Bubbles', '7777777', 'M'],
    ['Blossom1', 'Michael1', '2', 'F'],
    ['Jake', 'Buttercup', '555555555555555555555555555555', 'M']]
    print(*name_format(people), sep='\n')

#expected
#Ms. Blossom Michael
#Mr. Michael Blossom
#Mr. Kevin Bubbles
#Ms. Bubbles Kevin
#Mr. Jake Buttercup
#Ms. Buttercup Jake