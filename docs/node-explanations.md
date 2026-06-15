# Node Explanations

## Purpose

The Node Explanation Engine converts technical ComfyUI node names into artist-friendly descriptions.

Many workflows contain dozens or hundreds of nodes. New artists often struggle to understand their purpose. This engine translates node functionality into simple workflow language.

---

# Model Loading Nodes

## UNETLoader

Purpose:

Loads the primary AI image generation model used by Flux workflows.

Artist View:

This is the main AI brain that generates the image.

---

## CheckpointLoader

Purpose:

Loads a Stable Diffusion checkpoint.

Artist View:

The primary model responsible for image creation.

---

## CLIPLoader

Purpose:

Loads the text encoder.

Artist View:

Converts prompts into instructions understood by the AI.

---

## VAELoader

Purpose:

Loads the image decoder.

Artist View:

Converts generated latent information into a visible image.

---

# Generation Nodes

## KSampler

Purpose:

Performs diffusion sampling.

Artist View:

The actual image generation process.

---

## KSamplerAdvanced

Purpose:

Advanced diffusion sampling controls.

Artist View:

Provides additional control over image generation quality.

---

# Input Nodes

## LoadImage

Purpose:

Loads source images.

Artist View:

Brings external images into the workflow.

---

## VHS_LoadVideo

Purpose:

Loads videos and extracts frames.

Artist View:

Imports video footage for processing.

---

# Guidance Nodes

## ControlNetLoader

Purpose:

Loads ControlNet models.

Artist View:

Adds reference guidance to generation.

---

## ApplyControlNet

Purpose:

Applies ControlNet information.

Artist View:

Controls pose, depth, composition, or structure.

---

# Enhancement Nodes

## UpscaleModelLoader

Purpose:

Loads image enhancement models.

Artist View:

Improves resolution and detail.

---

## ImageUpscaleWithModel

Purpose:

Performs image upscaling.

Artist View:

Creates larger and sharper images.

---

# Output Nodes

## SaveImage

Purpose:

Exports PNG images.

Artist View:

Saves the final result.

---

## SaveEXRFrames

Purpose:

Exports EXR sequences.

Artist View:

Creates professional VFX-ready image sequences.
