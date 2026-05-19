# Transparency

##  Overview
- *Transparency** is used to adjust the transparency of **Surfaces** and **Slices**.  (For other transparencies in PyMOL, see Cartoon Transparency, Sphere Transparency, and Stick Transparency.

## Usage
```python
set transparency, F, selection
```

where **F** is a floating point number in the range *[0.0 - 1.0]*, where **selection** is the selected surface to apply the change to (for examples, see below).

For the value of *F*, 1.0 will be an invisible and 0.0 a completely solid surface.

## Examples
### Whole Surface
Change the transparency of the whole surface to 50%.

```python
1. show all surfaces with 50% transparency.
set transparency, 0.5
```

Image: Surf065.png | Image showing partial surface transparencies
Image: Surfall_065.png | Image showing 100% of the surface with 65% transparency.

### Selected Surface Elements
Simple example showing how to do partial surface transparency.  This allows different selections to have different transparencies on the same object (or also on different objects).

```python
1. load a random protein
fetch 1rty

1. set the partial transparency for the selected residues
set transparency, 0.65, i. 1-100
```

Image:Diffy_transp.png|Different transparency settings on different objects.
Image:Diffy_transp2.png|Different transparency settings on the same object.
