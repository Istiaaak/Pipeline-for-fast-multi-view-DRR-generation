from dataclasses import dataclass
from typing import Tuple


@dataclass
class Config:  

    # CT parameters
    target_iso_mm: float = 1.875
    hu_window: Tuple[float, float] = (-500, 1300)
    orientation: str = "RAS"

    # Tigre geometry
    sid: float = 1500.0
    sod: float = 1000.0
    n_angles: int = 3
    end_angle: float = 90.0

    # Detector parameters
    det_pixels: Tuple[int, int] = (512, 512)
    det_padding: float = 0.6

    # Mode
    mode:str = "parallel"

    # Store images
    write_png: bool = True

    # Path
    input_dir: str = "../data/CTs"
    output_dir: str= f"../dataset_{n_angles}views_{end_angle}deg"