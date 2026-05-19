# Cif use auth

When loading **mmCIF** structure files, the cif_use_auth setting (default: on) controls whether the **auth_*** fields are used or not.

- New in PyMOL 1.7.8*

With the PDBx/mmCIF format, the PDB introduced new residue and chain numbering schemes. The numbering which is found in PDB files is available in mmCIF files from the **auth_*** fields. The new numbering, which for example has no insertion codes and strictly increments residue numbers, is available from the **label_*** fields. For compatibility with PDB files, PyMOL by default will read the **auth_*** fields (if available, with fallback to **label_*** fields).

Note that **_atom_site.label_asym_id** is always loaded into the **segi** field, independant of the **cif_use_auth** setting.

Note that non-polymer molecules (e.g. water) are not enumerated by **_atom_site.label_seq_id** and will appear as a single residue in PyMOL (sequence viewer, when making selections, etc.) with **cif_use_auth**=off.

##  Currently affected fields
- _atom_site.auth_atom_id (ID)
- _atom_site.auth_comp_id (resn)
- _atom_site.auth_seq_id (resi)
- _atom_site.auth_asym_id (chain)
- _atom_site.pdbx_pdb_ins_code (resi suffix)

##  Examples
"auth" versus "label" asym_id of 1oky:

 PyMOL>set cif_use_auth
 PyMOL>fetch 1oky, authon, async=0
 PyMOL>get_chains authon
  cmd.get_chains:  ['A']

 PyMOL>set cif_use_auth, off
 PyMOL>fetch 1oky, authoff, async=0
 PyMOL>get_chains authoff
  cmd.get_chains:  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
