
# Dominosteine

# Gib alle möglichen Dominosteine in der folgenden Form aus.
# Falls jemand das Spiel nicht kennt: https://de.wikipedia.org/wiki/Domino

"""
(0|0)(0|1)(0|2)(0|3)(0|4)(0|5)(0|6)
     (1|1)(1|2)(1|3)(1|4)(1|5)(1|6)
          (2|2)(2|3)(2|4)(2|5)(2|6)
               (3|3)(3|4)(3|5)(3|6)
                    (4|4)(4|5)(4|6)
                         (5|5)(5|6)
                              (6|6)
"""

for i in range(7):
    print('      ' * i, end=' ')
    for j in range(i, 7):
        print(f"({i},{j})", end=' ')
    print()
