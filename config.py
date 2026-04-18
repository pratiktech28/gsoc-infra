# Simulation Constants
BASE_INPUT_FILE = 'user_model.in'
PERMITTIVITY_SWEEP = [3.0, 5.0, 8.0, 12.0] 
OUTPUT_DIR = 'parametric_results'

# Physics Parameters
TIME_STEP = 1.0e-11 # dt value
RECEIVER_COMPONENT = 'Ez' # Signal component to analyze

# Database Settings
DB_NAME = f"{OUTPUT_DIR}/simulations.db"
LOG_FILE = f"{OUTPUT_DIR}/summary.txt"

# Thresholds for Validation 
NRMSE_THRESHOLD = 0.01

# Visualization Settings
PLOT_FILENAME = f"{OUTPUT_DIR}/analysis.png"
DPI_QUALITY = 300
