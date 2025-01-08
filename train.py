import numpy as np

def run_training_job():
    """Run a simple dummy training job."""
    print("Starting dummy training job...")

    try:
        # Replace this with your actual training script or command.
        result = np.array([1, 1]) + np.array([2, 3])
        
        print(result)
        return result 
        
    except:
        print(f"Training job failed ...")
        
   

if __name__ == "__main__":
    run_training_job()