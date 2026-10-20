from threading import Event, Thread

_stop = Event()
_animation = None
_width = 0

def show_text(payload):
    global _animation, _width
    hide_text()
    _stop.clear()
    _width = len(payload) + 3

    def animate():
        dots = 1
        while not _stop.is_set():
            print(f"\r{payload}{'.' * dots:<3}", end="", flush=True)
            if _stop.wait(0.4):
                break
            dots = dots % 3 + 1

    _animation = Thread(target=animate, daemon=True)
    _animation.start()


def hide_text():
    global _animation
    if _animation is None:
        return
    _stop.set()
    _animation.join()
    _animation = None
    print("\r" + " " * _width + "\r", end="", flush=True)