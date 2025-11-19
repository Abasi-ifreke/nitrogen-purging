import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error
from sklearn.feature_extraction import DictVectorizer
import pickle


def load_and_prepare_data(path="Book2.csv"):
    df = pd.read_csv("Book2.csv")
    df.columns = df.columns.str.replace(" ", "_").str.lower()
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    return df

def train_model(df):
    df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
    y_train_full = df_full_train["nitrogen_volume_needed"]
    y_test = df_test["nitrogen_volume_needed"]
    df_full_train = df_full_train.drop(columns=["nitrogen_volume_needed"])
    df_test = df_test.drop(columns=["nitrogen_volume_needed"])

    dv = DictVectorizer(sparse=False)
    X_train_full = dv.fit_transform(df_full_train.to_dict(orient="records"))
    X_test = dv.transform(df_test.to_dict(orient="records"))

    dtrain = xgb.DMatrix(X_train_full, label=y_train_full, feature_names=dv.get_feature_names_out().tolist())
    dtest = xgb.DMatrix(X_test, label=y_test, feature_names=dv.get_feature_names_out().tolist())

    params = {
        'objective': 'reg:squarederror',
        'eval_metric': 'rmse',
        'eta': 0.3,
        'max_depth': 3,
        'min_child_weight': 1,
        'seed': 1,
        'verbosity': 0
    }

    model = xgb.train(params, dtrain, num_boost_round=60)
    y_pred = model.predict(dtest)
    rmse = root_mean_squared_error(y_test, y_pred)
    print(f"Test RMSE: {rmse:.2f}")

    with open("model.bin", "wb") as f_out:
        pickle.dump((dv, model), f_out)


if __name__ == "__main__":
    df = load_and_prepare_data()
    train_model(df)