from pydub import AudioSegment


def mp3_to_wav(mp3_path, wav_path):
    song = AudioSegment.from_mp3(mp3_path)
    song.export(wav_path, format="wav")


def wav_to_mp3(wav_path, mp3_path):
    song = AudioSegment.from_wav(wav_path)
    song.export(mp3_path, format="mp3")


if __name__ == '__main__':
    mp3_to_wav('mp3_path', 'wav_path')
    wav_to_mp3('wav_path', 'mp3_path')
