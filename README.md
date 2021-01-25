# A Regex for European Article Number
An [European Article Number][wikipedia:ean] (EAN) is

> a standard describing a barcode symbology and numbering system used in global trade to identify a specific retail product type, in a specific packaging configuration, from a specific manufacturer.

During a discussion at work about regexes, I made the claim that EANs can be accepted with a regular expression. This project demonstrates that claim.

## Plan
The plan of proof is as follows.

1. Create a [deterministic finite automaton][wikipedia:dfa] (DFA) that accept an EAN.
2. Convert the DFA into a regular expression.

The code in this project will take care of step 1. Step 2 will be delegated to [fsm2regex][].

[wikipedia:ean]: https://en.wikipedia.org/wiki/International_Article_Number
[wikipedia:dfa]: https://en.wikipedia.org/wiki/Deterministic_finite_automaton
[fsm2regex]: http://ivanzuzak.info/noam/webapps/fsm2regex/