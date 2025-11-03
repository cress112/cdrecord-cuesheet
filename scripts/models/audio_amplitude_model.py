from typing import Optional
from pydantic import BaseModel


class AudioAmplitudeModel(BaseModel):
    input_file_path: str
    input_file_normalized_max_loudness: Optional[float] = None

    output_file_path: str
