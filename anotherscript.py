import csv
import json




f = csv.writer(open("test.csv", "w"))

header = ["teama_off_rating", "teama_def_rating", "teama_ast_pct", "teama_ast_tov", "teama_ast_ratio", "teama_oreb_pct", "teama_dreb_pct", "teama_treb_pct", "teama_tm_tov_pct", "teama_efg_pct", "teama_ts_pct", "teama_usg_pct", "teama_pace", "teama_pie", "teamb_off_rating", "teamb_def_rating", "teamb_ast_pct", "teamb_ast_tov", "teamb_ast_ratio", "teamb_oreb_pct", "teamb_dreb_pct", "teamb_treb_pct", "teamb_tm_tov_pct", "teamb_efg_pct", "teamb_ts_pct", "teamb_usg_pct", "teamb_pace", "teamb_pie", "winner", "teama_id", "teamb_id"]


f.writerow(header)

for i in anotherjson:
    f.writerow(i.values())