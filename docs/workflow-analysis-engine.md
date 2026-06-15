# Workflow Analysis Engine

## Overview

The Workflow Analysis Engine is the core intelligence layer of Workflow Guide Generator.

It inspects workflow JSON and extracts meaningful information without executing the workflow.

---

# Responsibilities

The analyzer detects:

* Workflow Type
* Node Count
* Link Count
* Input Nodes
* Output Nodes
* Complexity
* Workflow Stages
* Branching
* Dependencies

---

# Workflow Classification

Supported workflow categories:

## Flux Workflow

Detected when:

* UNETLoader exists
* Flux-specific nodes exist

Produces:

* AI image generation documentation

---

## ControlNet Workflow

Detected when:

* ControlNet nodes exist

Produces:

* Guided image generation documentation

---

## Inpainting Workflow

Detected when:

* Mask nodes exist

Produces:

* Image editing workflow documentation

---

## Video Workflow

Detected when:

* Video nodes exist

Produces:

* Frame processing documentation

---

## Video To EXR Workflow

Detected when:

* VHS_LoadVideo exists
* SaveEXRFrames exists

Produces:

* Professional VFX workflow documentation

---

## Complexity Detection

### Simple

Less than 10 nodes.

### Medium

10–29 nodes.

### Complex

30+ nodes.

---

# Workflow Stages

Each node contributes to workflow stages.

Example:

Load Model
↓
Encode Prompt
↓
Generate Image
↓
Decode Image
↓
Save Result

---

# Benefits

Artists can understand:

* What the workflow does
* How data flows
* Which components are important
* Where modifications can be made

without manually inspecting every node.
