import json
from fractions import Fraction
from math import factorial, gcd, isqrt


def next_prime(lower):
    candidate = lower + 1
    while any(candidate % divisor == 0 for divisor in range(2, isqrt(candidate) + 1)):
        candidate += 1
    return candidate


def nth_primes(count):
    result = [0]
    while len(result) <= count:
        result.append(next_prime(result[-1] if result[-1] else 1))
    return result


def coefficient_recurrence(series, exponent, degree):
    powered = [Fraction(1)]
    for index in range(1, degree + 1):
        numerator = sum(((exponent + 1) * position - index) * series[position] * powered[index - position]
                        for position in range(1, min(index + 1, len(series))))
        powered.append(Fraction(numerator, index))
    return powered


def product(first, second, degree):
    return [sum(first[position] * second[index - position]
                for position in range(max(0, index - len(second) + 1), min(index + 1, len(first))))
            for index in range(degree + 1)]


def coefficient_power(series, exponent, degree):
    result = [1] + [0] * degree
    factor = list(series) + [0] * max(0, degree + 1 - len(series))
    while exponent > 0:
        if exponent & 1:
            result = product(result, factor, degree)
        exponent >>= 1
        if exponent:
            factor = product(factor, factor, degree)
    return result


def construct(schedule, slope, degree):
    series = [Fraction(1), Fraction(slope)]
    for index in range(2, degree + 1):
        numerator = coefficient_recurrence(series, schedule[index], index)[index]
        series.append(-numerator / schedule[index])
    return series


def logarithmic_coefficients(series, degree):
    coefficients = [0]
    for index in range(1, degree + 1):
        coefficients.append(index * series[index] - sum(coefficients[position] * series[index - position]
                                                       for position in range(1, index)))
    return coefficients


def check_family(schedule, slope, degree):
    assert all(schedule[index] > 0 and gcd(schedule[index], factorial(index)) == 1
               for index in range(2, degree + 1))
    series = construct(schedule, slope, degree)
    assert all(value.denominator == 1 for value in series)
    series = [int(value) for value in series]
    logarithm = logarithmic_coefficients(series, degree)
    inverse = [1]
    for index in range(1, degree + 1):
        inverse.append(-sum(series[position] * inverse[index - position] for position in range(1, index + 1)))
    assert product(series, inverse, degree) == [1] + [0] * degree
    direct_logarithm = [0] + [sum(position * series[position] * inverse[index - position]
                                  for position in range(1, index + 1)) for index in range(1, degree + 1)]
    assert logarithm == direct_logarithm
    sibling = []
    for index in range(2, degree + 1):
        exponent = schedule[index]
        powered = coefficient_power(series, exponent, index)
        assert powered == coefficient_recurrence(series, exponent, index)
        assert powered[index] == 0
        assert all(value % exponent == 0 for value in powered[1:])
        assert logarithm[index] % exponent == 0
        assert all(exponent * sum(logarithm[position] * powered[order - position]
                                  for position in range(1, order + 1)) == order * powered[order]
                   for order in range(1, index + 1))
        sibling.append(powered[index - 1] // exponent)
        for change in (Fraction(1), Fraction(-2), Fraction(1, 2)):
            modified = list(series[:index]) + [series[index] + change]
            assert coefficient_power(modified, exponent, index)[index] == exponent * change
    reconstructed = [Fraction(1)]
    for index in range(1, degree + 1):
        reconstructed.append(sum(Fraction(logarithm[position]) * reconstructed[index - position]
                                 for position in range(1, index + 1)) / index)
    assert reconstructed == series
    return series, logarithm, sibling


def main():
    degree = 64
    primes = nth_primes(degree)
    series, logarithm, sibling = check_family(primes, 1, degree)
    expected_source = [1, 1, -1, 2, -5, 13, -31, 48, 129, -2035, 12963, -20703,
                       -782282, 14675113, -177056253, 1716591959]
    expected_logarithm = [1, -3, 10, -35, 121, -390, 1037, -1083, -14030, 137837,
                          -382106, -8791718, 199408912, -2701500413, 28888970650]
    expected_sibling = [1, 1, 1, 5, 6, 37, 45, 316, 7096, 9670, 224327, 1236047]
    assert series[:len(expected_source)] == expected_source
    assert logarithm[1:len(expected_logarithm) + 1] == expected_logarithm
    assert sibling[:len(expected_sibling)] == expected_sibling
    displayed_rows = {3: [1, 3, 0, 1, -3, 6, -1, -93, 834],
                      5: [1, 5, 5, 0, 0, -4, 30, -190, 1145],
                      7: [1, 7, 14, 7, 0, -7, 35, -188, 1050]}
    assert all(coefficient_power(series, exponent, 8) == row for exponent, row in displayed_rows.items())
    family_degree = 24
    schedules = {'nth-prime': nth_primes(family_degree),
                 'least-prime-above-n': [0, 0] + [next_prime(index) for index in range(2, family_degree + 1)],
                 'least-prime-above-2n': [0, 0] + [next_prime(2 * index) for index in range(2, family_degree + 1)],
                 'square-of-least-prime-above-n': [0, 0] + [next_prime(index) ** 2 for index in range(2, family_degree + 1)]}
    slopes = [-3, -1, 0, 1, 2, 3]
    for schedule in schedules.values():
        for slope in slopes:
            check_family(schedule, slope, family_degree)
    assert logarithm[1] == 1 and logarithm[1] % primes[1] != 0
    bad_schedule = [0, 0, 2]
    assert construct(bad_schedule, 1, 2)[2] == Fraction(-1, 2)
    result = {'status': 'ALL_CHECKS_OK', 'arithmetic': 'exact integers and rational numbers',
              'original_indices': [2, 64], 'data_matches': {'A381353': [0, 15], 'A381355': [1, 15]},
              'sibling_data_indices': [2, 13], 'displayed_power_rows': [3, 5, 7], 'displayed_max_degree': 8,
              'exponent_schedules': list(schedules), 'integer_slopes': slopes, 'family_indices': [2, 24],
              'family_count': len(slopes) * len(schedules),
              'checks': ['rational construction before integrality', 'binary powers versus coefficient recurrence',
                         'zero diagonal equations', 'coefficient congruences', 'logarithmic divisibility',
                         'inverse and logarithmic recurrences', 'derivative identity', 'rational perturbation law',
                         'companion integrality', 'formal exponential reconstruction', 'excluded-index and noncoprime examples'],
              'initial_a_over_prime': [logarithm[index] // primes[index] for index in range(2, 13)],
              'scope': 'Finite coefficient identities; the all-index theorems have written proofs in note.tex.'}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
