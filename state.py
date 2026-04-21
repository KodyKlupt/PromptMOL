def get_scene_state() -> str:
    try:
        from pymol import cmd

        objects = cmd.get_object_list() or []
        selections = [s for s in (cmd.get_names("selections") or []) if not s.startswith("_")]
        atom_count = cmd.count_atoms("all") if objects else 0

        lines = ["Current PyMOL scene:"]
        if objects:
            lines.append(f"  Loaded objects: {', '.join(objects)}")
        else:
            lines.append("  No objects loaded.")
        if selections:
            lines.append(f"  Named selections: {', '.join(selections)}")
        lines.append(f"  Total atoms visible: {atom_count}")
        return "\n".join(lines)
    except Exception as e:
        return f"(Could not read scene state: {e})"
