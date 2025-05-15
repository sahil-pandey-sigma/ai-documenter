
# Turns Codebase into Easy Tutorial with AI

## Project Overview

This project demonstrates how to build an AI agent that analyzes GitHub repositories or local codebases and generates beginner-friendly tutorials explaining how the code works. The AI:

* Analyzes code structure and key abstractions
* Automatically generates Markdown tutorials
* Converts Mermaid diagrams in code explanations to SVGs and embeds them
* Exports polished PDFs with fully rendered diagrams
* Supports multiple output formats and languages

## Example Results

Tutorials are automatically generated for various repositories, with clear explanations and visual diagrams that help beginners understand workflows and core concepts.

---

## Getting Started

1. **Clone the Repository**

```bash
git clone https://github.com/sahil-pandey-sigma/ai-documenter
```

2. **Install Python Dependencies**

```bash
pip install -r requirements.txt
```

3. **Install Required Node.js Tools**

The project uses Node.js-based tools for rendering Mermaid diagrams and generating PDFs. Install them globally by running:

```bash
npm install -g @mermaid-js/mermaid-cli md-to-pdf
npx playwright install chromium
npx puppeteer browsers install chrome
```

4. **Set Up AI Client**

Configure your AI client in `utils/call_llm.py` by providing your API credentials or using the default AI Studio key:

```python
client = genai.Client(
  api_key=os.getenv("GEMINI_API_KEY", "your-api_key"),
)
```

Test the setup:

```bash
python utils/call_llm.py
```

---

## Generate a Tutorial

Run the script to analyze a GitHub repository or a local directory:

**For GitHub Repository**

```bash
python main.py --repo https://github.com/username/repo --include "*.py" "*.js" --exclude "tests/*" --max-size 50000
```

**For Local Directory**

```bash
python main.py --dir /path/to/your/codebase --include "*.py" --exclude "*test*"
```

**Specify Language for Tutorial**

```bash
python main.py --repo https://github.com/username/repo --language "Chinese"
```

---

## Command Line Arguments

| Argument             | Description                                                            | Default         |
| -------------------- | ---------------------------------------------------------------------- | --------------- |
| `--repo` or `--dir`  | GitHub repo URL or local directory path (required, mutually exclusive) | N/A             |
| `-n`, `--name`       | Project name (optional)                                                | N/A             |
| `-t`, `--token`      | GitHub token or set `GITHUB_TOKEN` env var                             | N/A             |
| `-o`, `--output`     | Output directory                                                       | `./output`      |
| `-i`, `--include`    | File patterns to include                                               | N/A             |
| `-e`, `--exclude`    | File patterns to exclude                                               | N/A             |
| `-s`, `--max-size`   | Max file size in bytes                                                 | 100000          |
| `--language`         | Language for tutorial                                                  | `english`       |
| `--max-abstractions` | Max number of abstractions to identify                                 | 10              |
| `--no-cache`         | Disable LLM response caching                                           | caching enabled |

---

## New Features

* **Mermaid Diagram Rendering:** Mermaid code blocks are detected, converted to SVGs, and embedded in the generated Markdown and PDF.
* **PDF Generation:** Automatically creates a polished PDF tutorial including diagrams using `md-to-pdf`.
* **Environment Variable Auto-Setup:** The tool automatically sets the `PUPPETEER_EXECUTABLE_PATH` based on OS to ensure Mermaid CLI (`mmdc`) works without manual user setup.
* **Automatic Cleanup:** Intermediate files like `.mmd`, temporary Markdown files, and SVGs are cleaned after PDF generation to keep your output folder tidy.
* **Multi-language Support:** Tutorials can be generated in different languages (e.g., Chinese).
* **Gemini Model Exploration:** Tested Google Gemini paid version as an LLM backend, comparing results with GPT-4.

---

## How It Works

1. The tool crawls the specified GitHub repository or local directory.
2. It analyzes the code structure and identifies core abstractions.
3. Generates Markdown tutorial chapters and an index.
4. Extracts Mermaid diagrams from the Markdown, converts them to SVG images.
5. Combines all Markdown files and exports a PDF with fully rendered diagrams.
6. Cleans up temporary files to maintain a clean project output.

---

## Development Notes

* Built using the Agentic Coding paradigm for AI-assisted code writing.
* Uses local and cloud AI LLMs (GPT-4, Gemini) with flexible backend switching planned.
* PDF generation leverages Node.js tools `md-to-pdf` and Puppeteer for accurate rendering.

---

## Troubleshooting

* Ensure Node.js, npm, and Chrome/Chromium are installed and accessible.
* Run `npx puppeteer browsers install chrome` once to download required Chromium for Mermaid CLI.
* If Mermaid diagrams fail to render, verify environment variables and Chrome installation paths.

---

## License

MIT License

---

If you want, I can also help prepare:

* A changelog
* Demo scripts
* Docker environment for easier setup

Just ask!
