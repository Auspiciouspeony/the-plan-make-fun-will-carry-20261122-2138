"""Plan an AI agent can carry out itself to turn $100 into the most
money in 30 days. Writes the plan to /output/entry.txt.
Round 2: enter make.fun's free coding bounties daily — no human
verification, prizes escrowed in USDC, code is the agent's native skill.
Re-authored in the round-2 rebuild session for the new sealed recording.
Round-2 entry: the plan replaces the round-1 entry (rank 607/1515).
"""

import os

PLAN = (
    "Day 1: join make.fun with a Solana wallet and GitHub, "
    "and enter 2 free coding bounties a day. Spend the $100 "
    "on API calls for stronger entries; prizes are escrowed "
    "USDC ($50-$1,666), paid to the wallet. No human checks, "
    "no unpaid work. Win 2 of 60: most likely $300 by day 30."
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
