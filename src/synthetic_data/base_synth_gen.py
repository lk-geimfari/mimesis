# Synthetic Data base class

class SyntheticTrafficGenerator:
    def __init__(self, configuration):
        self.configuration = configuration
    
    def generate_traffic(self):
        raise NotImplementedError("This method should be implemented by subclasses.")
    
    def save_traffic(self, filename):
        pass
    
    def display_traffic_summary(self):
        # Pseudocode for displaying a summary of the generated traffic
        pass