[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/peCxHnxY)
# EE267_LAB0: Access Carla

Please refer to the instructions [here](https://docs.google.com/document/d/1PwzTUXI43FQObJ2Cy7xu3a_J-AEyEal76FWF_SttEhE/edit?usp=sharing)

## Files added

| File | Description |
|------|------------|
| `traffic_sim.py` | Runs a traffic simulation with vehicles and pedestrians. |
| `instance_segmentation.py` | Captures and saves instance segmentation output from CARLA. |
| `bounding_boxes.py` | Displays bounding boxes around detected actors within the simulation. |
| `bounding_boxes_export.py` | Exports bounding box images to disk for dataset generation. |

---

## How to Run

### On BCOE GPU Machines (with VirtualGL)
```bash
vglrun python <python_file>
```

### On Local Ubuntu Machine with CARLA Docker Image
```bash
python <python_file>
```

Replace `<python_file>` with one of:
- `traffic_sim.py`
- `instance_segmentation.py`
- `bounding_boxes.py`
- `bounding_boxes_export.py`

---

## Output Configuration

### For `bounding_boxes_export.py`
To change the output directory, edit:
```python
frame_path = 'output/%06d' % image.frame
image.save_to_disk(frame_path + '.png')
```
> Modify `'output/'` to your preferred folder (e.g., `data/bbox_output/`).

### instance_segmentation.py
To customize the save location:
```python
instance_image.save_to_disk('instance_segmentation.png')
```
> Example change: `instance_image.save_to_disk('results/seg/frame_%06d.png')`

