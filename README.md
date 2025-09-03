# EvoSuite Examples

This repository contains examples, scenarios, notebooks, and educational templates for the EvoSuite evolutionary optimization framework.

## Structure

```
examples/
├── getting-started/          # Basic usage tutorials
├── notebooks/               # Jupyter notebooks with interactive examples
├── scenarios/               # Complete optimization scenarios
├── benchmarks/              # Performance benchmarks and comparisons
└── templates/               # Project templates for common use cases
```

## Quick Start

1. Install EvoSuite core and desired plugins:
```bash
pip install evosuite-core evosuite-plugins-official evosuite-providers[openai]
```

2. Run a basic example:
```bash
cd getting-started
python basic_optimization.py
```

3. Explore Jupyter notebooks:
```bash
pip install jupyter
jupyter notebook notebooks/
```

## Examples Index

### Getting Started
- `basic_optimization.py` - Simple optimization loop
- `configuration_layers.py` - Using layered configuration
- `plugin_discovery.py` - Working with plugins

### Scenarios
- `code_optimization/` - Optimizing code quality metrics
- `ml_hyperparams/` - Machine learning hyperparameter tuning
- `business_process/` - Business process optimization

### Advanced
- `custom_plugins/` - Building custom evaluators and mutators
- `multi_objective/` - Multi-objective optimization
- `distributed/` - Distributed optimization across multiple nodes

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new examples.