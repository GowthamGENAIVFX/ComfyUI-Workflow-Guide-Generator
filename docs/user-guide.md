# User Guide

## Overview

Workflow Guide Generator automatically analyzes ComfyUI workflows and creates an Artist Workflow Guide.

The generated guide helps artists understand workflows before modifying or executing them.

---

## Using the Node

Add:

Workflow Guide Generator

to your workflow.

Press:

Generate Artist Guide

The documentation panel will be generated automatically.

---

## Generated Sections

### Workflow Purpose

Explains what the workflow is designed to do.

---

### Overview

Provides a concise summary of workflow functionality.

---

### Models Used

Displays:

* Main AI Model
* Text Encoder
* Image Decoder

---

### Main Settings

Displays:

* Sampler
* Scheduler
* Steps
* CFG
* Resolution

---

### Workflow Flow

Shows simplified workflow stages.

Example:

Load Models
↓
Process Prompt
↓
Generate Image
↓
Build Final Image
↓
Save Result

---

### Output

Displays the workflow output type.

Examples:

* PNG Image
* EXR Sequence
* Video Output

---

### Performance Tips

Provides optimization recommendations.

---

### Key Nodes Used

Explains important workflow nodes in artist-friendly language.

---

## Supported Workflow Types

* Flux
* Stable Diffusion
* ControlNet
* Inpainting
* Upscaling
* Video Processing
* Video to EXR
