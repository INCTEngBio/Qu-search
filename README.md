# Qu-Search: Pure Quantum Sequence Search via Grover Amplitude Amplification

**QuSearch** (integrated with QuBio) is an open-source quantum bioinformatics pipeline engineered to identify biological target sequences within an \\(n\\)-qubit Hilbert space. Operating as an end-to-end quantum search primitive, the algorithm integrates uniform superposition initialization, orthogonal single-qubit nucleotide mapping, a phase-kickback biological oracle with exact Hermitian uncomputation, and iterative Grover diffusion executed on the Qiskit Aer simulator.

---

## 🧬 Key Features

* **Canonical Orthogonal Nucleotide Encoding:** Direct mapping of biological nitrogenous bases into discrete, distinguishable single-qubit states:
  * **Adenine (A):** \\(|0\rangle\\) (Ground computational state / `pass`)
  * **Thymine (T):** \\(|1\rangle\\) (Bit-flip via Pauli-\\(X\\) gate)
  * **Cytosine (C):** \\(|+\rangle\\) (Equal superposition via Hadamard \\(H\\) gate)
  * **Guanine (G):** \\(|-\rangle\\) (Phase superposition via Pauli-\\(X\\) followed by Hadamard \\(H\\) gate)

* **Biological Target Oracle with Exact Uncomputation:**
  * **Pre-computation:** Rotates arbitrary candidate target motifs (e.g., benchmark sequences from *JCVI-Syn3.0*) into the all-ones activation basis \\(|11\dots 1\rangle\\).
  * **Phase Kickback:** Inverts the quantum phase of the marked target state using an \\((n-1)\\)-controlled NOT gate (`MCXGate`) conjugated by Hadamard gates on the target register.
  * **Hermitian Uncomputation:** Executes mirrored gate reversal (\\(U_{\text{oracle}}^\dagger\\)) across data registers to eliminate entanglement artifacts, insulate qubits against phase leakage, and preserve quantum state coherence.

* **Quantum Diffusion Operator (\\(U_s\\)):** Implements the full inversion-about-the-mean operator (\\(U_s = 2|s\rangle\langle s| - I\\)) utilizing uniform Hadamard transformations, Pauli-\\(X\\) reflections, and multi-controlled phase gates.

* **Multi-Iteration Simulation Engine:** Evaluates quantum state evolution across sequential iteration steps (\\(k = 1\\) to `MAX_ITER = 5`), capturing empirical amplitude amplification and constructive interference across 1,024 shots per iteration on the `qasm_simulator`.

* **Automated Visual Analytics:** Generates publication-ready diagnostic plots:
  * **Grover Amplification Curve:** Demonstrates the empirical probability trajectory of measuring the biological target as a function of iteration count.
  * **State Frequency Distribution:** Visualizes the shot distribution across all measured computational basis states at peak iteration depth.
---

## 📦 Requirements and Dependencies

* **Python 3.8+**
* [Qiskit](https://qiskit.org/) (`qiskit >= 0.45.0` or `1.0+`)
* [Qiskit Aer](https://github.com/Qiskit/qiskit-aer) (`qiskit-aer`)
* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)

---

## 💻 Installation and Execution

1. **Clone the repository:**
   ```bash
   git clone [suspicious link removed]
   cd QuSearch
hitecture
