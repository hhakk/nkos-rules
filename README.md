# nkos-rules
Python code to create all the rules from "New Kind of Science" by Stephen Wolfram

![Example](example.gif)

## Dependencies

### Python

* NumPy 1.18.4

### External (to batch create videos)

* GNU parallel
* ffmpeg

## Usage

```
python rule.py <rule_number> <size_x> <size_y> <steps>

rule_number - number of rule
size_x, size_y - Canvas size
steps - How many steps to compute, must be < size_y

```

Alternatively, create all rules as webm videos with ffmpeg (Linux)

```
bash run_all.sh
```
