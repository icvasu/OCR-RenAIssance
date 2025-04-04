# OCR-RenAIssance

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
