# CreditCardFraudDetection



## 项目结构
```text
CreditCardFraudDetection/  
├── data/                                   # 原始数据目录  
│   └── creditcard.csv                      # 原始数据文件  
├── notebooks/                              # 分析笔记本  
│   ├── 1_EDA.ipynb                         # 数据探索与可视化分析  
│   ├── 2_Modeling_Comparison.ipynb         # 多模型构建与评估（含SMOTE）  
│   └── 3_XGBoost_SHAP_Explain.ipynb        # XGBoost + SHAP 可解释性分析  
├── models/                                 # 训练好的模型文件  
│   ├── xgboost_model.pkl                   # 主力模型  
│   ├── lightgbm_model.pkl                  # LightGBM 模型  
│   ├── rf_model.pkl                        # 随机森林模型  
│   └── logreg_model.pkl                    # 逻辑回归模型  
├── output/                                 # 结果输出  
│   ├── confusion_matrix_xgb.png            # 混淆矩阵（XGBoost）  
│   ├── confusion_matrix_lgbm.png           # 混淆矩阵（LightGBM）  
│   ├── model_comparison_plot.png           # 多模型指标对比图  
│   ├── shap_summary_xgb.png                # SHAP 全局特征重要性  
│   ├── shap_waterfall_example.png          # 示例样本解释图（可选）  
│   └── roc_pr_curve_all_models.png         # ROC/PR 曲线（可选）  
├── main.py                                 # 模型加载与推理接口  
├── requirements.txt                        # 依赖库（xgboost/lightgbm/shap等）  
└── README.md                               # 项目说明与结果总结  
```

## License

This project is licensed under the GNU GPL v3 (see [LICENSE](./LICENSE)),  
with additional terms described in [LICENSE_ADDITIONAL](./LICENSE_ADDITIONAL).

本项目在 GNU GPL v3 许可下发布（详见 [LICENSE](./LICENSE)），  
附加条款见 [LICENSE_ADDITIONAL](./LICENSE_ADDITIONAL)。
