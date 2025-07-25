<!--
README.md for Pruthviraj Chavan || 3D, Hacker Theme, Animated, Agentic AI Focus
Paste this entire file into your GitHub README.md and enable the use of HTML/CSS for full effect.
-->

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Pruthviraj Chavan - Agentic AI Developer</title>
<style>
  body {
    background: #0A0A0A;
    color: #39ff14;
    font-family: 'Fira Mono', 'Courier New', Courier, monospace;
    margin: 0;
    padding: 2rem;
    min-height: 100vh;
    /* 3D lighting effect */
    box-shadow: 0 0 120px 8px #00ffd5 inset, 0 5px 40px #ff00c8, 0 0 10px #222;
  }
  h1, h2, h3, h4 {
    border-bottom: 2px solid #39ff14;
    padding-bottom: 0.3rem;
    margin-bottom: 1.2rem;
    letter-spacing: 1.5px;
  }
  h1.glitch {
    font-size: 3.1rem;
    font-weight: bold;
    text-shadow:
      2px 0px 3px #ff00c8,
      -2px 1px 3px #00ffd5,
      0 0 7px #39ff14;
    position: relative;
    animation: glitch 1.5s infinite;
  }
  @keyframes glitch {
    0%, 100% { transform: none; }
    20% { transform: translate(-2px, 2px) skew(-2deg); }
    40% { transform: translate(2px, -1px) skew(1deg); }
    60% { transform: translate(-1px, 1px) skew(0deg); }
    80% { transform: translate(2px, 0px) skew(-1deg); }
  }
  .animated-gradient {
    background: linear-gradient(
      120deg, #0fffc6, #ff00c8, #FFD600, #39ff14, #00ffd5, #ff00c8, #0fffc6
    );
    background-size: 600% 600%;
    animation: gradientAnimate 9s ease-in-out infinite;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  @keyframes gradientAnimate {
    0% { background-position:0% 50%; }
    40% { background-position:100% 50%; }
    100% { background-position:0% 50%; }
  }
  /* 3D floating UI container */
  .container {
    max-width: 1050px;
    margin: 4vw auto 0 auto;
    background: rgba(18,22,33,0.97);
    border-radius: 24px;
    box-shadow: 0 18px 48px #00ffd544, 0 2px 12px #ff00c877;
    padding: 2.5rem 3.5rem 2rem 3.5rem;
    border: 2.5px solid #00ffd5;
    transition: box-shadow 0.2s;
  }
  .container:hover {
    box-shadow: 0 28px 64px #ff00c888, 0 2px 24px #39ff1466;
  }
  .typing {
    font-size: 1.3rem;
    color: #FFD600;
    border-right: 3px solid #FFD600;
    overflow: hidden;
    white-space: nowrap;
    width: 0;
    animation: typing 4s steps(55) forwards, blink .93s step-end infinite;
    margin-bottom: 1.1rem;
    margin-top: 2.5rem;
    font-weight: 600;
    letter-spacing: 1.2px;
    text-shadow: 0 0 8px #FFD60088;
  }
  @keyframes typing {
    from { width: 0;}
    to { width: 32ch;}
  }
  @keyframes blink {
    from, to { border-color: transparent;}
    50% { border-color: #FFD600;}
  }
  /* Tech Stack: 3D badges */
  .tech-badge {
    display: inline-block;
    background: linear-gradient(145deg, #111 73%, #212121 100%);
    border: 1.7px solid #39ff14;
    border-radius: 18px;
    padding: 0.4rem 1.1rem;
    margin: 0.3rem 0.2rem 0.6rem 0;
    color: #00ffd5;
    font-size: 1rem;
    font-weight: bold;
    text-shadow: 0 2px 5px #222, 0 0 8px #FFD60033;
    user-select: none;
    text-transform: uppercase;
    transition: transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 3px 11px #0fffc644, 0 0 1px #FFD600;
  }
  .tech-badge:hover {
    background: #0d1117;
    color: #FFD600;
    transform: scale(1.11) rotate(-2deg);
    box-shadow: 0 5px 28px #ff00c888;
    border-color: #FFD600;
  }
  /* Social Icons */
  .social-links a {
    display: inline-block;
    margin-right: 1.1rem;
    margin-bottom: 0.6rem;
    font-size: 1.15rem;
    padding: 0.55rem 1rem;
    border-radius: 20px;
    background: linear-gradient(105deg, #00ffd5 35%, #ff00c8 60%, #39ff14 100%);
    color: #181818;
    text-decoration: none;
    font-weight: 700;
    letter-spacing: 0.4px;
    box-shadow: 0 2px 11px #00ffd555;
    transition: background 0.33s, color 0.2s, transform 0.2s;
    border: none;
  }
  .social-links a:hover {
    background: linear-gradient(105deg, #FFD600 45%, #ff00c8 70%, #00ffd5 100%);
    color: #0A0A0A;
    transform: scale(1.13) rotate(-2deg);
  }
  /* Project List Hack Glow */
  ul.projects li {
    margin-bottom: 1rem;
    padding: 0.7rem 1.1rem;
    background: rgba(44,255,96,0.045);
    border-left: 3px solid #00ffd5;
    border-radius: 10px;
    box-shadow: 0 0 8px #00ffd533;
    font-size: 1.06rem;
    color: #ff00c8;
    font-family: 'Fira Mono', monospace;
  }
  ul.projects li strong {
    color: #FFD600;
    letter-spacing: 0.5px;
  }
  footer {
    color: #555;
    margin: 6rem 0 1.1rem 0;
    font-size: 0.98rem;
    letter-spacing: 0.2px;
    text-align: center;
  }
  @media (max-width: 700px) {
    .container { padding: 0.9rem 0.8rem;}
    h1, h2, h3, h4 { font-size: 1.2em;}
    .tech-badge { font-size:0.95em; }
  }
</style>
</head>
<body>
  <div class="container">
    <h1 class="glitch">Pruthviraj Chavan<br><span class="animated-gradient">Agentic AI & Automation Developer</span></h1>
    <div class="typing">🚀 Transforming data & automation with real-world AI agents!</div>
    <section>
      <h2 class="animated-gradient">About Me</h2>
      <ul style="line-height:1.9; font-size:1.1rem;">
        <li>💼 <b>Role:</b> Software Developer (AI, Automation, Backend)</li>
        <li>💡 <b>Agentic AI:</b> Specialized in building autonomous workflow agents and AI automations</li>
        <li>⚡ <b>Expertise:</b> Python, Machine Learning, Deep Learning, Data Analysis, Big Data (Hadoop & Spark)</li>
        <li>🌐 <b>Web:</b> HTML, CSS, JavaScript (UI/UX)</li>
        <li>🖥️ <b>Programming:</b> Core Java, C++, Python</li>
        <li>☁️ <b>Cloud:</b> AWS, Firebase, Heroku, GitHub Pages</li>
        <li>🧰 <b>Databases:</b> MySQL, MongoDB</li>
      </ul>
    </section>
    <section>
      <h2 class="animated-gradient">Tech Stack</h2>
      <div>
        <span class="tech-badge">C++</span>
        <span class="tech-badge">C</span>
        <span class="tech-badge">Python</span>
        <span class="tech-badge">JavaScript</span>
        <span class="tech-badge">HTML5</span>
        <span class="tech-badge">CSS3</span>
        <span class="tech-badge">TensorFlow</span>
        <span class="tech-badge">PyTorch</span>
        <span class="tech-badge">Keras</span>
        <span class="tech-badge">scikit-learn</span>
        <span class="tech-badge">Pandas</span>
        <span class="tech-badge">NumPy</span>
        <span class="tech-badge">Matplotlib</span>
        <span class="tech-badge">MLflow</span>
        <span class="tech-badge">AWS</span>
        <span class="tech-badge">MySQL</span>
        <span class="tech-badge">MongoDB</span>
        <span class="tech-badge">Django</span>
        <span class="tech-badge">Firebase</span>
        <span class="tech-badge">Heroku</span>
        <span class="tech-badge">Power BI</span>
        <span class="tech-badge">Hadoop</span>
        <span class="tech-badge">Spark</span>
      </div>
    </section>
    <section>
      <h2 class="animated-gradient">Find Me Online</h2>
      <div class="social-links">
        <a href="https://instagram.com/pruthvya_07/" target="_blank">Instagram</a>
        <a href="https://www.linkedin.com/in/pruthvirajchavan-/" target="_blank">LinkedIn</a>
      </div>
    </section>
    <section>
      <h2 class="animated-gradient">🚦 Projects & Agentic AI</h2>
      <ul class="projects">
        <li><strong>Lead Generation Automation Agent:</strong> End-to-end workflow integrating web scraping, data qualification, and personalized email sends using Python, n8n, and AWS. <span style="color:#39ff14">(35% more qualified leads, 80% reduction in manual work)</span></li>
        <li><strong>Sales Intelligence Dashboard:</strong> Interactive Power BI dashboard for advanced sales analytics and churn prediction, automating regional and product segmentation.</li>
        <li><strong>Voice Bot for Political Outreach:</strong> AI voice chatbot (5,000+ daily calls), built with NLP, Django, and agentic bot architectures for scalable real-time voter engagement.</li>
        <li><strong>ML Model Development:</strong> Trained deep and classical learning models with TensorFlow, scikit-learn, PyTorch for business analytics, clustering, segmentation.</li>
        <li><strong>Agentic AI at Axzora Inc:</strong> Orchestrated autonomous AI solutions using n8n, Make.com, AWS, integrating bots and analytics into scalable business intelligence stacks.</li>
      </ul>
    </section>
  </div>
  <footer>🕶️ Hacker-vision theme · Made with <span style="color:#ff00c8">AI &lt;3</span> by Pruthviraj Chavan</footer>
</body>
</html>
