

import glfw
from OpenGL.GL import *

def main():
    # Initialize GLFW
    if not glfw.init():
        print("GLFW initialization failed")
        return

    # Request OpenGL 3.3
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(
        glfw.OPENGL_PROFILE,
        glfw.OPENGL_CORE_PROFILE
    )

    # Create an 800 x 600 window
    window = glfw.create_window(
        800, 600,
        "HCI and Computer Graphics - Lab 1",
        None, None
    )

    if not window:
        print("Window creation failed")
        glfw.terminate()
        return

    # Activate the OpenGL context
    glfw.make_context_current(window)

    # Print OpenGL information
    print("OpenGL Version:", glGetString(GL_VERSION).decode())
    print("Renderer:", glGetString(GL_RENDERER).decode())

    # Set the background colour to blue
    glClearColor(0.2, 0.4, 0.6, 1.0)

    # Keep the window open
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
