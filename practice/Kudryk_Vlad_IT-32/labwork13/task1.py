import math

NAME, SURNAME, GROUP = "Vlad", "Kudryk", "IT-32"

ROOM_L, ROOM_W, ROOM_H = 4.2, 3.5, 2.7
DOOR_W, DOOR_H = 0.9, 2.0
WIN_W, WIN_H = 1.4, 1.5
TILE_W, TILE_H = 0.30, 0.30
TILE_PRICE = 42.30
SPARE = 0.10
PAINT_PER_M2 = 0.1   
COATS = 2
CAN_SIZE = 2.5

print(f"{NAME} {SURNAME}, {GROUP}")

floor_area = ROOM_L * ROOM_W
wall_area = 2 * (ROOM_L + ROOM_W) * ROOM_H - DOOR_W * DOOR_H - WIN_W * WIN_H
floor_diag = math.hypot(ROOM_L, ROOM_W)
room_diag = math.dist((0, 0, 0), (ROOM_L, ROOM_W, ROOM_H))

tiles_exact = floor_area / (TILE_W * TILE_H)
tiles_to_buy = math.ceil(tiles_exact * (1 + SPARE))

paint_l = wall_area * PAINT_PER_M2 * COATS
cans = math.ceil(paint_l / CAN_SIZE)

cost_mul = tiles_to_buy * TILE_PRICE
cost_sum = 0.0
for _ in range(tiles_to_buy):
    cost_sum += TILE_PRICE

print(f"room:          {ROOM_L} x {ROOM_W} x {ROOM_H} m")
print(f"floor area:    {floor_area:.2f} m2")
print(f"wall area:     {wall_area:.2f} m2 (without door and window)")
print(f"floor diag:    {floor_diag:.2f} m")
print(f"room diag:     {room_diag:.2f} m")
print()
print(f"tiles exact:   {tiles_exact:.2f}")
print(f"  round:       {round(tiles_exact)}")
print(f"  floor:       {math.floor(tiles_exact)}")
print(f"  ceil:        {math.ceil(tiles_exact)}")
print(f"tiles to buy:  {tiles_to_buy} (+{SPARE:.0%} spare)")
print(f"paint:         {paint_l:.2f} l -> {cans} cans of {CAN_SIZE} l")
print()
print(f"tiles cost:    {cost_mul:.2f} UAH")
print(f"sum == mul:    {cost_sum == cost_mul}")
print(f"isclose:       {math.isclose(cost_sum, cost_mul)}")
print(f"difference:    {abs(cost_sum - cost_mul)}")