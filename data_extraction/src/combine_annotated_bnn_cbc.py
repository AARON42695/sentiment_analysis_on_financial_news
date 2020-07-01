
"""
Combine the annotated data from both sources, users can call this script
after annotation is finished.
"""
import pandas as pd

import os


def combine_bnn_cbc(bloomberg_file, cbc_file, out_name):
    """
    combine the annotated bloomberg articles with annotated CBC articles
    """
    bloomberg_df = pd.read_csv(bloomberg_file)
    bloomberg_df = bloomberg_df[['source', 'title', 'description', 'publishedAt', 'title_desc_sent_1']]
    
    CBC_df = pd.read_csv(cbc_file)
    CBC_df.rename(columns = {'date':'publishedAt'}, inplace = True)
    
    concat_df = pd.concat([bloomberg_df, CBC_df], sort=True)
    concat_df = concat_df.sort_values(by='publishedAt', ascending=False)
    concat_df.reset_index(drop=True, inplace=True)
    concat_df['title_desc'] = concat_df['title'] + '. ' + concat_df['description']
    concat_df = concat_df[['source', 'title_desc', 'publishedAt', 'title_desc_sent_1']]
    
    concat_df.to_csv(out_name + '.csv')


bloomberg_file_path = "../data/annotated_data/bloomberg/"
cbc_file_path = "../data/annotated_data/cbc/"
output_file_path = "../data/annotated_data/combined/"
# test
# output_file_path = "../data/annotated_data/test/"

combine_bnn_cbc(bloomberg_file_path + 'employment_bloomberg_sampled.csv', cbc_file_path + 'employment_cbc_sampled.csv', output_file_path + 'annotated_employment_bnn&CBC')
assert os.path.exists(output_file_path + 'annotated_employment_bnn&CBC.csv')

combine_bnn_cbc(bloomberg_file_path + 'gdp_bloomberg_sampled.csv', cbc_file_path + 'gdp_cbc_sampled.csv', output_file_path + 'annotated_GDP_bnn&CBC')
assert os.path.exists(output_file_path + 'annotated_GDP_bnn&CBC.csv')


combine_bnn_cbc(bloomberg_file_path + 'housing_bloomberg_sampled.csv', cbc_file_path + 'housing_cbc_sampled.csv', output_file_path + 'annotated_housing_bnn&CBC')
assert os.path.exists(output_file_path + 'annotated_housing_bnn&CBC.csv')

combine_bnn_cbc(bloomberg_file_path + 'interestrates_bloomberg_sampled.csv', cbc_file_path + 'interestrates_cbc_sampled.csv', output_file_path + 'annotated_interestrates_bnn&CBC')
assert os.path.exists(output_file_path + 'annotated_interestrates_bnn&CBC.csv')

combine_bnn_cbc(bloomberg_file_path + 'mortgagerates_bloomberg_sampled.csv', cbc_file_path + 'mortgagerates_cbc_sampled.csv', output_file_path + 'annotated_mortgagerates_bnn&CBC')
assert os.path.exists(output_file_path + 'annotated_mortgagerates_bnn&CBC.csv')


combine_bnn_cbc(bloomberg_file_path + 'tsx_bloomberg_sampled.csv', cbc_file_path + 'tsx_bloomberg_sampled.csv', output_file_path + 'annotated_stock_bnn&CBC')
assert os.path.exists(output_file_path + 'annotated_stock_bnn&CBC.csv')
