import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Waxaan beddelaynaa CSS-ka dots-ka si uu u noqdo mid aad u qurux badan
old_css = """
        .dots-animation { width: 150px; height: 150px; position: relative; }
        .dot { position: absolute; background: white; border-radius: 50%; animation: float 3s infinite ease-in-out alternate; }
        @keyframes float { 0% { transform: translateY(0px) scale(1); opacity: 0.5; } 100% { transform: translateY(-10px) scale(1.2); opacity: 1; } }
"""
new_css = """
        .dots-animation { width: 200px; height: 200px; position: relative; display: flex; justify-content: center; align-items: center; }
        .dot { position: absolute; background: white; border-radius: 50%; opacity: 0; animation: popIn 0.5s ease forwards, float 4s infinite ease-in-out alternate; }
        @keyframes popIn { 0% { transform: scale(0); opacity: 0; } 100% { transform: scale(1); opacity: 1; } }
        @keyframes float { 0% { transform: translateY(0px) scale(1); box-shadow: 0 0 5px rgba(255,255,255,0.2); } 100% { transform: translateY(-15px) scale(1.5); box-shadow: 0 0 15px rgba(255,255,255,0.8); } }
"""
if old_css in c:
    c = c.replace(old_css, new_css)
else:
    # Haddii CSS-kii hore yara duwanaa, waxaan isticmaalaynaa regex
    c = re.sub(r'\.dots-animation \{.*?@keyframes float \{.*?\}', new_css, c, flags=re.DOTALL)

# 2. Waxaan beddelaynaa JavaScript-ka abuuraya dots-ka si ay u noqdaan kuwo badan oo quruxsan
old_js = """
        // Animation Dots
        const dotsContainer = document.getElementById('dots');
        if (dotsContainer) {
            for (let i = 0; i < 40; i++) {
                let dot = document.createElement('div');
                dot.classList.add('dot');
                dot.style.width = Math.random() * 4 + 2 + 'px';
                dot.style.height = dot.style.width;
                dot.style.left = Math.random() * 100 + '%';
                dot.style.top = Math.random() * 100 + '%';
                dot.style.animationDelay = Math.random() * 2 + 's';
                dotsContainer.appendChild(dot);
            }
        }
"""
new_js = """
        // Animation Dots (Qurux badan)
        const dotsContainer = document.getElementById('dots');
        if (dotsContainer) {
            const colors = ['#ffffff', '#a0a0a0', '#505050']; // Midabyo kala duwan
            for (let i = 0; i < 50; i++) {
                let dot = document.createElement('div');
                dot.classList.add('dot');
                
                // Size kala duwan
                let size = Math.random() * 5 + 2;
                dot.style.width = size + 'px';
                dot.style.height = size + 'px';
                
                // Meelaha ay ka soo baxaan (Wareeg)
                let angle = Math.random() * Math.PI * 2;
                let radius = Math.random() * 80; // 80px gudaha
                let x = Math.cos(angle) * radius + 100; // 100 waa badhka container-ka
                let y = Math.sin(angle) * radius + 100;
                
                dot.style.left = x + 'px';
                dot.style.top = y + 'px';
                dot.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
                
                // Delay kala duwan si ay u soo baxaan si tartiib ah
                dot.style.animationDelay = (Math.random() * 2) + 's, ' + (Math.random() * 4) + 's';
                
                dotsContainer.appendChild(dot);
            }
        }
"""
c = c.replace(old_js, new_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Animations-kii quruxda badnaa waa la soo celiyay!")
