import os
import subprocess
import numpy as np

# Simulation Settings
base_input_file = 'user_model.in'
permittivity_values = [3.0, 5.0, 8.0] # Alag-alag mitti (soil) ke types
output_dir = 'parametric_results'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def run_simulation(eps_value):
    # 1. Nayi input file banana specific permittivity ke saath
    new_filename = f"model_eps_{eps_value}.in"
    with open(base_input_file, 'r') as f:
        content = f.read()
    
    # Model ke andar permittivity value ko replace karna
    updated_content = content.replace('MATERIAL_EPS', str(eps_value))
    
    with open(new_filename, 'w') as f:
        f.write(updated_content)
    
    print(f"🚀 Running simulation for Eps: {eps_value}...")
    
    # 2. gprMax command chalana (Terminal command automation)
    subprocess.run(['python', '-m', 'gprMax', new_filename, '-n', '1'], check=True)
    
    print(f"✅ Simulation for {eps_value} finished!")

# Loop through all values
for eps in permittivity_values:
    run_simulation(eps)
