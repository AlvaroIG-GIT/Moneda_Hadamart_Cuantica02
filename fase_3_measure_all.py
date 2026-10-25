from pyquil import Program, get_qc
from pyquil.gates import H

p = Program()
for q in range(6):
    p += H(q)
p.measure_all()
p.wrap_in_numshots_loop(25)

qc = get_qc('9q-generic-qvm')
matriz = qc.run(qc.compile(p)).readout_data['ro']

caras = (matriz == 0).sum()
cruces = (matriz == 1).sum()

print("Matriz (25x6):\n", matriz)
print(f"A (Cara): {caras} | B (Cruz): {cruces}")
print("Ganador:", "A" if caras > cruces else "B" if cruces > caras else "Empate")