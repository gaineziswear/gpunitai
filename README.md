# GpunitAI

GpunitAI is a decentralized, modular GPU aggregator and task orchestrator designed to harness and optimize GPU compute resources from various platforms like Colab, Vast.ai, OpenAI, DeepSeek, Meta, and others.

---

## Features

- **GPU Platform Integration**: Supports training and execution on Colab, Vast.ai, OpenAI, DeepSeek, and Meta platforms.
- **Quantum-Inspired Optimization**: Integrates publicly available quantum algorithms (cuQuantum, CUDA-Q, Qibo) to enhance compute efficiency.
- **Dynamic Load Balancing**: Automatically adjusts task routing to avoid overloading any single GPU platform.
- **Hashrate Optimization**: Targets high-performance computing output ranging from 1000 to 2500 MH/s using optimized parallelism.
- **Redis-based Task Queue**: Real-time job management and scheduling using Redis + RQ.
- **CLI & Web UI**: Launch and manage jobs either from a terminal or browser interface.
- **Dockerized**: Fully containerized environment for easy deployment.

---

## Architecture

```
User CLI / Web UI
        |
        v
  Task Queue (Redis + RQ)
        |
        v
 Task Router + Load Balancer
        |
        +--------------------+
        |        |           |
    Colab     Vast.ai     OpenAI ...
  (Notebook)  (Instance)   (API)
```

---

## Installation

```bash
# Clone the repo
git clone https://github.com/gaineziswear/gpunitai.git
cd gpunitai

# Setup environment variables
cp .env.template .env
nano .env  # insert your API keys and settings

# Start the system
bash startup.sh
```

---

## Quantum Algorithms

GpunitAI supports:
- **cuQuantum / CUDA-Q**: NVIDIA GPU-accelerated quantum simulation
- **Qibo**: Open-source framework for quantum circuit simulation

These are used in the `quantum_models/` directory to improve task resolution and simulation workloads.

---

## Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Create a Pull Request

---

## License

MIT License
