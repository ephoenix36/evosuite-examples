#!/usr/bin/env python3
"""
Basic EvoSuite optimization example.

This example demonstrates the core concepts of EvoSuite:
1. Loading configuration
2. Discovering and using plugins
3. Running a simple optimization loop
"""

import asyncio
from pathlib import Path

try:
    from evosuite import load_agent_os_config, AgentCoordinator
    from evosuite.plugins import Evaluator, Mutator
except ImportError:
    print("EvoSuite core not installed. Run: pip install evosuite-core")
    exit(1)

try:
    import pkg_resources
except ImportError:
    print("pkg_resources not available. Plugin discovery may not work.")
    pkg_resources = None


async def discover_plugins():
    """Discover available plugins."""
    if not pkg_resources:
        return {}
    
    plugins = {}
    for entry_point in pkg_resources.iter_entry_points('evosuite.plugins'):
        try:
            plugin_class = entry_point.load()
            plugin_instance = plugin_class()
            plugins[entry_point.name] = plugin_instance
            print(f"✅ Loaded plugin: {entry_point.name}")
        except Exception as e:
            print(f"❌ Failed to load plugin {entry_point.name}: {e}")
    
    return plugins


async def basic_optimization():
    """Run a basic optimization example."""
    print("🚀 Starting EvoSuite Basic Optimization Example")
    
    # Load configuration
    config = load_agent_os_config(Path.cwd())
    print(f"📋 Loaded config from: {config.get('_provenance', [])}")
    
    # Discover plugins
    plugins = await discover_plugins()
    
    # Find evaluator and mutator plugins
    evaluator = None
    mutator = None
    
    for name, plugin in plugins.items():
        if isinstance(plugin, Evaluator):
            evaluator = plugin
            print(f"🎯 Using evaluator: {name}")
        elif isinstance(plugin, Mutator):
            mutator = plugin
            print(f"🔀 Using mutator: {name}")
    
    if not evaluator:
        print("⚠️  No evaluator plugin found. Install evosuite-plugins-official")
        return
    
    if not mutator:
        print("⚠️  No mutator plugin found. Install evosuite-plugins-official")
        return
    
    # Simple optimization loop
    print("\n🔄 Starting optimization loop...")
    
    # Initial population
    population = ["candidate_1", "candidate_2", "candidate_3"]
    
    for generation in range(3):
        print(f"\n--- Generation {generation + 1} ---")
        
        # Evaluate population
        evaluated = []
        for candidate in population:
            result = await evaluator.evaluate(candidate, {"generation": generation})
            evaluated.append((candidate, result["total_score"]))
            print(f"Evaluated '{candidate}': score = {result['total_score']:.2f}")
        
        # Sort by fitness (higher is better)
        evaluated.sort(key=lambda x: x[1], reverse=True)
        best_candidate, best_score = evaluated[0]
        
        print(f"🏆 Best candidate: '{best_candidate}' (score: {best_score:.2f})")
        
        # Generate new population through mutation
        new_population = [best_candidate]  # Keep best
        
        for i in range(len(population) - 1):
            mutated = await mutator.mutate(best_candidate, {"generation": generation})
            new_population.append(mutated)
        
        population = new_population
        print(f"📝 New population: {population}")
    
    print(f"\n🎉 Optimization complete! Final best: '{best_candidate}'")


if __name__ == "__main__":
    asyncio.run(basic_optimization())