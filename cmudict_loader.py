"""
CMUdict Loader - A simple module to work with the CMU Pronouncing Dictionary

This module provides functions to:
- Load the CMU dictionary from the text file
- Look up word pronunciations
- Find rhymes
- Count syllables
- Analyze phonetic patterns

The CMUdict format:
- Each line contains a word followed by its phonetic transcription
- Phonemes are represented using the ARPAbet phonetic transcription code
- Stress markers: 0 (no stress), 1 (primary stress), 2 (secondary stress)
- Variants are marked with (2), (3), etc. for alternative pronunciations
"""

import re
from collections import defaultdict
from typing import Dict, List, Tuple, Optional


ARPA_TO_IPA = {
    "AA": "ɑ",
    "AE": "æ",
    "AH": "ʌ",
    "AO": "ɔ",
    "AW": "aʊ",
    "AY": "aɪ",
    "EH": "ɛ",
    "ER": "ɝ",
    "EY": "eɪ",
    "IH": "ɪ",
    "IY": "i",
    "OW": "oʊ",
    "OY": "ɔɪ",
    "UH": "ʊ",
    "UW": "u",
    "AX": "ə",
    "AXR": "ɚ",
    "IX": "ɨ",
    "EL": "l̩",
    "EM": "m̩",
    "EN": "n̩",
    "B": "b",
    "CH": "tʃ",
    "D": "d",
    "DH": "ð",
    "DX": "ɾ",
    "F": "f",
    "G": "ɡ",
    "HH": "h",
    "JH": "dʒ",
    "K": "k",
    "L": "l",
    "M": "m",
    "N": "n",
    "NG": "ŋ",
    "P": "p",
    "R": "ɹ",
    "S": "s",
    "SH": "ʃ",
    "T": "t",
    "TH": "θ",
    "V": "v",
    "W": "w",
    "Y": "j",
    "Z": "z",
    "ZH": "ʒ",
}


