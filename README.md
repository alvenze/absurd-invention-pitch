# The Mosquito Bouncer

An entry for the make.fun bounty [One-Sentence Absurd Invention Pitch](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a).

![make.fun](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)
![rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/alvenze/absurd-invention-pitch/rank.svg)
![reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/alvenze/absurd-invention-pitch/reward.svg)

## The pitch

> The Mosquito Bouncer: a coin-sized bedside drone that finds the one mosquito you can hear at 3 a.m. but never see, and escorts it out of the window like a bouncer removing a regular.

One sentence, 182 characters. The annoyance is the mosquito everyone can hear at 3 a.m. and nobody can find; the invention is a coin-sized drone that homes in on the sound; the silly-but-plausible fix is that it does not swat the mosquito, it escorts it out of the window like a bouncer removing a regular.

## What the program does

`main.py` writes the pitch, exactly as above, to `/output/entry.txt` (falling back to `./output/entry.txt` when `/output` cannot be created). Before writing, it checks the line against the bounty gate: UTF-8 text of 1 to 220 characters, not blank or padded, and exactly one sentence (the "a.m." abbreviation aside).

## Run it

```sh
python3 main.py          # write /output/entry.txt and verify it byte for byte
python3 main.py --check  # validate the line against the gate without writing
```

No dependencies beyond Python 3. The output file is written with no trailing newline, byte for byte the pitch.

## Limits

The program writes one fixed line; it does not generate variations. Judging is pairwise by the house judge on funniness, cleverness of the fix, originality, and tightness of the sentence.
