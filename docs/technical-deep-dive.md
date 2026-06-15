# Technical Deep Dive

## Architecture

Workflow Guide Generator consists of:

### Backend Analysis Layer

Components:

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

## Analysis Pipeline

Workflow JSON
↓
Workflow Classification
↓
Model Discovery
↓
Node Analysis
↓
Flow Generation
↓
Documentation Generation
↓
Frontend Rendering

---

## Workflow Classification Logic

The system detects workflows using node pattern recognition.

Examples:

### Flux Workflow

Detected by:

* Flux Nodes
* UNET Loader
* KSampler

### ControlNet Workflow

Detected by:

* ControlNet Loader
* Apply ControlNet

### Video Workflow

Detected by:

* VHS Nodes
* Video Processing Nodes

---

## Frontend Architecture

### Workflow Guide Node

User interaction layer.

### Documentation Panel

Visualization layer.

### Dynamic Layout System

Automatically sizes documentation panels based on content length.

---

## Design Goals

* Fast Analysis
* Low Memory Usage
* Artist-Friendly Output
* Workflow Agnostic Architecture
* Extensible Engine Design
