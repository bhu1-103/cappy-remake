import pandas as pd

file_path = "../../../../capstone/dataste-generation/cappy-definitive-edition/step2/z_output/input_nodes_copy_deployment_000.csv"

df = pd.read_csv(file_path, delimiter=";")
df_numeric = df.drop(df.columns[[0, 2]], axis=1)
variance = df_numeric.var()
print(variance)

df_cleaned = df_numeric.drop(columns=variance[variance == 0].index)

df_cleaned.to_csv("clean1-part2.csv",index=False,sep=";")
