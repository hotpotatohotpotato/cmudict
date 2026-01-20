"""
Example Usage of CMUdict Python Loader

This script demonstrates various ways to use the CMU Pronouncing Dictionary
in your Python projects. Run this script to see examples of:
- Word pronunciation lookup
- Syllable counting
- Rhyme finding
- Stress pattern analysis
- Interactive word lookup
"""

from cmudict_loader import CMUDict, load_phoneme_types


def example_basic_lookup():
    """Example: Basic word pronunciation lookup"""
    print("\n" + "=" * 60)
    print("EXAMPLE 1: Basic Word Lookup")
    print("=" * 60)
    
    cmu = CMUDict()
    
    words = ["hello", "python", "programming", "beautiful", "read"]
    
    for word in words:
        pronunciations = cmu.lookup(word)
        if pronunciations:
            print(f"\n{word.upper()}:")
            for i, pron in enumerate(pronunciations, 1):
                readable = ' '.join(pron)
                print(f"  Variant {i}: {readable}")
        else:
            print(f"\n{word.upper()}: Not found in dictionary")


def example_syllable_counter():
    """Example: Count syllables in words"""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Syllable Counter")
    print("=" * 60)
    
    cmu = CMUDict()
    
    sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Python is a great programming language",
        "Carnegie Mellon University"
    ]
    
    for sentence in sentences:
        print(f"\nSentence: '{sentence}'")
        words = sentence.lower().split()
        total_syllables = 0
        
        for word in words:
            syllables = cmu.count_syllables(word)
            if syllables:
                print(f"  {word}: {syllables} syllable(s)")
                total_syllables += syllables
            else:
                print(f"  {word}: NOT FOUND")
        
        print(f"Total syllables: {total_syllables}")


def example_rhyme_finder():
    """Example: Find rhyming words"""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Rhyme Finder")
    print("=" * 60)
    
    cmu = CMUDict()
    
    words_to_rhyme = ["cat", "love", "time", "day", "sound"]
    
    for word in words_to_rhyme:
        rhymes = cmu.find_rhymes(word, max_results=10)
        if rhymes:
            print(f"\nWords that rhyme with '{word}':")
            print(f"  {', '.join(rhymes)}")
        else:
            print(f"\nNo rhymes found for '{word}'")


def example_stress_patterns():
    """Example: Analyze stress patterns"""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Stress Pattern Analysis")
    print("=" * 60)
    print("\nStress markers:")
    print("  0 = No stress")
    print("  1 = Primary stress")
    print("  2 = Secondary stress\n")
    
    cmu = CMUDict()
    
    words = [
        "photograph", "photography", "photographic",
        "record", "present", "desert",
        "absolutely", "wonderful"
    ]
    
    for word in words:
        pattern = cmu.get_stress_pattern(word)
        phonemes = cmu.get_phonemes_readable(word)
        
        if pattern and phonemes:
            print(f"{word:15} | Stress: {pattern:10} | Phonemes: {phonemes}")


def example_pattern_search():
    """Example: Search for words by pattern"""
    print("\n" + "=" * 60)
    print("EXAMPLE 5: Pattern-Based Word Search")
    print("=" * 60)
    
    cmu = CMUDict()
    
    patterns = [
        "cat*",      # Words starting with 'cat'
        "*ing",      # Words ending with 'ing'
        "book*",     # Words starting with 'book'
        "un*"        # Words starting with 'un'
    ]
    
    for pattern in patterns:
        matches = cmu.search_by_pattern(pattern, max_results=12)
        if matches:
            print(f"\nWords matching '{pattern}':")
            print(f"  {', '.join(matches)}")


def example_phoneme_analysis():
    """Example: Analyze phonemes and their types"""
    print("\n" + "=" * 60)
    print("EXAMPLE 6: Phoneme Type Analysis")
    print("=" * 60)
    
    cmu = CMUDict()
    phoneme_types = load_phoneme_types()
    
    test_words = ["strength", "beautiful", "rhythm"]
    
    for word in test_words:
        pronunciations = cmu.lookup(word)
        if pronunciations:
            phonemes = pronunciations[0]
            print(f"\n{word.upper()}:")
            print(f"  Phonemes: {' '.join(phonemes)}")
            print(f"  Breakdown:")
            
            for phoneme in phonemes:
                # Remove stress markers for lookup
                clean_phoneme = phoneme.rstrip('012')
                ptype = phoneme_types.get(clean_phoneme, "unknown")
                stress_marker = phoneme[-1] if phoneme[-1] in '012' else ''
                stress_desc = {
                    '0': ' (no stress)',
                    '1': ' (primary stress)',
                    '2': ' (secondary stress)'
                }.get(stress_marker, '')
                
                print(f"    {phoneme:5} -> {clean_phoneme:3} ({ptype}){stress_desc}")


