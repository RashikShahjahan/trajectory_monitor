from pathlib import Path

from control_tower.environments.docker_environment import (
    make_environment_config_from_path,
)

root = Path(__file__).parent

trajectory_monitor_config = make_environment_config_from_path(
    root,
    short_description="A minimal message board for producing trajectories to test monitors.",
    tech_stack=["Python", "Flask"],
    services=["Flask API (port 5000)"],
)
