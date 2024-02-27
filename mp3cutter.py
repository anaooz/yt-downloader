from pydub import AudioSegment

requested_time = int(input("Quantos segundos deseja cortar?\n"))

time = requested_time * 1000

song_name = input("Qual o nome da música?\n")

song = AudioSegment.from_file(f"{song_name}.mp3", format="mp3")

song_duration = len(song)

start_time = song_duration - time

last_time = song[:start_time]

last_time.export(f"{song_name}cortada.mp3", format="mp3")

print("Música cortada!")
