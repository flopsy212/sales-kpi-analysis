# sales-kpi-analysis

# 営業KPI分析プロジェクト - Sales KPI Insight

## 🔍 プロジェクト概要
成約率に差がある営業メンバーのKPIデータをもとに、
行動傾向や顧客属性との関係を分析し、改善の示唆を行う。

## 🎯 課題と仮説
- 成約率が高い人は「特定業界」に強いのでは？
- 商談数が少ない人の成約率はどうか？
- 担当顧客の規模・エリアが影響している可能性？

## 📊 分析対象データ
- `sales.csv`：営業ごとのアポ数、商談数、成約数
- `clients.csv`：顧客の業種、規模、地域
- `activities.csv`：各営業の活動ログ（日時、顧客、商談内容など）

## 🛠 使用技術
- Python（pandas, matplotlib, seaborn）
- SQL（BigQuery風のJOIN集計も一部想定）
- Streamlit（簡易BIダッシュボード風に）

## 🧠 得られたインサイト（抜粋）
- 【仮説①】が〇〇で裏付けられた
- 商談数が少なくても特定業種には強い営業がいる
- エリア別の成約率に偏りがあった → テリトリー配分の見直し提案

## 🖥 ダッシュボードイメージ
（Streamlitの画面キャプチャ or 動画リンク）

## 📚 分析ストーリー詳細
（notebooks/01_analysis.ipynb に記載）

## 🗂 ディレクトリ構成
sales-kpi-analysis/
├── data/
│   ├── raw/              ← 擬似元データ（CSVなど）
│   └── processed/        ← 加工済データ
├── notebooks/
│   └── 01_analysis.ipynb ← 仮説検証・可視化ノート
├── streamlit_app/
│   ├── app.py            ← ダッシュボード本体
│   └── components.py     ← グラフや関数（分離も可）
├── er_diagram.png        ← ER図（構想段階でも可）
├── README.md             ← 背景・仮説・構成・結果まとめ
└── requirements.txt      ← pandas, streamlitなど依存関係

[GitHub](https://github.com/flopsy212) / [Qiita](https://qiita.com/flopsy_tech)
