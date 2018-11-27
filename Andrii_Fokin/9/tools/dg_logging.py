import logging as logg
from sys import stdout

DG_loger = logg.Logger('Dg_loger')
DG_debug_hendler = logg.FileHandler('DG_debug_log.txt', 'w')
DG_info_hendler = logg.StreamHandler(stdout)

DG_debug_hendler.setLevel(logg.DEBUG)
DG_info_hendler.setLevel(logg.INFO)

DG_debug_formater = logg.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
Dg_info_formater = logg.Formatter('%(message)s')

DG_debug_hendler.setFormatter(DG_debug_formater)
DG_info_hendler.setFormatter(Dg_info_formater)

DG_loger.addHandler(DG_debug_hendler)
DG_loger.addHandler(DG_info_hendler)