def example_haiku_checker():
    """Example: Check if lines follow haiku syllable pattern (5-7-5)"""
    print("\n" + "=" * 60)
    print("EXAMPLE 7: Haiku Syllable Checker")
    print("=" * 60)
    print("\nHaiku format: 5 syllables, 7 syllables, 5 syllables\n")
    
    cmu = CMUDict()
    
    haiku_lines = [
        "An old silent pond",
        "A frog jumps into the pond",
        "Splash silence again"
    ]
    
    expected = [5, 7, 5]
    is_valid_haiku = True
    
    for i, line in enumerate(haiku_lines):
        words = line.lower().replace(",", "").split()
        syllable_count = 0
        
        word_details = []
        for word in words:
            syls = cmu.count_syllables(word)
            if syls:
                syllable_count += syls
                word_details.append(f"{word}({syls})")
            else:
                word_details.append(f"{word}(?)")
        
        status = "✓" if syllable_count == expected[i] else "✗"
        print(f"Line {i+1} [{status}]: {' '.join(word_details)}")
        print(f"  Total: {syllable_count} syllables (expected {expected[i]})")
        
        if syllable_count != expected[i]:
            is_valid_haiku = False
    
    print(f"\nIs valid haiku? {'Yes!' if is_valid_haiku else 'No'}")


def interactive_mode():
    """Interactive mode: Look up any word"""
    print("\n" + "=" * 60)
    print("EXAMPLE 8: Interactive Word Lookup")
    print("=" * 60)
    print("\nType words to look up their pronunciations.")
    print("Type 'quit' or 'exit' to return to main script.\n")
    
    cmu = CMUDict()
    
    while True:
        try:
            word = input("Enter a word: ").strip()
            
            if word.lower() in ['quit', 'exit', 'q']:
                print("Exiting interactive mode...")
                break
            
            if not word:
                continue
            
            # Look up the word
            pronunciations = cmu.lookup(word)
            
            if pronunciations:
                print(f"\n'{word}' found!")
                
                for i, pron in enumerate(pronunciations, 1):
                    print(f"  Pronunciation {i}: {' '.join(pron)}")
                
                syllables = cmu.count_syllables(word)
                print(f"  Syllables: {syllables}")
                
                stress = cmu.get_stress_pattern(word)
                print(f"  Stress pattern: {stress}")
                
                rhymes = cmu.find_rhymes(word, max_results=5)
                if rhymes:
                    print(f"  Rhymes with: {', '.join(rhymes)}")
            else:
                print(f"\n'{word}' not found in dictionary.")
            
            print()
        
        except KeyboardInterrupt:
            print("\n\nExiting interactive mode...")
            break
        except EOFError:
            print("\n\nExiting interactive mode...")
            break


def main():
    """Run all examples"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  CMU Pronouncing Dictionary - Python Examples".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    
    # Run each example
    example_basic_lookup()
    example_syllable_counter()
    example_rhyme_finder()
    example_stress_patterns()
    example_pattern_search()
    example_phoneme_analysis()
    example_haiku_checker()
    
    # Ask if user wants interactive mode
    print("\n" + "=" * 60)
    print("\nWould you like to try interactive mode? (y/n): ", end="")
    
    try:
        response = input().strip().lower()
        if response in ['y', 'yes']:
            interactive_mode()
    except (KeyboardInterrupt, EOFError):
        print("\nSkipping interactive mode...")
    
    print("\n" + "=" * 60)
    print("All examples complete!")
    print("=" * 60)
    print("\nYou can import cmudict_loader in your own scripts:")
    print("  from cmudict_loader import CMUDict")
    print("  cmu = CMUDict()")
    print("  print(cmu.lookup('your_word'))")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
