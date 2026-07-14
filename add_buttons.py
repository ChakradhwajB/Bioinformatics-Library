import os
import re

pages = ['io.html', 'genetics.html', 'kmers.html', 'find_motif.html', 'dot_plot.html', 'distances.html', 'needleman_wunsch.html', 'suffix_array.html', 'trie.html']

for page in pages:
    path = os.path.join('frontend', 'pages', page)
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for bg in ['bg-emerald-50', 'bg-indigo-50', 'bg-rose-50']:
        pattern = r'(<div class="' + bg + r'[^>]*>.*?<\/p>)\s*<\/div>'
        replacement = r'\1\n              <button onclick="window.loadSandboxChallenge(this)" class="mt-2 text-[9px] font-bold bg-white border border-[rgba(0,0,0,0.1)] text-slate-700 px-2.5 py-1 rounded shadow-sm hover:bg-white/50 transition-colors uppercase tracking-wider">Try in Sandbox &rarr;</button>\n            </div>'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Added Sandbox buttons to Practice Problems.')
