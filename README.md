# A Regex for European Article Number
An [European Article Number][wikipedia:ean] (EAN) is

> a standard describing a barcode symbology and numbering system used in global trade to identify a specific retail product type, in a specific packaging configuration, from a specific manufacturer.

During a discussion at work about regexes, I made the claim that EANs can be accepted with a regular expression. This project demonstrates that claim.

## Plan
The plan of proof is as follows.

1. Create a [deterministic finite automaton][wikipedia:dfa] (DFA) that accept an EAN.
2. Convert the DFA into a regular expression.

The code in this project will take care of both steps.

### DFA
Generate a DFA that accepts an EAN of length `n` with the following command

```bash
python3 dfa.py <n>
```

For example a DFA that accepts EANs of length 2 is

```plain
#states
s0
s1
s2
s3
s4
s5
s6
s7
s8
s9
s10
s11
s12
s13
s14
s15
s16
s17
s18
s19
s20
#initial
s0
#accepting
s11
#alphabet
0
1
2
3
4
5
6
7
8
9
#transitions
s0:0>s1
s0:1>s4
s0:2>s7
s0:3>s10
s0:4>s3
s0:5>s6
s0:6>s9
s0:7>s2
s0:8>s5
s0:9>s8
s1:0>s11
s1:1>s12
s1:2>s13
s1:3>s14
s1:4>s15
s1:5>s16
s1:6>s17
s1:7>s18
s1:8>s19
s1:9>s20
s2:0>s12
s2:1>s13
s2:2>s14
s2:3>s15
s2:4>s16
s2:5>s17
s2:6>s18
s2:7>s19
s2:8>s20
s2:9>s11
s3:0>s13
s3:1>s14
s3:2>s15
s3:3>s16
s3:4>s17
s3:5>s18
s3:6>s19
s3:7>s20
s3:8>s11
s3:9>s12
s4:0>s14
s4:1>s15
s4:2>s16
s4:3>s17
s4:4>s18
s4:5>s19
s4:6>s20
s4:7>s11
s4:8>s12
s4:9>s13
s5:0>s15
s5:1>s16
s5:2>s17
s5:3>s18
s5:4>s19
s5:5>s20
s5:6>s11
s5:7>s12
s5:8>s13
s5:9>s14
s6:0>s16
s6:1>s17
s6:2>s18
s6:3>s19
s6:4>s20
s6:5>s11
s6:6>s12
s6:7>s13
s6:8>s14
s6:9>s15
s7:0>s17
s7:1>s18
s7:2>s19
s7:3>s20
s7:4>s11
s7:5>s12
s7:6>s13
s7:7>s14
s7:8>s15
s7:9>s16
s8:0>s18
s8:1>s19
s8:2>s20
s8:3>s11
s8:4>s12
s8:5>s13
s8:6>s14
s8:7>s15
s8:8>s16
s8:9>s17
s9:0>s19
s9:1>s20
s9:2>s11
s9:3>s12
s9:4>s13
s9:5>s14
s9:6>s15
s9:7>s16
s9:8>s17
s9:9>s18
s10:0>s20
s10:1>s11
s10:2>s12
s10:3>s13
s10:4>s14
s10:5>s15
s10:6>s16
s10:7>s17
s10:8>s18
s10:9>s19
```

## Regular Expression
Eliminating states will convert DFA into a regular expression. Since our DFA is well structured eleminiating states can be done per level.

[wikipedia:ean]: https://en.wikipedia.org/wiki/International_Article_Number
[wikipedia:dfa]: https://en.wikipedia.org/wiki/Deterministic_finite_automaton
[fsm2regex]: http://ivanzuzak.info/noam/webapps/fsm2regex/