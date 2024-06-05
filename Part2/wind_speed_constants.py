# Dataset processing
INSTANCES = 100
PAST_SAMPLES = 300
TRAIN_SET_SIZE = 0.7
DATE_COLUMNS = "DATE"

# Model configurations
EPOCHS = 25
BATCH_SIZE = INSTANCES
LEARNING_RATE_FUNCTION = lambda x: 1e-3 * 0.90 ** x # Exponential Decay Schedule

# File names
DATA_FILE = "wind_dataset.csv" 
PREDICTION_OUTPUT_FILE = "prediction_output.csv"
LOSS_FUNCTION_PLOT_FILE_NAME = "loss_plot.png"
PICKEL_FILE_NAME = "model.pkl"