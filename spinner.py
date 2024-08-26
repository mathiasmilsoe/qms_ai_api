# spinner.py
import sys
import time
import threading

def spinner_loader(text):
    spinner = ['|', '/', '-', '\\']
    stop_event = threading.Event()

    def spinner_task():
        i = 0
        while not stop_event.is_set():
            # Write the spinner and text to the same line
            sys.stdout.write(f'\r{text}... {spinner[i % len(spinner)]}')
            sys.stdout.flush()
            time.sleep(0.1)  # Adjust this to control spinner speed
            i += 1
        # Clear the spinner line after completion
        sys.stdout.write('\r' + ' ' * (len(text) + 10) + '\r')
        sys.stdout.flush()

    spinner_thread = threading.Thread(target=spinner_task)
    spinner_thread.start()

    return stop_event, spinner_thread

