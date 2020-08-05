import pandas as pd
from tqdm.notebook import tqdm
from post_process import post_process

translated_test = pd.read_csv('./data/translated_test.csv')
submiss = pd.DataFrame({"translation_output":translated_test["translated"].progress_apply(post_process)})
submiss.to_csv('submiss.csv', index=False)