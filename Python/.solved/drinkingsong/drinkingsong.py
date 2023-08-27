i = int(input())
drink = input()

def lyric(num):
    return f"{num} bottle{'s' if num > 1 else ''} of {drink} on the wall, {num} bottle{'s' if num > 1 else ''} of {drink}.\nTake {'it' if num == 1 else 'one'} down, pass it around, {str(num-1) + ' bottles' if num > 2 else '1 bottle' if num == 2 else 'no more bottles'} of {drink + '.' if num == 1 else drink + ' on the wall.'}"

print("\n\n".join([lyric(v) for v in range(i, 0, -1)]))