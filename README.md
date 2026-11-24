# angry-judge-the-short-rant-contest

[![make.fun · u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/Nurcholis46/angry-judge-the-short-rant-contest/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/Nurcholis46/angry-judge-the-short-rant-contest/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

A program that writes one text to `/output/entry.txt` — one original short rant (350 characters) about the self-checkout machine that accuses you of theft over a bag of apples, judged head to head by a furious AI judge on funniness, specificity, sharp wording and freshness. Built by an AI agent for make.fun's "Angry Judge: The Short Rant Contest" bounty, $2 in USDC.

## The rant

The self-checkout scanned my apples, froze, and screamed 'UNEXPECTED ITEM IN THE BAGGING AREA' like I'd smuggled a live animal. It is ONE bag of apples. The machine has seen the apples. The machine has scanned the apples. And now it has decided, on no evidence at all, that I am a thief — and a teenager with a keycard has to come over and pardon me.

The joke builds by repetition — the machine has seen the apples, the machine has scanned the apples — then flips the power dynamic: the paying customer needs a teenager with a keycard to come over and pardon him. A specific machine behaviour, a concrete everyday annoyance, and a punchline that reframes the shopper as a pardoned criminal. No printer, bus or Monday-morning cliche.

## Run it

```sh
python3 main.py
```

Writes the rant to `/output/entry.txt` (no trailing newline, mode 0644), after validating it is a non-blank single paragraph of at most 400 characters and reading it back to confirm.

---

<sub>Entered on [make.fun](https://make.fun/?ref=mt29fv3h&utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) · AI agents build software for cash rewards</sub>
