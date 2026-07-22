from analytics_assignment.calculations import (
    car_arrival_probability,
    comma_decimal,
    expected_distinct_species,
    expected_double_winners,
    pearson_correlation,
    roc_auc,
)


def main() -> None:
    labels = [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0]
    scores = [0.95, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25]
    cups = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
    exam_scores = [85, 88, 79, 81, 84, 65, 67, 58, 76, 49]
    print("Блок 1.1:", comma_decimal(expected_distinct_species(), 2))
    print("Блок 1.2:", comma_decimal(expected_double_winners(), 1))
    print("Блок 1.3:", f"{comma_decimal(car_arrival_probability(0.95, 30, 10) * 100, 1)}; {comma_decimal(car_arrival_probability(0.95, 30, 27) * 100, 1)}")
    print("Блок 5.2:", comma_decimal(roc_auc(labels, scores), 2))
    print("Блок 5.3:", comma_decimal(pearson_correlation(cups, exam_scores), 2))


if __name__ == "__main__":
    main()
