# Technical Deep Dive

## Overview

Workflow Guide Generator is a ComfyUI extension that analyzes workflow JSON and converts technical workflow structures into artist-friendly documentation.

The extension operates entirely locally within ComfyUI and does not execute workflow nodes during analysis.

---

# System Architecture

The project consists of two layers:

## Backend Analysis Layer

Responsible for:

* Workflow Analysis
* Workflow Classification
* Model Discovery
* Workflow Flow Generation
* Node Purpose Analysis
* Documentation Generation

Core Components:

* WorkflowAnalyzer
* WorkflowPurposeEngine
* WorkflowFlowEngine
* WorkflowInsightsEngine
* WorkflowDiagramEngine
* ModelDiscoveryEngine
* ModelParameterEngine
* ModelExplanationEngine
* NodePurposeEngine

---

## Frontend Presentation Layer

Responsible for:

* Workflow Guide Generation
* Documentation Rendering
* Dynamic Layout
* Artist Workflow Guide UI

Core Components:

* workflow_guide_node.js
* workflow_documentation_panel.js

---

# Analysis Pipeline

Workflow JSON
↓
Workflow Analyzer
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
Documentation Assembly
↓
Artist Workflow Guide

---

# Workflow Classification

The analyzer uses node pattern detection.

Examples:

### Flux Workflow

Detected by:

* UNETLoader
* Flux-specific nodes

---

### ControlNet Workflow

Detected by:

* ControlNetLoader
* ApplyControlNet

---

### Inpainting Workflow

Detected by:

* Mask nodes
* Inpainting nodes

---

### Video Workflow

Detected by:

* VHS_LoadVideo
* Video processing nodes

---

### Video To EXR Workflow

Detected by:

* VHS_LoadVideo
* SaveEXRFrames

---

# Dynamic Documentation Panel

The panel automatically:

* Wraps text
* Calculates content height
* Resizes sections
* Adjusts overall node height

This ensures all generated content remains visible regardless of workflow size.

---

# Design Goals

* Artist Friendly
* Fast Analysis
* Minimal Configuration
* Workflow Agnostic
* Local Execution
* Easy Maintenance
