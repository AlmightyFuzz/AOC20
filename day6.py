test_data1 = """abcx
abcy
abcz""" #6

test_data2 = """abc

a
b
c

ab
ac

a
a
a
a

b""" #11

def get_puzzle_input():
    with open("InputData/day6.txt") as file:
        return [group.split('\n') for group in file.read().split('\n\n')]

def count_questions(groups):
    total = 0
    for group in groups:
        questions = set()

        for person in group:
            questions.update(person)

        print(len(questions))
        total += len(questions)

    return total

if __name__ == "__main__":
    #input = [group.split('\n') for group in test_data1.split('\n\n')]
    #input = [group.split('\n') for group in test_data2.split('\n\n')]

    input = get_puzzle_input()
    
    num_qs = count_questions(input)
    #num_qs = sum( [len(set(''.join(group))) for group in input] )

    print(num_qs)