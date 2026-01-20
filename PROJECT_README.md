# CMUdict Python Project

A simple, lightweight Python project for working with the Carnegie Mellon University Pronouncing Dictionary (CMUdict). This project provides an easy-to-use interface for looking up word pronunciations, counting syllables, finding rhymes, and analyzing phonetic patterns.

## 📁 Project Structure

```
cmudict/
│
├── cmudict.dict          # Main dictionary file (134,000+ words)
├── cmudict.phones        # Phoneme type definitions
├── cmudict.symbols       # Phoneme symbols
├── cmudict.vp            # Vowel/consonant markers
│
├── cmudict_loader.py     # Main module with CMUDict class
├── example_usage.py      # Comprehensive examples
├── requirements.txt      # Python dependencies (none required!)
│
├── LICENSE               # CMU License
├── README                # Original CMUdict README
└── PROJECT_README.md     # This file
```

## 🚀 Quick Start

### 1. Prerequisites

- **Python 3.7 or higher** is recommended
- No external dependencies required! Uses only Python standard library

### 2. Verify Python Installation

Open a command prompt and run:

```cmd
python --version
```

You should see Python 3.7 or higher.

### 3. Run the Demo

Try the built-in demo to see the module in action:

```cmd
python cmudict_loader.py
```

This will run a demo showing:
- Word pronunciation lookups
- Syllable counting
- Rhyme finding
- Stress pattern analysis
- Pattern-based searches

### 4. Run Examples

For more comprehensive examples:

```cmd
python example_usage.py
```

This includes 7 different examples and an interactive mode!

## 📖 Usage Guide

### Basic Usage

```python
from cmudict_loader import CMUDict

# Initialize the dictionary
cmu = CMUDict()

# Look up a word's pronunciation
pronunciations = cmu.lookup("hello")
print(pronunciations)
# Output: [['HH', 'AH0', 'L', 'OW1']]

# Count syllables
syllables = cmu.count_syllables("beautiful")
print(syllables)  # Output: 3

# Find rhymes
rhymes = cmu.find_rhymes("cat", max_results=5)
print(rhymes)
# Output: ['bat', 'hat', 'mat', 'pat', 'sat']
```

### Available Methods

#### `CMUDict` Class

**`__init__(dict_path="cmudict.dict")`**
- Initializes and loads the dictionary
- Parameters:
  - `dict_path`: Path to the dictionary file (default: "cmudict.dict")

**`lookup(word: str) → List[List[str]] | None`**
- Returns all pronunciations for a word
- Returns `None` if word not found
- Each pronunciation is a list of phonemes

**`count_syllables(word: str) → int | None`**
- Counts syllables in a word
- Based on the number of vowel phonemes with stress markers
- Returns `None` if word not found

**`find_rhymes(word: str, max_results: int = 10) → List[str]`**
- Finds words that rhyme with the given word
- Returns up to `max_results` rhyming words

**`get_stress_pattern(word: str) → str | None`**
- Returns the stress pattern (e.g., "1 0 2")
- Stress levels: 0 = no stress, 1 = primary, 2 = secondary

**`get_phonemes_readable(word: str) → str | None`**
- Returns a readable string of phonemes

**`word_exists(word: str) → bool`**
- Checks if a word exists in the dictionary

**`search_by_pattern(pattern: str, max_results: int = 20) → List[str]`**
- Search using wildcards (e.g., "cat*" finds "cat", "cats", "catastrophe")

### Helper Functions

**`load_phoneme_types(phones_path: str = "cmudict.phones") → Dict[str, str]`**
- Loads phoneme type information
- Returns a dictionary mapping phonemes to their types (vowel, consonant, etc.)

## 🔍 Understanding the Dictionary Format

### Dictionary File (`cmudict.dict`)

Each line contains:
```
WORD  PHONEME1 PHONEME2 PHONEME3 ...
```

Example:
```
HELLO  HH AH0 L OW1
WORLD  W ER1 L D
PYTHON  P AY1 TH AA0 N
```

- Words are in UPPERCASE
- Alternative pronunciations are marked with (2), (3), etc.
- Comments start with `#`

### Phoneme Notation (ARPAbet)

Phonemes use ARPAbet symbols:

**Vowels** (with stress markers 0, 1, or 2):
- `AA` - odd (AA1 D)
- `AE` - at (AE1 T)
- `AH` - hut (HH AH1 T)
- `AO` - ought (AO1 T)
- `EH` - Ed (EH1 D)
- `ER` - hurt (HH ER1 T)
- `IH` - it (IH1 T)
- `IY` - eat (IY1 T)
- `OW` - oat (OW1 T)
- `UH` - hood (HH UH1 D)
- `UW` - two (T UW1)

**Consonants**:
- `B, D, F, G, K, L, M, N, P, R, S, T, V, W, Z` - similar to English
- `CH` - cheese
- `SH` - she
- `TH` - theta
- `DH` - thee
- `ZH` - seizure
- `HH` - he
- `JH` - gee
- `NG` - ping
- `Y` - yield

