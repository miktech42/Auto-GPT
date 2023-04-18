from autogpt.speech.base import VoiceBase
import pythoncom
import win32com.client

class MicrosoftSAPIVoice(VoiceBase):
    def _setup(self) -> None:
        pass

    def _speech(self, text: str, voice_index: int = 0) -> bool:
        pythoncom.CoInitialize()
        speaker = win32com.client.Dispatch("SAPI.SpVoice")

        if voice_index < len(speaker.GetVoices()):
            speaker.Voice = speaker.GetVoices().Item(voice_index)

        speaker.Speak(text)
        return True
