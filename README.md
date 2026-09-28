# 🔬 SonicAnalytics Lab

<div align="center">

**Multimodal Auditory Cueing & Cognitive Workload Experimental Platform (HCI Dual-Task)**  
多模態音響提示與認知負荷實驗平台 ｜ 多モーダル音響提示と認知的負荷評価プラットフォーム

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED.svg)](https://www.docker.com/)
[![Audio API](https://img.shields.io/badge/Audio-Web_Audio_API-orange.svg)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)

### 🚀 [點此直接啟動線上實驗平台 (Live Demo)](https://peenlin.github.io/SonicAnalytics/)

[English](#-english) | [日本語](#-日本語) | [繁體中文](#-繁體中文)

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
- **Zero-Latency Sound Synthesis**: Native Web Audio API generates auditory stimuli programmatically without external audio file loading delays.
- **Ecological Preflight Validation**: Automated hardware heuristics detect pointer precision and multi-touch to block mobile devices and eliminate touchscreen latency bias.
- **Dual-Task Cognitive Assessment**:
  - Millisecond reaction time logging per stimulus trial.
  - Multi-dimensional NASA-TLX workload radar visualization.
  - Client-side real-time One-Way ANOVA ($F$-statistic) computation.
- **Resilient Backend Pipeline**: Headless ingestion via FastAPI (`/api/v1/submit`), schema-enforced with Pydantic, stored in SQLite, and containerized via Docker.

---

## 🇯🇵 日本語

### プロジェクト概要
**SonicAnalytics Lab** は、ヒューマンコンピュータインタラクション（HCI）および実験心理物理学向けに設計された二重課題（Dual-Task）認知的負荷評価プラットフォームです。高負荷タスク環境下において、異なる音響提示手法（純粋視覚、固定周波数ビープ音、動的変調音）が注意の狭窄（Cognitive Tunneling）および周辺アラートへの反応時間（Reaction Time）に与える影響を検証します。

### 主な機能
- **3段階自動実験プロトコル**：視覚単独条件 (30s) → 固定ビープ音 (30s) → 動的音響提示 (30s)。
- **Web Audio API によるゼロ遅延音声合成**：オシレーター（OscillatorNode）で直接波形を生成し、ロード遅延を完全排除。
- **ハードウェア事前検証**：タッチ端末・スマートフォンを自動検出し、ミリ秒精度の測定のためPC環境（物理キーボード）を強制。
- **認知的指標のリアルタイム解析**：各試行の反応時間計測、NASA-TLX 6次元レーダーチャート表示、一元配置分散分析（ANOVA）による $F$ 値算出。
- **堅牢なデータパイプライン**：FastAPI + SQLite + Docker によるデータ永続化。

---

## 🇹🇼 繁體中文

### 專案簡介
**SonicAnalytics Lab** 是一套專為人機互動（HCI）與實驗心理物理學打造的雙任務（Dual-Task）認知負荷評估平台。本實驗旨在探討於高心智負荷作業情境下，不同音響提示模態（純視覺、固定頻率蜂鳴、動態頻率調變音）對使用者注意力窄化（Cognitive Tunneling）與周邊警報反應時間（Reaction Time）之影響。

### 核心特性
- **三階段標準化實驗流程**：純視覺基準組 (30s) ➔ 固定逼逼聲組 (30s) ➔ 動態頻譜提示組 (30s)。
- **Web Audio API 原生音訊合成**：利用底層振盪器（OscillatorNode）實時合成音效，免除外部檔案載入延遲，確保微秒級實驗內部效度。
- **嚴格環境硬體偵測鎖定**：自動分析指針精度與觸控點，強制阻絕手機與平板裝置，排除觸控屏硬體延遲誤差。
- **即時認知指標運算**：毫秒級反應時間追蹤、NASA-TLX 六大心智維度雷達圖、前端即時單因子變異數分析（One-way ANOVA）。
- **輕量化高容錯後端**：FastAPI 結構化 API 接收、SQLite 本地持久化資料庫與 Docker 容器化配置。

---

### 檔案結構