import pandas as pd
from tqdm import tqdm
from post_process import post_process
from evaluate import eval

tqdm.pandas()

train_en = pd.read_csv("./data/train_en.csv")
train_tcn = pd.read_csv("./data/train_tcn.csv")

dev_en = pd.read_csv("./data/dev_en.csv")
dev_tcn = pd.read_csv("./data/dev_tcn.csv")
dev_data = pd.read_csv("./data/dev.csv")
translated_test = pd.read_csv("./data/translated_test.csv")
test = pd.read_csv("./data/test_tcn.csv")

texts = dev_data.text.tolist()
preds = dev_data.translated.progress_apply(post_process)
refs = dev_data.ground_truth
score, preds, refs = eval(preds, refs)

# validation score
print(score)
