# Lab 8: VHDL Code for Sequential Circuits — Counters
---
## Objective

- To design and simulate a 4-bit synchronous up counter in VHDL.
- To design and simulate a 4-bit synchronous up/down counter in VHDL.

---

## Theory

A counter is a sequential circuit that cycles through a predefined sequence of states on each clock edge. Counters are built from flip-flops and are fundamental to timing, sequencing, and frequency division.

| Term | Description |
|------|-------------|
| **Synchronous Counter** | All flip-flops are clocked simultaneously — faster and more reliable than ripple (asynchronous) counters. |
| **Up Counter** | Increments the count by 1 on each rising clock edge. |
| **Up/Down Counter** | Increments or decrements based on a direction control signal (`UP`). |
| **Reset** | An active-high synchronous reset returns the count to zero on the next rising clock edge. |

A 4-bit counter cycles through values 0 to 15 (0000 to 1111 in binary). On reaching 15, an up counter wraps back to 0 on the next clock edge. Similarly, a down counter wraps from 0 back to 15.

Both counters in this lab use the `NUMERIC_STD` library to perform unsigned arithmetic on an internal `unsigned` signal, which is then converted back to `std_logic_vector` for the output port.

---

## Output

The waveform was loaded in GTKWave. Signals `CLK`, `RST`, `UP`, `COUNT_UP`, and `COUNT_UD` were appended and COUNT signals were displayed in decimal format.

![GTKWave Simulation Output](image.png)

**Observation:** The up counter incremented from 0 to 15 continuously, wrapping back to 0 after each overflow. The up/down counter incremented correctly when `UP = '1'` and decremented correctly when `UP = '0'`. Both counters reset to 0 immediately on the next rising clock edge when `RST = '1'`, confirming correct synchronous reset behavior.

---

## Discussion and Conclusion

This lab demonstrated the design and simulation of two 4-bit synchronous counters in VHDL using the Behavioral modeling style. The up counter incremented its internal unsigned count on every rising clock edge, while the up/down counter used a direction control signal to switch between incrementing and decrementing modes. Both designs used a synchronous active-high reset to return the count to zero. The `NUMERIC_STD` library enabled clean arithmetic operations on `unsigned` signals with straightforward conversion to `std_logic_vector` for output. The GTKWave waveform confirmed correct counting, direction control, overflow wrapping, and reset behavior for both counters. This lab reinforced the practical application of sequential VHDL design and provided a foundation for building more complex state machines and timing circuits.
