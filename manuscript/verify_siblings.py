import json
from fractions import Fraction
from math import factorial, gcd

from verify import coefficient_power, coefficient_recurrence, logarithmic_coefficients, nth_primes


def construct_diagonal(schedule, slope, degree, diagonal):
    series = [Fraction(1), Fraction(slope)]
    targets = [0, 0]
    for index in range(2, degree + 1):
        exponent = schedule[index]
        powered = coefficient_recurrence(series, exponent, index)
        target = diagonal(index, exponent, powered)
        targets.append(target)
        series.append(target - powered[index] / exponent)
    return series, targets


def check_diagonal(schedule, slope, degree, diagonal):
    series, targets = construct_diagonal(schedule, slope, degree, diagonal)
    assert all(gcd(schedule[index], factorial(index)) == 1 for index in range(2, degree + 1))
    assert all(value.denominator == 1 for value in series)
    series = [int(value) for value in series]
    logarithm = logarithmic_coefficients(series, degree)
    for index in range(2, degree + 1):
        exponent = schedule[index]
        powered = coefficient_power(series, exponent, index)
        assert powered[index] == exponent * targets[index]
        assert (logarithm[index] - index * targets[index]) % exponent == 0
    return series, logarithm, targets


def complete_runs(values):
    runs = []
    length = 1
    for index in range(1, len(values)):
        if values[index] % 2 == values[index - 1] % 2:
            length += 1
        else:
            runs.append(length)
            length = 1
    return runs


def main():
    degree = 64
    primes = nth_primes(degree)
    shifted = lambda index, exponent, powered: powered[index - 1]
    series, logarithm, targets = check_diagonal(primes, 1, degree, shifted)
    expected_series = [1, 1, 2, 10, 82, 1610, 21103, 557487, 10593462, 339062614,
                       13734633778, 396036333970, 20579031011201, 876507655312569,
                       38770769823590773, 2095528583370973781, 129010872768620618787,
                       8461720386355980968547, 506790238377256700760459,
                       40023759959023038602678651, 2897244094881589021494018202]
    expected_logarithm = [1, 3, 25, 287, 7601, 116337, 3740017, 80014415, 2949026857,
                          133787267943, 4200083163057, 241983191914853,
                          11120075525056265, 530169345622378745, 30835220884142971385,
                          2029889748240816948527, 141614089508017106620961,
                          8967246922112275916862825, 750640275823651591748840329,
                          57132832447805992338691195027]
    expected_runs = [2, 4, 2, 4, 8, 2, 6, 4, 10, 6, 4, 2, 2, 2, 4, 4, 2, 2]
    assert series[:len(expected_series)] == expected_series
    assert logarithm[1:len(expected_logarithm) + 1] == expected_logarithm
    assert all(logarithm[index] % primes[index] == 0 for index in range(2, degree + 1))
    assert all(value % 2 == 1 for value in logarithm[1:])
    assert all(series[index] % 2 == series[index + 1] % 2 for index in range(0, degree, 2))
    runs = complete_runs(series)
    assert runs == expected_runs[:len(runs)]
    assert all(length % 2 == 0 for length in runs)
    assert logarithm[3] == 25 and primes[2] == 3 and logarithm[3] % primes[2] == 1
    family_degree = 24
    squares = [0, 0] + [primes[index] ** 2 for index in range(2, family_degree + 1)]
    diagonal_rules = [lambda index, exponent, powered: index * index - 7,
                      lambda index, exponent, powered: (-1) ** index * index,
                      lambda index, exponent, powered: exponent * (index + 1),
                      lambda index, exponent, powered: (-1) ** index * powered[index - 1]]
    for schedule in [primes, squares]:
        for slope in [-2, 0, 3]:
            for rule in diagonal_rules:
                check_diagonal(schedule, slope, family_degree, rule)
    result = {
        'status': 'ALL_CHECKS_OK',
        'arithmetic': 'exact integers and rational numbers',
        'shifted_indices': [2, degree],
        'source_data_matches': {'A393866': [0, 20], 'A393867': [1, 20]},
        'paired_parity_indices': [0, 63],
        'logarithmic_oddness_indices': [1, degree],
        'complete_run_lengths': runs,
        'printed_formula_counterexample': {
            'source': 'A393866 revision 17 FORMULA (2)',
            'index': 2, 'coefficient_x_squared_of_derivative_quotient': 25,
            'prime_at_index': 3, 'remainder': 1,
            'correct_coefficient_degree': 'n-1',
        },
        'inhomogeneous_family_count': 24,
        'inhomogeneous_indices': [2, family_degree],
        'congruence': 'a_n = n*d_n modulo m_n when [x^n]F^m_n = m_n*d_n',
        'scope': 'Finite coefficient identities; the all-index assertions have written proofs in note.tex.',
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
