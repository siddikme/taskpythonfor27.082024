import math

def end_corona(recovers, new_cases, active_cases):
    daily_net_reduction = recovers - new_cases
    days_needed = math.ceil(active_cases / daily_net_reduction)
    return days_needed

recovers = int(input("Введите количество выздоровевших в день: "))
new_cases = int(input("Введите количество новых случаев в день: "))
active_cases = int(input("Введите текущее количество активных случаев: "))

days = end_corona(recovers, new_cases, active_cases)
print(f"Количество дней до достижения нуля активных случаев: {days}")
