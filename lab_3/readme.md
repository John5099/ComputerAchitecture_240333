# Lab 3: VHDL Code for Combinational Circuits (Encoder and Decoder)

---

## Objective

- To design and simulate a **4-to-2 priority encoder** using VHDL.  
- To design and simulate a **2-to-4 decoder** using VHDL.  

---

## Theory

### Encoder

An encoder is a combinational logic circuit that converts \(2^n\) input lines into an **n-bit binary output**. At any instant, only one input is assumed to be active (HIGH).

A **4-to-2 encoder** consists of four inputs (I0–I3) and produces a 2-bit output (Y1, Y0).

A **priority encoder** is a modified encoder that resolves multiple active inputs by assigning priority to the highest-order input.

#### Truth Table (4-to-2 Priority Encoder)

| I3 | I2 | I1 | I0 | Y1 | Y0 |
|----|----|----|----|----|----|
| 0  | 0  | 0  | 1  | 0  | 0  |
| 0  | 0  | 1  | X  | 0  | 1  |
| 0  | 1  | X  | X  | 1  | 0  |
| 1  | X  | X  | X  | 1  | 1  |

---

### Decoder

A decoder is a combinational circuit that performs the reverse operation of an encoder by converting an **n-bit binary input** into one of \(2^n\) output lines.

A **2-to-4 decoder** has a 2-bit input (A1, A0) and four outputs (Y0–Y3). At any time, only one output is active based on the input combination.

#### Truth Table (2-to-4 Decoder)

| A1 | A0 | Y3 | Y2 | Y1 | Y0 |
|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | 1  |
| 0  | 1  | 0  | 0  | 1  | 0  |
| 1  | 0  | 0  | 1  | 0  | 0  |
| 1  | 1  | 1  | 0  | 0  | 0  |

---

## Output

### Encoder Output
<img width="1065" height="206" alt="encoder" src="https://github.com/user-attachments/assets/26c5b455-83aa-465a-b9b1-59879d450e2d" />


### Decoder Output
<img width="1003" height="259" alt="decoder" src="https://github.com/user-attachments/assets/b5c077e9-dfae-43c4-9a02-c812c93acccc" />



---

## Discussion

In this experiment, two combinational logic circuits, namely a **priority encoder** and a **decoder**, were designed and simulated using VHDL.

The priority encoder was able to identify the highest-priority active input and generate the corresponding binary output. The decoder successfully translated binary input data into the appropriate output line by activating only one output at a time.

The simulation outputs confirmed that both circuits operated as expected:
- The priority encoder correctly selected the highest active input when multiple inputs were present.
- The decoder produced the correct output for each binary input combination by enabling only the corresponding output line.

---

## Conclusion

This experiment provided practical knowledge of designing and implementing **combinational logic circuits using VHDL**.

The following objectives were successfully achieved:
- Implementation of a **4-to-2 priority encoder**
- Implementation of a **2-to-4 decoder**
- Verification of circuit operation through simulation using **GTKWave**

The simulation results matched the expected outputs, confirming the correct functioning of both circuits. The experiment also improved understanding of combinational circuit design and VHDL programming concepts.
