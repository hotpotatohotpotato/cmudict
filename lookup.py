"""
Simple Word Pronunciation Lookup Tool

This script lets you type in any word and see its pronunciation
from the CMU Pronouncing Dictionary.

Usage: python lookup.py
"""

from cmudict_loader import CMUDict


def main():
    """Main function to run the word lookup tool"""
    
    # Print a welcome message
    print("=" * 60)
    print("CMUdict Word Pronunciation Lookup")
    print("=" * 60)
    print()
    print("This tool shows you how words are pronounced using")
    print("phonetic symbols (ARPAbet notation).")
    print()
    print("Type 'quit' or 'exit' to close the program.")
    print("=" * 60)
    print()
    
    # Load the dictionary (this might take a few seconds)
    print("Loading dictionary... please wait...")
    cmu = CMUDict()
    print("Dictionary loaded! You can now look up words.")
    print()
    
    # Keep asking for words until the user wants to quit
    while True:
        # Get a word from the user
        word = input("Enter a word to look up: ").strip()
        
        # Check if the user wants to quit
        if word.lower() in ['quit', 'exit', 'q', '']:
            print("\nGoodbye!")
            break
        
        print()  # Print a blank line for readability
        
        # Look up the word in the dictionary
        pronunciations = cmu.lookup(word)
        
        # Check if we found the word
        if pronunciations:
            # Word was found! Show the pronunciation(s)
            print(f"✓ Found '{word}' in the dictionary!")
            print()
            
            # Some words have multiple pronunciations
            if len(pronunciations) == 1:
                print("Pronunciation:")
            else:
                print(f"This word has {len(pronunciations)} pronunciations:")
            
            # Show each pronunciation
            for i, phonemes in enumerate(pronunciations, 1):
                # Join the phoneme list into a readable string
                pronunciation = ' '.join(phonemes)
                
                if len(pronunciations) == 1:
                    print(f"  {pronunciation}")
                else:
                    print(f"  {i}. {pronunciation}")
            
            # Show additional information
            print()
            syllable_count = cmu.count_syllables(word)
            print(f"Syllables: {syllable_count}")
            
            # Show stress pattern
            stress = cmu.get_stress_pattern(word)
            print(f"Stress pattern: {stress}")
            print("  (0 = no stress, 1 = primary stress, 2 = secondary stress)")
            
        else:
            # Word was not found
            print(f"✗ Sorry, '{word}' was not found in the dictionary.")
            print()
            print("Possible reasons:")
            print("  - The word might be spelled incorrectly")
            print("  - It might be a very new word or slang")
            print("  - It might be a proper noun not in the dictionary")
            print("  - Try a different spelling or form of the word")
        
        print()  # Print a blank line before the next lookup
        print("-" * 60)
        print()


# This runs the main function when the script is executed
if __name__ == "__main__":
    main()
