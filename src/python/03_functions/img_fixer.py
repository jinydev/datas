import os
import shutil

# Base directories
WORK_DIR = "d:/site/jinydev/datas/src/python/03_functions"
ARTIFACT_DIR = "C:/Users/infoh/.gemini/antigravity/brain/264599f8-603f-4b27-bbdc-d3508062c123"

# List of folders to ensure exist
FOLDERS = [
    f"{WORK_DIR}/img",
    f"{WORK_DIR}/01_function_origin/img",
    f"{WORK_DIR}/02_function_concepts/img",
    f"{WORK_DIR}/03_function_usage/img",
    f"{WORK_DIR}/04_advanced_parameters/img",
    f"{WORK_DIR}/05_variable_scope/img",
    f"{WORK_DIR}/06_lambda_and_recursion/img",
    f"{WORK_DIR}/07_built_in_functions/img",
    f"{WORK_DIR}/08_math_module/img",
]

for folder in FOLDERS:
    os.makedirs(folder, exist_ok=True)

# File mappings (Artifact PNG -> Destination)
PNG_MAPPINGS = {
    # Re-use blackbox for main intro
    "function_blackbox_webtoon_1773657468869.png": f"{WORK_DIR}/img/functions_intro.png",
    
    "function_origin_webtoon_1773657453759.png": f"{WORK_DIR}/01_function_origin/img/function_origin_webtoon.png",
    "function_blackbox_webtoon_1773657468869.png": f"{WORK_DIR}/02_function_concepts/img/function_blackbox_webtoon.png",
    "def_vs_function_webtoon_1773657500196.png": f"{WORK_DIR}/03_function_usage/img/def_vs_function_webtoon.png",
    "parameter_vs_argument_webtoon_1773657516332.png": f"{WORK_DIR}/03_function_usage/img/parameter_vs_argument_webtoon.png",
    
    "alonzo_church_lambda_webtoon_1773657542950.png": f"{WORK_DIR}/06_lambda_and_recursion/img/alonzo_church_lambda_webtoon.png",
    "lambda_disposable_webtoon_1773657557156.png": f"{WORK_DIR}/06_lambda_and_recursion/img/lambda_disposable_webtoon.png",
    "recursion_matryoshka_webtoon_1773657583461.png": f"{WORK_DIR}/06_lambda_and_recursion/img/recursion_matryoshka_webtoon.png",
    
    "builtin_functions_toolbox_webtoon_1773657601900.png": f"{WORK_DIR}/07_built_in_functions/img/builtin_functions_toolbox_webtoon.png",
    "module_mealkit_webtoon_1773657617226.png": f"{WORK_DIR}/08_math_module/img/module_mealkit_webtoon.png"
}

for artifact, dest in PNG_MAPPINGS.items():
    src = os.path.join(ARTIFACT_DIR, artifact)
    if os.path.exists(src):
        shutil.copy2(src, dest)
        print(f"Copied: {artifact} -> {dest}")
    else:
        print(f"[ERROR] PNG missing in Artifacts: {artifact}")

