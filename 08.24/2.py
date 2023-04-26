from pathlib import Path


def audio_file_processing(

        path_file: str,
        /,
        format: int | str,
        *,
        channels: int | str,
        sampling: int | str,
        bit_depth: int | str
) -> str:
    """Функция принимает параметры аудио-файла, проверяет корректность переданных аргументов и выводит на печать результат проверки."""

    song_file_path = Path(path_file)
    sampling_value = (
        8000, 11025, 16000, 22050, 32000, 44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000
    )
    bit_depth_value = (8, 16, 24, 32)
    result = ''

    if song_file_path.suffix[1:] == 'wav' or song_file_path.suffix[1:] == 'WAV':
        result += f"{path_file = } is Correct\n"
    else:
        result += f"{path_file = } is not Correct\n"

    if format in range(0, 10000):
        result += f"{format = } is Correct\n"
    else:
        result += f"{format = } is not Correct\n"

    if channels in range(1, 11):
        result += f"{channels = } is Correct\n"
    else:
        result += f"{channels = } is not Correct\n"

    if sampling in sampling_value:
        result += f"{sampling = } is Correct\n"
    else:
        result += f"{sampling = } is not Correct\n"

    if bit_depth in bit_depth_value:
        result += f"{bit_depth = } is Correct\n"
    else:
        result += f"{bit_depth = } is not Correct\n"

    return result


print(audio_file_processing(
    "/audio/music/file_name.wav",
    1,
    channels=6,
    sampling=44100,
    bit_depth=32
))
print(audio_file_processing("/audio/music/file_name.mp3", 9999, channels=10, sampling=96000, bit_depth=8))
print(audio_file_processing("/audio/music/file_name.ogg", 10000, channels=11, sampling=9000, bit_depth=15))
print(audio_file_processing("/audio/music/file_name.wav", 999, 8, sampling=16000, bit_depth=16))
