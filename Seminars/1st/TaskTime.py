# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
Sek = int(input('введите число секунд: '))
days = Sek // 86400
temp = Sek % 86400
hours = temp // 3600
temp = temp % 3600
minutes = temp // 60
seconds = temp % 60
print(f'{days}d:{hours}h:{minutes}m:{seconds}s')
