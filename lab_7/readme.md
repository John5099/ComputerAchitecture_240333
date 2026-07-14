# Lab 7: VHDL Code for Sequential Circuits — Flip-Flops


---

## Objective

- To design and simulate SR, D, JK, and T flip-flops in VHDL.
- To understand the role of the clock signal in sequential circuits.

---

## Theory

A flip-flop is a bistable sequential element that stores one bit of state. Unlike combinational circuits, the output of a flip-flop depends on both the current inputs **and** its previous state. All flip-flops in this lab are triggered on the **rising edge** of the clock signal.

---

### SR Flip-Flop

The SR flip-flop has two inputs: Set (S) and Reset (R). The forbidden state occurs when both S and R are HIGH simultaneously.

| S | R | Q (next)       |
|---|---|----------------|
| 0 | 0 | Q (no change)  |
| 0 | 1 | 0 (reset)      |
| 1 | 0 | 1 (set)        |
| 1 | 1 | X (forbidden)  |

---

### D Flip-Flop

The D flip-flop captures the value of input D on every rising clock edge. It eliminates the forbidden state of the SR flip-flop.

```
Q(next) = D
```

---

### JK Flip-Flop

The JK flip-flop eliminates the forbidden state of the SR flip-flop. When J = K = 1, the output **toggles**.

```
Q(next) = J·Q' + K'·Q
```

| J | K | Q (next)      |
|---|---|---------------|
| 0 | 0 | Q (no change) |
| 0 | 1 | 0 (reset)     |
| 1 | 0 | 1 (set)       |
| 1 | 1 | Q' (toggle)   |

---

### T Flip-Flop

The T (Toggle) flip-flop toggles its output when T = 1 and holds its state when T = 0.

```
Q(next) = T ⊕ Q
```

| T | Q (next)      |
|---|---------------|
| 0 | Q (no change) |
| 1 | Q' (toggle)   |

---

## Output

The waveform was loaded in GTKWave. The clock signal and all flip-flop inputs and outputs were appended and the display was zoomed to fit.

![GTKWave Simulation Output](flipflops.png)

**Observation:** All four flip-flops operated as expected according to their input conditions at each rising clock edge. The SR flip-flop successfully performed the set and reset operations without entering the invalid state. The D flip-flop accurately stored the input value on every rising edge of the clock. The JK flip-flop correctly toggled its output whenever both J and K were set to 1. The T flip-flop changed its state on each rising edge when T = 1 and maintained its previous state when T = 0. In every case, the complementary output (QB) remained the inverse of Q.

---

## Discussion and Conclusion

This lab focused on the implementation and simulation of four basic sequential circuit elements—SR, D, JK, and T flip-flops—using Behavioral modeling in VHDL. Each flip-flop was designed with a rising-edge-triggered clock and an internal signal to generate the Q and QB outputs. A unified testbench, featuring a clock generation process and sequential input stimuli, was used to validate the functionality of all valid input combinations. The simulation results observed in GTKWave verified the correct operation of each flip-flop, including set, reset, hold, and toggle functions. Overall, the lab provided a solid foundation in the design and analysis of synchronous sequential circuits, which is essential for developing more advanced digital systems such as registers, counters, and finite state machines in future experiments.
