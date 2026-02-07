import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

planeId = p.loadURDF("plane.urdf")

euler_angles = [0, 0, 0]
startOrientation = p.getQuaternionFromEuler(euler_angles)
startPosition = [0, 0, 1]

robotId = p.loadURDF("robot.urdf", startPosition, startOrientation)

# SLIDERS
joint1_slider = p.addUserDebugParameter(
    "base_to_link1 (Z)",
    -3.14,
    3.14,
    0.0
)

joint2_slider = p.addUserDebugParameter(
    "link1_to_link2 (X)",
    -3.14,
    3.14,
    0.0
)

for i in range(10000):
    p.stepSimulation()
    time.sleep(1./240.)

    # Leer valores de los sliders
    q1 = p.readUserDebugParameter(joint1_slider)
    q2 = p.readUserDebugParameter(joint2_slider)


    # Aplicar valores de los sliders a los joints
    p.setJointMotorControl2(
        robotId,
        0,  # base_to_link1
        p.POSITION_CONTROL,
        targetPosition=q1
    )

    p.setJointMotorControl2(
        robotId,
        1,  # link1_to_link2
        p.POSITION_CONTROL,
        targetPosition=q2
    )


p.disconnect()