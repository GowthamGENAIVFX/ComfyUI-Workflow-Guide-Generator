<div align="center">

<img src="assets/workflow_guide_generator_logo.png" width="120" alt="Workflow Guide Generator Logo">

# Workflow Guide Generator

### Artist Workflow Documentation Platform for ComfyUI

**Analyze • Understand • Explain • Document • Discover • Onboard • Visualize ComfyUI Workflows**

Workflow Purpose • Workflow Overview • Models Used • Main Settings • Workflow Flow • Performance Tips • Key Nodes Used

<p align="center">

<img src="https://img.shields.io/badge/ComfyUI-Compatible-green?style=flat-square">

<img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square">

<img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square">

<img src="https://img.shields.io/badge/Status-Active-success?style=flat-square">

<img src="https://img.shields.io/badge/Version-1.0.0-orange?style=flat-square">

</p>

<p align="center">
  <a href="#-installation">📥 Install</a>
  &nbsp;·&nbsp;
  <a href="#-artist-workflow-guide">📋 Workflow Guide</a>
  &nbsp;·&nbsp;
  <a href="#-analysis-engines">🧠 Engines</a>
  &nbsp;·&nbsp;
  <a href="#-documentation">📖 Documentation</a>
  &nbsp;·&nbsp;
  <a href="#-project-structure">🏗 Architecture</a>
  &nbsp;·&nbsp;
  <a href="#-roadmap">🛠 Roadmap</a>
  &nbsp;·&nbsp;
  <a href="#-contributing">🤝 Contributing</a>
</p>

</div>

---

<p align="center">
  <img src="assets/workflow-guide-preview.png" width="95%" alt="Workflow Guide Generator">
</p>

---

# 🚀 What is Workflow Guide Generator?

Workflow Guide Generator is an artist-focused workflow documentation platform built specifically for ComfyUI.

As workflows become larger and more complex, understanding what a workflow does becomes increasingly difficult.

Many shared workflows contain:

* Hundreds of nodes
* Multiple AI models
* Custom node packs
* Complex routing
* Little or no documentation

Workflow Guide Generator automatically analyzes workflows and generates an Artist Workflow Guide directly inside ComfyUI.

The generated guide helps artists understand workflows before modifying or executing them.

---

# 🎯 Key Features

### 🎯 Workflow Purpose

Automatically identifies workflow intent.

Provides:

* Workflow Type
* Workflow Purpose
* Workflow Description

---

### 📖 Workflow Overview

Generates a high-level explanation of the workflow.

Provides:

* Workflow Summary
* Workflow Context
* Workflow Complexity Overview

---

### 📥 Models Used

Automatically discovers workflow models.

Provides:

* Main Model
* Text Encoder
* Image Decoder

---

### ⚙ Main Settings

Extracts important workflow settings.

Provides:

* Sampler
* Scheduler
* Steps
* CFG
* Resolution
* Estimated VRAM

---

### 🗺 Workflow Flow

Converts technical workflows into understandable stages.

Example:

```text
Load Models
      ↓

Process Prompt
      ↓

Generate Image
      ↓

Build Final Image
      ↓

Save Result
```

---

### 🚀 Performance Tips

Generates workflow-specific optimization recommendations.

Provides:

* Rendering Tips
* Optimization Suggestions
* Workflow Recommendations

---

### 📋 Key Nodes Used

Explains important workflow nodes.

Provides:

* Node Purpose
* Workflow Role
* Artist-Friendly Explanations

---

# 📋 Artist Workflow Guide

Generated documentation includes:

```text
Workflow Purpose

Overview

Models Used

Main Settings

Workflow Flow

Output

Performance Tips

Key Nodes Used
```

The guide is generated automatically from workflow data and displayed directly inside ComfyUI.

---

# 🧠 Analysis Engines

Current Analysis Engines:

```text
Workflow Analyzer

Workflow Purpose Engine

Workflow Flow Engine

Workflow Diagram Engine

Workflow Insights Engine

Model Discovery Engine

Model Parameter Engine

Model Explanation Engine

Node Purpose Engine
```

---

# 🔄 Documentation Pipeline

```text
Workflow
      ↓

Workflow Analysis
      ↓

Workflow Type Detection
      ↓

Model Discovery
      ↓

Workflow Insights
      ↓

Workflow Flow Generation
      ↓

Node Purpose Analysis
      ↓

Documentation Generation
      ↓

Artist Workflow Guide
```

