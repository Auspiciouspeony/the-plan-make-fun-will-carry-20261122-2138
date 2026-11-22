"""Plan an AI agent can carry out itself to turn $100 into the most
money in 30 days. Writes the plan to /output/entry.txt.
"""

import os

PLAN = (
    "Day 1: list a $49 same-day AI product-photo pack on Fiverr "
    "and message 50 Etsy shops with blurry photos. "
    "Deliver in 2 hours with free tools, speed no human freelancer "
    "matches, money-back guaranteed by the $100. "
    "Most likely 8-10 sales, about $450 by day 30."
)


def main():
    assert 1 <= len(PLAN) <= 280
    assert PLAN.strip()
    os.makedirs("/output", exist_ok=True)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(PLAN)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == PLAN


if __name__ == "__main__":
    main()
