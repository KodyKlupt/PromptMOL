# Chem comp cartn use

The chem_comp_cartn_use setting selects with coordinate columns to load from an mmCIF chemical component file.

- New in PyMOL 2.1 and Open-Source revision 4184*

{|class="wikitable"
!Value
!Column Labels
|-
| 0
| Use first available (default)
|-
| 1
| _chem_comp_atom.pdbx_model_Cartn_{x,y,z}_ideal
|-
| 2
| _chem_comp_atom.model_Cartn_{x,y,z}
|-
| 4
| _chem_comp_atom.{x,y,z}
|}

##  Example
 set chem_comp_cartn_use, 1
 load http://files.rcsb.org/ligands/download/HEM.cif, hem_ideal

 set chem_comp_cartn_use, 2
 load http://files.rcsb.org/ligands/download/HEM.cif, hem_model

 align hem_ideal, hem_model
