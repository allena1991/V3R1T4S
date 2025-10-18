#!/usr/bin/env python3
"""
Tests for the Ultimate Metaprkmpf
"""

import unittest
from metaprkmpf import UltimateMetaprkmpf, TruthLevel, Pattern


class TestUltimateMetaprkmpf(unittest.TestCase):
    """Test suite for the Ultimate Metaprkmpf"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.metaprkmpf = UltimateMetaprkmpf()
        
    def test_initialization(self):
        """Test that metaprkmpf initializes correctly"""
        self.assertIsNotNone(self.metaprkmpf)
        self.assertEqual(len(self.metaprkmpf.patterns), 0)
        self.assertEqual(len(self.metaprkmpf.transformations), 0)
        self.assertEqual(len(self.metaprkmpf.discovered_truths), 0)
        
    def test_add_pattern(self):
        """Test adding patterns"""
        self.metaprkmpf.add_pattern(
            "test_pattern",
            r"\btest\b",
            TruthLevel.VERIFIED
        )
        self.assertEqual(len(self.metaprkmpf.patterns), 1)
        self.assertEqual(self.metaprkmpf.patterns[0].name, "test_pattern")
        self.assertEqual(self.metaprkmpf.patterns[0].truth_level, TruthLevel.VERIFIED)
        
    def test_add_transformation(self):
        """Test adding transformations"""
        self.metaprkmpf.add_transformation(
            "reverse",
            lambda text: text[::-1]
        )
        self.assertEqual(len(self.metaprkmpf.transformations), 1)
        self.assertIn("reverse", self.metaprkmpf.transformations)
        
    def test_recognize_patterns(self):
        """Test pattern recognition"""
        self.metaprkmpf.add_pattern(
            "truth_word",
            r"\btruth\b",
            TruthLevel.ABSOLUTE
        )
        
        text = "The truth is out there"
        results = self.metaprkmpf.recognize(text)
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['pattern_name'], "truth_word")
        self.assertEqual(results[0]['matched_text'], "truth")
        self.assertEqual(results[0]['truth_level'], "ABSOLUTE")
        
    def test_transform(self):
        """Test text transformation"""
        self.metaprkmpf.add_transformation(
            "uppercase",
            lambda text: text.upper()
        )
        
        result = self.metaprkmpf.transform("hello", "uppercase")
        self.assertEqual(result, "HELLO")
        
    def test_transform_not_found(self):
        """Test transformation with invalid name"""
        with self.assertRaises(ValueError):
            self.metaprkmpf.transform("hello", "nonexistent")
            
    def test_meta_analyze(self):
        """Test meta-analysis functionality"""
        self.metaprkmpf.add_pattern(
            "word",
            r"\bword\b",
            TruthLevel.PROBABLE
        )
        
        text = "This is a test word for analysis"
        analysis = self.metaprkmpf.meta_analyze(text)
        
        self.assertIn('total_characters', analysis)
        self.assertIn('total_lines', analysis)
        self.assertIn('total_words', analysis)
        self.assertIn('patterns_found', analysis)
        self.assertIn('truth_levels', analysis)
        self.assertIn('complexity_score', analysis)
        
        self.assertEqual(analysis['total_words'], 7)
        self.assertEqual(analysis['patterns_found'], 1)
        
    def test_ultimate_process(self):
        """Test the ultimate processing function"""
        self.metaprkmpf.add_pattern(
            "ultimate",
            r"\bultimate\b",
            TruthLevel.ABSOLUTE
        )
        
        text = "The ultimate truth"
        result = self.metaprkmpf.ultimate_process(text)
        
        self.assertIn('patterns', result)
        self.assertIn('analysis', result)
        self.assertIn('insights', result)
        self.assertIn('ultimate_truth', result)
        
        self.assertIsInstance(result['patterns'], list)
        self.assertIsInstance(result['analysis'], dict)
        self.assertIsInstance(result['insights'], list)
        self.assertIsInstance(result['ultimate_truth'], str)
        
    def test_truth_levels(self):
        """Test that truth levels are properly categorized"""
        self.assertEqual(TruthLevel.UNKNOWN.value, 0)
        self.assertEqual(TruthLevel.PROBABLE.value, 1)
        self.assertEqual(TruthLevel.VERIFIED.value, 2)
        self.assertEqual(TruthLevel.ABSOLUTE.value, 3)
        
    def test_pattern_dataclass(self):
        """Test Pattern dataclass"""
        pattern = Pattern(
            name="test",
            regex=r"\btest\b",
            truth_level=TruthLevel.VERIFIED,
            metadata={"key": "value"}
        )
        
        self.assertEqual(pattern.name, "test")
        self.assertEqual(pattern.regex, r"\btest\b")
        self.assertEqual(pattern.truth_level, TruthLevel.VERIFIED)
        self.assertEqual(pattern.metadata["key"], "value")
        
    def test_multiple_patterns(self):
        """Test recognition of multiple patterns"""
        self.metaprkmpf.add_pattern("truth", r"\btruth\b", TruthLevel.ABSOLUTE)
        self.metaprkmpf.add_pattern("pattern", r"\bpattern\b", TruthLevel.VERIFIED)
        
        text = "The truth follows a pattern"
        results = self.metaprkmpf.recognize(text)
        
        self.assertEqual(len(results), 2)
        pattern_names = [r['pattern_name'] for r in results]
        self.assertIn("truth", pattern_names)
        self.assertIn("pattern", pattern_names)
        
    def test_no_patterns_found(self):
        """Test behavior when no patterns are found"""
        self.metaprkmpf.add_pattern("xyz", r"\bxyz\b", TruthLevel.PROBABLE)
        
        text = "This text has no matching patterns"
        results = self.metaprkmpf.recognize(text)
        
        self.assertEqual(len(results), 0)
        
    def test_insights_generation(self):
        """Test insight generation"""
        # Add multiple patterns to trigger insights
        for i in range(15):
            self.metaprkmpf.add_pattern(f"pattern_{i}", r"\btest\b", TruthLevel.VERIFIED)
            
        text = " ".join(["test"] * 15)
        result = self.metaprkmpf.ultimate_process(text)
        
        self.assertGreater(len(result['insights']), 0)
        
    def test_complexity_score(self):
        """Test complexity score calculation"""
        self.metaprkmpf.add_pattern("test", r"\btest\b", TruthLevel.VERIFIED)
        
        text = "test " * 100
        analysis = self.metaprkmpf.meta_analyze(text)
        
        self.assertGreater(analysis['complexity_score'], 0)
        
    def test_case_insensitive_matching(self):
        """Test that pattern matching is case-insensitive"""
        self.metaprkmpf.add_pattern("truth", r"\btruth\b", TruthLevel.ABSOLUTE)
        
        text = "TRUTH Truth truth"
        results = self.metaprkmpf.recognize(text)
        
        self.assertEqual(len(results), 3)


if __name__ == '__main__':
    unittest.main()
