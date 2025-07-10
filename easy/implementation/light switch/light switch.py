# link https://quera.org/problemset/49028

observation_time = int(input())

switch_count = 0
last_state = int(input())
for _ in range(observation_time - 1):
    current_state = int(input())
    if last_state != current_state:
        last_state = current_state
        switch_count += 1
print(switch_count)
