import os
import pypandoc

def convert_md_to_docx():
    # Get current directory
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "corrections_in_progress")

    # Make sure output folder exists
    os.makedirs(output_dir, exist_ok=True)

    # Loop through files in directory
    for filename in os.listdir(current_dir):
        if filename.endswith(".md") and "instructions" not in filename.lower() and "template" not in filename.lower():
            md_path = os.path.join(current_dir, filename)
            docx_filename = os.path.splitext(filename)[0] + ".docx"
            docx_path = os.path.join(output_dir, docx_filename)

            print(f"Converting {filename} → {docx_filename}")

            # Convert with pandoc
            pypandoc.convert_text(
                open(md_path, encoding="utf-8").read(),
                "docx",
                format="md",
                outputfile=docx_path,
                extra_args=['--standalone']
            )

    print(f"\nAll conversions complete. Files saved in: {output_dir}")

if __name__ == "__main__":
    convert_md_to_docx()
