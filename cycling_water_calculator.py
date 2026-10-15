"""Cycling Water Calculator — estimates litres of water needed based on cycling time."""

import math

hours = int(input("How long are you cycling (hours)? "))
litres = math.floor(hours * 0.5)
print(f"You should drink {litres} litre(s) of water.")
