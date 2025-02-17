import subprocess
import os

def run_process(command):
    print(f"Running command: {command}")
    process = subprocess.Popen(command, shell=True)

if __name__ == "__main__":
    commands = [
        # "~/git/uxv_research/AirSimNH/LinuxNoEditor/AirSimNH.sh",
        # "~/git/uxv_research/Blocks/LinuxBlocks1.8.1/LinuxNoEditor/Blocks.sh",
        "~/git/uxv_research/LandscapeMountains/LinuxNoEditor/LandscapeMountains.sh",
        "cd ~/git/uxv_research/ardupilot && sim_vehicle.py -v ArduCopter -f airsim-copter",
        "cd ~/git/uxv_research/MissionPlanner && ./gc.sh"
    ]

    for command in commands:
        run_process(command)
