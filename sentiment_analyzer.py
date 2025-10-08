"""
Sentiment Analysis Tool using TextBlob
Analyzes sentiment (positive, negative, neutral) of text input
"""

from textblob import TextBlob
import sys

class SentimentAnalyzer:
    """A class to perform sentiment analysis on text"""
    
    def __init__(self):
        self.history = []
    
    def analyze_sentiment(self, text):
        """
        Analyze the sentiment of given text
        
        Args:
            text (str): The text to analyze
            
        Returns:
            dict: Dictionary containing sentiment analysis results
        """
        if not text.strip():
            return None
        
        # Create TextBlob object
        blob = TextBlob(text)
        
        # Get polarity (-1 to 1) and subjectivity (0 to 1)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        # Determine sentiment category
        if polarity > 0.1:
            sentiment = "Positive"
            emoji = "😊"
        elif polarity < -0.1:
            sentiment = "Negative"
            emoji = "😞"
        else:
            sentiment = "Neutral"
            emoji = "😐"
        
        # Create result dictionary
        result = {
            'text': text,
            'sentiment': sentiment,
            'polarity': round(polarity, 3),
            'subjectivity': round(subjectivity, 3),
            'emoji': emoji
        }
        
        # Add to history
        self.history.append(result)
        
        return result
    
    def print_result(self, result):
        """Pretty print the sentiment analysis result"""
        if result is None:
            print("❌ No text provided!")
            return
        
        print("\n" + "="*60)
        print(f"📝 TEXT: {result['text']}")
        print("="*60)
        print(f"{result['emoji']} SENTIMENT: {result['sentiment']}")
        print(f"📊 POLARITY: {result['polarity']} (Range: -1 to 1)")
        print(f"   • -1 = Very Negative")
        print(f"   •  0 = Neutral")
        print(f"   • +1 = Very Positive")
        print(f"🎭 SUBJECTIVITY: {result['subjectivity']} (Range: 0 to 1)")
        print(f"   •  0 = Very Objective (Factual)")
        print(f"   •  1 = Very Subjective (Opinion)")
        print("="*60 + "\n")
    
    def analyze_batch(self, texts):
        """Analyze multiple texts at once"""
        results = []
        for text in texts:
            result = self.analyze_sentiment(text)
            if result:
                results.append(result)
        return results
    
    def print_history(self):
        """Print analysis history"""
        if not self.history:
            print("📭 No analysis history available.")
            return
        
        print("\n" + "="*60)
        print("📜 ANALYSIS HISTORY")
        print("="*60)
        for i, result in enumerate(self.history, 1):
            print(f"\n{i}. {result['emoji']} {result['sentiment']}")
            print(f"   Text: {result['text'][:50]}{'...' if len(result['text']) > 50 else ''}")
            print(f"   Polarity: {result['polarity']}, Subjectivity: {result['subjectivity']}")
        print("="*60 + "\n")
    
    def get_statistics(self):
        """Get statistics from analysis history"""
        if not self.history:
            print("📭 No data to analyze.")
            return
        
        total = len(self.history)
        positive = sum(1 for r in self.history if r['sentiment'] == 'Positive')
        negative = sum(1 for r in self.history if r['sentiment'] == 'Negative')
        neutral = sum(1 for r in self.history if r['sentiment'] == 'Neutral')
        
        avg_polarity = sum(r['polarity'] for r in self.history) / total
        avg_subjectivity = sum(r['subjectivity'] for r in self.history) / total
        
        print("\n" + "="*60)
        print("📊 SENTIMENT STATISTICS")
        print("="*60)
        print(f"Total Analyses: {total}")
        print(f"😊 Positive: {positive} ({positive/total*100:.1f}%)")
        print(f"😞 Negative: {negative} ({negative/total*100:.1f}%)")
        print(f"😐 Neutral: {neutral} ({neutral/total*100:.1f}%)")
        print(f"\nAverage Polarity: {avg_polarity:.3f}")
        print(f"Average Subjectivity: {avg_subjectivity:.3f}")
        print("="*60 + "\n")


def display_menu():
    """Display the main menu"""
    print("\n" + "🎭 SENTIMENT ANALYSIS TOOL 🎭".center(60))
    print("="*60)
    print("1. Analyze single text")
    print("2. Analyze multiple texts")
    print("3. Analyze sample reviews")
    print("4. View analysis history")
    print("5. View statistics")
    print("6. Exit")
    print("="*60)


def main():
    """Main function to run the sentiment analyzer"""
    analyzer = SentimentAnalyzer()
    
    # Sample reviews for demonstration
    sample_reviews = [
        "This product is absolutely amazing! I love it so much.",
        "Terrible experience. The worst purchase I've ever made.",
        "It's okay, nothing special but does the job.",
        "Outstanding quality and excellent customer service!",
        "Very disappointed. Not worth the money at all.",
        "The product works as described. Pretty standard."
    ]
    
    print("\n" + "="*60)
    print("Welcome to the Sentiment Analysis Tool!".center(60))
    print("Powered by TextBlob".center(60))
    print("="*60)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            # Single text analysis
            print("\n📝 Enter the text to analyze (or 'back' to return):")
            text = input(">>> ").strip()
            if text.lower() == 'back':
                continue
            result = analyzer.analyze_sentiment(text)
            analyzer.print_result(result)
            
        elif choice == '2':
            # Multiple texts analysis
            print("\n📝 Enter multiple texts (one per line).")
            print("Type 'DONE' on a new line when finished:")
            texts = []
            while True:
                line = input(">>> ").strip()
                if line.upper() == 'DONE':
                    break
                if line:
                    texts.append(line)
            
            if texts:
                results = analyzer.analyze_batch(texts)
                for result in results:
                    analyzer.print_result(result)
            else:
                print("❌ No texts provided!")
        
        elif choice == '3':
            # Sample reviews analysis
            print("\n🔍 Analyzing sample product reviews...\n")
            results = analyzer.analyze_batch(sample_reviews)
            for result in results:
                analyzer.print_result(result)
            analyzer.get_statistics()
        
        elif choice == '4':
            # View history
            analyzer.print_history()
        
        elif choice == '5':
            # View statistics
            analyzer.get_statistics()
        
        elif choice == '6':
            # Exit
            print("\n👋 Thank you for using the Sentiment Analysis Tool!")
            print("="*60 + "\n")
            break
        
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)