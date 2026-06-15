# Architecture

## High-Level Architecture

Workflow Guide Generator converts workflow JSON into artist-friendly documentation.

Workflow JSON
↓
Workflow Analysis
↓
Model Discovery
↓
Workflow Classification
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

---

# Backend Components

## WorkflowAnalyzer

Responsible for:

* Workflow Type Detection
* Complexity Analysis
* Input Detection
* Output Detection
* Workflow Stage Discovery

---

## WorkflowPurposeEngine

Responsible for:

* Workflow Purpose Generation
* Workflow Overview Generation

---

## WorkflowFlowEngine

Responsible for:

* Workflow Stage Generation
* Artist-Friendly Workflow Flow

---

## WorkflowInsightsEngine

Responsible for:

* Settings Extraction
* Resolution Detection
* Sampler Detection
* Scheduler Detection

---

## ModelDiscoveryEngine

Responsible for:

* Main Model Detection
* Text Encoder Detection
* Image Decoder Detection

---

## NodePurposeEngine

Responsible for:

* Node Explanation Generation
* Artist-Friendly Descriptions

---

# Frontend Components

## Workflow Guide Generator Node

Entry point for documentation generation.

Provides:

* Generate Artist Guide button

---

## Documentation Panel

Displays:

* Workflow Purpose
* Overview
* Models Used
* Main Settings
* Workflow Flow
* Output
* Performance Tips
* Key Nodes Used

---

# Design Principles

* Simplicity
* Clarity
* Artist Focus
* Fast Rendering
* Local Execution
