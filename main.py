#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue.

Writes the monologue to /output/entry.txt for the make.fun judge.
The speaker is Malachar, Tithe-Keeper of the nine valleys: a villain with
a scheme (the tithe, the raising) and a history (the dragon, the
stablemaster, the barons), whose tiredness lives in the pauses and the
deflections, never in a plain announcement.
"""
import os

MONOLOGUE = (
    "The nine valleys run on paperwork now. I signed the tithe in triplicate "
    "before breakfast, in blood, and by noon the western barons were haggling "
    "over grain like fishwives. I have a dragon. It sleeps in the east vault "
    "on invoices because the stablemaster quit. Again. Tonight I raise the "
    "dead, third Tuesday; half of them look more rested than I do. The hero "
    "comes at dawn, sword shining. I have left the gate unlocked. Let him "
    "climb the stairs. I will be in the library, feet up. Some villains want "
    "the world. I want a nap and a quiet Tuesday."
)


def main():
    os.makedirs("/output", exist_ok=True)
    text = MONOLOGUE.strip()
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
