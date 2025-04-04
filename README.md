 OCR-RenAIssance

An OCR pipeline project for extracting main text from Renaissance-era scanned documents while ignoring embellishments. This project leverages EasyOCR (based on a CRNN architecture) to convert PDF pages to images and extract text efficiently.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Evaluation Metrics](#evaluation-metrics)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **OCR-RenAIssance** project focuses on developing an Optical Character Recognition system for Renaissance-era documents. The goal is to accurately extract the main textual content while filtering out any embellishments. This is crucial for historical document digitization and analysis.

## Features

- **PDF to Image Conversion:** Utilizes `pdf2image` to convert scanned documents into images.
- **Text Extraction:** Implements EasyOCR for efficient text recognition.
- **Evaluation Metrics:** Calculates Character Error Rate (CER) and Word Error Rate (WER) to assess OCR accuracy.
- **Clean Output:** Outputs results in a well-structured text file with clear page delineations.

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/icvasu/OCR-RenAIssance.git
   cd OCR-RenAIssance

2.Create a Virtual Environment
   ```sh
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

```
3.Install Dependencies:
```sh
pip install -r requirements.txt
```
4.Install Poppler:

Windows Users:
Download Poppler from Poppler for Windows, extract it (e.g., to C:\poppler\), and add C:\poppler\Library\bin to your system PATH.

Mac/Linux Users:
Install via Homebrew (brew install poppler) or your package manager.
Usage
1.Prepare Your PDF:

Place your Renaissance PDF in the project folder.

Update the pdf_path variable in main.py with the correct path.

2.Run the OCR Script:

```sh

python main.py
```

3.Check the Output:

The OCR results will be saved in ocr_output.txt inside the repository.

Outputs are also organized in the outputs/ folder.

Output
The ocr_output.txt file includes the extracted text from each page, clearly separated by page numbers.


Evaluation Metrics
To assess the performance of the OCR model, the following metrics are used:

Character Error Rate (CER): Measures the accuracy at the character level.

Word Error Rate (WER): Measures the accuracy at the word level.

These metrics help in fine-tuning the OCR pipeline and ensuring reliable performance.

