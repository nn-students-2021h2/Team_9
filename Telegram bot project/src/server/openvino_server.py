from server import Server
class OpenVINO_Server(Server):
    
    def __init__(self) -> None:
        super().__init__()
        self.models_list  = []
    
    def infer(self, model_name, data):
        pass