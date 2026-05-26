
# Lab 2:  VHDL Code for Realizing Logic Gates

## Objective

- Design and implement structural/behavioral VHDL code for all fundamental logic gates: AND, OR, NOT, NAND, NOR, XOR, and XNOR.
- Simulate the circuit behaviors and validate their corresponding truth tables using GTKWave.

---

## Theory 

Logic gates serve as the foundational structural elements of modern digital systems. Each gate processes binary input variables to yield a deterministic single-bit output based on Boolean algebra.

| Gate Type | VHDL Operator |     Boolean Expression      |
| :-------- | :-----------: | :-------------------------: |
| AND       |     `and`     |       $Y = A \cdot B$       |
| OR        |     `or`      |         $Y = A + B$         |
| NOT       |     `not`     |        $Y = \bar{A}$        |
| NAND      |    `nand`     | $Y = \overline{A \cdot B}$  |
| NOR       |     `nor`     |   $Y = \overline{A + B}$    |
| XOR       |     `xor`     |      $Y = A \oplus B$       |
| XNOR      |    `xnor`     | $Y = \overline{A \oplus B}$ |

---

## Expected Truth Table

| Input A | Input B | AND | OR  | NOT A | NAND | NOR | XOR | XNOR |
| :-----: | :-----: | :-: | :-: | :---: | :--: | :-: | :-: | :--: |
|    0    |    0    |  0  |  0  |   1   |  1   |  1  |  0  |  1   |
|    0    |    1    |  0  |  1  |   1   |  1   |  0  |  1  |  0   |
|    1    |    0    |  0  |  1  |   0   |  1   |  0  |  1  |  0   |
|    1    |    1    |  1  |  1  |   0   |  0   |  0  |  0  |  1   |

---

## Simulation Output

The generated Value Change Dump (`.vcd`) file was visualized using GTKWave to confirm timing accuracy and signal transitions.
<img width="1307" height="323" alt="output" src="https://github.com/user-attachments/assets/b1190924-f916-4b29-8a18-d6a08844278a" />

---

## Discussion and Conclusion

The VHDL code for all seven basic logic gates was successfully compiled, executed, and verified. By tracking the runtime waveform transitions inside the GTKWave environment, the functional behavioral integrity of the underlying hardware blocks was validated against theoretical Boolean models. This establishes a verified baseline for constructing complex combinational and sequential sub-systems in subsequent lab modules.
```
