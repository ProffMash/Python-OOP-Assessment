class Engine:
    def start(self):
        print("Engine has started.")

    def stop(self):
        print("Engine has stopped.")

class Car:
    def __init__(self):
        # Composition: Car has an Engine
        self.engine = Engine()

    def start_engine(self):
        # Use the Engine's start method
        self.engine.start()

    def stop_engine(self):
        # Use the Engine's stop method
        self.engine.stop()

# Demonstrating composition
my_car = Car()

# Start and stop the engine through the Car class
my_car.start_engine()  # Output: Engine has started.
my_car.stop_engine()   # Output: Engine has stopped.
