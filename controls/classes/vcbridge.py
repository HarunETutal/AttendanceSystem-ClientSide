# -*- title: View-Control Bridge -*-
# -*- author: Harun Emre Tutal -*-

from kivy.event import EventDispatcher

class VCBridge(EventDispatcher):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = EventDispatcher.__new__(cls)
        return cls._instance

    def __init__(self, **kwargs):
        if hasattr(self, "_initialized"):
            return
        
        super().__init__(**kwargs)
        self._initialized = True


if __name__ == "__main__":
    print(id(VCBridge()))
    print(id(VCBridge()))
