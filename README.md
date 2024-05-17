# Rock-Paper-Scissors Simulation Game

This project is a simple animation game implemented using Python and the Pygame library. It features animated Rock, Paper, and Scissors images moving around the screen, with collision detection to simulate the interactions between the shapes according to the classic Rock-Paper-Scissors rules.

## Main Game Loop
The main game loop handles the animation, movement, and collision detection of the shapes.

Shapes are initialized with random speeds and directions.
On collision, shapes interact according to Rock-Paper-Scissors rules and switch images accordingly.## Installation

1. **Clone the repository:**

    ```python
    git clone https://github.com/AsrinTopal/Rock-Paper-Scissors.git
    cd Rock-Paper-Scissors
    ```

2. **Install the required dependencies:**

    Make sure you have Python and Pygame installed. You can install Pygame using pip:

    ```python
    pip install pygame
    ```
    ## Usage

To run the game, simply execute the following command:

```python
python main.py
```
## Code Explanation
1. **Image Resizing:**
    The resize_image function resizes the given image to the specified width and height.
    ```python
    def resize_image(image_path, new_width, new_height):
    image = pygame.image.load(image_path)
    resized_image = pygame.transform.scale(image, (new_width, new_height))
    pygame.image.save(resized_image, image_path)
    ```
2. **Image Loading:**
    The load_image function loads the image from the given path.
    ```python
    def load_image(image_path):
    return pygame.image.load(image_path)
    ```
2. **Collision Detection:**
    The check_collision function checks if two rectangles collide.
    ```python
    def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)
    ```
## Demo


## Authors

- [@AsrinTopal](https://www.github.com/AsrinTopal)
- [@MehmetEminTurkkal](https://github.com/RHShank)

## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

