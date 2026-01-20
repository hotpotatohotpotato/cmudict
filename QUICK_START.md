# Quick Start Guide - CMUdict Python Project

## 🎯 Get Started in 3 Steps

### Step 1: Check Python
```cmd
python --version
```
You need Python 3.7+. If you don't have it, download from [python.org](https://www.python.org/).

### Step 2: Run the Simple Lookup Tool
```cmd
cd C:\Users\Mike\Documents\GitHub\cmudict
python lookup.py
```

Then type any word to see its pronunciation! Type 'quit' to exit.

### Step 3: Try Other Scripts
Run the full demo:
```cmd
python cmudict_loader.py
```

Run comprehensive examples:
```cmd
python example_usage.py
```

## 📚 What Each File Does

| File | Purpose |
|------|---------|
| **lookup.py** | **⭐ START HERE!** Simple interactive word lookup tool |
| **cmudict_loader.py** | Main module with CMUDict class - your workhorse |
| **example_usage.py** | 7 comprehensive examples + interactive mode |
| **PROJECT_README.md** | Complete documentation |
| **requirements.txt** | Dependencies (none needed!) |
| **cmudict.dict** | The actual dictionary data (126,000+ words) |

## 🔥 Common Operations Cheat Sheet

```python
from cmudict_loader import CMUDict
cmu = CMUDict()

# Look up pronunciation
cmu.lookup("word")              # Returns: [['W', 'ER1', 'D']]

# Count syllables
cmu.count_syllables("beautiful") # Returns: 3

# Find rhymes
cmu.find_rhymes("cat", max_results=10)

# Get stress pattern
cmu.get_stress_pattern("computer")  # Returns: "0 1 0"

# Check if word exists
cmu.word_exists("python")           # Returns: True

# Search with wildcards
cmu.search_by_pattern("cat*")       # Returns: ['cat', 'cats', 'catastrophe', ...]

# Get readable phonemes
cmu.get_phonemes_readable("hello")  # Returns: "HH AH0 L OW1"
```

## 💡 Example Projects You Can Build

1. **Syllable Counter** - Count syllables in poems or songs
2. **Rhyme Finder** - Find perfect rhymes for poetry
3. **Haiku Validator** - Check if text follows 5-7-5 pattern
4. **Pronunciation Tutor** - Show how words are pronounced
5. **Word Game** - Find words with specific patterns or rhymes
6. **Text-to-Speech Helper** - Generate pronunciation guides

## 🚨 Troubleshooting

**Q: I get "No module named 'cmudict_loader'"**
```cmd
# Make sure you're in the right directory:
cd C:\Users\Mike\Documents\GitHub\cmudict
```

**Q: I get "FileNotFoundError: cmudict.dict"**
```cmd
# Run from the cmudict directory, or use full path:
cmu = CMUDict(dict_path="C:/Users/Mike/Documents/GitHub/cmudict/cmudict.dict")
```

**Q: Word not found in dictionary**
- The dictionary has 126,000+ words but not every word
- Try variations or check spelling
- Very new slang words might not be included

## 📖 Learn More

- Full documentation: See **PROJECT_README.md**
- Run examples: `python example_usage.py`
- Interactive mode: Run examples and choose "y" for interactive

## 🎓 Understanding the Output

When you lookup "hello":
```python
[['HH', 'AH0', 'L', 'OW1']]
```

This means:
- `HH` = "h" sound (like in "he")
- `AH0` = "uh" sound, no stress
- `L` = "l" sound
- `OW1` = "oh" sound, primary stress (1)

Result: "huh-LOH" (emphasis on second syllable)

## ✨ That's It!

You're ready to start using CMUdict in your Python projects. Have fun! 🎉

For more details, see **PROJECT_README.md**.
