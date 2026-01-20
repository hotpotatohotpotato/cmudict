"""
Rhyme Finder Tool

This script finds words that rhyme with a given word using the 
CMU Pronouncing Dictionary and phonetic analysis.

HOW RHYMING WORKS WITH PHONETIC DATA:
--------------------------------------
Two words rhyme if they share the same sounds from the last stressed 
vowel to the end of the word.

For example:
- "CAT" = K AE1 T
- "BAT" = B AE1 T
  
Both end with "AE1 T" (starting from the stressed vowel), so they rhyme!

Another example:
- "COMPUTER" = K AH0 M P Y UW1 T ER0
- "COMMUTER" = K AH0 M Y UW1 T ER0

Both end with "UW1 T ER0" (from the last stressed vowel), so they rhyme!

The key is finding the LAST STRESSED VOWEL (marked with 1 or 2) and 
comparing everything after that point.

Usage: python rhymes.py
"""

from cmudict_loader import CMUDict


def explain_rhyme(word, rhyme_word, cmu):
    """
    Show why two words rhyme by displaying their phonetic structure.
    
    Args:
        word: The original word
        rhyme_word: A word that rhymes with it
        cmu: The CMUDict instance
    """
    # Get pronunciations for both words
    word_pron = cmu.lookup(word)
    rhyme_pron = cmu.lookup(rhyme_word)
    
    if not word_pron or not rhyme_pron:
        return
    
    # Get the rhyming parts (from last stressed vowel to end)
    word_rhyme_part = cmu.get_rhyming_part(word)
    rhyme_rhyme_part = cmu.get_rhyming_part(rhyme_word)
    
    print(f"\n  {word.upper():15} → {' '.join(word_pron[0])}")
    print(f"  {rhyme_word.upper():15} → {' '.join(rhyme_pron[0])}")
    print(f"  Matching part:    {word_rhyme_part}")


def main():
    """Main function to run the rhyme finder tool"""
    
    # Print welcome message
    print("=" * 60)
    print("CMUdict Rhyme Finder")
    print("=" * 60)
    print()
    print("This tool finds words that rhyme with your input word.")
    print()
    print("HOW IT WORKS:")
    print("  1. We look at the phonetic pronunciation of your word")
    print("  2. We find the last stressed vowel (marked with 1 or 2)")
    print("  3. We compare everything from that vowel to the end")
    print("  4. Words with matching endings are rhymes!")
    print()
    print("Type 'quit' or 'exit' to close the program.")
    print("=" * 60)
    print()
    
    # Load the dictionary
    print("Loading dictionary... please wait...")
    cmu = CMUDict()
    print("Dictionary loaded! You can now find rhymes.")
    print()
    
    # Keep asking for words until the user wants to quit
    while True:
        # Get a word from the user
        word = input("Enter a word to find rhymes for: ").strip()
        
        # Check if the user wants to quit
        if word.lower() in ['quit', 'exit', 'q', '']:
            print("\nGoodbye!")
            break
        
        print()  # Blank line for readability
        
        # Look up the word in the dictionary
        pronunciations = cmu.lookup(word)
        
        # Check if the word exists
        if not pronunciations:
            print(f"✗ Sorry, '{word}' was not found in the dictionary.")
            print("  Please try a different word or check the spelling.")
            print()
            print("-" * 60)
            print()
            continue
        
        # Show the word's pronunciation
        print(f"✓ Found '{word}' in the dictionary!")
        print(f"  Pronunciation: {' '.join(pronunciations[0])}")
        
        # Get the rhyming part (this is what we'll match against)
        rhyme_part = cmu.get_rhyming_part(word)
        print(f"  Rhyming part:  {rhyme_part}")
        print("  (This is from the last stressed vowel to the end)")
        print()
        
        # Find rhyming words
        # We'll get more than 20 and then filter/display them
        print("Searching for rhymes...")
        rhymes = cmu.find_rhymes(word, max_results=50)
        
        if rhymes:
            print(f"\n✓ Found {len(rhymes)} words that rhyme with '{word}':")
            print()
            
            # Display rhymes in a nice format (multiple columns)
            # Show them 5 per line for readability
            for i in range(0, len(rhymes), 5):
                # Get the next 5 rhymes (or fewer if we're at the end)
                batch = rhymes[i:i+5]
                # Join them with commas and proper spacing
                print("  " + ", ".join(batch))
            
            # Offer to show detailed explanation for a few examples
            print()
            show_examples = input("Show detailed rhyme examples? (y/n): ").strip().lower()
            
            if show_examples in ['y', 'yes']:
                print()
                print("RHYME EXAMPLES (showing phonetic breakdown):")
                print("-" * 60)
                
                # Show up to 3 examples
                num_examples = min(3, len(rhymes))
                for i in range(num_examples):
                    explain_rhyme(word, rhymes[i], cmu)
                
                if len(rhymes) > 3:
                    print(f"\n  ... and {len(rhymes) - 3} more rhymes")
        else:
            # No rhymes found
            print(f"\n✗ No perfect rhymes found for '{word}'.")
            print()
            print("Possible reasons:")
            print("  - The word has a unique sound pattern")
            print("  - Rhyming words exist but aren't in the dictionary")
            print("  - Try a more common word")
            print()
            
            # Show the word's structure to help understand why
            syllables = cmu.count_syllables(word)
            stress = cmu.get_stress_pattern(word)
            print("Word information:")
            print(f"  Syllables: {syllables}")
            print(f"  Stress pattern: {stress}")
        
        print()
        print("-" * 60)
        print()


# This runs the main function when the script is executed
if __name__ == "__main__":
    main()
