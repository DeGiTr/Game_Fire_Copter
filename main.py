# print("🌲🌳🌊〰️🔥🚁🗲🏥✚🏦🟩🟥🟧⬛🟦🟨🟪🟫🖤🤍💛💧🪣☁🏆")
from map import Map

tmp = Map(29, 10)
tmp.generate_forest(3, 10)
tmp.generate_river(10)
tmp.generate_river(30)
tmp.generate_river(10)
tmp.print_map()