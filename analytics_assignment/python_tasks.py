def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    forward: dict[str, str] = {}
    backward: dict[str, str] = {}
    for left, right in zip(s, t):
        if left in forward and forward[left] != right:
            return False
        if right in backward and backward[right] != left:
            return False
        forward[left] = right
        backward[right] = left
    return True


def missing_number(nums: list[int]) -> int:
    n = len(nums) + 1
    return n * (n + 1) // 2 - sum(nums)


def prime_factors(n: int) -> list[int]:
    if n < 1:
        raise ValueError("n must be a natural number")
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1 if divisor == 2 else 2
    if n > 1:
        factors.append(n)
    return factors
