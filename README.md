# 🎭 Sentiment Analysis Tool (CLI)

A powerful command-line sentiment analysis application built with Python and TextBlob. Analyze the sentiment of text data through an interactive terminal interface with comprehensive features and detailed insights.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![TextBlob](https://img.shields.io/badge/TextBlob-0.15+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example Outputs](#example-outputs)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [What You'll Learn](#what-youll-learn)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This sentiment analysis tool helps you understand the emotional tone and subjectivity of text data through a simple command-line interface. Whether you're analyzing customer reviews, social media posts, or any text content, this tool provides instant insights with clear, formatted output.

**Key Metrics:**
- **Sentiment Classification**: Positive 😊, Negative 😞, or Neutral 😐
- **Polarity Score**: Ranges from -1 (very negative) to +1 (very positive)
- **Subjectivity Score**: Ranges from 0 (objective/factual) to 1 (subjective/opinion)

## ✨ Features

### 🔍 **Single Text Analysis**
- Analyze individual sentences or paragraphs
- Real-time sentiment detection
- Detailed polarity and subjectivity scores
- Color-coded emoji indicators

### 📚 **Batch Analysis**
- Analyze multiple texts simultaneously
- Process line-by-line input
- Comprehensive results for each text
- Statistical summary

### 🧪 **Sample Reviews**
- Pre-loaded product reviews for testing
- Instant analysis of 6 sample reviews
- Statistical overview of results
- Quick way to understand the tool's capabilities

### 📜 **Analysis History**
- Track all your previous analyses
- View complete history with timestamps
- Review past results anytime
- No data loss during session

### 📊 **Statistics Dashboard**
- Overall sentiment distribution
- Percentage breakdown (Positive/Negative/Neutral)
- Average polarity and subjectivity scores
- Comprehensive session summary

### 🎨 **User-Friendly Interface**
- Clean, formatted output
- Interactive menu system
- Emoji indicators for quick understanding
- Easy navigation

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/sentiment-analysis-cli.git
cd sentiment-analysis-cli
```

### Step 2: Install Required Packages

```bash
pip install textblob
```

### Step 3: Download TextBlob Corpora

```bash
python -m textblob.download_corpora
```

### Alternative: Using requirements.txt

Create a `requirements.txt` file with:

```
textblob>=0.15.3
```

Then install:

```bash
pip install -r requirements.txt
```

## 💻 Usage

### Running the Application

1. Navigate to the project directory:
```bash
cd sentiment-analysis-cli
```

2. Run the Python script:
```bash
python sentiment_analyzer.py
```

3. Follow the interactive menu to analyze text

### Menu Options

The application presents a menu with 6 options:

```
🎭 SENTIMENT ANALYSIS TOOL 🎭
============================================================
1. Analyze single text
2. Analyze multiple texts
3. Analyze sample reviews
4. View analysis history
5. View statistics
6. Exit
============================================================
```

### Usage Examples

#### **Option 1: Analyze Single Text**

```bash
Enter your choice (1-6): 1

📝 Enter the text to analyze (or 'back' to return):
>>> This product is absolutely amazing! I love it.

============================================================
📝 TEXT: This product is absolutely amazing! I love it.
============================================================
😊 SENTIMENT: Positive
📊 POLARITY: 0.625 (Range: -1 to 1)
   • -1 = Very Negative
   •  0 = Neutral
   • +1 = Very Positive
🎭 SUBJECTIVITY: 0.6 (Range: 0 to 1)
   •  0 = Very Objective (Factual)
   •  1 = Very Subjective (Opinion)
============================================================
```

#### **Option 2: Analyze Multiple Texts**

```bash
Enter your choice (1-6): 2

📝 Enter multiple texts (one per line).
Type 'DONE' on a new line when finished:
>>> Great product!
>>> Terrible quality.
>>> It's okay.
>>> DONE
```

#### **Option 3: Analyze Sample Reviews**

```bash
Enter your choice (1-6): 3

🔍 Analyzing sample product reviews...

[Displays analysis of 6 pre-loaded reviews]
[Shows statistics dashboard]
```

#### **Option 4: View History**

```bash
Enter your choice (1-6): 4

============================================================
📜 ANALYSIS HISTORY
============================================================

1. 😊 Positive
   Text: This product is absolutely amazing! I love it.
   Polarity: 0.625, Subjectivity: 0.6

2. 😞 Negative
   Text: Terrible quality. Not worth the money.
   Polarity: -0.7, Subjectivity: 0.65
============================================================
```

#### **Option 5: View Statistics**

```bash
Enter your choice (1-6): 5

============================================================
📊 SENTIMENT STATISTICS
============================================================
Total Analyses: 10
😊 Positive: 4 (40.0%)
😞 Negative: 3 (30.0%)
😐 Neutral: 3 (30.0%)

Average Polarity: 0.125
Average Subjectivity: 0.567
============================================================
```

## 🔬 How It Works

### Sentiment Analysis Process

1. **Text Input**: User provides text through the command-line interface
2. **TextBlob Processing**: The text is processed using TextBlob's sentiment analyzer
3. **Polarity Calculation**: 
   - Measures how positive or negative the text is
   - Range: -1.0 (most negative) to +1.0 (most positive)
   - Based on sentiment lexicon and linguistic rules
4. **Subjectivity Calculation**:
   - Measures how subjective or objective the text is
   - Range: 0.0 (very objective) to 1.0 (very subjective)
   - Distinguishes facts from opinions
5. **Classification**:
   - **Positive** 😊: polarity > 0.1
   - **Negative** 😞: polarity < -0.1
   - **Neutral** 😐: -0.1 ≤ polarity ≤ 0.1

### TextBlob's Approach

TextBlob uses a pre-trained sentiment analyzer based on:
- **Pattern library**: Sentiment lexicon with word polarities
- **Context analysis**: Considers modifiers, negations, and intensifiers
- **Linguistic rules**: Grammar-based sentiment detection

## 📸 Example Outputs

### Positive Sentiment Example
```
============================================================
📝 TEXT: Outstanding quality and excellent customer service!
============================================================
😊 SENTIMENT: Positive
📊 POLARITY: 0.85
🎭 SUBJECTIVITY: 0.9
============================================================
```

### Negative Sentiment Example
```
============================================================
📝 TEXT: Very disappointed. Not worth the money at all.
============================================================
😞 SENTIMENT: Negative
📊 POLARITY: -0.65
🎭 SUBJECTIVITY: 0.75
============================================================
```

### Neutral Sentiment Example
```
============================================================
📝 TEXT: The product works as described. Pretty standard.
============================================================
😐 SENTIMENT: Neutral
📊 POLARITY: 0.05
🎭 SUBJECTIVITY: 0.35
============================================================
```

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core programming language | 3.7+ |
| **TextBlob** | Natural language processing and sentiment analysis | 0.15.3+ |

### Why TextBlob?

- ✅ Easy to use and beginner-friendly
- ✅ Pre-trained sentiment analyzer
- ✅ Reliable polarity and subjectivity scores
- ✅ No training data required
- ✅ Handles multiple languages (with translation)
- ✅ Active community and documentation

## 📁 Project Structure

```
sentiment-analysis-cli/
│
├── sentiment_analyzer.py      # Main application file
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── LICENSE                    # MIT License file
```

### Code Structure

The application consists of:

1. **SentimentAnalyzer Class**
   - `analyze_sentiment()`: Analyzes single text
   - `analyze_batch()`: Analyzes multiple texts
   - `print_result()`: Formats and displays results
   - `print_history()`: Shows analysis history
   - `get_statistics()`: Calculates session statistics

2. **Helper Functions**
   - `display_menu()`: Shows the main menu
   - `main()`: Runs the application loop

3. **Features**
   - Session-based history tracking
   - Error handling for invalid inputs
   - Keyboard interrupt handling (Ctrl+C)

## 📚 What You'll Learn

By exploring and using this project, you'll learn:

### Technical Skills
- ✅ **Sentiment Analysis**: Understanding polarity and subjectivity metrics
- ✅ **Natural Language Processing**: Working with TextBlob library
- ✅ **Python Programming**: Classes, methods, and data structures
- ✅ **CLI Development**: Creating interactive command-line interfaces
- ✅ **Error Handling**: Managing exceptions and user input validation
- ✅ **Data Management**: Tracking and organizing analysis results

### NLP Concepts
- ✅ **Polarity Detection**: How to measure emotional tone
- ✅ **Subjectivity Analysis**: Distinguishing facts from opinions
- ✅ **Text Preprocessing**: Handling and cleaning text data
- ✅ **Sentiment Classification**: Categorizing text sentiment
- ✅ **Batch Processing**: Analyzing multiple texts efficiently

### Software Engineering
- ✅ **Object-Oriented Programming**: Class design and encapsulation
- ✅ **User Interface Design**: Creating intuitive CLI experiences
- ✅ **Code Organization**: Structuring maintainable code
- ✅ **Documentation**: Writing clear code comments

## 🎓 Educational Use Cases

This tool is perfect for:

- **Students**: Learning NLP and sentiment analysis basics
- **Researchers**: Quick sentiment analysis of text data
- **Business Analysts**: Analyzing customer feedback and reviews
- **Content Creators**: Understanding the tone of their content
- **Data Scientists**: Prototyping sentiment analysis solutions
- **Python Learners**: Understanding CLI application development

## 🔧 Customization

### Adjusting Sentiment Thresholds

You can modify the sentiment classification in the `analyze_sentiment` method:

```python
# Current thresholds
if polarity > 0.1:  # Positive threshold
    sentiment = "Positive"
elif polarity < -0.1:  # Negative threshold
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# Example: Stricter classification
if polarity > 0.3:  # More strict positive
    sentiment = "Positive"
elif polarity < -0.3:  # More strict negative
    sentiment = "Negative"
```

### Adding Custom Features

Extend the tool with:
- Export results to CSV/JSON
- Custom word lists for domain-specific analysis
- Integration with file inputs
- Sentiment trend visualization
- Multi-language support
- Custom sentiment models

### Example: Adding CSV Export

```python
def export_to_csv(self, filename="results.csv"):
    """Export analysis history to CSV"""
    import csv
    
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['text', 'sentiment', 'polarity', 'subjectivity'])
        writer.writeheader()
        writer.writerows(self.history)
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'textblob'`
```bash
Solution: pip install textblob
```

**Issue**: `LookupError: Resource 'corpora/brown' not found`
```bash
Solution: python -m textblob.download_corpora
```

**Issue**: Incorrect sentiment for specific domain
```bash
Solution: TextBlob is trained on general text. Consider custom models for specific domains
```

**Issue**: Unicode/Encoding errors
```bash
Solution: Ensure your terminal supports UTF-8 encoding
```

## 💡 Tips for Better Results

1. **Write Clear Text**: Well-structured sentences get better results
2. **Context Matters**: Short phrases may not capture full sentiment
3. **Domain Specificity**: General-purpose models may struggle with technical jargon
4. **Multiple Sentences**: Longer texts provide more accurate analysis
5. **Test with Examples**: Use sample reviews to understand behavior

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a new branch (`git checkout -b feature/YourFeature`)
3. **Make** your changes
4. **Commit** your changes (`git commit -m 'Add some feature'`)
5. **Push** to the branch (`git push origin feature/YourFeature`)
6. **Open** a Pull Request

### Ideas for Contributions
- Add support for multiple languages
- Implement file input/output
- Create data visualization exports
- Add more pre-trained models
- Improve error handling
- Write unit tests

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[Full MIT License text...]
```

