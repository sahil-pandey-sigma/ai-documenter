import os
import re
import subprocess

def extract_mermaid_blocks(md_path, output_dir):
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Find all ```mermaid blocks
    pattern = re.compile(r"```mermaid\n(.*?)\n```", re.DOTALL)
    matches = list(pattern.finditer(md_content))

    svg_filenames = []

    for i, match in enumerate(matches):
        mermaid_code = match.group(1).strip()
        diagram_id = f"diagram_{i+1}"
        mmd_path = os.path.join(output_dir, f"{diagram_id}.mmd")
        svg_path = os.path.join(output_dir, f"{diagram_id}.svg")

        # Write Mermaid .mmd file
        with open(mmd_path, "w", encoding="utf-8") as mmd_file:
            mmd_file.write(mermaid_code)

        # Render SVG using mmdc
        try:
            result = subprocess.run(
                ["mmdc", "-i", mmd_path, "-o", svg_path],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            print(f"✅ Rendered: {svg_path}")

            # Replace mermaid block with image link ONLY if rendering succeeded
            md_content = md_content.replace(match.group(0), f"![]({diagram_id}.svg)")
            svg_filenames.append(svg_path)

        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.decode()
            print(f"❌ Failed to render {mmd_path}:\n{error_msg}")
            # Remove invalid .mmd file so it doesn't clutter
            os.remove(mmd_path)
            # Don't replace this Mermaid block in the markdown

    # Output new Markdown file
    new_md_path = os.path.join(output_dir, "combined_with_svgs.md")
    with open(new_md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"\n✅ Rewritten Markdown with SVGs: {new_md_path}")
    return new_md_path, svg_filenames


if __name__ == "__main__":
    project_folder = "output/TicTacToe"  # Change this if needed
    md_path = os.path.join(project_folder, "combined.md")
    extract_mermaid_blocks(md_path, project_folder)
