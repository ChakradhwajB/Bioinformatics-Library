import os

pages = ['io.html', 'genetics.html', 'kmers.html', 'find_motif.html', 'dot_plot.html', 'distances.html', 'needleman_wunsch.html', 'smith_waterman.html', 'trie.html', 'suffix_array.html']

for page in pages:
    path = os.path.join('frontend', 'pages', page)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<div id="sandbox-container"></div>' not in content:
        content = content.replace('</main>', '  <div id="sandbox-container"></div>\n      <div id="quiz-container"></div>\n    </main>')
    
    if 'src="../src/sandbox.js"' not in content:
        content = content.replace('</body>', '  <script src="../src/quiz.js"></script>\n  <script src="../src/sandbox.js"></script>\n</body>')
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated all 10 module pages successfully.')
