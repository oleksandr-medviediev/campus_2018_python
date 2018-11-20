import logging as log
from sys import stdout

DG_loger = log.Logger('Dg_loger')
DG_debug_hendler = log.FileHandler('DG_debug_log.txt', 'w')
DG_info_hendler = log.StreamHandler(stdout)

DG_debug_hendler.setLevel(log.DEBUG)
DG_info_hendler.setLevel(log.INFO)

DG_debug_formater = log.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
Dg_info_formater = log.Formatter('%(message)s')

DG_debug_hendler.setFormatter(DG_debug_formater)
DG_info_hendler.setFormatter(Dg_info_formater)

DG_loger.addHandler(DG_debug_hendler)
DG_loger.addHandler(DG_info_hendler)
