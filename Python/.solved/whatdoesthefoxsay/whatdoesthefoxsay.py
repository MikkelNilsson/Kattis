n = int(input())

for _ in range(n):
    recording = " " + input() + " "
    i = input()

    while i != "what does the fox say?":
        sound = " " + i.split(" goes ")[1] + " "
        tmprecording = recording.replace(sound, " ", 1)

        while tmprecording != recording:
            recording = tmprecording
            tmprecording = recording.replace(sound, " ", 1)

        i = input()

    print(recording.strip())