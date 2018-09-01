import matplotlib.pyplot as plt
import numpy as np
from lidar_pro import lidar_to_2d_front_view
import numpy as np
import matplotlib.pyplot as plt

HRES = 0.35         # horizontal resolution (assuming 20Hz setting)
VRES = 0.4          # vertical res
VFOV = (-24.9, 2.0) # Field of view (-ve, +ve) along vertical axis
Y_FUDGE = 5         # y fudge factor for velodyne HDL 64E

lidar = (np.fromfile('/home/wu/umm.bin', dtype=np.float32)).reshape(-1, 4)

lidar_to_2d_front_view(lidar, v_res=VRES, h_res=HRES, v_fov=VFOV, val="depth",
                       saveto="/home/wu/lidar_depth.png", y_fudge=Y_FUDGE)

lidar_to_2d_front_view(lidar, v_res=VRES, h_res=HRES, v_fov=VFOV, val="height",
                       saveto="/home/wu/lidar_height.png", y_fudge=Y_FUDGE)

lidar_to_2d_front_view(lidar, v_res=VRES, h_res=HRES, v_fov=VFOV,
                       val="reflectance", saveto="/home/wu/lidar_reflectance.png",
                       y_fudge=Y_FUDGE)