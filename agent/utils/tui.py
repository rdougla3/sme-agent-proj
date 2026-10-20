import threading

def progress_text(message: str):
    stop_event = threading.Event()

    def print_dots():
        print(message, end="", flush=True)
        while not stop_event.wait(0.5):
            print(".", end="", flush=True)
        print()

    thread = threading.Thread(target=print_dots, daemon=True)
    thread.start()

    def stop_text():
        stop_event.set()
        thread.join()

    return stop_text