class CMUDict:
    """A class to load and query the CMU Pronouncing Dictionary"""
    
    def __init__(self, dict_path: str = "cmudict.dict"):
        """
        Initialize the CMUDict loader.
        
        Args:
            dict_path: Path to the cmudict.dict file
        """
        self.dict_path = dict_path
        self.pronunciations: Dict[str, List[List[str]]] = defaultdict(list)
        self.load_dictionary()
    
    def load_dictionary(self) -> None:
        """Load the dictionary file and parse it into memory"""
        print(f"Loading CMU dictionary from {self.dict_path}...")
        
        with open(self.dict_path, 'r', encoding='latin-1') as f:
            for line in f:
                # Remove comments (anything after #)
                line = line.split('#')[0].strip()
                
                # Skip empty lines
                if not line:
                    continue
                
                # Parse the line: WORD PHONEME1 PHONEME2 ...
                parts = line.split()
                if len(parts) < 2:
                    continue
                
                word = parts[0].lower()
                phonemes = parts[1:]
                
                # Handle variant markers like 'word(2)'
                # Remove the variant number but keep track of all pronunciations
                word = re.sub(r'\(\d+\)$', '', word)
                
                # Store the pronunciation
                self.pronunciations[word].append(phonemes)
        
        print(f"Loaded {len(self.pronunciations)} words with pronunciations.")
    
    def lookup(self, word: str) -> Optional[List[Dict[str, object]]]:
        """
        Look up a word's pronunciation(s).
        
        Args:
            word: The word to look up
            
        Returns:
            List of pronunciation dictionaries, or None if not found
        """
        word = word.lower().strip()
        pronunciations = self.pronunciations.get(word)
        if not pronunciations:
            return None
        
        results = []
        for phonemes in pronunciations:
            results.append({
                "arpa": " ".join(phonemes),
                "ipa": self.arpa_to_ipa(phonemes),
                "syllables": self.count_syllables_in_pronunciation(phonemes),
                "rhymes": self.find_rhymes_by_phonemes(word, phonemes),
            })
        
        return results
    
    def arpa_to_ipa(self, phonemes: List[str]) -> str:
        """
        Convert an ARPAbet phoneme list to a simple IPA string.
        
        Args:
            phonemes: List of ARPAbet phonemes
        
        Returns:
            IPA string wrapped in slashes
        """
        ipa_symbols = []
        for phoneme in phonemes:
            base = re.sub(r"\d", "", phoneme)
            ipa_symbols.append(ARPA_TO_IPA.get(base, base.lower()))
        return f"/{' '.join(ipa_symbols)}/"
    
    def count_syllables_in_pronunciation(self, phonemes: List[str]) -> int:
        """
        Count syllables in a pronunciation by counting stress digits.
        
        Args:
            phonemes: List of ARPAbet phonemes
        
        Returns:
            Number of syllables
        """
        return sum(1 for p in phonemes if re.search(r"[012]", p))
    
    def get_rhyming_part_from_phonemes(self, phonemes: List[str]) -> Optional[Tuple[str, ...]]:
        """
        Get the rhyming part of a pronunciation (last stressed vowel to end).
        
        Args:
            phonemes: List of ARPAbet phonemes
        
        Returns:
            Tuple of phonemes from the last stressed vowel onward, or None
        """
        last_stress_idx = -1
        for i in range(len(phonemes) - 1, -1, -1):
            if re.search(r"[012]", phonemes[i]):
                last_stress_idx = i
                break
        
        if last_stress_idx == -1:
            return None
        
        return tuple(phonemes[last_stress_idx:])
    
    def find_rhymes_by_phonemes(
        self,
        word: str,
        phonemes: List[str],
        max_results: int = 10,
    ) -> List[str]:
        """
        Find rhymes for a specific pronunciation.
        
        Args:
            word: Word to exclude from results
            phonemes: Pronunciation phoneme list to rhyme with
            max_results: Maximum number of rhymes to return
        
        Returns:
            List of rhyming words
        """
        rhyme_part = self.get_rhyming_part_from_phonemes(phonemes)
        if not rhyme_part:
            return []
        
        rhymes = []
        seen = set()
        for other_word, other_prons in self.pronunciations.items():
            if other_word == word.lower():
                continue
            for other_pron in other_prons:
                other_rhyme = self.get_rhyming_part_from_phonemes(other_pron)
                if other_rhyme == rhyme_part:
                    if other_word not in seen:
                        rhymes.append(other_word)
                        seen.add(other_word)
                    break
            if len(rhymes) >= max_results:
                break
        
        return rhymes
    
    def count_syllables(self, word: str) -> Optional[int]:
        """
        Count syllables in a word based on its first pronunciation.
        Syllables are counted by the number of vowel phonemes (those with stress markers).
        
        Args:
            word: The word to analyze
            
        Returns:
            Number of syllables, or None if word not found
        """
        pronunciations = self.pronunciations.get(word.lower().strip())
        if not pronunciations:
            return None
        
        # Use the first pronunciation
        phonemes = pronunciations[0]
        
        # Count phonemes with stress markers (0, 1, or 2)
        return self.count_syllables_in_pronunciation(phonemes)
    
    def get_rhyming_part(self, word: str) -> Optional[str]:
        """
        Get the rhyming part of a word (from the last stressed vowel to the end).
        
        Args:
            word: The word to analyze
            
        Returns:
            String representation of the rhyming part, or None if not found
        """
        pronunciations = self.pronunciations.get(word.lower().strip())
        if not pronunciations:
            return None
        
        phonemes = pronunciations[0]
        
        rhyme_part = self.get_rhyming_part_from_phonemes(phonemes)
        if not rhyme_part:
            return None
        
        return ' '.join(rhyme_part)
    
    def find_rhymes(self, word: str, max_results: int = 10) -> List[str]:
        """
        Find words that rhyme with the given word.
        
        Args:
            word: The word to find rhymes for
            max_results: Maximum number of rhymes to return
            
        Returns:
            List of rhyming words
        """
        pronunciations = self.pronunciations.get(word.lower().strip())
        if not pronunciations:
            return []
        
        return self.find_rhymes_by_phonemes(word, pronunciations[0], max_results=max_results)
    
    def get_stress_pattern(self, word: str) -> Optional[str]:
        """
        Get the stress pattern of a word (e.g., "1 0" for primary-unstressed).
        
        Args:
            word: The word to analyze
            
        Returns:
            Stress pattern string, or None if not found
        """
        pronunciations = self.pronunciations.get(word.lower().strip())
        if not pronunciations:
            return None
        
        phonemes = pronunciations[0]
        
        # Extract just the stress markers from vowels
        stress = [p[-1] for p in phonemes if p[-1] in '012']
        return ' '.join(stress)
    
    def get_phonemes_readable(self, word: str) -> Optional[str]:
        """
        Get a readable representation of the phonemes.
        
        Args:
            word: The word to look up
            
        Returns:
            String of phonemes, or None if not found
        """
        pronunciations = self.pronunciations.get(word.lower().strip())
        if not pronunciations:
            return None
        
        # Return the first pronunciation as a readable string
        return ' '.join(pronunciations[0])
    
    def word_exists(self, word: str) -> bool:
        """Check if a word exists in the dictionary"""
        return word.lower() in self.pronunciations
    
    def search_by_pattern(self, pattern: str, max_results: int = 20) -> List[str]:
        """
        Search for words matching a wildcard pattern.
        
        Args:
            pattern: Search pattern (supports * as wildcard)
            max_results: Maximum results to return
            
        Returns:
            List of matching words
        """
        # Convert wildcard pattern to regex
        regex_pattern = pattern.replace('*', '.*')
        regex = re.compile(f'^{regex_pattern}$', re.IGNORECASE)
        
        matches = []
        for word in self.pronunciations:
            if regex.match(word):
                matches.append(word)
                if len(matches) >= max_results:
                    break
        
        return matches


