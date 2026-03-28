from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, QuizResult, RoadmapProgress
from roadmap_data import ROADMAPS
import random
import json
import os

app = Flask(__name__)
app.secret_key = "stem_explorer_tsa_2026_secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///stempathdb.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "Please sign in to continue."

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

with app.app_context():
    db.create_all()

# ─────────────────────────────────────────────
#  CAREER DATA
# ─────────────────────────────────────────────
CAREERS = {
    "software_engineer": {
        "id": "software_engineer",
        "title": "Software Engineer",
        "color": "#00d4ff",
        "gradient": "linear-gradient(135deg, #00d4ff, #0066ff)",
        "salary": "$110,000 – $125,000",
        "growth": "25%",
        "growth_label": "Much faster than average",
        "description": (
            "Software engineers design, develop, and maintain the applications and systems "
            "that power modern life — from mobile apps to cloud infrastructure. They translate "
            "complex problems into elegant code and collaborate on teams to ship products used "
            "by millions of people. This field rewards creativity, logical thinking, and a "
            "passion for continuous learning as technology rapidly evolves."
        ),
        "hs_courses": [
            "AP Computer Science A / Principles",
            "AP Calculus AB/BC",
            "AP Statistics",
            "AP Physics 1 & 2",
            "Pre-Calculus / Algebra II",
            "Introduction to Programming (Python/Java)",
        ],
        "extracurriculars": [
            "FIRST Robotics Competition (FRC)",
            "Hackathons (MLH, local collegiate events)",
            "Coding clubs / competitive programming",
            "Build personal projects and publish on GitHub",
            "App development for school/community",
            "TSA Software Development event",
        ],
        "skills": [
            "Python, Java, JavaScript", "Data Structures & Algorithms",
            "Version control (Git)", "Problem decomposition",
            "Agile / Scrum teamwork", "Debugging & testing",
            "Cloud basics (AWS / GCP)", "API design",
        ],
        "education_links": [
            {"label": "MIT OpenCourseWare - Intro to CS (free)", "url": "https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/"},
            {"label": "freeCodeCamp - Full Stack Certification (free)", "url": "https://www.freecodecamp.org/learn"},
            {"label": "Coursera - Google IT Support Certificate", "url": "https://www.coursera.org/professional-certificates/google-it-support"},
            {"label": "CS50 Harvard (free audit)", "url": "https://cs50.harvard.edu/x/"},
        ],
        "entry_jobs": [
            "Junior Software Developer",
            "Front-End / Back-End Developer",
            "QA / Test Engineer",
            "DevOps Engineer (entry)",
            "Software Development Intern",
        ],
        "pathway": [
            {"stage": "9th-10th Grade", "desc": "Take Algebra II, intro programming courses; join robotics or coding club."},
            {"stage": "11th-12th Grade", "desc": "AP CS A, AP Calc; build 2-3 personal projects; compete in hackathons."},
            {"stage": "College (4 yr)", "desc": "B.S. in Computer Science or Software Engineering; complete internships."},
            {"stage": "Internship", "desc": "Summer SWE internship at a tech company; contribute to open-source."},
            {"stage": "Entry-Level Job", "desc": "Junior Developer role; grow skills, earn promotions within 2-3 years."},
        ],
        "notable_companies": [
            {"name": "Google", "note": "Search, Android, Cloud"},
            {"name": "Meta", "note": "Social platforms, AR/VR"},
            {"name": "Apple", "note": "iOS, macOS, hardware software"},
            {"name": "Microsoft", "note": "Azure, Office, Xbox"},
            {"name": "Amazon", "note": "AWS, e-commerce, Alexa"},
            {"name": "Stripe", "note": "Payments infrastructure"},
            {"name": "Netflix", "note": "Streaming, distributed systems"},
            {"name": "Spotify", "note": "Music tech, data-driven UX"},
            {"name": "Salesforce", "note": "CRM, enterprise SaaS"},
            {"name": "Adobe", "note": "Creative & document software"},
        ],
    },

    "data_scientist": {
        "id": "data_scientist",
        "title": "Data Scientist",
        "color": "#8b5cf6",
        "gradient": "linear-gradient(135deg, #8b5cf6, #ec4899)",
        "salary": "$92,000 – $108,000",
        "growth": "36%",
        "growth_label": "Explosive growth",
        "description": (
            "Data scientists extract meaningful insights from massive datasets using statistics, "
            "machine learning, and programming. They help organizations make smarter decisions by "
            "identifying patterns and building predictive models. In an era of big data, data "
            "scientists are among the most sought-after professionals across every industry."
        ),
        "hs_courses": [
            "AP Statistics",
            "AP Calculus AB/BC",
            "AP Computer Science A / Principles",
            "AP Research / Science Research",
            "Linear Algebra (if offered)",
            "Introduction to Data Science",
        ],
        "extracurriculars": [
            "Kaggle competitions (beginner to advanced)",
            "Science fair / research projects",
            "Math olympiad / AMC competitions",
            "Data analysis projects (sports stats, climate data)",
            "Statistics/Math team",
            "TSA Data Science & Analytics event",
        ],
        "skills": [
            "Python (pandas, NumPy, scikit-learn)", "R programming",
            "SQL & databases", "Machine learning fundamentals",
            "Data visualization (matplotlib, Tableau)", "Statistical modeling",
            "Storytelling with data", "Jupyter Notebooks",
        ],
        "education_links": [
            {"label": "Coursera - IBM Data Science Professional Certificate", "url": "https://www.coursera.org/professional-certificates/ibm-data-science"},
            {"label": "Kaggle Learn - Free ML & Data courses", "url": "https://www.kaggle.com/learn"},
            {"label": "edX - Harvard Data Science Certificate", "url": "https://www.edx.org/professional-certificate/harvardx-data-science"},
            {"label": "DataCamp - Data Scientist Track", "url": "https://www.datacamp.com/tracks/data-scientist-with-python"},
        ],
        "entry_jobs": [
            "Data Analyst",
            "Business Intelligence Analyst",
            "Machine Learning Engineer (entry)",
            "Research Data Analyst",
            "Data Science Intern",
        ],
        "pathway": [
            {"stage": "9th-10th Grade", "desc": "Excel in statistics and math; start learning Python or R online."},
            {"stage": "11th-12th Grade", "desc": "AP Stats + AP CS; enter science fair with data-driven project; try Kaggle."},
            {"stage": "College (4 yr)", "desc": "B.S. in Statistics, Mathematics, or CS with data science concentration."},
            {"stage": "Internship", "desc": "Data analyst internship; build portfolio of end-to-end ML projects on GitHub."},
            {"stage": "Entry-Level Job", "desc": "Data Analyst or Junior Data Scientist role; pursue advanced certifications."},
        ],
        "notable_companies": [
            {"name": "Google DeepMind", "note": "AI & applied ML research"},
            {"name": "Meta AI", "note": "Large-scale social data, LLMs"},
            {"name": "Netflix", "note": "Recommendation systems"},
            {"name": "Airbnb", "note": "Pricing & demand modeling"},
            {"name": "Spotify", "note": "Music & podcast personalization"},
            {"name": "LinkedIn", "note": "Professional network analytics"},
            {"name": "Palantir", "note": "Government & enterprise analytics"},
            {"name": "Two Sigma", "note": "Quantitative data-driven investing"},
            {"name": "McKinsey Analytics", "note": "Consulting with data science"},
            {"name": "IBM Research", "note": "Enterprise AI & Watson"},
        ],
    },

    "biomedical_engineer": {
        "id": "biomedical_engineer",
        "title": "Biomedical Engineer",
        "color": "#10b981",
        "gradient": "linear-gradient(135deg, #10b981, #06b6d4)",
        "salary": "$68,000 – $82,000",
        "growth": "10%",
        "growth_label": "Faster than average",
        "description": (
            "Biomedical engineers sit at the intersection of engineering and medicine, designing "
            "devices and systems that save lives — from MRI machines to artificial limbs to drug "
            "delivery systems. They collaborate with doctors, biologists, and manufacturers to "
            "translate scientific discoveries into real medical solutions."
        ),
        "hs_courses": [
            "AP Biology",
            "AP Chemistry",
            "AP Physics C: Mechanics",
            "AP Calculus BC",
            "Anatomy & Physiology",
            "Introduction to Engineering / PLTW",
        ],
        "extracurriculars": [
            "Science Olympiad (anatomy, chemistry events)",
            "Hospital / healthcare volunteering",
            "Research internship at university lab",
            "HOSA - Future Health Professionals",
            "3D printing / prototyping club",
            "TSA Medical Technology event",
        ],
        "skills": [
            "Biology & physiology fundamentals", "Engineering design process",
            "CAD / SolidWorks", "Lab techniques & safety",
            "Regulatory knowledge (FDA)", "Teamwork & communication",
            "MATLAB / simulation", "Critical thinking",
        ],
        "education_links": [
            {"label": "Johns Hopkins - Biomedical Engineering Dept.", "url": "https://www.bme.jhu.edu/"},
            {"label": "Coursera - Bioinformatics Specialization (UCSD)", "url": "https://www.coursera.org/specializations/bioinformatics"},
            {"label": "edX - Biomedical Engineering MicroMasters (MIT)", "url": "https://www.edx.org/masters/micromasters/mitx-biomechanics"},
            {"label": "Purdue BME - Undergrad Program", "url": "https://engineering.purdue.edu/BME"},
        ],
        "entry_jobs": [
            "Biomedical Equipment Technician",
            "R&D Engineer (medical devices)",
            "Clinical Engineer",
            "Regulatory Affairs Specialist",
            "Biomechanics Research Assistant",
        ],
        "pathway": [
            {"stage": "9th-10th Grade", "desc": "Strong foundation in biology and chemistry; join Science Olympiad."},
            {"stage": "11th-12th Grade", "desc": "AP Bio + AP Chem + AP Calc; volunteer at hospital; research internship."},
            {"stage": "College (4 yr)", "desc": "B.S. Biomedical Engineering; complete lab rotations and senior design project."},
            {"stage": "Internship", "desc": "Medical device company internship; present research at undergraduate symposium."},
            {"stage": "Entry-Level Job", "desc": "R&D or clinical engineering role; many pursue graduate school (M.S./Ph.D.)."},
        ],
        "notable_companies": [
            {"name": "Medtronic", "note": "Pacemakers, insulin pumps, neurostimulators"},
            {"name": "Johnson & Johnson MedTech", "note": "Surgical robots, orthopaedics"},
            {"name": "Stryker", "note": "Implants, surgical navigation"},
            {"name": "Boston Scientific", "note": "Cardiac & vascular devices"},
            {"name": "Abbott", "note": "Diagnostics, heart valves, CGMs"},
            {"name": "GE HealthCare", "note": "MRI, CT, ultrasound systems"},
            {"name": "Siemens Healthineers", "note": "Medical imaging & diagnostics"},
            {"name": "Intuitive Surgical", "note": "da Vinci robotic surgery systems"},
            {"name": "Zimmer Biomet", "note": "Joint replacement implants"},
            {"name": "Edwards Lifesciences", "note": "Heart valves, hemodynamic monitoring"},
        ],
    },

    "aerospace_engineer": {
        "id": "aerospace_engineer",
        "title": "Aerospace Engineer",
        "color": "#f59e0b",
        "gradient": "linear-gradient(135deg, #f59e0b, #ef4444)",
        "salary": "$80,000 – $94,000",
        "growth": "6%",
        "growth_label": "Average (high specialization)",
        "description": (
            "Aerospace engineers design, test, and develop aircraft, spacecraft, satellites, and "
            "missiles. They apply principles of aerodynamics, propulsion, and structural analysis "
            "to create vehicles that operate at the edge of human capability. With the rise of "
            "commercial spaceflight and drone technology, aerospace engineering is entering an "
            "exciting new era with massive opportunities for innovation."
        ),
        "hs_courses": [
            "AP Physics C: Mechanics & E&M",
            "AP Calculus BC",
            "AP Chemistry",
            "Pre-Engineering / PLTW Aerospace",
            "AP Computer Science A",
            "Trigonometry / Precalculus",
        ],
        "extracurriculars": [
            "Model rocketry (Tripoli Rocketry Association)",
            "FIRST Robotics Competition (FRC)",
            "AIAA high school programs",
            "NASA Student Launch Initiative",
            "RC aircraft / drone building clubs",
            "TSA Aerospace Technology event",
        ],
        "skills": [
            "Aerodynamics & fluid mechanics", "CAD (CATIA, SolidWorks)",
            "MATLAB & simulation", "Structural analysis",
            "Propulsion systems knowledge", "Systems engineering",
            "Technical writing", "Attention to precision",
        ],
        "education_links": [
            {"label": "MIT OpenCourseWare - Aeronautics & Astronautics", "url": "https://ocw.mit.edu/courses/aeronautics-and-astronautics/"},
            {"label": "NASA STEM Engagement - Student Programs", "url": "https://www.nasa.gov/stem/"},
            {"label": "Purdue AAE - Undergraduate Aerospace Eng.", "url": "https://engineering.purdue.edu/AAE"},
            {"label": "Coursera - Spacecraft Dynamics (Univ. of Colorado)", "url": "https://www.coursera.org/specializations/spacecraft-dynamics-control"},
        ],
        "entry_jobs": [
            "Aerospace Test Engineer",
            "Systems Integration Engineer",
            "Propulsion Engineer (entry)",
            "Avionics / Flight Software Engineer",
            "Structural Analysis Engineer",
        ],
        "pathway": [
            {"stage": "9th-10th Grade", "desc": "Physics, math focus; join model rocketry or robotics club."},
            {"stage": "11th-12th Grade", "desc": "AP Physics C + AP Calc BC; enter NASA student programs; build rockets."},
            {"stage": "College (4 yr)", "desc": "B.S. Aerospace Engineering; internships at NASA, Boeing, SpaceX, Lockheed."},
            {"stage": "Internship", "desc": "NASA co-op or defense contractor internship; obtain security clearance if needed."},
            {"stage": "Entry-Level Job", "desc": "Test or systems engineer role; many specialize further with M.S. degree."},
        ],
        "notable_companies": [
            {"name": "NASA", "note": "Space exploration & research"},
            {"name": "SpaceX", "note": "Falcon, Starship, Starlink"},
            {"name": "Boeing Defense", "note": "Commercial & military aircraft"},
            {"name": "Lockheed Martin", "note": "F-35, spacecraft, satellites"},
            {"name": "Northrop Grumman", "note": "B-21 bomber, space systems"},
            {"name": "Raytheon Technologies", "note": "Missiles, avionics, engines (RTX)"},
            {"name": "Blue Origin", "note": "New Shepard, New Glenn rockets"},
            {"name": "General Dynamics", "note": "Defense systems & IT"},
            {"name": "L3Harris Technologies", "note": "Avionics, ISR systems"},
            {"name": "Airbus", "note": "Commercial aircraft & helicopters"},
        ],
    },

    "environmental_scientist": {
        "id": "environmental_scientist",
        "title": "Environmental Scientist",
        "color": "#22c55e",
        "gradient": "linear-gradient(135deg, #22c55e, #3b82f6)",
        "salary": "$52,000 – $66,000",
        "growth": "7%",
        "growth_label": "Average (growing urgency)",
        "description": (
            "Environmental scientists study how natural systems work and how human activity affects "
            "ecosystems, air, water, and climate. They collect and analyze data from field and lab "
            "settings to inform policies that protect public health and the planet. As climate change "
            "accelerates, environmental scientists are in high demand at government agencies, "
            "non-profits, and private companies worldwide."
        ),
        "hs_courses": [
            "AP Environmental Science",
            "AP Biology",
            "AP Chemistry",
            "AP Statistics",
            "Earth Science / Geology",
            "AP Research",
        ],
        "extracurriculars": [
            "Environmental / ecology clubs",
            "Stream / watershed monitoring programs",
            "National Wildlife Federation programs",
            "Local park service volunteering",
            "Citizen science projects (eBird, iNaturalist)",
            "TSA Environmental Science event",
        ],
        "skills": [
            "Field data collection & sampling", "GIS / mapping (ArcGIS, QGIS)",
            "Laboratory analysis techniques", "Environmental regulations (EPA)",
            "Statistical data analysis (R / Excel)", "Technical & science writing",
            "Communication to public & policy makers", "Sustainability frameworks",
        ],
        "education_links": [
            {"label": "EPA - Student Environmental Education Programs", "url": "https://www.epa.gov/education"},
            {"label": "NOAA - Education Resources & Internships", "url": "https://www.noaa.gov/education"},
            {"label": "Coursera - Climate Science (Columbia University)", "url": "https://www.coursera.org/learn/climate-change-mitigation"},
            {"label": "edX - Sustainability and Green Design (MIT)", "url": "https://www.edx.org/learn/sustainability"},
        ],
        "entry_jobs": [
            "Environmental Technician",
            "Field Research Assistant",
            "Environmental Health & Safety Specialist",
            "GIS Analyst (environmental)",
            "Sustainability Coordinator",
        ],
        "pathway": [
            {"stage": "9th-10th Grade", "desc": "AP Env. Science + Biology; join environmental club; do citizen science."},
            {"stage": "11th-12th Grade", "desc": "AP Chem + AP Stats + AP Research; field research internship; science fair."},
            {"stage": "College (4 yr)", "desc": "B.S. Environmental Science / Ecology; fieldwork, lab rotations, REU programs."},
            {"stage": "Internship", "desc": "EPA, NOAA, or conservation organization internship; publish undergraduate research."},
            {"stage": "Entry-Level Job", "desc": "Environmental technician or analyst; many pursue M.S. for senior roles."},
        ],
        "notable_companies": [
            {"name": "U.S. EPA", "note": "Federal environmental regulation & research"},
            {"name": "NOAA", "note": "Oceans, atmosphere, climate monitoring"},
            {"name": "The Nature Conservancy", "note": "Global conservation projects"},
            {"name": "Environmental Defense Fund", "note": "Climate & pollution policy"},
            {"name": "AECOM", "note": "Environmental engineering & consulting"},
            {"name": "Tetra Tech", "note": "Water, environment, infrastructure"},
            {"name": "Jacobs Engineering", "note": "Environmental remediation & design"},
            {"name": "WSP Global", "note": "Sustainability & environmental consulting"},
            {"name": "CDM Smith", "note": "Water & hazardous waste engineering"},
            {"name": "Burns & McDonnell", "note": "Renewable energy & env. projects"},
        ],
    },

    "cybersecurity_analyst": {
        "id": "cybersecurity_analyst",
        "title": "Cybersecurity Analyst",
        "color": "#ec4899",
        "gradient": "linear-gradient(135deg, #ec4899, #8b5cf6)",
        "salary": "$82,000 – $96,000",
        "growth": "33%",
        "growth_label": "Much faster than average",
        "description": (
            "Cybersecurity analysts protect organizations' networks, systems, and data from "
            "hackers, malware, and breaches. They monitor threats, investigate incidents, and "
            "design security frameworks that keep critical infrastructure safe. With cyberattacks "
            "costing the global economy trillions of dollars annually, skilled cybersecurity "
            "professionals are desperately needed across every sector."
        ),
        "hs_courses": [
            "AP Computer Science A / Principles",
            "AP Statistics",
            "AP Calculus AB",
            "Networking Fundamentals (CompTIA IT Fundamentals)",
            "Introduction to Cybersecurity",
            "AP Physics 1",
        ],
        "extracurriculars": [
            "CyberPatriot National Cyber Defense Competition",
            "picoCTF & other Capture-the-Flag (CTF) competitions",
            "Coding / programming clubs",
            "Build a home lab (VMs, Kali Linux practice)",
            "SANS CyberStart program (free)",
            "TSA Cybersecurity event",
        ],
        "skills": [
            "Networking (TCP/IP, DNS, HTTP)", "Linux & Windows administration",
            "Python scripting for security", "Ethical hacking fundamentals",
            "Cryptography basics", "Incident response",
            "SIEM tools (Splunk, ELK)", "Risk assessment & compliance",
        ],
        "education_links": [
            {"label": "CompTIA Security+ Certification Prep", "url": "https://www.comptia.org/certifications/security"},
            {"label": "SANS CyberStart - Free student program", "url": "https://www.cyberstart.com/"},
            {"label": "Cybrary - Free Cybersecurity Courses", "url": "https://www.cybrary.it/"},
            {"label": "TryHackMe - Hands-on Security Learning", "url": "https://tryhackme.com/"},
        ],
        "entry_jobs": [
            "SOC (Security Operations Center) Analyst",
            "IT Security Specialist",
            "Penetration Tester (Junior)",
            "Network Security Engineer",
            "Incident Response Analyst",
        ],
        "pathway": [
            {"stage": "9th-10th Grade", "desc": "AP CS + networking basics; join CyberPatriot team; try CyberStart."},
            {"stage": "11th-12th Grade", "desc": "CTF competitions; build home lab; earn CompTIA IT Fundamentals cert."},
            {"stage": "College / Cert", "desc": "B.S. Cybersecurity or CS; OR fast-track with CompTIA A+, Net+, Security+."},
            {"stage": "Internship", "desc": "SOC internship; contribute to bug bounty programs (HackerOne, Bugcrowd)."},
            {"stage": "Entry-Level Job", "desc": "SOC Analyst or IT Security Specialist; pursue CEH or OSCP certification."},
        ],
        "notable_companies": [
            {"name": "CrowdStrike", "note": "Endpoint detection & threat intelligence"},
            {"name": "Palo Alto Networks", "note": "Firewalls, SASE, SOC automation"},
            {"name": "Mandiant (Google)", "note": "Incident response & threat hunting"},
            {"name": "Cisco Talos", "note": "Threat research & network security"},
            {"name": "Microsoft Security", "note": "Azure Defender, Sentinel, Identity"},
            {"name": "Booz Allen Hamilton", "note": "Government & defense cyber ops"},
            {"name": "MITRE Corporation", "note": "ATT&CK framework, CVE program"},
            {"name": "SentinelOne", "note": "AI-powered endpoint security"},
            {"name": "Deloitte Cyber", "note": "Enterprise risk & security consulting"},
            {"name": "NSA / CISA", "note": "Federal intelligence & infrastructure defense"},
        ],
    },

    "robotics_engineer": {
        "id": "robotics_engineer",
        "title": "Robotics Engineer",
        "color": "#f97316",
        "gradient": "linear-gradient(135deg, #f97316, #eab308)",
        "salary": "$84,000 – $98,000",
        "growth": "13%",
        "growth_label": "Faster than average",
        "description": (
            "Robotics engineers design, build, and program automated systems and robots used in "
            "manufacturing, surgery, exploration, and everyday life. This field uniquely combines "
            "mechanical engineering, electronics, and software - making it one of the most "
            "interdisciplinary STEM careers. With AI and automation transforming every industry, "
            "robotics engineers are on the front lines of the future of work."
        ),
        "hs_courses": [
            "AP Physics C: Mechanics",
            "AP Calculus BC",
            "AP Computer Science A",
            "Introduction to Engineering (PLTW)",
            "Electronics / Arduino fundamentals",
            "AP Statistics",
        ],
        "extracurriculars": [
            "FIRST Robotics Competition (FRC) - highest priority",
            "VEX Robotics Competition",
            "Build Arduino / Raspberry Pi projects",
            "3D printing and CAD clubs",
            "Science Olympiad (robot tour event)",
            "TSA Robotics & Automation event",
        ],
        "skills": [
            "C++ / Python / ROS programming", "CAD & mechanical design",
            "Electronics & circuit design", "Control systems",
            "3D printing & prototyping", "Sensor integration",
            "PID controllers & motion planning", "Teamwork & iteration",
        ],
        "education_links": [
            {"label": "edX - Robotics MicroMasters (Penn)", "url": "https://www.edx.org/micromasters/pennx-robotics"},
            {"label": "Coursera - Robotics Specialization (UPenn)", "url": "https://www.coursera.org/specializations/robotics"},
            {"label": "ROS Tutorials - Robot Operating System (free)", "url": "https://docs.ros.org/en/humble/Tutorials.html"},
            {"label": "MIT OpenCourseWare - Robotics: Science & Systems", "url": "https://ocw.mit.edu/courses/6-832-underactuated-robotics-spring-2009/"},
        ],
        "entry_jobs": [
            "Robotics Technician",
            "Automation Engineer (entry)",
            "Controls Engineer",
            "Mechatronics Engineer",
            "Robotics Software Developer",
        ],
        "pathway": [
            {"stage": "9th-10th Grade", "desc": "Physics + CS + engineering; join FRC or VEX robotics team ASAP."},
            {"stage": "11th-12th Grade", "desc": "Lead robotics sub-team; build Arduino/RPi projects; AP Physics C + Calc."},
            {"stage": "College (4 yr)", "desc": "B.S. Mechanical, Electrical, or Computer Engineering with robotics focus."},
            {"stage": "Internship", "desc": "Robotics or automation company internship; contribute to open-source ROS."},
            {"stage": "Entry-Level Job", "desc": "Controls or automation engineer role; rapidly growing field with excellent prospects."},
        ],
        "notable_companies": [
            {"name": "Boston Dynamics", "note": "Spot, Atlas, Stretch robots"},
            {"name": "iRobot", "note": "Roomba & consumer/defense robots"},
            {"name": "Amazon Robotics", "note": "Warehouse automation & fulfillment"},
            {"name": "Tesla (Optimus)", "note": "Humanoid robots & factory automation"},
            {"name": "Waymo", "note": "Autonomous vehicle robotics"},
            {"name": "Intuitive Surgical", "note": "da Vinci robotic surgery platforms"},
            {"name": "ABB Robotics", "note": "Industrial arms & automation"},
            {"name": "FANUC", "note": "CNC & factory floor robots"},
            {"name": "Universal Robots", "note": "Collaborative robot arms (cobots)"},
            {"name": "KUKA", "note": "Automotive & heavy industry robots"},
        ],
    },

    "quantitative_analyst": {
        "id": "quantitative_analyst",
        "title": "Quantitative Analyst",
        "color": "#a78bfa",
        "gradient": "linear-gradient(135deg, #a78bfa, #06b6d4)",
        "salary": "$115,000 – $130,000",
        "growth": "9%",
        "growth_label": "Faster than average",
        "description": (
            "Quantitative analysts — known as 'quants' — use advanced mathematics, statistics, "
            "and programming to model financial markets, price complex derivatives, and build "
            "algorithmic trading strategies. They work at hedge funds, investment banks, and "
            "asset management firms where rigorous mathematical thinking directly drives "
            "financial decisions worth billions of dollars. This is consistently one of the "
            "highest-compensating STEM career tracks available."
        ),
        "hs_courses": [
            "AP Calculus BC",
            "AP Statistics",
            "AP Computer Science A",
            "AP Physics C: Mechanics",
            "AP Economics (Micro & Macro)",
            "Linear Algebra (if offered)",
        ],
        "extracurriculars": [
            "AMC / AIME / USAMO math competitions",
            "Stock market simulation & investing clubs",
            "Competitive programming (USACO, Codeforces)",
            "Chess or other strategic thinking clubs",
            "Personal algorithmic trading projects (paper trading)",
            "TSA Data Science & Statistics event",
        ],
        "skills": [
            "Python & C++ for quantitative work", "Probability & stochastic calculus",
            "Linear algebra & numerical methods", "Financial derivatives pricing",
            "Statistical modeling & ML", "Time series analysis",
            "SQL & data pipelines", "Risk management frameworks",
        ],
        "education_links": [
            {"label": "MIT Mathematics of Finance (OCW, free)", "url": "https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/"},
            {"label": "Coursera - Financial Engineering & Risk Management (Columbia)", "url": "https://www.coursera.org/specializations/financialengineering"},
            {"label": "CFA Institute - Investment Foundations Certificate", "url": "https://www.cfainstitute.org/en/programs/investment-foundations"},
            {"label": "QuantLib - Open-source quantitative finance library", "url": "https://www.quantlib.org/"},
        ],
        "entry_jobs": [
            "Junior Quantitative Analyst",
            "Quantitative Developer",
            "Risk Analyst (entry)",
            "Algorithmic Trading Researcher",
            "Financial Data Analyst",
        ],
        "pathway": [
            {"stage": "9th-10th Grade", "desc": "Compete in AMC/AIME; excel in algebra and precalculus; join investing club."},
            {"stage": "11th-12th Grade", "desc": "AP Calc BC + AP Stats + AP CS; build a paper-trading algorithm; USACO."},
            {"stage": "College (4 yr)", "desc": "B.S. in Mathematics, Statistics, CS, or Physics; minor in finance or economics."},
            {"stage": "Internship", "desc": "Summer analyst at a bank, hedge fund, or trading firm; build quant project portfolio."},
            {"stage": "Entry-Level Job", "desc": "Junior quant or quant developer role; many pursue an M.S. or Ph.D. for advancement."},
        ],
        "notable_companies": [
            {"name": "Two Sigma", "note": "Data-driven hedge fund, heavy Python & ML"},
            {"name": "Citadel", "note": "Top multi-strategy quant hedge fund"},
            {"name": "D.E. Shaw", "note": "Computational finance & proprietary trading"},
            {"name": "Renaissance Technologies", "note": "Medallion Fund, pioneered quant trading"},
            {"name": "Jane Street", "note": "Market making, ETFs, functional programming"},
            {"name": "Virtu Financial", "note": "High-frequency & algorithmic trading"},
            {"name": "AQR Capital Management", "note": "Factor investing & academic research"},
            {"name": "Bridgewater Associates", "note": "Macro quant strategies, principles-driven"},
            {"name": "Goldman Sachs Strats", "note": "Quant research within a major bank"},
            {"name": "Morgan Stanley QIS", "note": "Quant Investment Strategies group"},
        ],
    },
}

