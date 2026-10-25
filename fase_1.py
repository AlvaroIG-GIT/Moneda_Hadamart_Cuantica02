from pyquil import Program, get_qc
from pyquil.gates import H

p = Program()
ro = p.declare('ro', 'BIT', 1)
p += H(0)
p += p.measure(0, ro[0])
p.wrap_in_numshots_loop(1)

qc = get_qc('1q-qvm')
resultado = qc.run(qc.compile(p)).readout_data['ro'][0][0]

nombre = "Cara" if resultado == 0 else "Cruz"
print(f"Resultado: {resultado} ({nombre})")