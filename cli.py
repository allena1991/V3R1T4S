#!/usr/bin/env python3
"""
Command-line interface for the Ultimate Metaprkmpf
"""

import sys
import argparse
from metaprkmpf import UltimateMetaprkmpf, TruthLevel


def setup_default_patterns(metaprkmpf):
    """Set up default pattern recognizers"""
    # Truth-related patterns
    metaprkmpf.add_pattern(
        "truth_declaration",
        r"\b(truth|veritas|reality|verity)\b",
        TruthLevel.VERIFIED,
        {"category": "truth"}
    )
    
    # Pattern-related patterns
    metaprkmpf.add_pattern(
        "pattern_reference",
        r"\b(pattern|structure|system|framework)\b",
        TruthLevel.PROBABLE,
        {"category": "structure"}
    )
    
    # Ultimate concepts
    metaprkmpf.add_pattern(
        "ultimate_concept",
        r"\b(ultimate|supreme|absolute|final|perfect)\b",
        TruthLevel.ABSOLUTE,
        {"category": "transcendent"}
    )
    
    # Meta concepts
    metaprkmpf.add_pattern(
        "meta_concept",
        r"\bmeta[-\w]*",
        TruthLevel.VERIFIED,
        {"category": "meta"}
    )
    
    # Knowledge concepts
    metaprkmpf.add_pattern(
        "knowledge",
        r"\b(knowledge|wisdom|understanding|insight)\b",
        TruthLevel.VERIFIED,
        {"category": "epistemology"}
    )


def analyze_text(args):
    """Analyze text from file or stdin"""
    metaprkmpf = UltimateMetaprkmpf()
    setup_default_patterns(metaprkmpf)
    
    # Read text
    if args.file:
        try:
            with open(args.file, 'r') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found", file=sys.stderr)
            sys.exit(1)
    else:
        text = sys.stdin.read()
    
    # Process
    result = metaprkmpf.ultimate_process(text)
    
    # Output
    if args.json:
        import json
        print(json.dumps(result, indent=2, default=str))
    else:
        print_formatted_result(result, args)


def print_formatted_result(result, args):
    """Print result in human-readable format"""
    print("\n" + "=" * 60)
    print("ULTIMATE METAPRKMPF - ANALYSIS RESULTS")
    print("=" * 60 + "\n")
    
    if args.verbose or args.patterns:
        print(f"PATTERNS DISCOVERED: {len(result['patterns'])}")
        print("-" * 60)
        for pattern in result['patterns']:
            print(f"  [{pattern['truth_level']}] {pattern['pattern_name']}: "
                  f"'{pattern['matched_text']}' at position {pattern['position']}")
        print()
    
    if args.verbose or args.analysis:
        print("META-ANALYSIS:")
        print("-" * 60)
        for key, value in result['analysis'].items():
            print(f"  {key}: {value}")
        print()
    
    if args.verbose or args.insights:
        print("INSIGHTS:")
        print("-" * 60)
        for insight in result['insights']:
            print(f"  • {insight}")
        print()
    
    print("ULTIMATE TRUTH:")
    print("-" * 60)
    print(f"  >>> {result['ultimate_truth']}")
    print("\n" + "=" * 60 + "\n")


def transform_text(args):
    """Transform text using built-in transformations"""
    metaprkmpf = UltimateMetaprkmpf()
    
    # Add transformations
    metaprkmpf.add_transformation("upper", lambda t: t.upper())
    metaprkmpf.add_transformation("lower", lambda t: t.lower())
    metaprkmpf.add_transformation("reverse", lambda t: t[::-1])
    metaprkmpf.add_transformation(
        "leet",
        lambda t: t.replace('e', '3').replace('a', '4').replace('o', '0')
                   .replace('t', '7').replace('s', '5').replace('i', '1')
    )
    metaprkmpf.add_transformation(
        "title",
        lambda t: t.title()
    )
    
    # Read text
    if args.file:
        try:
            with open(args.file, 'r') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found", file=sys.stderr)
            sys.exit(1)
    else:
        text = sys.stdin.read()
    
    # Transform
    try:
        result = metaprkmpf.transform(text, args.transformation)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        print(f"Available transformations: upper, lower, reverse, leet, title", 
              file=sys.stderr)
        sys.exit(1)


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Ultimate Metaprkmpf - Meta Pattern Recognition & Truth Discovery",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze a file
  %(prog)s analyze file.txt
  
  # Analyze from stdin
  echo "The ultimate truth" | %(prog)s analyze
  
  # Show only patterns
  %(prog)s analyze -p file.txt
  
  # Transform text to uppercase
  %(prog)s transform -t upper file.txt
  
  # Get JSON output
  %(prog)s analyze --json file.txt
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze text for patterns')
    analyze_parser.add_argument('file', nargs='?', help='File to analyze (or stdin)')
    analyze_parser.add_argument('-v', '--verbose', action='store_true',
                               help='Show all details')
    analyze_parser.add_argument('-p', '--patterns', action='store_true',
                               help='Show discovered patterns')
    analyze_parser.add_argument('-a', '--analysis', action='store_true',
                               help='Show meta-analysis')
    analyze_parser.add_argument('-i', '--insights', action='store_true',
                               help='Show insights')
    analyze_parser.add_argument('--json', action='store_true',
                               help='Output as JSON')
    
    # Transform command
    transform_parser = subparsers.add_parser('transform', help='Transform text')
    transform_parser.add_argument('file', nargs='?', help='File to transform (or stdin)')
    transform_parser.add_argument('-t', '--transformation', required=True,
                                 choices=['upper', 'lower', 'reverse', 'leet', 'title'],
                                 help='Transformation to apply')
    
    # Demo command
    demo_parser = subparsers.add_parser('demo', help='Run demonstration')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    if args.command == 'analyze':
        analyze_text(args)
    elif args.command == 'transform':
        transform_text(args)
    elif args.command == 'demo':
        from metaprkmpf import main as demo_main
        demo_main()


if __name__ == "__main__":
    main()