# SVG Generation data
SVGS = {
    f"{WORK_DIR}/01_function_origin/img/math_mapping_anim.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 200">
    <rect width="600" height="200" fill="#f8f9fa" rx="10"/>
    <g transform="translate(50, 60)">
        <rect width="100" height="80" rx="10" fill="#e9ecef" stroke="#ced4da" stroke-width="2"/>
        <text x="50" y="35" font-family="sans-serif" font-size="20" text-anchor="middle" fill="#495057">Input (x)</text>
        <rect x="25" y="45" width="50" height="30" rx="5" fill="#4dabf7"/>
        <text x="50" y="66" font-family="sans-serif" font-size="18" text-anchor="middle" fill="white">2</text>
    </g>
    <g transform="translate(200, 40)">
        <rect width="200" height="120" rx="15" fill="#fcc419"/>
        <text x="100" y="40" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle" fill="#fff">Logic (Function)</text>
        <rect x="25" y="60" width="150" height="40" rx="5" fill="#fff"/>
        <text x="100" y="86" font-family="monospace" font-size="22" font-weight="bold" text-anchor="middle" fill="#d9480f">y = 3*x + 1</text>
    </g>
    <g transform="translate(450, 60)">
        <rect width="100" height="80" rx="10" fill="#e9ecef" stroke="#ced4da" stroke-width="2"/>
        <text x="50" y="35" font-family="sans-serif" font-size="20" text-anchor="middle" fill="#495057">Output (y)</text>
        <rect x="25" y="45" width="50" height="30" rx="5" fill="#fa5252"/>
        <text x="50" y="66" font-family="sans-serif" font-size="18" text-anchor="middle" fill="white">7</text>
    </g>
    <path d="M 160 100 L 190 100" stroke="#868e96" stroke-width="4" marker-end="url(#arrow)"/>
    <path d="M 410 100 L 440 100" stroke="#868e96" stroke-width="4" marker-end="url(#arrow)"/>
    <defs>
        <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
            <path d="M0,0 L0,6 L9,3 z" fill="#868e96" />
        </marker>
    </defs>
</svg>''',

    f"{WORK_DIR}/02_function_concepts/img/function_domain_anim.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 300">
    <rect width="500" height="300" fill="#ffffff" rx="10" stroke="#e9ecef" stroke-width="2"/>
    <ellipse cx="150" cy="150" rx="80" ry="120" fill="#e3fafc" stroke="#15aabf" stroke-width="3"/>
    <text x="150" y="50" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle" fill="#0b7285">Domain (정의역)</text>
    <circle cx="150" cy="100" r="15" fill="#3bc9db"/>
    <text x="150" y="105" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#fff">A</text>
    <circle cx="150" cy="150" r="15" fill="#3bc9db"/>
    <text x="150" y="155" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#fff">B</text>
    <circle cx="150" cy="200" r="15" fill="#3bc9db"/>
    <text x="150" y="205" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#fff">C</text>
    
    <ellipse cx="350" cy="150" rx="80" ry="120" fill="#fff0f6" stroke="#f06595" stroke-width="3"/>
    <text x="350" y="50" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle" fill="#a61e4d">Codomain (공역)</text>
    <circle cx="350" cy="80" r="15" fill="#f06595"/>
    <text x="350" y="85" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#fff">1</text>
    <circle cx="350" cy="130" r="15" fill="#f06595"/>
    <text x="350" y="135" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#fff">2</text>
    <circle cx="350" cy="180" r="15" fill="#f06595"/>
    <text x="350" y="185" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#fff">3</text>
    <circle cx="350" cy="230" r="15" fill="#f06595"/>
    <text x="350" y="235" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#fff">4</text>
    
    <path d="M 175 100 Q 262 90 325 80" stroke="#868e96" fill="transparent" stroke-width="2" marker-end="url(#arrow_svg)"/>
    <path d="M 175 150 Q 262 140 325 130" stroke="#868e96" fill="transparent" stroke-width="2" marker-end="url(#arrow_svg)"/>
    <path d="M 175 200 Q 262 190 325 180" stroke="#868e96" fill="transparent" stroke-width="2" marker-end="url(#arrow_svg)"/>
    
    <defs>
        <marker id="arrow_svg" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
            <path d="M0,0 L0,6 L9,3 z" fill="#868e96" />
        </marker>
    </defs>
</svg>''',

    f"{WORK_DIR}/03_function_usage/img/flow_portal_anim.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300">
    <rect width="600" height="300" fill="#f8f9fa" rx="10"/>
    <rect x="50" y="30" width="200" height="240" rx="10" fill="#fff" stroke="#4dabf7" stroke-width="3"/>
    <text x="150" y="60" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle" fill="#364fc7">Main Program</text>
    <line x1="150" y1="80" x2="150" y2="120" stroke="#adb5bd" stroke-width="4"/>
    <circle cx="150" cy="130" r="15" fill="#74c0fc"/>
    <text x="150" y="135" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle" fill="#000">Call</text>
    <line x1="150" y1="145" x2="150" y2="240" stroke="#adb5bd" stroke-width="4" stroke-dasharray="5,5"/>
    
    <rect x="350" y="70" width="200" height="160" rx="10" fill="#fff" stroke="#ff922b" stroke-width="3"/>
    <text x="450" y="100" font-family="sans-serif" font-size="18" font-weight="bold" text-anchor="middle" fill="#d9480f">def calc_tax(x)</text>
    <rect x="400" y="120" width="100" height="50" rx="8" fill="#ffe8cc"/>
    <text x="450" y="140" font-family="monospace" font-size="12" text-anchor="middle" fill="#000">tax = x * 0.1</text>
    <text x="450" y="160" font-family="monospace" font-size="12" text-anchor="middle" fill="#000">return tax</text>

    <!-- Jump Path -->
    <path d="M 170 130 C 250 130 300 120 340 120" stroke="#9c36b5" fill="transparent" stroke-width="4" stroke-dasharray="8,4" marker-end="url(#jump)"/>
    <text x="260" y="115" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="#9c36b5">1. Jump (Pause)</text>
    
    <!-- Return Path -->
    <path d="M 390 145 C 320 145 280 180 165 180" stroke="#2b8a3e" fill="transparent" stroke-width="4" marker-end="url(#jump)"/>
    <text x="260" y="195" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="#2b8a3e">2. Return Value</text>

    <defs>
        <marker id="jump" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
            <path d="M0,0 L0,6 L9,3 z" fill="context-stroke" />
        </marker>
    </defs>
</svg>''',

    f"{WORK_DIR}/06_lambda_and_recursion/img/lambda_flow_anim.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 250">
    <rect width="600" height="250" fill="#fff" rx="10" stroke="#e9ecef" stroke-width="2"/>
    
    <!-- def function -->
    <text x="50" y="50" font-family="monospace" font-size="20" font-weight="bold" fill="#3b5bdb">def add(x, y):</text>
    <rect x="50" y="70" width="150" height="120" rx="10" fill="#e5dbff" stroke="#845ef7" stroke-width="4"/>
    <text x="125" y="100" font-family="sans-serif" font-size="16" text-anchor="middle" fill="#5f3dc4">Permanent</text>
    <text x="125" y="125" font-family="sans-serif" font-size="16" text-anchor="middle" fill="#5f3dc4">Memory Room</text>
    <circle cx="125" cy="160" r="15" fill="#be4bdb"/>
    
    <!-- lambda function -->
    <text x="350" y="50" font-family="monospace" font-size="20" font-weight="bold" fill="#2b8a3e">lambda x, y: x+y</text>
    <rect x="350" y="70" width="150" height="60" rx="5" fill="#e8fdf5" stroke="#20c997" stroke-width="3" stroke-dasharray="6,4"/>
    <text x="425" y="95" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#0ca678">Calculates &amp; Returns</text>
    <text x="425" y="115" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="#e03131">POOF! (Destroyed)</text>
    
    <!-- smoke particle representation -->
    <circle cx="400" cy="150" r="5" fill="#ced4da"/>
    <circle cx="430" cy="160" r="7" fill="#ced4da"/>
    <circle cx="450" cy="140" r="4" fill="#ced4da"/>
    <circle cx="415" cy="170" r="8" fill="#dee2e6"/>
</svg>''',

    f"{WORK_DIR}/06_lambda_and_recursion/img/recursion_stack_anim.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 350">
    <rect width="400" height="350" fill="#f8f9fa"/>
    <text x="200" y="30" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle" fill="#343a40">Call Stack for fact(3)</text>
    
    <!-- Stack Blocks -->
    <rect x="100" y="250" width="200" height="40" rx="5" fill="#ffc9c9" stroke="#fa5252" stroke-width="2"/>
    <text x="200" y="275" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#c92a2a">fact(3) : wait</text>
    
    <rect x="100" y="200" width="200" height="40" rx="5" fill="#ffec99" stroke="#fcc419" stroke-width="2"/>
    <text x="200" y="225" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#b1970b">fact(2) : wait</text>

    <rect x="100" y="150" width="200" height="40" rx="5" fill="#b2f2bb" stroke="#51cf66" stroke-width="2"/>
    <text x="200" y="175" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#2b8a3e">fact(1) : wait</text>

    <rect x="100" y="100" width="200" height="40" rx="5" fill="#a5d8ff" stroke="#339af0" stroke-width="2"/>
    <text x="200" y="125" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#1864ab">fact(0) -> BASE CASE!</text>

    <!-- Arrow Path Push -->
    <path d="M 60 270 L 60 120 L 90 120" stroke="#868e96" fill="transparent" stroke-width="4" marker-end="url(#arrow_svg)"/>
    <text x="40" y="200" font-family="sans-serif" font-size="14" font-weight="bold" fill="#868e96" transform="rotate(-90 40,200)">Push (Call)</text>
    
    <!-- Arrow Path Pop -->
    <path d="M 310 120 L 340 120 L 340 270" stroke="#f06595" fill="transparent" stroke-width="4" marker-end="url(#arrow_svg_p)"/>
    <text x="360" y="200" font-family="sans-serif" font-size="14" font-weight="bold" fill="#f06595" transform="rotate(90 360,200)">Pop (Return)</text>

    <defs>
        <marker id="arrow_svg_p" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
            <path d="M0,0 L0,6 L9,3 z" fill="#f06595" />
        </marker>
    </defs>
</svg>''',

    f"{WORK_DIR}/07_built_in_functions/img/casting_anim.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 200">
    <rect width="600" height="200" fill="#f1f3f5" rx="10"/>
    
    <g transform="translate(50, 70)">
        <rect width="120" height="60" rx="5" fill="#fcc419"/>
        <text x="60" y="25" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#fff">String</text>
        <text x="60" y="45" font-family="monospace" font-size="22" font-weight="bold" text-anchor="middle" fill="#fff">"2026"</text>
    </g>
    
    <g transform="translate(240, 50)">
        <rect x="0" y="0" width="120" height="100" rx="20" fill="#cc5de8" stroke="#862e9c" stroke-width="4"/>
        <text x="60" y="40" font-family="monospace" font-size="24" font-weight="bold" text-anchor="middle" fill="#fff">int()</text>
        <text x="60" y="70" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="#ffe3e3">FURNACE</text>
    </g>
    
    <g transform="translate(430, 70)">
        <rect width="120" height="60" rx="5" fill="#4dabf7"/>
        <text x="60" y="25" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#fff">Integer</text>
        <text x="60" y="45" font-family="monospace" font-size="22" font-weight="bold" text-anchor="middle" fill="#fff">2026</text>
    </g>
    
    <!-- Arrows -->
    <path d="M 180 100 L 230 100" stroke="#868e96" stroke-width="4" marker-end="url(#arrow)"/>
    <path d="M 370 100 L 420 100" stroke="#868e96" stroke-width="4" marker-end="url(#arrow)"/>
</svg>''',

    f"{WORK_DIR}/08_math_module/img/math_rounding_anim.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 200">
    <rect width="600" height="200" fill="#fff" rx="10" stroke="#dee2e6" stroke-width="2"/>
    
    <!-- ceil -->
    <g transform="translate(50, 50)">
        <rect width="140" height="100" rx="10" fill="#e3fafc" stroke="#1098ad" stroke-width="2"/>
        <text x="70" y="30" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#0b7285">math.ceil(3.1)</text>
        <text x="70" y="60" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#495057">Original: 3.1</text>
        <text x="70" y="85" font-family="monospace" font-size="22" font-weight="bold" text-anchor="middle" fill="#e03131">Result: 4</text>
        <path d="M 120 75 L 120 50 L 130 50" stroke="#e03131" fill="transparent" stroke-width="3" marker-end="url(#arrow)"/>
    </g>
    
    <!-- floor -->
    <g transform="translate(230, 50)">
        <rect width="140" height="100" rx="10" fill="#fff0f6" stroke="#d6336c" stroke-width="2"/>
        <text x="70" y="30" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#a61e4d">math.floor(3.9)</text>
        <text x="70" y="60" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#495057">Original: 3.9</text>
        <text x="70" y="85" font-family="monospace" font-size="22" font-weight="bold" text-anchor="middle" fill="#3b5bdb">Result: 3</text>
        <path d="M 120 60 L 120 85 L 130 85" stroke="#3b5bdb" fill="transparent" stroke-width="3" marker-end="url(#arrow)"/>
    </g>
    
    <!-- trunc -->
    <g transform="translate(410, 50)">
        <rect width="140" height="100" rx="10" fill="#f4fce3" stroke="#74b816" stroke-width="2"/>
        <text x="70" y="30" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#5c940d">math.trunc(-3.7)</text>
        <text x="70" y="60" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#495057">Original: -3.7</text>
        <text x="70" y="85" font-family="monospace" font-size="22" font-weight="bold" text-anchor="middle" fill="#2b8a3e">Result: -3</text>
        <!-- sword slash symbol -->
        <path d="M 90 55 L 110 35" stroke="#f03e3e" stroke-width="4"/>
    </g>
</svg>''',

    f"{WORK_DIR}/08_math_module/img/trig_waves_anim.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 200">
    <rect width="600" height="200" fill="#212529" rx="10"/>
    <line x1="50" y1="100" x2="550" y2="100" stroke="#495057" stroke-width="2" stroke-dasharray="5,5"/>
    <line x1="50" y1="20" x2="50" y2="180" stroke="#495057" stroke-width="2"/>
    
    <!-- sin wave -->
    <path d="M 50 100 Q 150 -50 250 100 T 450 100 T 650 100" stroke="#339af0" fill="transparent" stroke-width="4"/>
    <text x="100" y="30" fill="#339af0" font-family="sans-serif" font-weight="bold">y = sin(x)</text>
    
    <!-- cos wave (shifted) -->
    <path d="M 50 10 Q 150 250 250 100 Q 350 -50 450 100 T 650 100" stroke="#ff922b" fill="transparent" stroke-width="3" stroke-dasharray="10,5"/>
    <text x="250" y="30" fill="#ff922b" font-family="sans-serif" font-weight="bold">y = cos(x)</text>
</svg>'''
}

for dest, content in SVGS.items():
    with open(dest, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated SVG: {dest}")

print("All perfectly organized!")
