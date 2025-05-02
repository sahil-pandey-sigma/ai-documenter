# 🤖 AI Code Document Generator

This tool analyzes source code from a ZIP file and generates high-quality technical documentation in **Word (.docx)** and **Markdown (.md)** formats using a local LLM (Large Language Model).

---

## 🚀 Features

- Extracts and reads supported code files from ZIP archives
- Generates:
  - 🔹 Project-level summary (Purpose, Intuition, Tech Stack, Improvements)
  - 🔹 File-level summaries (Purpose, Working, Errors)
- Outputs both **.docx** and **.md** documentation files
- Fully offline — powered by a local LLM (`Nous Hermes Mistral 2.5 4k`)

---

## 🛠 Tech Stack

- Python 3
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- docx (python-docx)
- re, os, zipfile, tempfile
- LLM model: **Nous Hermes Mistral 2.5 4k GGUF**

---