# ─────────────────────────────────────────────
#  CAREER ID LIST & WEIGHT HELPER
# ─────────────────────────────────────────────
_C = [
    "software_engineer", "data_scientist", "biomedical_engineer",
    "aerospace_engineer", "environmental_scientist", "cybersecurity_analyst",
    "robotics_engineer", "quantitative_analyst",
]

def W(sw, ds, bme, ae, env, cs, rb, qa):
    """Build weights dict from positional args (one per career)."""
    return dict(zip(_C, [sw, ds, bme, ae, env, cs, rb, qa]))

# ─────────────────────────────────────────────
#  QUIZ QUESTIONS  (28 questions, randomized)
# ─────────────────────────────────────────────
QUIZ_QUESTIONS = [

    # SUBJECTS
    {
        "id": "q1",
        "question": "Which high school subject do you find most engaging?",
        "options": [
            {"text": "Computer science or programming",        "weights": W(3,2,0,1,0,3,2,1)},
            {"text": "Biology or anatomy",                     "weights": W(0,1,3,0,2,0,0,0)},
            {"text": "Physics or physical science",            "weights": W(1,1,1,3,1,0,3,1)},
            {"text": "Statistics or data analysis",            "weights": W(2,3,1,1,2,1,0,3)},
            {"text": "Environmental science or earth science", "weights": W(0,1,1,0,3,0,0,0)},
            {"text": "Engineering or technology courses",      "weights": W(1,0,2,2,0,1,3,0)},
        ],
    },
    {
        "id": "q2",
        "question": "When you have a math assignment, which type do you prefer?",
        "options": [
            {"text": "Algorithms and logic puzzles",         "weights": W(3,2,0,1,0,3,1,1)},
            {"text": "Statistics and probability problems",  "weights": W(1,3,1,1,2,1,0,3)},
            {"text": "Applied physics calculations",         "weights": W(0,1,1,3,0,0,2,0)},
            {"text": "Biology-related math (genetics, etc.)","weights": W(0,1,3,0,1,0,0,0)},
            {"text": "Geometry and spatial reasoning",       "weights": W(1,0,1,2,0,0,3,0)},
            {"text": "Pure math proofs and number theory",   "weights": W(1,2,0,1,0,0,0,3)},
        ],
    },
    {
        "id": "q3",
        "question": "Which of these best describes your relationship with chemistry?",
        "options": [
            {"text": "Love it - I enjoy lab experiments and reactions",      "weights": W(0,1,3,1,2,0,0,0)},
            {"text": "Like it for the data and measurement side",            "weights": W(1,2,1,0,2,0,0,1)},
            {"text": "It is okay but I prefer the physics applications",     "weights": W(0,0,1,3,1,0,1,0)},
            {"text": "Not my strength - I prefer computers or math instead", "weights": W(3,2,0,0,0,3,2,2)},
        ],
    },

    # PERSONALITY
    {
        "id": "q4",
        "question": "When facing a difficult problem, what is your natural first instinct?",
        "options": [
            {"text": "Break it into logical steps and write out a solution",      "weights": W(3,2,1,2,0,3,2,2)},
            {"text": "Look for data or patterns that explain the root cause",     "weights": W(1,3,1,1,2,1,0,3)},
            {"text": "Sketch or build a physical model to understand it",         "weights": W(0,0,2,3,0,0,3,0)},
            {"text": "Research what others have done and learn from them",        "weights": W(1,2,2,1,3,1,1,1)},
            {"text": "Think about who is affected and what the human impact is",  "weights": W(0,1,3,0,2,1,0,0)},
        ],
    },
    {
        "id": "q5",
        "question": "Which phrase best describes how you work day to day?",
        "options": [
            {"text": "Methodical - I follow a clear process and document everything", "weights": W(2,2,1,3,1,2,1,2)},
            {"text": "Curious - I constantly ask why and dig deeper",                 "weights": W(2,3,2,2,3,2,2,2)},
            {"text": "Creative - I come up with original solutions others miss",      "weights": W(2,1,2,2,1,1,3,0)},
            {"text": "Cautious - I identify risks and think several steps ahead",     "weights": W(1,1,2,2,1,3,1,2)},
            {"text": "Driven - I set ambitious goals and push hard to meet them",     "weights": W(2,2,1,3,1,2,3,2)},
        ],
    },
    {
        "id": "q6",
        "question": "When you make a mistake, how do you typically respond?",
        "options": [
            {"text": "Immediately debug it line by line until I find the exact cause", "weights": W(3,2,0,1,0,3,1,1)},
            {"text": "Collect more information before drawing any conclusions",        "weights": W(1,3,1,1,2,1,0,3)},
            {"text": "Rebuild or redesign from scratch if needed",                     "weights": W(0,0,2,2,0,0,3,0)},
            {"text": "Consult a mentor or peer to get an outside perspective",         "weights": W(1,1,2,1,2,1,1,0)},
            {"text": "Document the error so the same thing never happens again",       "weights": W(2,2,2,2,1,2,1,2)},
        ],
    },
    {
        "id": "q7",
        "question": "Which work environment sounds most appealing to you?",
        "options": [
            {"text": "A modern tech office with multiple monitors and code",               "weights": W(3,2,0,0,0,3,1,1)},
            {"text": "A research lab analyzing samples and running experiments",           "weights": W(0,2,3,1,2,1,0,0)},
            {"text": "An engineering workshop building and testing physical prototypes",   "weights": W(0,0,1,3,0,0,3,0)},
            {"text": "Outdoors collecting field data in forests, rivers, or coastlines",  "weights": W(0,0,0,0,3,0,0,0)},
            {"text": "A secure operations center monitoring live systems and threats",     "weights": W(1,1,0,0,0,3,0,0)},
            {"text": "A trading floor or financial research desk running live models",     "weights": W(0,1,0,0,0,0,0,3)},
        ],
    },
    {
        "id": "q8",
        "question": "How do you prefer to learn new, complex material?",
        "options": [
            {"text": "Building something functional right away (learn by doing)", "weights": W(3,1,1,2,0,2,3,0)},
            {"text": "Studying the theory first, then applying it",               "weights": W(1,3,2,2,2,1,1,3)},
            {"text": "Watching real-world examples and case studies",             "weights": W(1,2,2,1,3,2,1,1)},
            {"text": "Experimenting in a hands-on lab setting",                   "weights": W(1,1,3,2,2,1,2,0)},
            {"text": "Reading documentation and writing detailed notes",          "weights": W(2,3,1,1,1,2,0,3)},
        ],
    },
    {
        "id": "q9",
        "question": "In a group project, which role do you naturally fall into?",
        "options": [
            {"text": "The one who codes or builds the technical solution",    "weights": W(3,1,1,2,0,2,3,0)},
            {"text": "The analyst who finds patterns in the data",            "weights": W(1,3,1,1,2,2,0,3)},
            {"text": "The designer who figures out the system architecture",  "weights": W(2,1,2,3,0,1,2,0)},
            {"text": "The researcher who gathers and verifies information",   "weights": W(0,2,2,1,3,1,0,2)},
            {"text": "The safety checker who finds flaws in the plan",        "weights": W(1,1,1,2,1,3,1,1)},
        ],
    },
    {
        "id": "q10",
        "question": "Which statement describes your attention span best?",
        "options": [
            {"text": "I can focus for hours on a single coding or debugging session",       "weights": W(3,2,0,1,0,3,1,1)},
            {"text": "I work best doing deep analysis and number-crunching for long periods","weights": W(1,3,1,1,1,1,0,3)},
            {"text": "I love iterating on a physical build over many hours",                "weights": W(0,0,2,3,0,0,3,0)},
            {"text": "I prefer varied tasks - fieldwork, lab work, writing, meetings",      "weights": W(0,1,2,1,3,0,1,0)},
            {"text": "I thrive in high-alert situations that require constant vigilance",   "weights": W(0,1,0,1,0,3,0,0)},
        ],
    },

    # HYPOTHETICALS
    {
        "id": "q11",
        "question": "You discover that a major hospital's patient records are unprotected online. What is your immediate priority?",
        "options": [
            {"text": "Report it and help them patch the vulnerability right away",     "weights": W(1,0,0,0,0,3,0,0)},
            {"text": "Analyze how the breach happened and document the full scope",    "weights": W(1,3,0,0,0,2,0,1)},
            {"text": "Work on a long-term secure system redesign for the hospital",    "weights": W(3,1,0,0,0,2,0,0)},
            {"text": "Assess the human health impact on patients and alert them",      "weights": W(0,1,3,0,1,0,0,0)},
            {"text": "Propose policy changes to prevent this across all hospitals",    "weights": W(0,1,2,0,2,1,0,1)},
        ],
    },
    {
        "id": "q12",
        "question": "You are given $10 million to fund any STEM project. Which do you choose?",
        "options": [
            {"text": "Build an AI system that personalizes education for every student",     "weights": W(2,3,0,0,0,2,0,1)},
            {"text": "Develop a prosthetic limb controlled entirely by brain signals",       "weights": W(1,0,3,0,0,0,2,0)},
            {"text": "Design a next-generation electric aircraft with zero emissions",       "weights": W(0,0,1,3,1,0,1,0)},
            {"text": "Create a global network of sensors to detect climate tipping points",  "weights": W(0,2,0,0,3,0,0,0)},
            {"text": "Build an unhackable open-source internet security infrastructure",     "weights": W(2,1,0,0,0,3,0,0)},
            {"text": "Engineer autonomous robots that can clean up oceanic plastic waste",   "weights": W(1,0,0,1,2,0,3,0)},
            {"text": "Fund a quantitative research lab to predict and prevent market crashes","weights": W(0,2,0,0,0,0,0,3)},
        ],
    },
    {
        "id": "q13",
        "question": "You are stranded on a remote island with a small team. What role do you immediately take on?",
        "options": [
            {"text": "Rig together communication technology from available parts",       "weights": W(2,0,0,1,0,2,3,0)},
            {"text": "Survey resources: water, food, and map the terrain systematically","weights": W(0,2,0,0,3,1,0,1)},
            {"text": "Design and build a sturdy shelter using engineering principles",   "weights": W(0,0,1,2,0,0,3,0)},
            {"text": "Identify medical risks and keep the team healthy",                 "weights": W(0,0,3,0,1,0,0,0)},
            {"text": "Look for threats and establish a security perimeter",              "weights": W(0,0,0,1,0,3,1,0)},
            {"text": "Analyze weather patterns to predict conditions and plan escape",   "weights": W(0,3,1,2,2,0,0,2)},
        ],
    },
    {
        "id": "q14",
        "question": "A news alert says a rare disease is spreading rapidly. If you were a scientist, what would be your role?",
        "options": [
            {"text": "Build a predictive model to forecast how the disease will spread", "weights": W(1,3,1,0,1,0,0,3)},
            {"text": "Design a medical device that can diagnose the disease quickly",    "weights": W(0,0,3,0,0,0,1,0)},
            {"text": "Investigate environmental factors that may have triggered it",     "weights": W(0,1,1,0,3,0,0,0)},
            {"text": "Create a secure database tracking all patient data globally",     "weights": W(2,2,0,0,0,2,0,0)},
            {"text": "Engineer robots to safely deliver medicine in quarantine zones",   "weights": W(0,0,1,0,0,0,3,0)},
            {"text": "Analyze biological samples in the lab to find the root pathogen", "weights": W(0,1,3,0,1,0,0,0)},
        ],
    },
    {
        "id": "q15",
        "question": "You are hired by NASA for a special project. Which role would excite you most?",
        "options": [
            {"text": "Writing the flight control software for a Mars lander",             "weights": W(3,1,0,2,0,1,2,0)},
            {"text": "Analyzing atmospheric data from distant planets",                  "weights": W(0,3,0,1,2,0,0,1)},
            {"text": "Designing the structural components of a next-gen spacecraft",     "weights": W(0,0,1,3,0,0,2,0)},
            {"text": "Building a robotic rover that autonomously navigates terrain",     "weights": W(1,0,0,2,0,0,3,0)},
            {"text": "Running cybersecurity for NASA's mission-critical systems",        "weights": W(0,0,0,1,0,3,0,0)},
            {"text": "Modeling the financial risk of launching a commercial space mission","weights": W(0,1,0,1,0,0,0,3)},
        ],
    },
    {
        "id": "q16",
        "question": "You wake up to find the internet has gone completely dark worldwide. What is your biggest concern?",
        "options": [
            {"text": "Getting systems back online - infrastructure must be restored",        "weights": W(2,0,0,0,0,3,1,0)},
            {"text": "Understanding what caused it - the data trail must be analyzed",      "weights": W(1,3,0,0,0,2,0,1)},
            {"text": "Hospitals and medical devices that rely on connectivity",             "weights": W(0,0,3,0,1,1,0,0)},
            {"text": "Environmental monitoring systems that track disasters going offline",  "weights": W(0,1,0,0,3,0,0,0)},
            {"text": "Air traffic control and aerospace navigation systems",                "weights": W(0,0,0,3,0,1,0,0)},
            {"text": "Global financial markets and trading systems collapsing",             "weights": W(0,1,0,0,0,0,0,3)},
        ],
    },
    {
        "id": "q17",
        "question": "You have one year to work on anything you want, fully funded. What do you do?",
        "options": [
            {"text": "Build an open-source app that solves a real community problem",    "weights": W(3,1,0,0,1,1,0,0)},
            {"text": "Conduct original research and publish a scientific paper",         "weights": W(0,3,2,1,2,0,0,2)},
            {"text": "Design and prototype a physical invention from scratch",           "weights": W(0,0,2,2,0,0,3,0)},
            {"text": "Travel and collect field data on environmental changes",           "weights": W(0,1,0,0,3,0,0,0)},
            {"text": "Build a complete cybersecurity audit system for small businesses", "weights": W(1,1,0,0,0,3,0,0)},
            {"text": "Develop and back-test an algorithmic trading strategy",            "weights": W(1,2,0,0,0,0,0,3)},
        ],
    },
    {
        "id": "q18",
        "question": "A corporation asks you to ethically evaluate their use of AI. What concerns you most?",
        "options": [
            {"text": "Whether their AI could be manipulated or hacked by bad actors",    "weights": W(1,1,0,0,0,3,0,0)},
            {"text": "Whether their data collection is biased and inaccurate",           "weights": W(1,3,0,0,1,1,0,2)},
            {"text": "Whether AI automation is safe around human workers",               "weights": W(0,0,1,0,0,0,3,0)},
            {"text": "Whether the AI systems have a measurable environmental footprint", "weights": W(0,1,0,0,3,0,0,0)},
            {"text": "Whether the AI is embedded safely in safety-critical software",    "weights": W(3,1,0,1,0,1,1,0)},
            {"text": "Whether the AI models used for trading are introducing systemic financial risk","weights": W(0,2,0,0,0,0,0,3)},
        ],
    },

    # VALUES
    {
        "id": "q19",
        "question": "Which outcome would make you feel most proud of your career?",
        "options": [
            {"text": "Building a product that millions of people use every day",           "weights": W(3,1,0,1,0,1,0,0)},
            {"text": "Publishing research that changes how a field thinks",                "weights": W(0,3,2,1,2,0,0,1)},
            {"text": "Designing a medical device that gives someone a better life",        "weights": W(0,0,3,0,0,0,1,0)},
            {"text": "Contributing to a mission that puts humans on another planet",       "weights": W(0,0,0,3,0,0,1,0)},
            {"text": "Protecting ecosystems for the next generation",                      "weights": W(0,1,0,0,3,0,0,0)},
            {"text": "Stopping a major cyberattack that could have caused disaster",       "weights": W(0,0,0,0,0,3,0,0)},
            {"text": "Building a robot that changes how an entire industry operates",      "weights": W(0,0,0,1,0,0,3,0)},
            {"text": "Developing a model that accurately predicted a major market event",  "weights": W(0,2,0,0,0,0,0,3)},
        ],
    },
    {
        "id": "q20",
        "question": "How important is working outdoors or in the field to you?",
        "options": [
            {"text": "Very important - I want to be outside as much as possible",        "weights": W(0,0,0,0,3,0,0,0)},
            {"text": "Somewhat important - a mix of lab and field would be ideal",       "weights": W(0,1,2,1,2,0,0,0)},
            {"text": "Neutral - I am fine either way",                                   "weights": W(1,1,1,1,1,1,1,1)},
            {"text": "I prefer indoors - office, lab, or workshop settings",             "weights": W(2,2,2,2,0,2,2,2)},
            {"text": "Strongly prefer indoors - I need a controlled environment",        "weights": W(3,2,1,1,0,3,2,3)},
        ],
    },
    {
        "id": "q21",
        "question": "Which of these long-term goals resonates with you most?",
        "options": [
            {"text": "Become a senior engineer at a leading technology company",          "weights": W(3,1,0,0,0,1,1,0)},
            {"text": "Lead a data science team driving strategic decisions",              "weights": W(0,3,0,0,0,1,0,1)},
            {"text": "Develop a breakthrough medical device and bring it to market",     "weights": W(0,0,3,0,0,0,0,0)},
            {"text": "Work on spacecraft design at NASA or a private space company",     "weights": W(0,0,0,3,0,0,0,0)},
            {"text": "Direct environmental policy at a government agency or NGO",        "weights": W(0,1,0,0,3,0,0,0)},
            {"text": "Build and lead a cybersecurity firm protecting critical systems",   "weights": W(0,0,0,0,0,3,0,0)},
            {"text": "Found a robotics startup that automates dangerous human labor",    "weights": W(0,0,0,0,0,0,3,0)},
            {"text": "Manage a quantitative research team at a hedge fund",              "weights": W(0,1,0,0,0,0,0,3)},
        ],
    },
    {
        "id": "q22",
        "question": "What trade-off are you most willing to accept in your career?",
        "options": [
            {"text": "Lower starting pay for work that has a direct positive impact",  "weights": W(0,0,2,0,3,0,0,0)},
            {"text": "High stress for the chance to work on cutting-edge innovation",  "weights": W(2,1,1,3,0,1,2,2)},
            {"text": "Lots of alone time in exchange for deep technical mastery",      "weights": W(3,3,0,1,0,2,1,3)},
            {"text": "Physical risk for the thrill of hands-on testing and fieldwork", "weights": W(0,0,1,3,1,0,2,0)},
            {"text": "Constant learning pressure to keep up with fast-moving threats", "weights": W(2,1,0,0,0,3,0,1)},
        ],
    },
    {
        "id": "q23",
        "question": "Which skill do you most want to be known for professionally?",
        "options": [
            {"text": "Writing clean, scalable, and efficient code",              "weights": W(3,1,0,0,0,2,1,0)},
            {"text": "Turning complex datasets into clear, actionable insights", "weights": W(0,3,1,0,1,1,0,2)},
            {"text": "Creating physical designs that actually work in the world", "weights": W(0,0,2,3,0,0,3,0)},
            {"text": "Understanding biological systems at a deep level",         "weights": W(0,1,3,0,2,0,0,0)},
            {"text": "Protecting systems and anticipating adversarial attacks",  "weights": W(0,0,0,0,0,3,0,0)},
            {"text": "Communicating science to decision-makers and the public",  "weights": W(0,2,1,0,3,0,0,0)},
            {"text": "Building and validating mathematical models of real systems","weights": W(0,2,0,1,0,0,0,3)},
        ],
    },

    # INTERESTS
    {
        "id": "q24",
        "question": "Which of these activities sounds most like something you would genuinely enjoy doing on a weekend?",
        "options": [
            {"text": "Working through coding challenges or building a personal app",  "weights": W(3,2,0,0,0,2,1,0)},
            {"text": "Analyzing a sports or finance dataset and visualizing patterns","weights": W(1,3,0,0,1,1,0,2)},
            {"text": "Taking apart electronics and figuring out how to improve them", "weights": W(0,0,1,1,0,1,3,0)},
            {"text": "Volunteering at a nature preserve or water quality project",   "weights": W(0,0,1,0,3,0,0,0)},
            {"text": "Playing a hacking simulation game or CTF challenge",           "weights": W(1,1,0,0,0,3,0,0)},
            {"text": "Designing a 3D-printed part and testing it in real life",      "weights": W(0,0,2,3,0,0,2,0)},
            {"text": "Back-testing a trading strategy on historical market data",    "weights": W(0,2,0,0,0,0,0,3)},
        ],
    },
    {
        "id": "q25",
        "question": "If you had to read a book this week, which topic would you choose?",
        "options": [
            {"text": "How great software systems were designed and built",           "weights": W(3,1,0,0,0,2,0,0)},
            {"text": "The history of data and how statistics changed society",       "weights": W(0,3,0,0,1,0,0,1)},
            {"text": "Breakthroughs in biomedical technology and medicine",          "weights": W(0,0,3,0,1,0,0,0)},
            {"text": "The science and engineering of space exploration",             "weights": W(0,1,1,3,0,0,0,0)},
            {"text": "How ecosystems work and the current state of the climate",     "weights": W(0,0,0,0,3,0,0,0)},
            {"text": "True stories of major cyberattacks and how they were stopped", "weights": W(1,1,0,0,0,3,0,0)},
            {"text": "The future of robotics and artificial intelligence",           "weights": W(1,2,0,0,0,0,3,0)},
            {"text": "How quantitative methods reshaped modern finance",             "weights": W(0,2,0,0,0,0,0,3)},
        ],
    },
    {
        "id": "q26",
        "question": "Which of these best describes the physical result you want from your work?",
        "options": [
            {"text": "A deployed app, website, or software system",             "weights": W(3,1,0,0,0,1,0,0)},
            {"text": "A published report, dashboard, or data model",            "weights": W(0,3,0,0,1,1,0,2)},
            {"text": "A physical device or prototype that functions reliably",  "weights": W(0,0,3,2,0,0,3,0)},
            {"text": "A cleaner, healthier, or better-monitored environment",   "weights": W(0,0,0,0,3,0,0,0)},
            {"text": "A secured network or hardened system with no open holes", "weights": W(0,0,0,0,0,3,0,0)},
            {"text": "A completed spacecraft or aircraft ready for testing",    "weights": W(0,0,0,3,0,0,1,0)},
            {"text": "A back-tested trading model with a consistent edge",      "weights": W(0,1,0,0,0,0,0,3)},
        ],
    },
    {
        "id": "q27",
        "question": "Which unsolved problem do you find most personally compelling?",
        "options": [
            {"text": "Making software and AI completely reliable and bug-free",            "weights": W(3,2,0,0,0,1,1,0)},
            {"text": "Understanding and predicting human behavior with data",              "weights": W(0,3,1,0,0,1,0,2)},
            {"text": "Growing replacement human organs using engineered tissue",           "weights": W(0,0,3,0,0,0,0,0)},
            {"text": "Reaching and sustaining human life on another planet",               "weights": W(0,0,0,3,0,0,1,0)},
            {"text": "Reversing biodiversity loss and restoring damaged ecosystems",       "weights": W(0,1,0,0,3,0,0,0)},
            {"text": "Making digital infrastructure fully resistant to nation-state attacks","weights": W(0,0,0,0,0,3,0,0)},
            {"text": "Building autonomous machines that can replace dangerous human labor","weights": W(1,0,0,1,0,0,3,0)},
            {"text": "Eliminating irrational market bubbles through quantitative modeling","weights": W(0,2,0,0,0,0,0,3)},
        ],
    },
    {
        "id": "q28",
        "question": "In ten years, which description would make you feel most fulfilled?",
        "options": [
            {"text": "I shipped software that runs on over a million devices",            "weights": W(3,0,0,0,0,0,0,0)},
            {"text": "My models helped a major organization make a pivotal decision",     "weights": W(0,3,0,0,0,0,0,1)},
            {"text": "My device improved the quality of life for patients worldwide",     "weights": W(0,0,3,0,0,0,0,0)},
            {"text": "I contributed to a mission that changed our understanding of space","weights": W(0,0,0,3,0,0,0,0)},
            {"text": "My research led to new environmental protections becoming law",     "weights": W(0,0,0,0,3,0,0,0)},
            {"text": "I stopped a cyberattack that could have crippled national infrastructure","weights": W(0,0,0,0,0,3,0,0)},
            {"text": "The robot I engineered is now used in disaster rescue operations",  "weights": W(0,0,0,0,0,0,3,0)},
            {"text": "My trading algorithm consistently outperforms the market by a wide margin","weights": W(0,1,0,0,0,0,0,3)},
        ],
    },
]


