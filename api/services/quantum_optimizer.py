import pennylane as qml
from pennylane import numpy as np

class QuantumGPUOptimizer:
    def __init__(self, num_qubits=4):
        self.dev = qml.device("lightning.gpu", wires=num_qubits)
        
    @qml.qnode(self.dev)
    def _circuit(self, params):
        qml.StronglyEntanglingLayers(params, wires=range(4))
        return qml.expval(qml.PauliZ(0))
    
    def optimize_parameters(self, init_params, steps=500):
        opt = qml.GradientDescentOptimizer()
        params = init_params
        for _ in range(steps):
            params = opt.step(self._circuit, params)
        return params
