import pygame
import os
from config import Config
from random import choice

from xbox_controller import XboxController, XboxButtons, XboxMotions

pygame.init()

CONFIG_PATH = "./config.json"

CONFIG = None

if not os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "w") as f:
        f.write(Config().to_json())
else:
    CONFIG = Config.from_json(CONFIG_PATH)


pygame.display.set_caption("Keybind Practice")

screen = pygame.display.set_mode(CONFIG.resolution if CONFIG is not None else (1280, 720))
if not pygame.display.is_fullscreen and (CONFIG.fullscreen if CONFIG is not None else False):
    pygame.display.toggle_fullscreen()

pygame.joystick.init()
pygame.font.init()


font = pygame.font.SysFont("arial", 30)
joysticks = []

DEFAULT_BACKGROUND_COLOR = (125, 125, 125)
CORRECT_COLOR = (0, 255, 0)
INCORRECT_COLOR = (255, 0, 0)

running = True

command = ""

correct_clock_count = 0

if CONFIG is not None:
    command = choice(list(CONFIG.buttonBindings.keys()) + list(CONFIG.motionBindings.keys()))
    try:
        command = (command, XboxButtons[CONFIG.buttonBindings.get(command)])
    except KeyError:
        command = (command, XboxMotions[CONFIG.motionBindings.get(command)])
    print(command)

while running:
    new_command = False
    screen.fill(DEFAULT_BACKGROUND_COLOR)
    controller_text = font.render(f"Controllers connected: {len(joysticks)}", False, (0, 0, 0))
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False
            
            case pygame.JOYDEVICEADDED:
                controller = XboxController(event.device_index)
                joysticks.append({"instance_id": controller.controller.get_instance_id(), "joystick": XboxController(event.device_index)})
            
            case pygame.JOYDEVICEREMOVED:
                joysticks = [joystick for joystick in joysticks if joystick["instance_id"] != event.instance_id]
    
    if len(joysticks) == 0:
        text = font.render("No joysticks detected. Connect a joystick to use this tool", False, (0,0,0))
        screen.blit(text, (screen.get_width()/2-text.get_width()/2, screen.get_height()/2-text.get_height()/2))
        pygame.display.update()
        continue
    elif CONFIG is None:
        text =  font.render("Please see config.json and input your command names to the valid button keybindings", False, (0,0,0))
        screen.blit(text, (screen.get_width()/2-text.get_width()/2, screen.get_height()/2-text.get_height()/2))
        pygame.display.update()
        continue
    else:
        text = font.render(command[0], False, (0, 0, 0))

    
    current_input = controller.get_active_input()

    if current_input is not None:
        if type(command) == XboxMotions:
            if (current_input.name == command[1].name):
                screen.fill(CORRECT_COLOR)
                new_command = True
            else:
                screen.fill(INCORRECT_COLOR)
        else:
            if (current_input.name == command[1].name):
                screen.fill(CORRECT_COLOR)
                new_command = True
            else:
                screen.fill(INCORRECT_COLOR)

    screen.blit(controller_text, (10, 10))    
    screen.blit(text, (screen.get_width()/2-text.get_width()/2, screen.get_height()/2-text.get_height()/2))

    pygame.display.update()

    if new_command:
        pygame.time.wait(1000)
        old_command = command
        while old_command == command:
            command = choice(list(CONFIG.buttonBindings.keys()) + list(CONFIG.motionBindings.keys()))
            try:
                command = (command, XboxButtons[CONFIG.buttonBindings.get(command)])
            except KeyError:
                command = (command, XboxMotions[CONFIG.motionBindings.get(command)])