def calculate_scores(answers: dict) -> list:
    """Score each career based on quiz answers and return sorted list."""
    scores = {cid: 0 for cid in CAREERS}
    max_possible = {cid: 0 for cid in CAREERS}

    for q in QUIZ_QUESTIONS:
        qid = q["id"]
        if qid not in answers:
            continue
        chosen_index = int(answers[qid])
        if chosen_index < 0 or chosen_index >= len(q["options"]):
            continue
        chosen = q["options"][chosen_index]
        for cid, w in chosen["weights"].items():
            scores[cid] += w

    for q in QUIZ_QUESTIONS:
        for cid in CAREERS:
            best = max(opt["weights"].get(cid, 0) for opt in q["options"])
            max_possible[cid] += best

    results = []
    for cid, score in scores.items():
        pct = round((score / max_possible[cid]) * 100) if max_possible[cid] > 0 else 0
        results.append({
            "career": CAREERS[cid],
            "score": score,
            "pct": pct,
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results


# ─────────────────────────────────────────────
#  ROUTES
# ─────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", careers=CAREERS)


@app.route("/quiz")
@login_required
def quiz():
    shuffled = QUIZ_QUESTIONS[:]
    random.shuffle(shuffled)
    return render_template("quiz.html", questions=shuffled)


@app.route("/results", methods=["POST"])
@login_required
def results():
    answers = {}
    for q in QUIZ_QUESTIONS:
        val = request.form.get(q["id"])
        if val is not None:
            answers[q["id"]] = val
    ranked = calculate_scores(answers)

    result_data = [
        {"career_id": r["career"]["id"], "pct": r["pct"], "title": r["career"]["title"]}
        for r in ranked
    ]
    qr = QuizResult(user_id=current_user.id, results_json=json.dumps(result_data))
    db.session.add(qr)
    db.session.commit()

    return render_template("results.html", ranked=ranked)


@app.route("/career/<career_id>")
@login_required
def career(career_id):
    c = CAREERS.get(career_id)
    if not c:
        return redirect(url_for("index"))
    all_careers = list(CAREERS.values())
    return render_template("career.html", career=c, all_careers=all_careers)


@app.route("/explore")
@login_required
def explore():
    return render_template("explore.html", careers=CAREERS)


# ─────────────────────────────────────────────
#  AUTH ROUTES
# ─────────────────────────────────────────────
@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if not username or not password:
            flash("Both fields are required.", "error")
        elif len(password) < 6:
            flash("Password must be at least 6 characters.", "error")
        elif User.query.filter_by(username=username).first():
            flash("Username already taken.", "error")
        else:
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for("dashboard"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page or url_for("dashboard"))
        flash("Invalid username or password.", "error")
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


# ─────────────────────────────────────────────
#  DASHBOARD
# ─────────────────────────────────────────────
@app.route("/dashboard")
@login_required
def dashboard():
    results = (
        QuizResult.query
        .filter_by(user_id=current_user.id)
        .order_by(QuizResult.created_at.desc())
        .all()
    )
    # Build active roadmaps list
    active_roadmaps = {}
    progress_rows = RoadmapProgress.query.filter_by(user_id=current_user.id).all()
    for row in progress_rows:
        if row.career_id not in active_roadmaps:
            career = CAREERS.get(row.career_id)
            if career:
                active_roadmaps[row.career_id] = {
                    "career": career,
                    "total": 0,
                    "done": 0,
                }
        if row.career_id in active_roadmaps:
            active_roadmaps[row.career_id]["total"] += 1
            if row.status == "done":
                active_roadmaps[row.career_id]["done"] += 1

    # Parse quiz results
    parsed_results = []
    for qr in results:
        data = qr.get_results()
        if data:
            parsed_results.append({"created_at": qr.created_at, "top": data[:3]})

    return render_template(
        "dashboard.html",
        parsed_results=parsed_results,
        active_roadmaps=list(active_roadmaps.values()),
        careers=CAREERS,
    )


# ─────────────────────────────────────────────
#  ROADMAP
# ─────────────────────────────────────────────
@app.route("/roadmap/<career_id>")
@login_required
def roadmap(career_id):
    career = CAREERS.get(career_id)
    roadmap_data = ROADMAPS.get(career_id)
    if not career or not roadmap_data:
        return redirect(url_for("explore"))

    # Fetch user's progress for this career
    rows = RoadmapProgress.query.filter_by(
        user_id=current_user.id, career_id=career_id
    ).all()
    progress_map = {row.node_id: row.status for row in rows}

    # Compute stats
    total_nodes = sum(len(stage["nodes"]) for stage in roadmap_data["stages"])
    done_count  = sum(1 for s in progress_map.values() if s == "done")
    ip_count    = sum(1 for s in progress_map.values() if s == "in_progress")

    return render_template(
        "roadmap.html",
        career=career,
        roadmap=roadmap_data,
        progress_map=progress_map,
        total_nodes=total_nodes,
        done_count=done_count,
        ip_count=ip_count,
    )


# ─────────────────────────────────────────────
#  API – PROGRESS UPDATE
# ─────────────────────────────────────────────
@app.route("/api/progress", methods=["POST"])
@login_required
def update_progress():
    data = request.get_json()
    career_id = data.get("career_id")
    node_id   = data.get("node_id")
    status    = data.get("status")

    if not career_id or not node_id or status not in ("not_started", "in_progress", "done"):
        return jsonify({"ok": False, "error": "Invalid input"}), 400

    row = RoadmapProgress.query.filter_by(
        user_id=current_user.id, career_id=career_id, node_id=node_id
    ).first()
    if row:
        row.status = status
    else:
        row = RoadmapProgress(
            user_id=current_user.id, career_id=career_id,
            node_id=node_id, status=status
        )
        db.session.add(row)
    db.session.commit()
    return jsonify({"ok": True, "status": status})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
