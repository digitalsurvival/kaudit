## Disclaimer

The following goals are a rough sketch of what *could* be done in a timely manner but are subject to change at any moment. :D

## Goals

### 0.4.0

### 0.3.0
* Be able to parse `.config` file for specific values.
* * If someone wants to check for btrfs, provide a true value confirming kernel support for btrfs.

### 0.2.0
* Extract and generate a beautiful HTML table of the standard feature set for the currently running kernel.
* This would be helpful for stager or other tools that will display information to the end user.

### 0.1.0
* Check for `/proc/config.gz` file.
* Appropriate output if the file doesn't exist or is inaccessible.
* Be able to detect and decode different types of compression for kernel `.config` files (gz, bz2, xz) and plain text.
* If /proc/config doesn't exist fall back to gathering `/proc` for data.

### 0.0.1
* Create a simple command-line interface using argparse.
* Do logging using Python's logging module.
* 
