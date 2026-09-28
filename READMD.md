# 🔬 SonicAnalytics Lab

<div align="center">

**Multimodal Auditory Cueing & Cognitive Workload Experimental Platform (HCI Dual-Task)**

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED.svg)](https://www.docker.com/)
[![Audio API](https://img.shields.io/badge/Audio-Web_Audio_API-orange.svg)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## 🌐 English

### Project Overview
**SonicAnalytics Lab** is a web-based Human-Computer Interaction (HCI) dual-task experimental platform designed to evaluate human cognitive workload, attentional tunneling, and peripheral response latency under varying auditory modalities. 

Participants perform a central visual working memory task (`J`/`K` discrimination) while simultaneously reacting to sporadic peripheral visual/auditory alerts (`Spacebar`). The system captures millisecond-precision reaction times, collects subjective workload metrics via NASA-TLX scales, and performs on-the-fly statistical inferencing.

### Key Capabilities
- **Three-Condition Automated Protocol**:
  - `Condition 1`: Visual Only baseline (30s)
  - `Condition 2`: Static 440Hz Square-wave Beep cueing (30s)
  - `Condition 3`: Dynamic Synthesized Audio cueing (620Hz → 950Hz Sine sweep, 30s)
- **Zero-Latency In-Browser Sound Synthesis**: Native Web Audio API generates auditory stimuli programmatically without external asset loading delays.
- **Strict Ecological Preflight Validation**: Automated hardware heuristics reject mobile and touchscreen environments to eliminate tactile input latency bias.
- **Dual-Task Cognitive Assessment**:
  - Millisecond reaction time logging per stimulus trial.
  - Multi-dimensional NASA-TLX workload radar visualization (Mental, Physical, Temporal, Performance, Effort, Frustration).
  - Real-time One-Way ANOVA ($F$-statistic) computation directly inside the browser client.
- **Resilient Backend Pipeline**: Headless ingestion via FastAPI (`/api/v1/submit`), schema-enforced with Pydantic, stored in SQLite, and containerized via Docker for lightweight self-hosted deployments.
- **Multilingual Support**: Fully localized in English, Japanese, and Traditional Chinese.

### System Architecture
[Browser Client: index.html]
├── Device & Keyboard Latency Precheck
├── Dual-Task Stimulus Loop (Working Memory + Peripheral Alert)
├── Web Audio API Real-time Oscillator (Static vs. Dynamic Sweep)
├── NASA-TLX Interactive Radar (Chart.js)
└── Client-Side Real-Time One-way ANOVA
↓ JSON Payload (CORS REST API)
[Backend Node: main.py (FastAPI)]
├── Pydantic Schema Validation (Subject ID, Trials, TLX Scores)
└── SQLite Persistence (experiment_records table)
#### 1. Client-Side Only (Standalone Mode)
Simply double-click `index.html` in any desktop browser. Completed trials can be downloaded locally as `data_sample.csv`.

#### 2. Full-Stack Ingestion Server (Docker)
```bash
# Build Docker image
docker build -t sonicanalytics-api .

# Run API server on port 8000
docker run -d -p 8000:8000 --name sonicanalytics sonicanalytics-api
---

### 2. 日本語 (`README_ja.md`)

```markdown
# 🔬 SonicAnalytics Lab

<div align="center">

**多モーダル音響提示と認知的負荷評価プラットフォーム (HCI Dual-Task)**

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED.svg)](https://www.docker.com/)
[![Audio API](https://img.shields.io/badge/Audio-Web_Audio_API-orange.svg)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## 🇯🇵 日本語

### プロジェクト概要
**SonicAnalytics Lab** は、ヒューマンコンピュータインタラクション（HCI）および実験心理物理学向けに設計された二重課題（Dual-Task）認知的負荷評価プラットフォームです。高負荷タスク環境下において、異なる音響提示手法（純粋視覚、固定周波数ビープ音、動的変調音）が注意の狭窄（Cognitive Tunneling）および周辺アラートへの反応時間（Reaction Time）に与える影響を検証します。

被験者は中央の視覚ワーキングメモリ弁別タスク（J/K キー）を遂行しながら、周辺に突発的に発生する警告に対して最短時間で応答（Space キー）します。

### 主な機能と特徴
- **3段階自動実験プロトコル**：
  - `条件1`：視覚単独基準条件（30秒）
  - `条件2`：固定ビープ音提示（440Hz 矩形波、30秒）
  - `条件3`：動的音響提示（620Hz〜950Hz 正弦波スウィープ、30秒）
- **Web Audio API によるゼロ遅延音声合成**：ブラウザネイティブのオシレーター（OscillatorNode）で動的に音声を合成し、音源ロード遅延を完全に排除。ミリ秒精度の内的妥当性を担保。
- **厳密なハードウェア事前検証（Preflight Check）**：タッチデバイス・スマートフォンを自動検出しアクセスをブロック。物理キーボード環境のみを許可し、入力遅延バイアスを排除。
- **認知的指標のリアルタイム解析**：
  - 各試行ごとのミリ秒単位反応時間（RT）追跡。
  - NASA-TLX 多次元負荷レーダーチャート（精神的要求、身体的要求、時間的切迫、作業成績、努力度、フラストレーション）。
  - クライアント側でリアルタイムに一元配置分散分析（One-way ANOVA）を実行し、$F$ 統計量を算出。
- **高耐障害性バックエンド**：FastAPI による JSON ペイロード受信、Pydantic バリデーション、SQLite 永続化、Docker コンテナ化対応。プライベートサーバーや NAS への即時展開が可能。
- **3言語完全ローカライズ**：日本語、英語、繁体字中国語に対応。

### 構成ファイル
SonicAnalytics_Lab/
├── index.html        # 実験フロントエンド (Web Audio、NASA-TLX、分散分析)
├── main.py           # FastAPI バックエンド & SQLite データベース
├── Dockerfile        # Python 3.11 コンテナ設定
├── data_sample.csv   # 実験サンプルデータ
└── README.md         # プロジェクト技術ドキュメント

3. 繁體中文 (README_zh.md)
Markdown
# 🔬 SonicAnalytics Lab

<div align="center">

**多模態音響提示與認知負荷實驗平台 (HCI Dual-Task)**

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED.svg)](https://www.docker.com/)
[![Audio API](https://img.shields.io/badge/Audio-Web_Audio_API-orange.svg)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## 🇹🇼 繁體中文

### 專案簡介
**SonicAnalytics Lab** 是一套專為人機互動（HCI）與實驗心理物理學打造的雙任務（Dual-Task）認知負荷評估平台。本實驗旨在探討於高心智負荷作業情境下，不同音響提示模態（純視覺、固定頻率蜂鳴、動態頻率調變音）對使用者注意力窄化（Cognitive Tunneling）與周邊警報反應時間（Reaction Time）之影響。

受試者需同時執行中央視覺工作記憶比對任務（J/K 鍵），並對周邊偶發警告做出最快即時反應（Space 鍵）。

### 核心特性
- **三階段標準化實驗流程**：
  - `階段一`：純視覺基準組（30 秒）
  - `階段二`：固定頻率逼逼聲組（440Hz 方波，30 秒）
  - `階段三`：動態頻譜提示組（620Hz 至 950Hz 動態上升正弦波，30 秒）
- **Web Audio API 原生音訊合成**：利用瀏覽器底層振盪器（OscillatorNode）實時合成音效，免除音訊載入延遲，確保微秒級實驗內部效度。
- **嚴格環境硬體偵測鎖定**：自動分析指針精度（Pointer coarse/fine）與觸控點，強制阻絕手機與平板裝置，排除觸控屏硬體延遲誤差。
- **即時認知指標運算**：
  - 毫秒級周邊反應時間（RT）追蹤與統計。
  - NASA-TLX 六大心智維度疊合雷達圖（精神需求、身體需求、時間急迫感、自我績效、努力程度、挫折感）。
  - 前端即時單因子變異數分析（One-way ANOVA）計算 $F$ 檢定統計量。
- **輕量化高容錯後端**：採用 FastAPI 架構接收標準化 JSON 酬載，結合 SQLite 本地持久化資料庫與 Docker 容器化配置，支援 NAS 或私有伺服器快速部署。
- **三語系國際化架構**：完整支援繁體中文、English、日本語介面切換與專屬量表規範。

### 檔案結構
SonicAnalytics_Lab/
├── index.html        # 前端實驗本體 (含 Web Audio、NASA-TLX 雷達圖、ANOVA 運算)
├── main.py           # FastAPI 資料接收後端與 SQLite 入庫
├── Dockerfile        # 輕量 Python 3.11 容器配置
├── data_sample.csv   # 受試者實驗數據樣本
└── README.md         # 專案研究說明文件