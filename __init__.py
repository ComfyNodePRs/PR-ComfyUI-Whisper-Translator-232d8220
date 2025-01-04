from .apply_whisper_x import ApplyWhisperNodeX
from .add_subtitles_to_frames_x import AddSubtitlesToFramesNodeX

NODE_CLASS_MAPPINGS = {
    "Apply WhisperX" : ApplyWhisperNodeX,
    "Add Subtitles To FramesX": AddSubtitlesToFramesNodeX,
}

NODE_DISPLAY_NAME_MAPPINGS = {
     "Apply WhisperX" : "Apply WhisperX",
     "Add Subtitles To FramesX": "Add Subtitles To FramesX",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']