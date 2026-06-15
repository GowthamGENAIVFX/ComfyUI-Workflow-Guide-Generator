# Architecture

## System Overview

Workflow Guide Generator consists of two major components.

### Backend Analysis Layer

Responsible for workflow inspection.

Components:

* WorkflowAnalyzer
* WorkflowPurposeEngine
* WorkflowDiagramEngine
* WorkflowInsightsEngine
* WorkflowFlowEngine
* ModelDiscoveryEngine
* ModelParameterEngine
* ModelExplanationEngine
* NodePurposeEngine

### Frontend Visualization Layer

Responsible for guide rendering.

Components:

* workflow_guide_node.js
* workflow_documentation_panel.js

## Workflow

Workflow JSON
↓
Workflow Analyzer
↓
Model Discovery
↓
Node Analysis
↓
Purpose Detection
↓
Flow Detection
↓
Documentation Generation
↓
Artist Guide Panel

## Backend Responsibilities

### WorkflowAnalyzer

Detects:

* Workflow type
* Complexity
* Input nodes
* Output nodes
* Dependencies

### WorkflowPurposeEngine

Generates workflow descriptions.

### WorkflowFlowEngine

Creates simplified workflow flow representations.

### ModelDiscoveryEngine

Detects:

* Models
* Encoders
* VAEs
* LoRAs
* ControlNets

### NodePurposeEngine

Provides artist-friendly node explanations.

## Frontend Responsibilities

### Workflow Guide Generator

User interaction entry point.

### Documentation Panel

Visual presentation layer.

Displays:

* Purpose
* Models
* Settings
* Workflow Flow
* Output
* Performance Tips
* Key Nodes

## Design Goals

* Artist Friendly
* Beginner Friendly
* Workflow Agnostic
* Fast Analysis
* Dynamic UI
* Minimal User Interaction
