# SonicAnalytics Lab: Multimodal Auditory & Cognitive Load Platform (HCI Dual-Task)

A web-based interactive psychophysical and human-computer interaction (HCI) evaluation platform designed to quantify cognitive load and situational awareness under dual-task conditions using adaptive auditory feedback.

---

## 📌 Overview / 概要

In modern high-workload and visually demanding environments, visual-only feedback often leads to cognitive overload and delayed reaction times. **SonicAnalytics Lab** is an empirical HCI experimentation tool that explores how multimodal auditory feedback (static vs. dynamic auditory cues) affects cognitive performance, response latency, and mental workload.

現代の視覚情報過多なタスク環境において、視覚提示への過度な依存は認知負荷（Cognitive Overload）を著しく増大させます。**SonicAnalytics Lab** は、聴覚刺激（静的音響提示・動的音響フィードバック）が人間の認知負荷や状況認識に与える影響を定量的に検証・評価するための HCI 二重課題（Dual-Task）実験プラットフォームです。

---

## 🔬 Key Experimental Features / 実験機能

1. **HCI Dual-Task Paradigm (二重課題実験パラダイム)**:
   - **Primary Task**: Visual matching task requiring sustained visual attention.
   - **Secondary Task**: Auditory/visual alert reaction task measuring situational response latency.
2. **Three Experimental Conditions (3つの比較実験条件)**:
   - `Condition 1`: Visual Only (Baseline)
   - `Condition 2`: Visual + Static Beep
   - `Condition 3`: Visual + Dynamic Audio Feedback (Adaptive Spectral Mapping)
3. **Cognitive Workload & Statistical Assessment (定量的認知負荷・統計解析)**:
   - Real-time Reaction Time (Mean RT) tracking.
   - **NASA-TLX 6-Dimension Workload Assessment**: Visualized via interactive radar chart (Mental, Physical, Temporal, Performance, Effort, Frustration).
   - Automated inferential statistics (**One-way ANOVA / F-Test**) for cross-condition validation.
   - One-click dataset export (`.csv`) for psychometric and behavioral data pipelines.

---

## 🛠️ System Architecture & Tech Stack / システム構成

- **Frontend / UI**: Streamlit (Reactive Web Interface, Multilingual Support: 繁體中文 / English / 日本語)
- **Backend / Real-time Processing**: Python (NumPy, SciPy, Pandas, Statsmodels)
- **Deployment**: Docker Containerized, compatible with cloud/local hosting

---

## 🎯 Research Applications / 修士研究への展開

- **Auditory Display & Sonification**: Designing optimal auditory cues to reduce mental workload without inducing acoustic fatigue.
- **Cognitive Ergonomics & Assistive Tech**: Sensory substitution and multimodal interaction design for visually restricted environments.
- **Human-in-the-Loop Evaluation**: Combining subjective scales (NASA-TLX) with physiological/behavioral telemetry for robust user studies.

---

## 👤 Author / 開発者

- **Pei-En Lin (林 沛恩)**
- Background: Music & Computer Science (National Tsing Hua University)
- Contact: [0979641610pn@gmail.com]