# Load phoneme types from cmudict.phones
def load_phoneme_types(phones_path: str = "cmudict.phones") -> Dict[str, str]:
    """
    Load the phoneme type information.
    
    Args:
        phones_path: Path to the cmudict.phones file
        
    Returns:
        Dictionary mapping phoneme symbols to their types
    """
    phoneme_types = {}
    
    with open(phones_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            parts = line.split('\t')
            if len(parts) == 2:
                phoneme, ptype = parts
                phoneme_types[phoneme] = ptype
    
    return phoneme_types


if __name__ == "__main__":
    # This code runs when the script is executed directly
    print("=" * 60)
    print("CMUdict Python Loader - Demo")
    print("=" * 60)
    print()
    
    # Initialize the dictionary
    cmu = CMUDict()
    print()
    
    # Demo 1: Look up a word
    print("DEMO 1: Looking up pronunciations")
    print("-" * 60)
    test_words = ["hello", "world", "python", "dictionary"]
    for word in test_words:
        pronunciations = cmu.lookup(word)
        if pronunciations:
            print(f"{word.upper()}:")
            for i, pron in enumerate(pronunciations, 1):
                print(f"  Pronunciation {i}: {pron['arpa']}")
                print(f"    IPA: {pron['ipa']}")
                print(f"    Syllables: {pron['syllables']}")
        else:
            print(f"{word.upper()}: NOT FOUND")
    print()
    
    # Demo 2: Count syllables
    print("DEMO 2: Counting syllables")
    print("-" * 60)
    for word in test_words:
        syllables = cmu.count_syllables(word)
        print(f"{word}: {syllables} syllable(s)")
    print()
    
    # Demo 3: Find rhymes
    print("DEMO 3: Finding rhymes")
    print("-" * 60)
    rhyme_word = "cat"
    rhymes = cmu.find_rhymes(rhyme_word, max_results=15)
    print(f"Words that rhyme with '{rhyme_word}': {', '.join(rhymes[:15])}")
    print()
    
    # Demo 4: Stress patterns
    print("DEMO 4: Stress patterns")
    print("-" * 60)
    stress_words = ["computer", "banana", "elephant"]
    for word in stress_words:
        pattern = cmu.get_stress_pattern(word)
        print(f"{word}: {pattern}")
    print()
    
    # Demo 5: Search by pattern
    print("DEMO 5: Pattern search")
    print("-" * 60)
    pattern = "cat*"
    matches = cmu.search_by_pattern(pattern, max_results=10)
    print(f"Words matching '{pattern}': {', '.join(matches)}")
    print()
    
    # Demo 6: Load phoneme types
    print("DEMO 6: Phoneme types")
    print("-" * 60)
    phoneme_types = load_phoneme_types()
    print(f"Loaded {len(phoneme_types)} phoneme types")
    print("Sample phonemes:")
    for phoneme, ptype in list(phoneme_types.items())[:10]:
        print(f"  {phoneme}: {ptype}")
    print()
    
    print("=" * 60)
    print("Demo complete! You can now use this module in your projects.")
    print("=" * 60)
