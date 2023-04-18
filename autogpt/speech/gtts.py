""" GTTS Voice. """
import os

import gtts
from playsound import playsound

from autogpt.speech.base import VoiceBase


class GTTSVoice(VoiceBase):
    """GTTS Voice."""

    def _setup(self) -> None:
        pass

    def _speech(self, text: str, _: int = 0) -> bool:
        """Play the given text."""
        tts = gtts.gTTS(text)
        
        # Updated file path
        file_path = os.path.join(os.path.expanduser("~"), "speech.mp3")

        # Save, play, and remove the file using the new path
        tts.save(file_path)
        playsound(file_path, True)
        os.remove(file_path)
        
        return True
