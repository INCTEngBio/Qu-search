### ==========================================================
### QUBIO + QUSEARCH - Integrated High-Impact Version
### ==========================================================

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.circuit.library import MCXGate
import matplotlib.pyplot as plt
import numpy as np
import math

# 1. Dataset Preparation [3]
target_sequence = 'GCAGCAGACTTTCGGTCGTGGCGGCCAGCACCAGTGCATCTACTGCGTGG'
database_sequence = '...' # Genoma JCVI-Syn3.0

# 2. Codificação Ortogonal das Bases [1]
def encode_nucleotide(qc, qubit, nucleotide):
    if nucleotide == 'A': pass
    elif nucleotide == 'T': qc.x(qubit)
    elif nucleotide == 'C': qc.h(qubit)
    elif nucleotide == 'G': qc.x(qubit); qc.h(qubit)

# 3. Oráculo Avançado com Pre-compute e Uncompute [2]
def nucleotide_oracle(qc, qubits, target):
    n = len(qubits)
    # Pre-compute
    for i, base in enumerate(target):
        if base == 'A': qc.x(qubits[i])
        elif base == 'C': qc.h(qubits[i]); qc.x(qubits[i])
        elif base == 'G': qc.h(qubits[i])
    # Phase Kickback
    qc.h(qubits[-1]); qc.append(MCXGate(n-1), qubits); qc.h(qubits[-1])
    # Uncompute
    for i, base in enumerate(target):
        if base == 'A': qc.x(qubits[i])
        elif base == 'C': qc.x(qubits[i]); qc.h(qubits[i])
        elif base == 'G': qc.h(qubits[i])

# 4. Operador de Difusão de Grover [2]
def diffuser(qc, n):
    qubits = list(range(n))
    qc.h(qubits); qc.x(qubits)
    qc.h(qubits[-1]); qc.append(MCXGate(n-1), qubits); qc.h(qubits[-1])
    qc.x(qubits); qc.h(qubits)

# 5. Workflow de Execução e Coleta de Dados para os Gráficos
sample_target = target_sequence[:4] # Amostra de 4 bases
n_qubits = len(sample_target)
MAX_ITER = 5
backend = Aer.get_backend('qasm_simulator')

iteration_probs = []
final_counts = {}

for it in range(1, MAX_ITER + 1):
    qc = QuantumCircuit(n_qubits)
    qc.h(range(n_qubits)) # Superposição inicial
    
    for _ in range(it):
        nucleotide_oracle(qc, list(range(n_qubits)), sample_target)
        diffuser(qc, n_qubits)
    
    qc.measure_all()
    t_qc = transpile(qc, backend)
    result = backend.run(t_qc, shots=1024).result()
    counts = result.get_counts()
    
    # Salva a probabilidade do melhor resultado (maior frequência) para o Gráfico 1
    max_prob = max(counts.values()) / 1024
    iteration_probs.append(max_prob)
    
    # Salva os dados da última iteração para o Gráfico 2
    if it == MAX_ITER:
        final_counts = counts

### ==========================================================
### 6. Visualização Integrada
### ==========================================================

# GRÁFICO 1: Curva de Probabilidade (Original do QuBio) [4]
plt.figure(figsize=(10, 5))
plt.plot(range(1, MAX_ITER + 1), iteration_probs, marker='o', linestyle='-', color='b')
plt.title(f"Grover Amplification Curve - Target: {sample_target}")
plt.xlabel("Number of Grover Iterations")
plt.ylabel("Probability of Measuring the Target")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# GRÁFICO 2: Histograma de Frequências (Original do QuSearch) [5]
plt.figure(figsize=(12, 6))
plt.bar(final_counts.keys(), final_counts.values(), color='teal')
plt.title(f"QuSearch Frequency Distribution (at Iteration {MAX_ITER})")
plt.xlabel("Quantum States (Nucleotide Mappings)")
plt.ylabel("Frequency (Shots)")
plt.xticks(rotation=45)
plt.show()

print(f"Análise concluída para o alvo: {sample_target}")
for i, p in enumerate(iteration_probs, 1):
    print(f"Iteração {i}: Probabilidade = {p:.3f}")