## 👨‍💻 Author

Created with ❤️ by Harvhoax

**About the Developer:**
- Learning and exploring Natural Language Processing
- Passionate about Python and CLI tools
- Building practical applications for text analysis

## 🙏 Acknowledgments

- **[TextBlob](https://textblob.readthedocs.io/)** - For the excellent sentiment analysis library
- **[Pattern](https://github.com/clips/pattern)** - Underlying NLP library used by TextBlob
- **Python Community** - For extensive documentation and support
- **NLTK Project** - For natural language processing tools

## 📚 Additional Resources

### Learn More About Sentiment Analysis
- [TextBlob Documentation](https://textblob.readthedocs.io/)
- [Sentiment Analysis Tutorial](https://realpython.com/sentiment-analysis-python/)
- [NLP with Python Book](https://www.nltk.org/book/)

### Related Projects
- VADER Sentiment Analysis
- Flair NLP
- spaCy sentiment extensions
- Hugging Face Transformers

## 🌟 Star This Project

If you find this project useful, please consider giving it a star on GitHub! ⭐

Your support helps others discover this tool and motivates continued development.

---

## 📊 Project Stats

- **Language**: Python
- **Lines of Code**: ~200
- **Dependencies**: 1 (TextBlob)
- **Platform**: Cross-platform (Windows, macOS, Linux)
- **Interface**: Command-line

---

**Happy Analyzing! 🎭✨**

*Built with Python and powered by TextBlob*
