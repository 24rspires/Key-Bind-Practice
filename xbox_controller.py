from pygame.joystick import Joystick
from enum import Enum

from typing import Union

class XboxButtons(Enum):
        SOUTH_BUTTON = 0
        WEST_BUTTON = 1
        EAST_BUTTON = 2
        NORTH_BUTTON = 3
        LEFT_BUMPER = 4
        RIGHT_BUMPER = 5
        SELECT_BUTTON = 6
        START_BUTTON = 7
        LEFT_STICK_IN = 8
        RIGHT_STICK_IN = 9
        XBOX_BUTTON = 10
        SHARE_BUTTON = 11

class XboxMotions(Enum):
        LEFT_STICK_RIGHT = 0
        LEFT_STICK_DOWN = 1
        LEFT_STICK_LEFT = 2
        LEFT_STICK_UP = 3
        RIGHT_STICK_UP = 4
        RIGHT_STICK_RIGHT = 5
        RIGHT_STICK_DOWN = 6
        RIGHT_STICK_LEFT = 7
        LEFT_TRIGGER = 8
        RIGHT_TRIGGER = 9
        DPAD_LEFT = 10
        DPAD_RIGHT = 11
        DPAD_UP = 12
        DPAD_DOWN = 13

class XboxController():

    def __init__(self, controller_id: int):
        self.controller = Joystick(controller_id)

    def get_active_input(self) -> Union[XboxButtons, XboxMotions]:
        for button in list(XboxButtons):
            if self.controller.get_button(button.value):
                return button
        
        left_stick_x = self.controller.get_axis(0)
        left_stick_y = self.controller.get_axis(1)

        if left_stick_x <= -0.9:
            return XboxMotions.LEFT_STICK_LEFT
        elif left_stick_x >= 0.9:
            return XboxMotions.LEFT_STICK_RIGHT
        
        if left_stick_y <= -0.9:
            return XboxMotions.LEFT_STICK_UP
        elif left_stick_y >= 0.9:
            return XboxMotions.LEFT_STICK_DOWN
        
        right_stick_x = self.controller.get_axis(2)
        right_stick_y = self.controller.get_axis(3)

        if right_stick_x <= -0.9:
            return XboxMotions.RIGHT_STICK_LEFT
        elif right_stick_x >= 0.9:
            return XboxMotions.RIGHT_STICK_RIGHT
        
        if right_stick_y <= -0.9:
            return XboxMotions.RIGHT_STICK_UP
        elif right_stick_y >= 0.9:
            return XboxMotions.RIGHT_STICK_DOWN
        
        left_trigger = self.controller.get_axis(4)
        right_trigger = self.controller.get_axis(5)

        if left_trigger >= 0.9:
            return XboxMotions.LEFT_TRIGGER
        elif right_trigger >= 0.9:
            return XboxMotions.RIGHT_TRIGGER
        
        dpad_x, dpad_y = self.controller.get_hat(0)

        if dpad_x == 1:
            return XboxMotions.DPAD_RIGHT
        elif dpad_x == -1:
            return XboxMotions.DPAD_LEFT
        
        if dpad_y == 1:
            return XboxMotions.DPAD_UP
        elif dpad_y == -1:
            return XboxMotions.DPAD_DOWN


    def get_a(self):
        return self.controller.get_button(0)
    
    def get_b(self):
        return self.controller.get_button(1)
    
    def get_x(self):
        return self.controller.get_button(2)
    
    def get_y(self):
        return self.controller.get_button(3)
    
    def get_left_bumper(self):
        return self.controller.get_button(4)
    
    def get_right_bumper(self):
        return self.controller.get_button(5)
    
    def get_select(self):
        return self.controller.get_button(6)
    
    def get_start(self):
        return self.controller.get_button(7)
    
    def get_left_stick_in(self):
        return self.controller.get_button(8)
    
    def get_right_stick_in(self):
        return self.controller.get_button(9)
    
    def get_left_stick_up(self):
        return self.controller.get_axis(1) >= 0.9
    
    def get_left_stick_down(self):
        return self.controller.get_axis(1) <= -0.9
    
    def get_left_stick_left(self):
        return self.controller.get_axis(0) <= -0.9
    
    def get_left_stick_right(self):
        return self.controller.get_axis(0) >= 0.9
    
    def get_right_stick_up(self):
        return self.controller.get_axis(3) >= 0.9
    
    def get_right_stick_down(self):
        return self.controller.get_axis(3) <= -0.9
    
    def get_right_stick_left(self):
        return self.controller.get_axis(2) <= -0.9
    
    def get_right_stick_right(self):
        return self.controller.get_axis(2) >= 0.9
    
    def get_left_trigger(self):
        return self.controller.get_axis(4) >= 0.9
    
    def get_right_trigger(self):
        return self.controller.get_axis(5) >= 0.9