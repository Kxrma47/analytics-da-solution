from math import sqrt


def expected_distinct_species(species_count: int = 6, visits: int = 6) -> float:
    return species_count * (1 - ((species_count - 1) / species_count) ** visits)


def expected_double_winners(chef_count: int = 80) -> float:
    strongest_opponents = chef_count - 1
    return sum((weaker_count / strongest_opponents) ** 2 for weaker_count in range(chef_count))


def car_arrival_probability(period_probability: float, period_minutes: int, target_minutes: int) -> float:
    return 1 - (1 - period_probability) ** (target_minutes / period_minutes)


def roc_auc(labels: list[int], scores: list[float]) -> float:
    positives = [score for label, score in zip(labels, scores) if label == 1]
    negatives = [score for label, score in zip(labels, scores) if label == 0]
    wins = 0.0
    for positive in positives:
        for negative in negatives:
            if positive > negative:
                wins += 1.0
            elif positive == negative:
                wins += 0.5
    return wins / (len(positives) * len(negatives))


def pearson_correlation(xs: list[float], ys: list[float]) -> float:
    x_mean = sum(xs) / len(xs)
    y_mean = sum(ys) / len(ys)
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
    x_sum = sum((x - x_mean) ** 2 for x in xs)
    y_sum = sum((y - y_mean) ** 2 for y in ys)
    return numerator / sqrt(x_sum * y_sum)


def comma_decimal(value: float, digits: int) -> str:
    return f"{value:.{digits}f}".replace(".", ",")
