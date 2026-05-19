# Sphere transparency

= Overview =
set sphere_transparency is used to adjust the transparency of spheres!

```python
set sphere_transparency, 0.5
```

or

```python
set sphere_transparency=0.5, selection
```

Where 1.0 is invisible and 0.0 completely solid

= Examples =

Image:Sphere transparency ex1.png|Example of transparent spheres
Image:Sphere transparency ex3.png|Example of transparent spheres

These images were made through the following script:

```python
fetch 1ifr; color wheat; hide; show spheres;
color red, i. 506-509;
color marine, byres all within 5 of color red;
set sphere_transparency,0.5,color marine;
```
