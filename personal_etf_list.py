from menu_option_one.search_for_data_of_specific_stock import SearchForStockData

etf_list = ['ORC', 'CSCO', 'IBM', 'CRF', 'CLM', 'ARR', 'IVR', 'NYMT', 'AGNC', 'EFC', 'O', 'DX', 'NLY', "STAG", 'RYLD'
            'XYLD', 'MVO', 'IEP', 'QYLD', 'IBM', 'LDI', 'ECC', 'GAIN', 'YYY', 'GECC', 'KBWD', 'OKE', 'RA', 'TROW',
            'DIVO', 'IRM', 'DHS', 'MAIN', 'VICI', 'ARCC', 'AMZA', 'DKL', 'OUSA', 'MRO', 'LTC', 'PSEC', 'UVV', 'TEF',
            'CIF', 'CSSEP', 'PBT', 'VALE', 'CRT', 'TWO', 'GLDI', 'NUSI', 'USOI', 'SBLK', 'SLVO', 'ZIM']

not_working = ['RYLD']

for stock in etf_list:
    run = SearchForStockData(stock)
    run.benjamin_graham_intrinsic_value()