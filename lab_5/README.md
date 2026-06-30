# Lab 5: VHDL Code for Combinational Circuits: Comparator



## Objectives

The primary goals of this laboratory exercise are to:

- Design, code, and simulate a 2-bit magnitude comparator using VHDL.
- Translate theoretical Boolean equations into hardware-level VHDL constructs (Dataflow/Behavioral modeling).
- Understand the underlying hardware architecture required for binary comparison operations.
- Verify the functional correctness of the design using waveform analysis and truth table validation.

---

## Theory

A magnitude comparator is a combinational circuit that compares two binary numbers and determines their relationship. For two 2-bit inputs **A = A1A0** and **B = B1B0**, the comparator produces three mutually exclusive output signals:

| Output | Condition | Description |
|--------|-----------|-------------|
| **EQ** | A = B | HIGH when both inputs are equal |
| **GT** | A > B | HIGH when A is greater than B |
| **LT** | A < B | HIGH when A is less than B |

The Boolean expressions for each output are:

```
EQ = (A1 ⊕ B1)' · (A0 ⊕ B0)'
GT = A1·B1' + (A1 ⊕ B1)' · A0·B0'
LT = A1'·B1 + (A1 ⊕ B1)' · A0'·B0
```

In VHDL, the comparator is implemented using the **Behavioral** modeling style with a `process` block and `if-elsif-else` statements. The `NUMERIC_STD` library is used to cast `std_logic_vector` inputs to `unsigned` type, enabling direct arithmetic comparison using standard relational operators (`=`, `>`, `<`).

### Expected Truth Table

| A  | B  | EQ | GT | LT |
|----|----|----|----|----|
| 00 | 00 |  1 |  0 |  0 |
| 01 | 00 |  0 |  1 |  0 |
| 00 | 01 |  0 |  0 |  1 |
| 10 | 11 |  0 |  0 |  1 |
| 11 | 10 |  0 |  1 |  0 |
| 11 | 11 |  1 |  0 |  0 |

---




![Output of comparator](image.png)
_Figure 1: Simulation waveform demonstrating the comparator's response to varying 2-bit inputs._

**Key Observations from Waveforms:**

- The outputs **EQ, GT,** and **LT** are strictly mutually exclusive; exactly one output is HIGH for any given input state.
- Transitions between states occur cleanly without glitches, confirming proper combinational logic synthesis.
- The simulated outputs perfectly match the theoretical truth table and the expected testbench assertions.

---

## Discussion

In this lab, we successfully modeled a 2-bit comparator in VHDL. The exercise highlighted several critical concepts in digital design:

1. **Hardware Mapping:** It demonstrated how abstract mathematical equations are directly mapped to logic gates (AND, OR, NOT, XNOR) during the synthesis process, or how behavioral `if-else` statements translate to multiplexer trees in hardware.
2. **Mutual Exclusivity:** The logic ensures that the three output states form a "one-hot" encoded result, which is crucial for downstream digital systems to avoid conflicting control signals.
3. **Scalability:** While this lab focused on a 2-bit design, the hierarchical nature of VHDL allows these 2-bit blocks to be cascaded to create 4-bit, 8-bit, or 32-bit comparators (similar to the 74LS85 IC).

---

## Conclusion 

This experiment reinforced the foundational role of **combinational logic** in digital systems. By designing and verifying a magnitude comparator, we gained practical experience in VHDL coding, testbench creation, and waveform analysis.