**Stress Markers**:
- `0` - No stress
- `1` - Primary stress
- `2` - Secondary stress

## 💡 Example Use Cases

### 1. Syllable Counter for Poetry

```python
from cmudict_loader import CMUDict

cmu = CMUDict()

def count_line_syllables(line):
    words = line.lower().split()
    total = sum(cmu.count_syllables(w) or 0 for w in words)
    return total

# Check if it's a haiku (5-7-5 syllables)
lines = [
    "An old silent pond",
    "A frog jumps into the pond",
    "Splash silence again"
]

for line in lines:
    print(f"{line}: {count_line_syllables(line)} syllables")
```

### 2. Rhyme Generator

```python
from cmudict_loader import CMUDict

cmu = CMUDict()

word = "love"
rhymes = cmu.find_rhymes(word, max_results=20)
print(f"Words that rhyme with '{word}': {', '.join(rhymes)}")
```

### 3. Pronunciation Comparison

```python
from cmudict_loader import CMUDict

cmu = CMUDict()

words = ["read", "lead", "tear"]  # Words with multiple pronunciations
for word in words:
    pronunciations = cmu.lookup(word)
    if pronunciations and len(pronunciations) > 1:
        print(f"\n{word.upper()} has {len(pronunciations)} pronunciations:")
        for i, pron in enumerate(pronunciations, 1):
            print(f"  {i}. {' '.join(pron)}")
```

### 4. Stress Pattern Analysis

```python
from cmudict_loader import CMUDict

cmu = CMUDict()

# Find words with specific stress patterns
words = ["photograph", "photography", "photographic"]
for word in words:
    pattern = cmu.get_stress_pattern(word)
    print(f"{word:15} stress pattern: {pattern}")
```

## 🎯 Advanced Features

### Custom Dictionary Path

```python
cmu = CMUDict(dict_path="path/to/your/cmudict.dict")
```

### Pattern Matching

```python
# Find all words starting with "un"
words = cmu.search_by_pattern("un*", max_results=50)

# Find all words ending with "tion"
words = cmu.search_by_pattern("*tion", max_results=50)
```

### Phoneme Type Analysis

```python
from cmudict_loader import load_phoneme_types

phoneme_types = load_phoneme_types()

# Check phoneme types
print(phoneme_types["AA"])  # Output: vowel
print(phoneme_types["B"])   # Output: stop
print(phoneme_types["S"])   # Output: fricative
```

## 📊 Dictionary Statistics

- **Total words**: ~134,000
- **Unique words**: ~119,400
- **Words with 2 pronunciations**: ~6,800
- **Words with 3+ pronunciations**: ~840
- **Total phonemes**: 39 (see `cmudict.phones`)

## 🛠️ Troubleshooting

### Issue: "File not found" error

**Solution**: Make sure you're running the script from the `cmudict` directory, or provide the full path:

```python
cmu = CMUDict(dict_path="C:/Users/Mike/Documents/GitHub/cmudict/cmudict.dict")
```

### Issue: Word not found

**Solution**: The dictionary contains ~134,000 words but not all English words. Very new words, slang, or proper nouns might be missing.

### Issue: Encoding errors

**Solution**: The dictionary uses `latin-1` encoding (already handled in the module). If you modify the code, ensure you use:

```python
with open(dict_path, 'r', encoding='latin-1') as f:
    # ...
```

## 📚 Additional Resources

- **Original CMUdict**: https://github.com/cmusphinx/cmudict
- **ARPAbet Documentation**: Wikipedia - ARPABET
- **CMU Speech Group**: http://www.speech.cs.cmu.edu/
- **NLTK CMUdict**: https://www.nltk.org/howto/corpus.html#pronouncing-dictionary

## 📄 License

The CMU Pronouncing Dictionary is Copyright (C) 1993-2014 by Carnegie Mellon University. Use of this dictionary for any research or commercial purpose is completely unrestricted.

See the `LICENSE` file for full details.

## 🤝 Contributing

This is a simple educational project. If you find issues or want to add features:

1. The original CMUdict is maintained at: https://github.com/cmusphinx/cmudict
2. For this Python wrapper, feel free to modify and extend as needed!

## 🎓 Learning More

### What is a Pronouncing Dictionary?

A pronouncing dictionary maps written words to their phonetic pronunciations. This is useful for:
- **Text-to-Speech (TTS)** systems
- **Speech Recognition** systems
- **Poetry analysis** (syllable counting, rhyme detection)
- **Language learning** applications
- **Linguistic research**

### Why CMUdict?

- ✅ Free and open source
- ✅ Large vocabulary (134,000+ words)
- ✅ High quality (maintained by Carnegie Mellon)
- ✅ Widely used in research and industry
- ✅ Simple text format (easy to parse)

## 🚀 Next Steps

1. **Run the demo**: `python cmudict_loader.py`
2. **Try the examples**: `python example_usage.py`
3. **Build something cool**: Use the library in your own projects!

---

**Happy coding! 🎉**
