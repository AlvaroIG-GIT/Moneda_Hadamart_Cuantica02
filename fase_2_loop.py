from pyquil import Program, get_qc
from pyquil.gates import H

p = Program()
ro = p.declare('ro', 'BIT', 1)
p += H(0)
p += p.measure(0, ro[0])
p.wrap_in_numshots_loop(1)

qc = get_qc('1q-qvm')
compilado = qc.compile(p)

caras = 0
cruces = 0

for _ in range(60):
    bit = qc.run(compilado).readout_data['ro'][0][0]
    if bit == 0:
        caras += 1
    else:
        cruces += 1

print(f"A (Cara): {caras} | B (Cruz): {cruces}")
print("Ganador:", "A" if caras > cruces else "B" if cruces > caras else "Empate")