---

# 🎯 Supported Workflow Types

### Flux Workflows

* Flux Dev
* Flux Schnell
* Flux Variants

---

### Stable Diffusion Workflows

* SDXL
* SD 1.5
* SDXL Turbo

---

### ControlNet Workflows

* Pose
* Depth
* Canny
* OpenPose

---

### Image Editing Workflows

* Inpainting
* Outpainting
* Image Enhancement

---

### Upscaling Workflows

* ESRGAN
* AI Upscaling Pipelines

---

### Video Workflows

* Video Processing
* Frame Extraction
* Video Enhancement

---

### VFX Pipelines

* Video To EXR
* Sequence Generation
* Production Rendering

---

# 📂 Project Structure

```text
ComfyUI-Workflow-Guide-Generator/

├── backend/
│   ├── workflow_analyzer.py
│   ├── workflow_purpose_engine.py
│   ├── workflow_flow_engine.py
│   ├── workflow_insights_engine.py
│   ├── workflow_diagram_engine.py
│   ├── model_discovery_engine.py
│   ├── model_parameter_engine.py
│   ├── model_explanation_engine.py
│   └── node_purpose_engine.py
│
├── docs/
│   ├── installation-guide.md
│   ├── user-guide.md
│   ├── architecture.md
│   ├── node-explanations.md
│   ├── workflow-analysis-engine.md
│   ├── optimization-notes.md
│   ├── recruiter-overview.md
│   ├── business-value.md
│   ├── project-highlights.md
│   ├── technical-deep-dive.md
│   ├── faq.md
│   ├── changelog.md
│   ├── contributing.md
│   ├── portfolio-case-study.md
│   └── roadmap.md
│
├── assets/
├── backend/
├── web/
├── nodes/
│
├── LICENSE
├── requirements.txt
└── README.md
```

---

# 📖 Documentation

Detailed documentation is available in:

```text
docs/
```

Included Guides:

* Installation Guide
* User Guide
* Architecture
* Node Explanations
* Workflow Analysis Engine
* Technical Deep Dive
* Optimization Notes
* Recruiter Overview
* Business Value
* Project Highlights
* FAQ
* Changelog
* Roadmap

---

# 📥 Installation

Navigate to your ComfyUI custom nodes directory:

```bash
cd ComfyUI/custom_nodes
```

Clone the repository:

```bash
git clone https://github.com/GowthamGENAIVFX/ComfyUI-Workflow-Guide-Generator
```

Restart ComfyUI.

Open ComfyUI and search for:

```text
Workflow Guide Generator
```

Press:

```text
Generate Artist Guide
```

The documentation panel will be generated automatically.

---

# 💡 Example Use Cases

### Workflow Onboarding

Help artists understand workflows instantly.

### Workflow Documentation

Automatically document workflow libraries.

### Team Collaboration

Share workflows with built-in explanations.

### Production Pipelines

Improve maintainability of workflow assets.

### Educational Workflows

Teach workflow design to new users.

### Workflow Auditing

Review workflow functionality before modification.

---

# 👥 Designed For

✅ ComfyUI Artists

✅ AI Engineers

✅ Technical Artists

✅ Workflow Designers

✅ VFX Professionals

✅ Content Creators

✅ Production Teams

---

# 🔒 Privacy

Workflow Guide Generator runs entirely within your local ComfyUI environment.

* No workflow uploads
* No cloud processing
* No external analysis services
* No workflow data sharing

All analysis remains local.

---

# 🛠 Roadmap

Future planned enhancements:

* Documentation Export
* PDF Reports
* Markdown Export
* Interactive Documentation
* Workflow Visualization
* Workflow Comparison
* Expanded Workflow Recognition

---

# 🤝 Contributing

Contributions are welcome.

Areas for contribution:

* Workflow Analysis Improvements
* New Workflow Types
* Node Explanation Enhancements
* Documentation Improvements
* UI Enhancements
* Performance Optimizations

---

# 📄 License

MIT License

See the LICENSE file for complete details.

---

# ⭐ Workflow Guide Generator

### Making Every ComfyUI Workflow Understandable

Workflow Documentation • Workflow Understanding • Model Discovery • Artist Onboarding • Workflow Intelligence
