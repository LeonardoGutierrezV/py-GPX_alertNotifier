#codific.art
#azucen.art
import time
import threading

def timer_on(running_timer):
    while running_timer.is_set():
        print("Ejecutando")
        time.sleep(1)

timer_runs_on=threading.Event()
timer_runs_on.set()

t = threading.Thread(target=timer_on, args=(timer_runs_on,) )
t.start()