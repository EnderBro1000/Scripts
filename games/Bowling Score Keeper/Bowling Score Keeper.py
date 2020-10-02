game = [[0, 0, 0, ' '], [0, 0, 0, ' '], [0, 0, 0, ' '], [0, 0, 0, ' '], [0, 0, 0, ' ']]

frame_counter = 0

# Ask score for frames
for frame in game:
    if frame_counter < 4:
        shot_number = 0
        for shot in range(2):
            game[frame_counter][shot_number] = int(input(f'Score for frame {frame_counter + 1}, shot {shot_number + 1}: '))
            shot_number += 1
        frame_counter += 1
        if 0 > game[frame_counter][0] + game[frame_counter][0] > 10:
            raise ValueError('values are too large or too small')
    else:
        for shot in range(game[frame_counter].count(0) - 1):
            game[4][shot] = int(input(f'Score for frame 10, shot {shot + 1}: '))
            if 0 > game[4][shot] > 10:
                raise ValueError('Value is too large or too small')
if game[4][0] == 10 and game[4][1] == 10:
    game[4] = ([10, 10, 20, 'X', 'X'], [0, 0, ' '])
    game[4][1][0] = int(input('Score for frame 10, shot 3: '))
    game[4][1][1] = game[4][1][0]
elif game[4][0] == 10:
    game[4] = ([10, 10, 'X'], [game[4][1], 0, 0, ' '])
    game[4][1][1] = int(input('Score for frame 10, shot 3: '))
elif game[4][0] + game[4][1] == 10:
    game[4] = ([game[4][0], game[4][1], 10, '/'], [0, 0, ' '])
    game[4][1][0] = int(input('Score for frame 10, shot 3: '))
    game[4][1][1] = game[4][1][0]

frame_counter = 1
print(game)
game.reverse()

# Count and organize scores
for frame in game[1:]:
    if frame[0] == 10 and frame[1] == 0:
        game[frame_counter][2] = 10 + game[frame_counter - 1][0]
        if game[frame_counter - 1][0] == 10 and frame_counter != 1:
            game[frame_counter][2] += game[frame_counter - 2][0]
        else:
            game[frame_counter][2] += game[frame_counter - 1][1]
        game[frame_counter][3] = 'X'
    elif frame[0] + frame[1] == 10:
        game[frame_counter][2] = 10 + game[frame_counter - 1][0]
        game[frame_counter][3] = '/'
    elif 0 < frame[0] + frame[1] < 10:
        game[frame_counter][2] = frame[0] + frame[1]
        game[frame_counter][3] = f'{frame[0] + frame[1]}'
    elif frame[0] + frame[1] == 0:
        game[frame_counter][2] = 0
        game[frame_counter][3] = '0'
    print(f'frame {4 - frame_counter} finished')
    print(game)
    frame_counter += 1
game.reverse()


print(game)
