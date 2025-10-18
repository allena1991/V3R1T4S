#!/usr/bin/env python3
"""
Examples demonstrating the Ultimate Metaprkmpf capabilities
"""

from metaprkmpf import UltimateMetaprkmpf, TruthLevel


def example_basic_usage():
    """Basic usage example"""
    print("=" * 60)
    print("EXAMPLE 1: Basic Pattern Recognition")
    print("=" * 60)
    
    metaprkmpf = UltimateMetaprkmpf()
    
    # Add a simple pattern
    metaprkmpf.add_pattern(
        "veritas",
        r"\bveritas\b",
        TruthLevel.ABSOLUTE,
        {"meaning": "truth in Latin"}
    )
    
    text = "In veritas, we trust the ultimate VERITAS"
    result = metaprkmpf.ultimate_process(text)
    
    print(f"Text: {text}")
    print(f"Patterns found: {len(result['patterns'])}")
    print(f"Ultimate truth: {result['ultimate_truth']}")
    print()


def example_code_analysis():
    """Analyze code patterns"""
    print("=" * 60)
    print("EXAMPLE 2: Code Pattern Analysis")
    print("=" * 60)
    
    metaprkmpf = UltimateMetaprkmpf()
    
    # Add code-related patterns
    metaprkmpf.add_pattern(
        "function_def",
        r"\bdef\s+\w+",
        TruthLevel.VERIFIED,
        {"type": "python_function"}
    )
    
    metaprkmpf.add_pattern(
        "class_def",
        r"\bclass\s+\w+",
        TruthLevel.VERIFIED,
        {"type": "python_class"}
    )
    
    metaprkmpf.add_pattern(
        "import_statement",
        r"\bimport\s+\w+",
        TruthLevel.PROBABLE,
        {"type": "dependency"}
    )
    
    code = """
    import sys
    import re
    
    class TruthSeeker:
        def find_truth(self):
            return "truth"
    
    def ultimate_function():
        pass
    """
    
    result = metaprkmpf.ultimate_process(code)
    
    print("Analyzing Python code...")
    print(f"Functions found: {sum(1 for p in result['patterns'] if 'function' in p['pattern_name'])}")
    print(f"Classes found: {sum(1 for p in result['patterns'] if 'class' in p['pattern_name'])}")
    print(f"Imports found: {sum(1 for p in result['patterns'] if 'import' in p['pattern_name'])}")
    print(f"Complexity score: {result['analysis']['complexity_score']:.2f}")
    print()


def example_transformations():
    """Demonstrate text transformations"""
    print("=" * 60)
    print("EXAMPLE 3: Text Transformations")
    print("=" * 60)
    
    metaprkmpf = UltimateMetaprkmpf()
    
    # Add transformations
    metaprkmpf.add_transformation("uppercase", lambda text: text.upper())
    metaprkmpf.add_transformation("reverse", lambda text: text[::-1])
    metaprkmpf.add_transformation(
        "leet_speak",
        lambda text: (text.replace('e', '3')
                          .replace('a', '4')
                          .replace('o', '0')
                          .replace('t', '7')
                          .replace('s', '5'))
    )
    
    original = "Veritas Ultimate"
    
    print(f"Original: {original}")
    print(f"Uppercase: {metaprkmpf.transform(original, 'uppercase')}")
    print(f"Reversed: {metaprkmpf.transform(original, 'reverse')}")
    print(f"Leet: {metaprkmpf.transform(original, 'leet_speak')}")
    print()


def example_philosophical_analysis():
    """Analyze philosophical text"""
    print("=" * 60)
    print("EXAMPLE 4: Philosophical Text Analysis")
    print("=" * 60)
    
    metaprkmpf = UltimateMetaprkmpf()
    
    # Add philosophical patterns
    metaprkmpf.add_pattern(
        "truth_concept",
        r"\b(truth|reality|veritas)\b",
        TruthLevel.ABSOLUTE
    )
    
    metaprkmpf.add_pattern(
        "knowledge_concept",
        r"\b(knowledge|wisdom|understanding)\b",
        TruthLevel.VERIFIED
    )
    
    metaprkmpf.add_pattern(
        "question",
        r"\b(what|why|how|where|when)\b",
        TruthLevel.UNKNOWN
    )
    
    text = """
    What is truth? Truth is the ultimate reality that transcends knowledge.
    Through understanding and wisdom, we approach the veritas.
    How do we know what we know? The pattern of reality reveals itself.
    """
    
    result = metaprkmpf.ultimate_process(text)
    
    print("Philosophical analysis:")
    print(f"Truth concepts: {sum(1 for p in result['patterns'] if 'truth' in p['pattern_name'])}")
    print(f"Knowledge concepts: {sum(1 for p in result['patterns'] if 'knowledge' in p['pattern_name'])}")
    print(f"Questions: {sum(1 for p in result['patterns'] if 'question' in p['pattern_name'])}")
    print()
    print("Insights:")
    for insight in result['insights']:
        print(f"  • {insight}")
    print()
    print(f"Ultimate Truth: {result['ultimate_truth']}")
    print()


def example_meta_pattern_analysis():
    """Demonstrate meta-pattern analysis"""
    print("=" * 60)
    print("EXAMPLE 5: Meta-Pattern Analysis")
    print("=" * 60)
    
    metaprkmpf = UltimateMetaprkmpf()
    
    # Add meta-patterns
    metaprkmpf.add_pattern(
        "meta_prefix",
        r"\bmeta[-\w]*",
        TruthLevel.VERIFIED,
        {"category": "meta-analysis"}
    )
    
    metaprkmpf.add_pattern(
        "recursive_pattern",
        r"\b(recursive|recursion|self-referential)\b",
        TruthLevel.VERIFIED,
        {"category": "recursion"}
    )
    
    metaprkmpf.add_pattern(
        "pattern_of_patterns",
        r"\bpattern[s]?\s+of\s+pattern[s]?\b",
        TruthLevel.ABSOLUTE,
        {"category": "meta-meta"}
    )
    
    text = """
    The metaprkmpf discovers meta-patterns through recursive analysis.
    It finds patterns of patterns, revealing the meta-structure of reality.
    This self-referential system uses metadata to understand metacognition.
    """
    
    result = metaprkmpf.ultimate_process(text)
    
    print("Meta-pattern analysis results:")
    for pattern in result['patterns']:
        print(f"  {pattern['pattern_name']}: '{pattern['matched_text']}' "
              f"[{pattern['truth_level']}]")
    
    print()
    print(f"Analysis: {result['analysis']['patterns_found']} meta-patterns discovered")
    print(f"Ultimate Truth: {result['ultimate_truth']}")
    print()


def main():
    """Run all examples"""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 8 + "ULTIMATE METAPRKMPF - EXAMPLES" + " " * 20 + "║")
    print("╚" + "═" * 58 + "╝")
    print("\n")
    
    example_basic_usage()
    example_code_analysis()
    example_transformations()
    example_philosophical_analysis()
    example_meta_pattern_analysis()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
