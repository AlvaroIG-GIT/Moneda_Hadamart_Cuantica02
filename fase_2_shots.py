from pyquil import Program, get_qc
from pyquil.gates import H

p = Program()
ro = p.declare('ro', 'BIT', 1)
p += H(0)
p += p.measure(0, ro[0])
p.wrap_in_numshots_loop(60)

qc = get_qc('1q-qvm')
tiradas = qc.run(qc.compile(p)).readout_data['ro'].flatten()

caras = (tiradas == 0).sum()
cruces = (tiradas == 1).sum()

print(f"Tiradas: {tiradas}")
print(f"A (Cara): {caras} | B (Cruz): {cruces}")
print("Ganador:", "A" if caras > cruces else "B" if cruces > caras else "Empate")