#This python file is intended to get the final pose of Bbox in RBOT frame of reference
#importing math module for performing trigonometric operations on Rotation matrix to fetch Euler angles.
import math
'''
Rotation  of Bbox in the RBOt frame of reference can be described as
Rotation of Rbot in DL frame (R_Rbot_dl_ * Roation of world DL wrt Camera DL (Rw_c_dl) * Rotation of Camera DL wrt Bbox DL (R_C_bbox_dl)
'''

#Rotation 4*4
Rw_c_dl = [[0.9833799 , 0.18146843, -0.00576319,0.],
          [-0.18155992, 0.9828844 , -0.03121508,0.],
          [-0. , 0.03174265, 0.9994961,0.],
          [0.  ,  0.       , 0.       ,1.]]

# Rotation 4*4
R_C_bbox_dl = [[-0.0226176,0. , 0.9997442,1.430479],
                [0.       , 1., 0.       ,-0.4734111],
                [-0.9997442, 0. , -0.0226176,0.68981165],
                 [0.       , 0. ,         0.,       1.]]

#Rotation matrix of RBot with respect to DL.
R_Rbot_dl= [[0. ,0. , 1.,0],
           [0., -1., 0.,0.],
           [1. ,0. , 0.,0.],
           [0., 0., 0.,1.]]
#Multiplying 2nd and 3rd matrices at first i.e Rw_c_dl * R_C_bbox_dl
Mult_2nd_3rd = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*R_C_bbox_dl)] for X_row in Rw_c_dl]
#Multiplying first matrix with the above matrix result. i.e R_Rbot_dl * Mult_2nd_3rd
rot_mat= [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Mult_2nd_3rd)] for X_row in R_Rbot_dl]
#printing the final matrix for debugging purposes.
for r in rot_mat:
   print(r)

#Calculating Yaw, Pitch and Roll
yaw = math.atan2(rot_mat[2][0], rot_mat[2][1])
pitch = math.acos(rot_mat[2][2])
roll = math.atan2(rot_mat[0][2], rot_mat[1][2])

#value of pi
pi=22/7
#printing the final values of Y,P, R in degrees of bbox in RBOT frame of reference.
print("Yaw of 3D bbox in RBOT frame of reference",(yaw*180/pi))
print("Pitch of 3D bbox in RBOT frame of reference", (pitch*180/pi))
print("Roll of 3D bbox in RBOT frame of reference",(roll * 180/pi))