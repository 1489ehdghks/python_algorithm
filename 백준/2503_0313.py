def strike_and_ball(number, guess):
    strike = 0
    ball = 0
    for i in range(3):
        if number[i] == guess[i]:
            strike += 1
        elif guess[i] in number:
            ball += 1
    return strike, ball


def find_possible_numbers(n):
    possible_numbers = 0

    for num in range(123, 988):
        number = str(num)
        if len(set(number)) != 3 or '0' in number:
            continue

        is_possible = True
        for _ in range(n):
            guess, strike, ball = map(int, input().split())
            guess = str(guess)
            calc_strike, calc_ball = strike_and_ball(number, guess)
            if calc_strike != strike or calc_ball != ball:
                is_possible = False
                break

        if is_possible:
            possible_numbers += 1

    return possible_numbers


print(find_possible_numbers(n))
