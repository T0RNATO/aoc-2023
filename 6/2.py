race_length = 45977295
record = 305106211101695
winning_options = 0

for i in range(race_length):
    distance = i * (race_length - i)
    if distance > record:
        winning_options += 1

print(winning_options)

