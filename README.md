# figure-defaults
A small library to create easy-to-manipulate default styles for matplotlib.

# Simple example

```python
import matplotlib.pyplot as plt
import figure_defaults
fd = figure_defaults.FigureDefaults(style='nature_dc')
plt.plot([0, 1])
plt.plot([1, 0], linewidth=fd.linewidth_narrow)
plt.figure()
fd.fontsize = 20
plt.plot([0, 1])
```
