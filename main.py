"""Write one money plan to /output/entry.txt.

The plan: a $49 same-day AI product-photo pack for Etsy sellers,
sold on Fiverr with direct outreach to shops whose photos are
visibly bad (pre-qualified buyers, already losing sales), delivered
in 2 hours with free tools, money-back guaranteed by the $100.
Most likely outcome, not the best case: 8-10 sales, about $450
by day 30. No network, no spend, deterministic output.
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
    """Write PLAN to /output/entry.txt, readable by every user."""
    assert 1 <= len(PLAN) <= 280, "plan must be 1-280 characters"
    assert PLAN.strip(), "plan must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    try:
        # Collection runs as another user: the folder must be
        # traversable too, not just the file inside it.
        os.chmod("/output", 0o755)
    except OSError:
        pass
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(PLAN)
    # The grader collects outputs as another user (uid 65534), so the
    # file must be world-readable: plain open() honours the umask, but
    # chmod explicitly to 0644 regardless of how the file was created.
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == PLAN, "written text differs from PLAN"


if __name__ == "__main__":
    main()
