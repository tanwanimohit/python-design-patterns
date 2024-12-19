class CPU:
    
    def power_on(self):
        print("Turning on the CPU")
        
    def cpu_ready(self):
        print("CPU is ready!")
        
class Memory:
    
    def init_memory(self):
        print("Initializing the memory")
        
class GPU:
    
    def enable_gpu(self):
        print("GPU graphics enabled.")
        
class IO:
    
    def attach_io(self):
        print("Attaching all I/Os")
        
class Network:
    
    def connect_networks(self):
        print("Networking enabled.")
        
class ComputerFacade:
    
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.gpu = GPU()
        self.io = IO()
        self.network = Network()
        
    def start_computer(self):
        self.cpu.power_on()
        self.memory.init_memory()
        self.gpu.enable_gpu()
        self.io.attach_io()
        self.network.connect_networks()
        self.cpu.cpu_ready()
        print("Computer is ready to Use.") 
        
if __name__ == "__main__":
    computer = ComputerFacade()
    computer.start_computer()