import os
import re

def fix_math_line_breaks(text):
    # Regex to find block math $$ ... $$
    def block_repl(match):
        math = match.group(0)
        # Replace standard \\ with \\\\ inside math blocks, preventing double-escaping
        # We replace any \\ that is not preceded or followed by another \
        math_clean = re.sub(r'(?<!\\)\\\\(?!\\)', r'\\\\\\\\', math)
        return math_clean

    # Regex to find inline math $ ... $
    def inline_repl(match):
        math = match.group(0)
        math_clean = re.sub(r'(?<!\\)\\\\(?!\\)', r'\\\\\\\\', math)
        return math_clean

    text = re.sub(r'\$\$.*?\$\$', block_repl, text, flags=re.DOTALL)
    text = re.sub(r'(?<!\$)\$[^\$\n]+?\$(?!\$)', inline_repl, text)
    return text

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    docs_dir = os.path.join(base_dir, "docs")
    benchmarks_dir = os.path.join(base_dir, "benchmarks")
    artifacts_dir = "C:\\Users\\gamer\\.gemini\\antigravity-cli\\brain\\cb3795ac-0c45-4ee9-bd7c-2e1d0f399069"
    
    targets = []
    
    # Add files in docs/
    for root, _, files in os.walk(docs_dir):
        for f in files:
            if f.endswith(".md"):
                targets.append(os.path.join(root, f))
                
    # Add files in benchmarks/
    for root, _, files in os.walk(benchmarks_dir):
        for f in files:
            if f.endswith(".md"):
                targets.append(os.path.join(root, f))
                
    # Add files in artifacts directory
    if os.path.exists(artifacts_dir):
        for f in os.listdir(artifacts_dir):
            if f.endswith(".md"):
                targets.append(os.path.join(artifacts_dir, f))

    for filepath in targets:
        print(f"Processing: {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        fixed_content = fix_math_line_breaks(content)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(fixed_content)

    print("All double backslashes inside math blocks have been successfully escaped to four backslashes!")

if __name__ == "__main__":
    main()
