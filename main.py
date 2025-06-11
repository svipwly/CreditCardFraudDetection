import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import recall_score, precision_score, f1_score, accuracy_score

def Standard_Scaler(df, col_names):
    features = df[col_names]
    scaler = StandardScaler().fit(features.values)
    features = scaler.transform(features.values)
    df[col_names] = features
    return df

def load_model(model_path):
    model = joblib.load(model_path)
    return model

def predict_and_score(data, model):
    col_names = ['Amount']
    data = Standard_Scaler(data, col_names)

    if 'Class' in data.columns:
        X_test = data.drop(columns='Class')
        y_test = data['Class']
        y_pred = model.predict(X_test)
        recall = recall_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Recall: {recall:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"F1 Score: {f1:.4f}")
        print(f"Accuracy: {accuracy:.4f}")
    else:
        X_test = data
        y_pred = model.predict(X_test)
        output = data.copy()
        output['Pred'] = y_pred
        output.to_csv('output/out.csv', index=False)
        print("预测结果已保存到 output/out.csv")
        print("预测标签：", y_pred)

def manual_input():
    feature_names = [
        'Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13',
        'V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount'
    ]
    input_data = []
    print("请依次输入以下参数：")
    for feat in feature_names:
        val = input(f"{feat}: ")
        input_data.append(float(val))
    data = pd.DataFrame([input_data], columns=feature_names)
    return data

def main():
    print("模型功能选择：1-从指定文件输入 2-手动输入")
    choice = input("请输入选择（1或2）：").strip()
    model = load_model("models/best_xgb_model.pkl")

    if choice == '1':
        data = pd.read_csv("data/test.csv")
        predict_and_score(data, model)
    elif choice == '2':
        data = manual_input()
        predict_and_score(data, model)
    else:
        print("输入有误，请输入1或2。")

if __name__ == "__main__":
    main()