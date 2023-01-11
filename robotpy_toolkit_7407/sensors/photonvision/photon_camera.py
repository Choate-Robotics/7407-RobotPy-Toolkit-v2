import photonvision
from robotpy_toolkit_7407.sensors.photonvision.photon_target import PhotonTarget
from wpimath.geometry import Pose3d

class PhotonCamera:
    def __init__(self, name, poseRelativeToRobot: Pose3d, height=None, pitch=None):
        self.camera = photonvision.PhotonCamera(cameraName=name)
        self.latest_best_target: PhotonTarget = None
        self.latest_targets_all: list[PhotonTarget] = None
        self.camera_to_robot_pose = poseRelativeToRobot
        self.height = height
        self.pitch = pitch

    def hasTargets(self):
        return self.latest_best_target is not None

    def refresh(self):  # Call at the beginning of every loop. Saves target for the loop to optimize lookup times.
        self.latest_targets_all = [PhotonTarget(target) for target in self.getLatestResult().getTargets()] if self.hasTargets() else None
        self.latest_best_target = PhotonTarget(self.getLatestResult().getBestTarget()) if self.hasTargets() else None
