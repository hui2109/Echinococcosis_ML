from pathlib import Path
import pandas as pd

root_path = Path(r'D:\exe_code\Python\17_Echinococcosis_ML\resources\process_results')
process_dir_list = []
for i in root_path.iterdir():
    if i.is_dir():
        process_dir_list.append(i)
process_dir_list.sort(key=lambda s: int(str(s).split('-')[-1]))

df = pd.DataFrame()
for i, process_dir in enumerate(process_dir_list):
    result_excel_file = process_dir / f'results_Process-{i + 1}.xlsx'
    df_tmp = pd.read_excel(result_excel_file)
    df = pd.concat([df, df_tmp])

final_result = Path('resources/extract_data/final_extract_results.xlsx')
with pd.ExcelWriter(final_result) as writer:
    df.to_excel(writer, index=False)
