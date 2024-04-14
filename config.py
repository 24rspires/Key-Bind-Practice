from json import dumps, loads
from xbox_controller import XboxButtons, XboxMotions


class Config:
    def __init__(self,
                buttonBindings : dict[str, str] = {f'command{button}' : button for button in [mapping.name for mapping in list(XboxButtons)]},
                motionBindings : dict[str, str] = {f'command{motion}' : motion for motion in [mapping.name for mapping in list(XboxMotions)]},
                resolution : tuple[int, int] = (1280, 720),
                fullscreen : bool = False):
            
            self.buttonBindings = buttonBindings
            self.motionBindings = motionBindings
            self.resolution = resolution
            self.fullscreen = fullscreen
    
    def to_json(self):
        config = {
            "buttonBindings": {k : XboxButtons[v].name for k, v in self.buttonBindings.items()},
            "motionBindings": {k : XboxMotions[v].name for k, v in self.motionBindings.items()},
            "resolution": self.resolution,
            "fullscreen": self.fullscreen
        }
        return dumps(config, indent=2)

    @staticmethod
    def from_json(json: str):
        with open("./config.json", "r") as f:
            json_str = "".join(f.readlines())
        config = loads(json_str)

        return Config({k : XboxButtons[v].name for k, v in config.get("buttonBindings").items()},
                        {k : XboxMotions[v].name for k, v in config.get("motionBindings").items()},
                        config.get("resolution"),
                        config.get("fullscreen"))
