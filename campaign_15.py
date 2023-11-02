from module.logger import logger
from module.map.map_base import CampaignMap
from module.map.map_grids import RoadGrids, SelectedGrids

# class CampaignBase derivatived from CampaignUI, Map and AutoSearchCombat
# It has methods as below:
# 1.battle_default()
# 2.battle_boss()
# 3.battle_fuction() 
# 1)battle with poor map data
# 2)clear_all
# 3)poor map data & clear_all is false
# 4.execute_a_battle()
# 5.run()
# 6._map_battle()
# 7.auto_search_execute_a_battle()






MAP = CampaignMap('15-4')
MAP.shape = 'K9'
MAP.camera_data = ['D2', 'D5', 'D7', 'H2', 'H5', 'H7']
MAP.camera_data_spawn_point = ['H2']
MAP.map_covered = ['A4']

# H3 1st team
# I3 2nd team
# H5 1st Boss
# D3 2nd Boss
# A9 3rd Boss

MAP.map_data = """
    ME -- ++ ++ -- ME ME ME ++ ++ ++
    -- ME ME ME ME ME ME -- SP SP --
    MB -- __ -- -- -- -- -- ME -- --
    MB ME -- Me Me -- Me ++ ++ -- ME
    MM -- Me ME -- Me -- MA ++ -- ME
    ++ ME ME -- ++ -- ME -- ME -- --
    ++ -- ME Me Me ME -- -- -- -- ++
    -- -- -- -- -- __ -- ME ME -- ME
    -- -- ++ MB MB ++ ++ MM ME ME ME
"""
MAP.weight_data = """
    40 40 40 40 50 50 50 50 50 50 50
    40 40 40 40 50 50 50 50 50 50 50
    40 40 40 40 50 50 50 50 50 50 50
    40 40 40 40 50 50 50 50 50 50 50
    40 40 40 40 50 50 50 50 50 50 50
    40 40 40 40 50 50 50 50 50 50 50
    40 40 40 40 50 50 50 50 50 50 50
    50 10 50 50 50 50 50 40 40 50 50
    50 50 50 50 50 50 50 50 50 40 50
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 3},
    {'battle': 1, 'enemy': 3},
    {'battle': 2, 'enemy': 2},
    {'battle': 3, 'enemy': 2},
    {'battle': 4, 'enemy': 1},
    {'battle': 5, 'enemy': 1},
    {'battle': 6},
    {'battle': 7, 'boss': 1},
]
MAP.spawn_data_loop = [
    {'battle': 0, 'enemy': 2},
    {'battle': 1, 'enemy': 3},
    {'battle': 2, 'enemy': 2},
    {'battle': 3, 'enemy': 2},
    {'battle': 4, 'enemy': 1},
    {'battle': 5, 'enemy': 1},
    {'battle': 6},
    {'battle': 7, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, I1, J1, K1, \
A2, B2, C2, D2, E2, F2, G2, H2, I2, J2, K2, \
A3, B3, C3, D3, E3, F3, G3, H3, I3, J3, K3, \
A4, B4, C4, D4, E4, F4, G4, H4, I4, J4, K4, \
A5, B5, C5, D5, E5, F5, G5, H5, I5, J5, K5, \
A6, B6, C6, D6, E6, F6, G6, H6, I6, J6, K6, \
A7, B7, C7, D7, E7, F7, G7, H7, I7, J7, K7, \
A8, B8, C8, D8, E8, F8, G8, H8, I8, J8, K8, \
A9, B9, C9, D9, E9, F9, G9, H9, I9, J9, K9, \
    = MAP.flatten()
