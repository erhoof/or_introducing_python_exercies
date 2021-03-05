# Chapter 4

def chapter_4():

    # Task 1
    guess_me = 7

    if guess_me < 7:
        print('too low')
    elif guess_me > 7:
        print('too high')
    else:
        print('just right')

    # Task 2
    guess_me = 7
    start = 1

    while True:
        if start < guess_me:
            print('too low')
        elif start == guess_me:
            print('found it!')
            break
        else:
            print('oops')
            break
        start += 1

    # Task 3
    for num in range(3, -1, -1):
        print(num)

    for num in list(range(3, -1, -1)):
        print(num)

    # Task 4
    nums = [number for number in range(10) if number % 2 == 0]
    print(nums)

    # Task 5
    squares = {number: number ** 2 for number in range(10)}
    print(squares)

    # Task 6
    odd = {number for number in range(10) if number % 2 == 0}
    print(odd)

    # Task 7
    gen = (number for number in range(10))
    for num in gen:
        print('Got', num)

    # Task 8
    def good():
        return ['Harry', 'Ron', 'Hermione']

    print(good())

    # Task 9
    def get_odds():
        for num in range(10):
            if num % 2 == 0:
                yield num

    count = 0
    for num in get_odds():
        if count == 2:
            print(num)
        count += 1

    # Task 10
    def test(func):
        def new_function(*args, **kwargs):
            print('start')
            result = func()
            print('end')
            return result
        return new_function

    @test
    def hello():
        print('Hello, World!')

    hello()

    # Task 11
    class OopsException(Exception):
        pass

    try:
        raise OopsException()
    except OopsException as ex:
        print('Caught an oops')

    # Task 12
    titles = ['Creature of Habit', 'Crewel Fate']
    plots = ['A nun turns into a monster', 'A haunted yarn shop']

    movies = dict(zip(titles, plots))
    print(movies)

