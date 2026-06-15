# Installation Guide

## Requirements

* ComfyUI
* Python 3.10+
* Latest ComfyUI Frontend

## Installation

### Step 1

Navigate to your ComfyUI custom_nodes folder.

```text
ComfyUI/custom_nodes/
```

### Step 2

Clone the repository.

```bash
git clone https://github.com/yourusername/ComfyUI-Workflow-Guide-Generator.git
```

### Step 3

Restart ComfyUI.

The extension automatically registers:

* Workflow Guide Generator
* Workflow Documentation Panel

### Step 4

Launch ComfyUI.

Navigate to:

```text
Workflow Documentation
```

You should now see:

* Workflow Guide Generator

## Updating

Pull the latest changes.

```bash
git pull
```

Restart ComfyUI.

## Troubleshooting

### Documentation panel not appearing

Verify:

* JavaScript files loaded correctly
* Browser cache cleared
* ComfyUI restarted

### Workflow analysis fails

Verify:

* Workflow JSON is valid
* Nodes are properly connected
* Workflow contains supported node types

### Frontend issues

Perform a hard refresh.

```text
CTRL + F5
```
