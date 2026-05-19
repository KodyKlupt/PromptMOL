# Format bonds

The script **format_bonds** will automatically format bonds in amino acids.

##  Usage
 format_bonds [ selection [, bonds ]]

##  Examples
Image:PHE_valence_0.png|format_bonds bonds=1
Image:PHE_valence_1_mode_1.png|format_bonds bonds=2
Image:PHE_delocalized.png|format_bonds

```python
import format_bonds

frag PHE
format_bonds

format_bonds bonds=2
```
