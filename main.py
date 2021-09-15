from switch_position import PV_Switch
import logging
import time

logging.basicConfig(level=logging.DEBUG)

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    switch_position = PV_Switch(24)

    while True:

        pos = switch_position.is_switch_set_to_pv_only()
        logging.fatal("Switch position: $s", pos)
        time.sleep(5)




