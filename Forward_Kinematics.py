import math

n = int(input("masukkan jumlah lengan robot: "))

x = y = total_sudut = 0

for i in range(n):
    panjang = float(input(f"panjang lengan ke-{i+1}: "))
    sudut = float(input(f"sudut lengan ke-{i+1} (°): "))
    total_sudut += math.radians(sudut)
    x += panjang * math.cos(total_sudut)
    y += panjang * math.sin(total_sudut)

print("\nhasil forward kinematics")
print(f"x = {x:.4f}")
print(f"y = {y:.4f}")

