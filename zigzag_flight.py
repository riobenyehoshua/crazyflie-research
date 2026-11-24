import time
import math

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.position_hl_commander import PositionHlCommander
from cflib.utils import uri_helper

# URI to the Crazyflie to connect to
uri = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

def simple_sequence():
    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        # Arm the Crazyflie
        scf.cf.supervisor.send_arming_request(True)
        time.sleep(1.0)

        with PositionHlCommander(scf, controller=PositionHlCommander.CONTROLLER_PID) as pc:
            pc.forward(1.0)
            pc.left(1.0)
            pc.back(1.0)
            pc.go_to(0.0, 0.0, 1.0)

def xz_zigzag():
    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        # Arm the Crazyflie
        scf.cf.supervisor.send_arming_request(True)
        time.sleep(1.0)

        with PositionHlCommander(scf, controller=PositionHlCommander.CONTROLLER_PID) as pc:
            x = -1.5
            y = 0
            z = 1
            pc.go_to(x, y, z)
            x = -2

            for i in range (7):
                if i % 2 == 0:
                    z = 1
                else:
                    z = 1.5

                x = x + 0.5
                pc.go_to(x, y, z)
                

            for i in range (6):
                if i % 2 == 0:
                    z = 1.5
                else:
                    z = 1

                x = x - 0.5
                pc.go_to(x, y, z)
               
                              
def circle_zigzag():
    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        # Arm the Crazyflie
        scf.cf.supervisor.send_arming_request(True)
        time.sleep(1.0)

        with PositionHlCommander(scf, controller=PositionHlCommander.CONTROLLER_PID) as pc:
            angle = math.pi/4
            x = 2
            y = 0
            z = 1
            pc.go_to(x, y, z)

            for i in range (8):
                if i % 2 == 0:
                    z = 1
                else:
                    z = 1.5

                x = 2*math.cos(angle*i)
                y = 2*math.sin(angle*i)
                pc.go_to(x, y, z)
                


if __name__ == '__main__':
    cflib.crtp.init_drivers()

while (1):
 #simple_sequence()
  #xy_zigzag()
  circle_zigzag()