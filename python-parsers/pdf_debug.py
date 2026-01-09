#!/usr/bin/env python3
"""
Enhanced debug script to diagnose PDF text extraction issues
"""

import sys
import re

try:
    import pdfplumber
except ImportError:
    print("Please install pdfplumber: pip install pdfplumber")
    sys.exit(1)

def comprehensive_pdf_debug(pdf_path: str):
    """Comprehensive PDF debugging."""
    print("=== COMPREHENSIVE PDF ANALYSIS ===\n")
    
    with pdfplumber.open(pdf_path) as pdf:
        print(f"PDF has {len(pdf.pages)} pages")
        print(f"PDF metadata: {pdf.metadata}")
        print()
        
        for page_num, page in enumerate(pdf.pages[:3], 1):
            print(f"--- PAGE {page_num} ANALYSIS ---")
            
            # Check page dimensions
            print(f"Page dimensions: {page.width} x {page.height}")
            
            # Try different text extraction methods
            print("\n1. Standard text extraction:")
            text1 = page.extract_text()
            if text1:
                lines1 = text1.split('\n')
                print(f"   Extracted {len(lines1)} lines")
                for i, line in enumerate(lines1[:10], 1):
                    print(f"   {i:2d}: '{line}'")
                if len(lines1) > 10:
                    print(f"   ... and {len(lines1) - 10} more lines")
            else:
                print("   No text extracted")
            
            print("\n2. Text extraction with layout:")
            text2 = page.extract_text(layout=True)
            if text2:
                lines2 = text2.split('\n')
                print(f"   Extracted {len(lines2)} lines")
                for i, line in enumerate(lines2[:10], 1):
                    print(f"   {i:2d}: '{line}'")
                if len(lines2) > 10:
                    print(f"   ... and {len(lines2) - 10} more lines")
            else:
                print("   No text extracted")
            
            print("\n3. Text extraction with x_tolerance:")
            try:
                text3 = page.extract_text(x_tolerance=2, y_tolerance=2)
                if text3:
                    lines3 = text3.split('\n')
                    print(f"   Extracted {len(lines3)} lines")
                    for i, line in enumerate(lines3[:10], 1):
                        print(f"   {i:2d}: '{line}'")
                    if len(lines3) > 10:
                        print(f"   ... and {len(lines3) - 10} more lines")
                else:
                    print("   No text extracted")
            except Exception as e:
                print(f"   Error: {e}")
            
            # Check for images
            print(f"\n4. Images on page: {len(page.images)}")
            if page.images:
                print("   This page contains images - might be a scanned PDF")
            
            # Check for text objects
            print(f"5. Text objects: {len(page.chars)}")
            if page.chars:
                print("   Sample characters:")
                for i, char in enumerate(page.chars[:20]):
                    print(f"   '{char['text']}' at ({char['x0']:.1f}, {char['y0']:.1f})")
                if len(page.chars) > 20:
                    print(f"   ... and {len(page.chars) - 20} more characters")
            
            # Check for tables
            print(f"\n6. Tables detected: {len(page.find_tables())}")
            
            print("\n" + "="*50 + "\n")

def try_alternative_extraction(pdf_path: str):
    """Try alternative text extraction methods."""
    print("=== TRYING ALTERNATIVE EXTRACTION METHODS ===\n")
    
    # Method 1: Extract words instead of text
    print("Method 1: Word extraction")
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages[:2], 1):
            words = page.extract_words()
            print(f"Page {page_num}: {len(words)} words extracted")
            if words:
                print("First 20 words:")
                for i, word in enumerate(words[:20]):
                    print(f"  {word['text']} at ({word['x0']:.1f}, {word['y0']:.1f})")
            print()
    
    # Method 2: Extract tables
    print("Method 2: Table extraction")
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages[:2], 1):
            tables = page.extract_tables()
            print(f"Page {page_num}: {len(tables)} tables extracted")
            for i, table in enumerate(tables):
                print(f"  Table {i+1}: {len(table)} rows, {len(table[0]) if table else 0} columns")
                if table:
                    print("  First few rows:")
                    for row in table[:3]:
                        print(f"    {row}")
            print()

def analyze_character_positions(pdf_path: str):
    """Analyze character positions to understand layout."""
    print("=== CHARACTER POSITION ANALYSIS ===\n")
    
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[0]
        chars = page.chars
        
        if not chars:
            print("No characters found on first page")
            return
        
        print(f"Found {len(chars)} characters on first page")
        
        # Group characters by line (similar y positions)
        lines = {}
        for char in chars:
            y = round(char['y0'])
            if y not in lines:
                lines[y] = []
            lines[y].append(char)
        
        print(f"Characters grouped into {len(lines)} lines")
        
        # Sort lines by y position (top to bottom)
        sorted_lines = sorted(lines.items(), key=lambda x: -x[0])  # Negative for top to bottom
        
        print("\nFirst 20 lines of text:")
        for i, (y, line_chars) in enumerate(sorted_lines[:20]):
            # Sort characters in line by x position
            line_chars.sort(key=lambda c: c['x0'])
            text = ''.join(c['text'] for c in line_chars)
            print(f"{i+1:2d}: y={y:3.0f} '{text.strip()}'")

def main():
    if len(sys.argv) != 2:
        print("Usage: python debug_zavala_parser.py <input_pdf>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    
    try:
        comprehensive_pdf_debug(pdf_path)
        try_alternative_extraction(pdf_path)
        analyze_character_positions(pdf_path)
    except Exception as e:
        print(f"Error analyzing PDF: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()