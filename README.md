# 営業KPI分析プロジェクト - Sales KPI Insight

## 🎯 目的
営業現場でよくある「数字を追っているのに結果が出ない」という課題に対し、  
営業メンバーごとのKPIデータ（アポ数・商談数・成約率）と顧客属性（業種・企業規模・地域）を分析し、  
成約率を左右する要因を特定することで、営業戦略や配属方針の改善に貢献することを目的としたプロジェクトです。

Streamlitを用いたダッシュボードにより、営業マネージャーがKPIを俯瞰・比較し、戦略判断に活用できる仕組みを構築しました。  
非エンジニアでも使いやすいことを重視し、軽量で即公開可能な **Streamlit** を採用しています。

## 🧑‍💻 使用技術・構成

| 分類 | 使用技術 | 理由・特徴 |
|------|-----------|-------------|
| 言語 | Python / SQL | 分析・集計・ETL処理の基本として |
| 可視化 | matplotlib / seaborn / Streamlit | 分析・ダッシュボードに活用 |
| バージョン管理 | GitHub | プロジェクト管理・アウトプット |
| ドキュメント | Qiita | 分析ストーリーと示唆の記録 |
| インフラ | ローカル + Streamlit Cloud | シンプルに公開できる構成 |

## 🧩 ER図

sales (営業)
├─ sales_id (PK)
├─ name
├─ age
├─ years_of_exp
├─ num_appointments
├─ num_negotiations
└─ num_successes

clients (顧客)
├─ client_id (PK)
├─ industry
├─ company_size
├─ region
└─ result (1: 成約 / 0: 失注)

activities (営業活動ログ)
├─ activity_id (PK)
├─ date
├─ sales_id (FK)
├─ client_id (FK)
└─ status

## インフラ構成図
[CSVデータ] → [Python / pandas処理] → [Streamlitダッシュボード] → [ローカル or Cloudで公開]

## 📊 分析対象データ（すべて擬似データ / 自作CSV）

- `sales.csv`：営業ごとのKPI（アポ・商談・成約数＋属性）
- `clients.csv`：顧客の業界、規模、地域、成否
- `activities.csv`：日付別の活動履歴

## 🔍 仮説リスト

- 営業個人の「数」ではなく「相性」が成否を分けているのでは？
- 営業経験が短い人ほど業界ごとの向き不向きがあるのでは？
- 午前中より午後の方がCV率が高いのでは？

## 💡 得られた示唆（例）

- 商談数が多い＝成約率が高い、とは限らない（むしろ逆転する場合あり）
- 小規模企業・IT業界に対して強い営業担当が存在
- 問い合わせ実施時間帯がCV率に影響（午後の方が高い傾向）
- 
## 🖥 Streamlitダッシュボード

- 営業別KPIサマリー（棒グラフ・CV率ソート）
- 業界別成約率ヒートマップ
- 顧客属性（業界×規模×地域）別の傾向分析
- 時間帯別の問い合わせ成果分析

👉 **[デモはこちら](https://your-app-link)**  
👉 ![dashboard gif](demo.gif)

## 🧠 工夫した点・チャレンジ技術

- データスキーマ設計からKPI定義・加工までを自分で設計
- SQL（JOIN・GROUP BY）とpandas処理を併用し、複雑な集計にも対応
- Streamlitでインタラクティブなフィルタを導入（営業別・業界別切り替え）
- READMEにER図・構成図・デモGIFを掲載し、ドキュメント力を強く意識

## 📂 ディレクトリ構成

sales-kpi-analysis/
├── data/
│   ├── raw/              # 擬似元データ（CSV）
│   └── processed/        # 加工後データ
├── notebooks/
│   └── 01_analysis.ipynb # 仮説検証・可視化用ノートブック
├── streamlit_app/
│   ├── app.py            # ダッシュボード本体
│   └── components.py     # グラフ描画関数など
├── er_diagram.png        # ER図
├── demo.gif              # ダッシュボード操作GIF
├── README.md
└── requirements.txt      # pandas, streamlit など


## 📝 今後の展望

- 顧客との商談内容（テキストログ）を使った自然言語解析の導入
- 成約予測モデルの構築（回帰/分類）
- Looker StudioやTableauを使ったBI連携の模擬開発
python -m etl.run_etl --input data/raw --output data/processed --db db/app.sqlite --table kpi_mart


[GitHub](https://github.com/flopsy212) / [Qiita](https://qiita.com/flopsy_tech)

