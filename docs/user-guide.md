# User Guide

## Overview

Workflow Guide Generator automatically analyzes ComfyUI workflows and generates artist-friendly documentation.

The generated guide explains:

* What the workflow does
* Which models are used
* Important settings
* Workflow processing stages
* Output information
* Performance recommendations

## Using the Node

Add:

```text
Workflow Guide Generator
```

to your workflow.

Press:

```text
Generate Artist Guide
```

The extension will create a documentation panel.

## Workflow Purpose

Explains the primary objective of the workflow.

Examples:

* Flux Image Generation
* Video to EXR Conversion
* Image Upscaling
* Inpainting

## Models Used

Displays:

* Main Model
* Text Encoder
* Image Decoder
* LoRAs
* ControlNets

## Main Settings

Displays important generation parameters.

Examples:

* Sampler
* Scheduler
* Steps
* CFG
* Resolution

## Workflow Flow

Shows the workflow in simplified artist language.

Example:

Load Models
↓
Process Prompt
↓
Generate Image
↓
Save Result

## Performance Tips

Provides workflow-specific optimization recommendations.

## Key Nodes

Explains major nodes used by the workflow.

This section helps artists understand workflows without manually tracing node connections.
