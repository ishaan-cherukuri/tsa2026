# ─────────────────────────────────────────────
#  ROADMAP DATA  (roadmap.sh-style node maps)
#  One roadmap per career, ~5 stages, ~4-5 nodes each
# ─────────────────────────────────────────────

ROADMAPS = {

    "software_engineer": {
        "title": "Software Engineer",
        "stages": [
            {
                "id": "se_s1",
                "title": "Programming Foundations",
                "nodes": [
                    {
                        "id": "se_python",
                        "title": "Learn Python",
                        "desc": "Master variables, loops, functions, classes, and file I/O. Python is the most versatile starting language for software engineers.",
                        "resources": [
                            {"label": "Python.org Official Tutorial", "url": "https://docs.python.org/3/tutorial/"},
                            {"label": "CS50P – Harvard Python Course (free)", "url": "https://cs50.harvard.edu/python/"},
                            {"label": "Automate the Boring Stuff (free book)", "url": "https://automatetheboringstuff.com/"},
                        ],
                    },
                    {
                        "id": "se_git",
                        "title": "Version Control with Git",
                        "desc": "Learn to track changes, branch, merge, and collaborate using Git and GitHub. Essential for every software job.",
                        "resources": [
                            {"label": "GitHub Skills (free, interactive)", "url": "https://skills.github.com/"},
                            {"label": "Pro Git Book (free)", "url": "https://git-scm.com/book/en/v2"},
                            {"label": "The Odin Project – Git Basics", "url": "https://www.theodinproject.com/lessons/foundations-git-basics"},
                        ],
                    },
                    {
                        "id": "se_dsa",
                        "title": "Data Structures & Algorithms",
                        "desc": "Arrays, linked lists, stacks, queues, trees, graphs, sorting, searching. This is what technical interviews test.",
                        "resources": [
                            {"label": "CS50 – Harvard (free audit)", "url": "https://cs50.harvard.edu/x/"},
                            {"label": "NeetCode.io – DSA Roadmap", "url": "https://neetcode.io/roadmap"},
                            {"label": "Visualgo – Algorithm Visualizer", "url": "https://visualgo.net/"},
                        ],
                    },
                    {
                        "id": "se_js",
                        "title": "Learn JavaScript",
                        "desc": "The language of the web. Learn DOM manipulation, async/await, and the core language features used in nearly every web project.",
                        "resources": [
                            {"label": "javascript.info (free, comprehensive)", "url": "https://javascript.info/"},
                            {"label": "freeCodeCamp JS Certification", "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/"},
                            {"label": "Eloquent JavaScript (free book)", "url": "https://eloquentjavascript.net/"},
                        ],
                    },
                ],
            },
            {
                "id": "se_s2",
                "title": "Core CS Concepts",
                "nodes": [
                    {
                        "id": "se_oop",
                        "title": "Object-Oriented Programming",
                        "desc": "Classes, inheritance, encapsulation, polymorphism. OOP is the foundation of most production codebases.",
                        "resources": [
                            {"label": "Real Python – OOP Tutorial", "url": "https://realpython.com/python3-object-oriented-programming/"},
                            {"label": "MIT 6.009 – Fundamentals of Programming", "url": "https://py.mit.edu/spring22"},
                        ],
                    },
                    {
                        "id": "se_db",
                        "title": "Databases & SQL",
                        "desc": "Relational databases, SQL queries, joins, indexing, and an introduction to NoSQL (MongoDB, Redis).",
                        "resources": [
                            {"label": "SQLZoo – Interactive SQL", "url": "https://sqlzoo.net/"},
                            {"label": "PostgreSQL Tutorial", "url": "https://www.postgresqltutorial.com/"},
                            {"label": "Khan Academy – SQL Course (free)", "url": "https://www.khanacademy.org/computing/computer-programming/sql"},
                        ],
                    },
                    {
                        "id": "se_os",
                        "title": "Operating Systems & Linux",
                        "desc": "Processes, memory management, file systems, and command-line proficiency. Most servers run Linux.",
                        "resources": [
                            {"label": "The Linux Command Line (free book)", "url": "https://linuxcommand.org/tlcl.php"},
                            {"label": "OverTheWire Bandit – Linux wargame", "url": "https://overthewire.org/wargames/bandit/"},
                            {"label": "MIT Missing Semester (free)", "url": "https://missing.csail.mit.edu/"},
                        ],
                    },
                    {
                        "id": "se_networking",
                        "title": "Computer Networking Basics",
                        "desc": "How the internet works: TCP/IP, HTTP/HTTPS, DNS, APIs, and client-server architecture.",
                        "resources": [
                            {"label": "CS50 Networks Lecture (free)", "url": "https://cs50.harvard.edu/x/"},
                            {"label": "Computerphile – Networking Videos", "url": "https://www.youtube.com/@Computerphile"},
                            {"label": "MDN – How the Web Works", "url": "https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works"},
                        ],
                    },
                ],
            },
            {
                "id": "se_s3",
                "title": "Web & App Development",
                "nodes": [
                    {
                        "id": "se_frontend",
                        "title": "Frontend Development",
                        "desc": "HTML5, CSS3, and a modern framework (React or Vue). Build UIs that users interact with directly.",
                        "resources": [
                            {"label": "The Odin Project – Full Stack Path (free)", "url": "https://www.theodinproject.com/"},
                            {"label": "React Official Tutorial", "url": "https://react.dev/learn"},
                            {"label": "CSS Tricks – Flexbox Guide", "url": "https://css-tricks.com/snippets/css/a-guide-to-flexbox/"},
                        ],
                    },
                    {
                        "id": "se_backend",
                        "title": "Backend Development",
                        "desc": "Build server-side APIs and business logic using Python (Flask/Django) or JavaScript (Node.js/Express).",
                        "resources": [
                            {"label": "Flask Mega-Tutorial (free)", "url": "https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world"},
                            {"label": "Django Girls Tutorial (free)", "url": "https://tutorial.djangogirls.org/"},
                            {"label": "Node.js Official Docs", "url": "https://nodejs.org/en/learn/getting-started/introduction-to-nodejs"},
                        ],
                    },
                    {
                        "id": "se_apis",
                        "title": "RESTful APIs & Testing",
                        "desc": "Design and consume APIs. Write unit tests, integration tests, and learn test-driven development (TDD).",
                        "resources": [
                            {"label": "REST API Tutorial", "url": "https://restfulapi.net/"},
                            {"label": "Postman Learning Center", "url": "https://learning.postman.com/"},
                            {"label": "pytest Documentation", "url": "https://docs.pytest.org/en/stable/"},
                        ],
                    },
                ],
            },
            {
                "id": "se_s4",
                "title": "DevOps & Cloud",
                "nodes": [
                    {
                        "id": "se_cloud",
                        "title": "Cloud Computing (AWS / GCP)",
                        "desc": "Deploy apps to the cloud. Learn EC2, S3, Lambda (AWS) or Cloud Run, BigQuery (GCP). Get cloud-certified.",
                        "resources": [
                            {"label": "AWS Cloud Practitioner Essentials (free)", "url": "https://aws.amazon.com/training/digital/aws-cloud-practitioner-essentials/"},
                            {"label": "Google Cloud Skills Boost", "url": "https://cloudskillsboost.google/"},
                            {"label": "A Cloud Guru – Free Tier", "url": "https://acloudguru.com/"},
                        ],
                    },
                    {
                        "id": "se_docker",
                        "title": "Docker & Containers",
                        "desc": "Package and ship applications consistently using Docker. Understand container orchestration with Kubernetes basics.",
                        "resources": [
                            {"label": "Docker Official Getting Started", "url": "https://docs.docker.com/get-started/"},
                            {"label": "Play with Docker (free browser lab)", "url": "https://labs.play-with-docker.com/"},
                        ],
                    },
                    {
                        "id": "se_cicd",
                        "title": "CI/CD Pipelines",
                        "desc": "Automate testing and deployment with GitHub Actions or similar tools. Shift-left quality practices.",
                        "resources": [
                            {"label": "GitHub Actions Documentation", "url": "https://docs.github.com/en/actions"},
                            {"label": "GitHub Skills – CI/CD", "url": "https://skills.github.com/#automate-workflows-with-github-actions"},
                        ],
                    },
                ],
            },
            {
                "id": "se_s5",
                "title": "Career Preparation",
                "nodes": [
                    {
                        "id": "se_portfolio",
                        "title": "Build Your Portfolio",
                        "desc": "Create 3–5 substantial projects on GitHub: a full-stack web app, a CLI tool, and a data-driven project.",
                        "resources": [
                            {"label": "GitHub Portfolio Guide", "url": "https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme"},
                            {"label": "40 Project Ideas for Developers", "url": "https://www.freecodecamp.org/news/javascript-projects-for-beginners/"},
                        ],
                    },
                    {
                        "id": "se_leetcode",
                        "title": "Interview Prep (LeetCode)",
                        "desc": "Solve 150+ LeetCode problems across arrays, trees, graphs, DP. Practice mock interviews to build speed and confidence.",
                        "resources": [
                            {"label": "NeetCode 150 (curated list)", "url": "https://neetcode.io/practice"},
                            {"label": "Blind 75 LeetCode Problems", "url": "https://neetcode.io/roadmap"},
                            {"label": "Pramp – Free Mock Interviews", "url": "https://www.pramp.com/"},
                        ],
                    },
                    {
                        "id": "se_oss",
                        "title": "Open Source Contributions",
                        "desc": "Contribute to open-source projects. Demonstrates real-world collaboration and code quality to employers.",
                        "resources": [
                            {"label": "First Contributions (beginner guide)", "url": "https://firstcontributions.github.io/"},
                            {"label": "Good First Issues", "url": "https://goodfirstissues.com/"},
                            {"label": "GitHub Explore – Trending Repos", "url": "https://github.com/explore"},
                        ],
                    },
                ],
            },
        ],
    },

    "data_scientist": {
        "title": "Data Scientist",
        "stages": [
            {
                "id": "ds_s1",
                "title": "Math & Stats Foundations",
                "nodes": [
                    {
                        "id": "ds_stats",
                        "title": "Statistics & Probability",
                        "desc": "Distributions, hypothesis testing, p-values, confidence intervals, Bayesian thinking. The math behind every ML model.",
                        "resources": [
                            {"label": "Khan Academy – Statistics (free)", "url": "https://www.khanacademy.org/math/statistics-probability"},
                            {"label": "StatQuest with Josh Starmer (YouTube)", "url": "https://www.youtube.com/@statquest"},
                            {"label": "Think Stats (free book)", "url": "https://greenteapress.com/wp/think-stats-2e/"},
                        ],
                    },
                    {
                        "id": "ds_linalg",
                        "title": "Linear Algebra",
                        "desc": "Vectors, matrices, eigenvalues, PCA. The language of machine learning — nearly every algorithm uses it.",
                        "resources": [
                            {"label": "3Blue1Brown – Essence of Linear Algebra", "url": "https://www.3blue1brown.com/topics/linear-algebra"},
                            {"label": "MIT OCW – Linear Algebra (free)", "url": "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"},
                        ],
                    },
                    {
                        "id": "ds_calculus",
                        "title": "Calculus for ML",
                        "desc": "Derivatives, chain rule, gradient descent. Understanding how models learn requires understanding calculus.",
                        "resources": [
                            {"label": "3Blue1Brown – Essence of Calculus", "url": "https://www.3blue1brown.com/topics/calculus"},
                            {"label": "Khan Academy – Calculus (free)", "url": "https://www.khanacademy.org/math/calculus-1"},
                        ],
                    },
                ],
            },
            {
                "id": "ds_s2",
                "title": "Programming for Data",
                "nodes": [
                    {
                        "id": "ds_python",
                        "title": "Python for Data Science",
                        "desc": "NumPy, Pandas, Matplotlib, Seaborn. The core toolkit for loading, cleaning, transforming, and visualizing data.",
                        "resources": [
                            {"label": "Kaggle – Python Course (free)", "url": "https://www.kaggle.com/learn/python"},
                            {"label": "Kaggle – Pandas Course (free)", "url": "https://www.kaggle.com/learn/pandas"},
                            {"label": "Python for Data Analysis (O'Reilly)", "url": "https://wesmckinney.com/book/"},
                        ],
                    },
                    {
                        "id": "ds_sql",
                        "title": "SQL for Data Analysis",
                        "desc": "Write complex queries, aggregations, window functions, and CTEs. SQL is the #1 data skill employers test.",
                        "resources": [
                            {"label": "Mode SQL Tutorial (free)", "url": "https://mode.com/sql-tutorial/"},
                            {"label": "SQLZoo – Interactive Practice", "url": "https://sqlzoo.net/"},
                            {"label": "Kaggle – SQL Course (free)", "url": "https://www.kaggle.com/learn/intro-to-sql"},
                        ],
                    },
                    {
                        "id": "ds_viz",
                        "title": "Data Visualization",
                        "desc": "Turn data into insights with charts, dashboards, and storytelling. Plotly, Tableau, and Power BI are industry tools.",
                        "resources": [
                            {"label": "Kaggle – Data Visualization (free)", "url": "https://www.kaggle.com/learn/data-visualization"},
                            {"label": "Tableau Public (free)", "url": "https://public.tableau.com/"},
                            {"label": "Plotly Python Documentation", "url": "https://plotly.com/python/"},
                        ],
                    },
                ],
            },
            {
                "id": "ds_s3",
                "title": "Machine Learning",
                "nodes": [
                    {
                        "id": "ds_ml_basics",
                        "title": "Classical ML Algorithms",
                        "desc": "Linear regression, logistic regression, decision trees, SVMs, k-means clustering, and how to evaluate models.",
                        "resources": [
                            {"label": "Kaggle – Intro to ML (free)", "url": "https://www.kaggle.com/learn/intro-to-machine-learning"},
                            {"label": "Scikit-Learn User Guide", "url": "https://scikit-learn.org/stable/user_guide.html"},
                            {"label": "Andrew Ng – ML Specialization (Coursera)", "url": "https://www.coursera.org/specializations/machine-learning-introduction"},
                        ],
                    },
                    {
                        "id": "ds_deep_learning",
                        "title": "Deep Learning & Neural Networks",
                        "desc": "CNNs, RNNs, transformers, and foundation models. PyTorch and TensorFlow are the main frameworks.",
                        "resources": [
                            {"label": "fast.ai – Practical Deep Learning (free)", "url": "https://course.fast.ai/"},
                            {"label": "Deep Learning Specialization (Coursera)", "url": "https://www.coursera.org/specializations/deep-learning"},
                            {"label": "PyTorch Official Tutorials", "url": "https://pytorch.org/tutorials/"},
                        ],
                    },
                    {
                        "id": "ds_feature_eng",
                        "title": "Feature Engineering & Model Tuning",
                        "desc": "Transform raw data into features that improve model performance. Cross-validation, hyperparameter tuning, pipelines.",
                        "resources": [
                            {"label": "Kaggle – Feature Engineering (free)", "url": "https://www.kaggle.com/learn/feature-engineering"},
                            {"label": "Optuna – Hyperparameter Optimization", "url": "https://optuna.org/"},
                        ],
                    },
                ],
            },
            {
                "id": "ds_s4",
                "title": "Data Engineering",
                "nodes": [
                    {
                        "id": "ds_pipelines",
                        "title": "Data Pipelines & ETL",
                        "desc": "Extract, transform, and load data at scale using Apache Spark, dbt, or Airflow. Production data science needs reliable pipelines.",
                        "resources": [
                            {"label": "dbt Learn (free)", "url": "https://courses.getdbt.com/"},
                            {"label": "Apache Spark Getting Started", "url": "https://spark.apache.org/docs/latest/quick-start.html"},
                        ],
                    },
                    {
                        "id": "ds_cloud_data",
                        "title": "Cloud Data Platforms",
                        "desc": "BigQuery (GCP), Redshift (AWS), Snowflake. Store and query petabyte-scale datasets in the cloud.",
                        "resources": [
                            {"label": "Google Cloud – BigQuery Sandbox (free)", "url": "https://cloud.google.com/bigquery/docs/sandbox"},
                            {"label": "Snowflake University (free)", "url": "https://www.snowflake.com/snowflake-university/"},
                        ],
                    },
                ],
            },
            {
                "id": "ds_s5",
                "title": "Projects & Career",
                "nodes": [
                    {
                        "id": "ds_kaggle",
                        "title": "Compete on Kaggle",
                        "desc": "Enter competitions to build skills and a portfolio under real competitive pressure. Top finishes impress employers.",
                        "resources": [
                            {"label": "Kaggle Competitions", "url": "https://www.kaggle.com/competitions"},
                            {"label": "Kaggle Getting Started Guide", "url": "https://www.kaggle.com/getting-started"},
                        ],
                    },
                    {
                        "id": "ds_portfolio",
                        "title": "End-to-End Project Portfolio",
                        "desc": "Complete 3 projects: data cleaning + EDA, a predictive model deployed as an API, and a dashboard. Host on GitHub.",
                        "resources": [
                            {"label": "Streamlit – Deploy ML Apps Free", "url": "https://streamlit.io/"},
                            {"label": "HuggingFace Spaces (free hosting)", "url": "https://huggingface.co/spaces"},
                        ],
                    },
                    {
                        "id": "ds_resume",
                        "title": "DS Resume & LinkedIn",
                        "desc": "Quantify your impact. 'Built model that improved X by Y%' beats a list of tools. List all Kaggle medals and certifications.",
                        "resources": [
                            {"label": "Towards Data Science – Career Guide", "url": "https://towardsdatascience.com/"},
                            {"label": "DataLemur – SQL Interview Prep", "url": "https://datalemur.com/"},
                        ],
                    },
                ],
            },
        ],
    },

    "biomedical_engineer": {
        "title": "Biomedical Engineer",
        "stages": [
            {
                "id": "bme_s1",
                "title": "Biology & Chemistry Foundations",
                "nodes": [
                    {
                        "id": "bme_biology",
                        "title": "Cell & Molecular Biology",
                        "desc": "Cell structure, genetics, protein synthesis, and biochemical pathways. The biological foundation for everything in biomedical engineering.",
                        "resources": [
                            {"label": "Khan Academy – Biology (free)", "url": "https://www.khanacademy.org/science/ap-biology"},
                            {"label": "MIT OCW – Biology (free)", "url": "https://ocw.mit.edu/courses/7-01sc-fundamentals-of-biology-fall-2011/"},
                            {"label": "CrashCourse Biology (YouTube)", "url": "https://www.youtube.com/playlist?list=PL3EED4C1D684D3ADF"},
                        ],
                    },
                    {
                        "id": "bme_chemistry",
                        "title": "Organic Chemistry",
                        "desc": "Functional groups, reaction mechanisms, polymers, and biomolecules. Essential for understanding biomaterials and drugs.",
                        "resources": [
                            {"label": "Khan Academy – Organic Chemistry (free)", "url": "https://www.khanacademy.org/science/organic-chemistry"},
                            {"label": "Organic Chemistry Tutor (YouTube)", "url": "https://www.youtube.com/@TheOrganicChemistryTutor"},
                        ],
                    },
                    {
                        "id": "bme_anatomy",
                        "title": "Human Anatomy & Physiology",
                        "desc": "Organ systems, cardiovascular mechanics, neural signaling. Context for designing devices that work inside or alongside the human body.",
                        "resources": [
                            {"label": "Visible Body – 3D Anatomy App", "url": "https://www.visiblebody.com/"},
                            {"label": "OpenStax Anatomy & Physiology (free)", "url": "https://openstax.org/books/anatomy-and-physiology/pages/1-introduction"},
                        ],
                    },
                ],
            },
            {
                "id": "bme_s2",
                "title": "Engineering Fundamentals",
                "nodes": [
                    {
                        "id": "bme_mechanics",
                        "title": "Biomechanics",
                        "desc": "Statics, dynamics, and material properties as applied to bones, tendons, and prosthetics. How forces interact with biological structures.",
                        "resources": [
                            {"label": "MIT OCW – Mechanics (free)", "url": "https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/"},
                            {"label": "CrashCourse Physics (YouTube)", "url": "https://www.youtube.com/playlist?list=PL8dPuuaLjXtN0ge7yDk_UA0ldZJdhwkoV"},
                        ],
                    },
                    {
                        "id": "bme_circuits",
                        "title": "Circuits & Bioelectronics",
                        "desc": "Ohm's law, amplifiers, filters, and biosignal processing (ECG, EEG). Electronic measurement is central to medical devices.",
                        "resources": [
                            {"label": "All About Circuits (free)", "url": "https://www.allaboutcircuits.com/"},
                            {"label": "Khan Academy – Electrical Engineering (free)", "url": "https://www.khanacademy.org/science/electrical-engineering"},
                        ],
                    },
                    {
                        "id": "bme_matlab",
                        "title": "MATLAB & Signal Processing",
                        "desc": "MATLAB is the standard tool in biomedical engineering labs. Learn signal filtering, FFT, and data acquisition.",
                        "resources": [
                            {"label": "MATLAB OnRamp (free, official)", "url": "https://matlabacademy.mathworks.com/"},
                            {"label": "Coursera – MATLAB Programming (free audit)", "url": "https://www.coursera.org/learn/matlab"},
                        ],
                    },
                ],
            },
            {
                "id": "bme_s3",
                "title": "Medical Device Knowledge",
                "nodes": [
                    {
                        "id": "bme_imaging",
                        "title": "Medical Imaging",
                        "desc": "MRI, CT, ultrasound, and X-ray physics and image processing. Image analysis is a core application of biomedical engineering.",
                        "resources": [
                            {"label": "OsiriX Imaging Software (free)", "url": "https://www.osirix-viewer.com/"},
                            {"label": "Radiopaedia – Imaging Reference (free)", "url": "https://radiopaedia.org/"},
                        ],
                    },
                    {
                        "id": "bme_biomaterials",
                        "title": "Biomaterials & Implants",
                        "desc": "Polymers, ceramics, metals, and composites used in medical devices. Biocompatibility, degradation, and tissue interaction.",
                        "resources": [
                            {"label": "MIT OCW – Biomaterials (free)", "url": "https://ocw.mit.edu/courses/3-051j-materials-for-biomedical-applications-spring-2006/"},
                        ],
                    },
                    {
                        "id": "bme_fda",
                        "title": "FDA Regulatory Basics",
                        "desc": "Class I/II/III medical devices, 510(k) clearance, PMA approval, GMP. Regulatory knowledge separates junior from senior BMEs.",
                        "resources": [
                            {"label": "FDA – Medical Device Overview (free)", "url": "https://www.fda.gov/medical-devices/device-advice-comprehensive-regulatory-assistance/overview-device-regulation"},
                            {"label": "FDA CDRH Learn (free courses)", "url": "https://www.fda.gov/training-and-continuing-education/cdrh-learn"},
                        ],
                    },
                ],
            },
            {
                "id": "bme_s4",
                "title": "Research & Lab Skills",
                "nodes": [
                    {
                        "id": "bme_lab",
                        "title": "Lab Techniques",
                        "desc": "PCR, gel electrophoresis, cell culture, microscopy, and sterilization protocols. Wet-lab experience is expected in biomedical roles.",
                        "resources": [
                            {"label": "iBiology – Lab Technique Videos (free)", "url": "https://www.ibiology.org/"},
                            {"label": "JoVE – Journal of Visualized Experiments", "url": "https://www.jove.com/"},
                        ],
                    },
                    {
                        "id": "bme_research",
                        "title": "Research Methods & Publishing",
                        "desc": "How to design experiments, write research papers, and understand peer review. Pursue a summer research internship at a university lab.",
                        "resources": [
                            {"label": "PubMed – Free Medical Literature", "url": "https://pubmed.ncbi.nlm.nih.gov/"},
                            {"label": "How to Read a Scientific Paper", "url": "https://www.science.org/content/article/how-seriously-read-scientific-paper"},
                        ],
                    },
                ],
            },
            {
                "id": "bme_s5",
                "title": "Career & Specialization",
                "nodes": [
                    {
                        "id": "bme_internship",
                        "title": "Industry Internship",
                        "desc": "Target medical device companies (Medtronic, Stryker, J&J) or hospital biomedical engineering departments for summer internships.",
                        "resources": [
                            {"label": "BMES – Biomedical Engineering Society (student resources)", "url": "https://www.bmes.org/"},
                            {"label": "Medtronic Careers", "url": "https://jobs.medtronic.com/"},
                        ],
                    },
                    {
                        "id": "bme_grad",
                        "title": "Graduate School Consideration",
                        "desc": "Many BME roles (especially R&D) require an M.S. or Ph.D. Research fellowship programs provide funded pathways.",
                        "resources": [
                            {"label": "NIH STEM Graduate Fellowship", "url": "https://www.nigms.nih.gov/training/pages/graduate.aspx"},
                            {"label": "GradCafe – Biomedical Forum", "url": "https://forum.thegradcafe.com/"},
                        ],
                    },
                ],
            },
        ],
    },

    "aerospace_engineer": {
        "title": "Aerospace Engineer",
        "stages": [
            {
                "id": "ae_s1",
                "title": "Physics & Math Foundations",
                "nodes": [
                    {
                        "id": "ae_mechanics",
                        "title": "Classical Mechanics",
                        "desc": "Kinematics, Newton's laws, rotational motion, energy, and momentum. The physics backbone of every aerospace system.",
                        "resources": [
                            {"label": "Khan Academy – Physics (free)", "url": "https://www.khanacademy.org/science/physics"},
                            {"label": "MIT OCW – Classical Mechanics (free)", "url": "https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/"},
                        ],
                    },
                    {
                        "id": "ae_calculus",
                        "title": "Multivariable Calculus & Diff Eq",
                        "desc": "Partial derivatives, integrals in 3D, and differential equations are used constantly in aerodynamics and orbital mechanics.",
                        "resources": [
                            {"label": "3Blue1Brown – Calculus Series", "url": "https://www.3blue1brown.com/topics/calculus"},
                            {"label": "MIT OCW – Differential Equations (free)", "url": "https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/"},
                        ],
                    },
                    {
                        "id": "ae_thermo",
                        "title": "Thermodynamics",
                        "desc": "Heat transfer, entropy, engine cycles (Brayton, Rankine). Critical for propulsion system design and hypersonic applications.",
                        "resources": [
                            {"label": "Khan Academy – Thermodynamics (free)", "url": "https://www.khanacademy.org/science/ap-physics-2/ap-thermodynamics"},
                            {"label": "Engineering Thermodynamics (free textbook)", "url": "https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/notes.html"},
                        ],
                    },
                ],
            },
            {
                "id": "ae_s2",
                "title": "Core Aerospace Engineering",
                "nodes": [
                    {
                        "id": "ae_aero",
                        "title": "Aerodynamics",
                        "desc": "Lift, drag, Bernoulli's principle, Navier-Stokes equations, and boundary layers. How aircraft actually fly.",
                        "resources": [
                            {"label": "NASA Aerodynamics Index (free)", "url": "https://www.grc.nasa.gov/www/k-12/airplane/"},
                            {"label": "MIT OCW – Aerodynamics (free)", "url": "https://ocw.mit.edu/courses/16-100-aerodynamics-fall-2005/"},
                        ],
                    },
                    {
                        "id": "ae_structures",
                        "title": "Structural Analysis",
                        "desc": "Stress, strain, finite element analysis (FEA), fatigue. Aircraft structures must be incredibly light yet withstand enormous loads.",
                        "resources": [
                            {"label": "MIT OCW – Structural Mechanics (free)", "url": "https://ocw.mit.edu/courses/16-20-structural-mechanics-spring-2013/"},
                            {"label": "ANSYS Student (free FEA software)", "url": "https://www.ansys.com/academic/students"},
                        ],
                    },
                    {
                        "id": "ae_propulsion",
                        "title": "Propulsion Systems",
                        "desc": "Jet engines, rockets, turbofans. Understand thrust, specific impulse, and the Tsiolkovsky rocket equation.",
                        "resources": [
                            {"label": "NASA Rocket Science Basics (free)", "url": "https://www.grc.nasa.gov/www/k-12/rocket/"},
                            {"label": "MIT OCW – Propulsion Systems (free)", "url": "https://ocw.mit.edu/courses/16-50-introduction-to-propulsion-systems-spring-2012/"},
                        ],
                    },
                ],
            },
            {
                "id": "ae_s3",
                "title": "Simulation & Design Tools",
                "nodes": [
                    {
                        "id": "ae_cad",
                        "title": "CAD & 3D Modeling",
                        "desc": "SolidWorks, CATIA, or Fusion 360 for designing parts and assemblies. Industry standard for aerospace hardware.",
                        "resources": [
                            {"label": "Autodesk Fusion 360 (free for students)", "url": "https://www.autodesk.com/education/edu-software/overview"},
                            {"label": "SolidWorks Student Edition", "url": "https://www.solidworks.com/sw/education/student-software-3d-mcad.htm"},
                        ],
                    },
                    {
                        "id": "ae_cfd",
                        "title": "Computational Fluid Dynamics (CFD)",
                        "desc": "Simulate airflow over surfaces digitally. OpenFOAM (free) and ANSYS Fluent are widely used in industry.",
                        "resources": [
                            {"label": "OpenFOAM – Free CFD Software", "url": "https://www.openfoam.com/"},
                            {"label": "NASA CFD Resources (free)", "url": "https://www.grc.nasa.gov/www/wind/valid/homepage.html"},
                        ],
                    },
                    {
                        "id": "ae_matlab",
                        "title": "MATLAB / Python for Simulation",
                        "desc": "Numerical simulation, control system design, orbital mechanics calculations. MATLAB is standard in aerospace academia and industry.",
                        "resources": [
                            {"label": "MATLAB OnRamp (free, official)", "url": "https://matlabacademy.mathworks.com/"},
                            {"label": "Aerospace Toolbox Documentation", "url": "https://www.mathworks.com/products/aerospace-toolbox.html"},
                        ],
                    },
                ],
            },
            {
                "id": "ae_s4",
                "title": "Systems & Orbital Mechanics",
                "nodes": [
                    {
                        "id": "ae_orbital",
                        "title": "Orbital Mechanics",
                        "desc": "Kepler's laws, Hohmann transfers, orbital maneuvers, and re-entry dynamics. Essential for space mission design.",
                        "resources": [
                            {"label": "Kerbal Space Program (learn orbital mechanics by playing)", "url": "https://www.kerbalspaceprogram.com/"},
                            {"label": "MIT OCW – Orbital Mechanics (free)", "url": "https://ocw.mit.edu/courses/16-346-astrodynamics-fall-2008/"},
                        ],
                    },
                    {
                        "id": "ae_avionics",
                        "title": "Avionics & Control Systems",
                        "desc": "Autopilot, flight control laws, PID controllers, and sensor fusion. Modern aircraft are fly-by-wire systems.",
                        "resources": [
                            {"label": "ArduPilot – Open Source Autopilot", "url": "https://ardupilot.org/"},
                            {"label": "MIT OCW – Control Systems (free)", "url": "https://ocw.mit.edu/courses/6-302-feedback-systems-spring-2007/"},
                        ],
                    },
                ],
            },
            {
                "id": "ae_s5",
                "title": "Career Preparation",
                "nodes": [
                    {
                        "id": "ae_aiaa",
                        "title": "AIAA Student Membership & Competitions",
                        "desc": "AIAA Design-Build-Fly, Rocketry challenges, and Design Competitions are the best resume items for aerospace students.",
                        "resources": [
                            {"label": "AIAA – Student Programs", "url": "https://www.aiaa.org/students"},
                            {"label": "Team America Rocketry Challenge", "url": "https://rocketcontest.org/"},
                        ],
                    },
                    {
                        "id": "ae_clearance",
                        "title": "Security Clearance Awareness",
                        "desc": "Many aerospace/defense roles require security clearance. Keep a clean record and understand the application process.",
                        "resources": [
                            {"label": "Defense Counterintelligence – Clearance Info", "url": "https://www.dcsa.mil/"},
                            {"label": "Northrop Grumman Careers (clearance roles)", "url": "https://www.northropgrumman.com/careers/"},
                        ],
                    },
                    {
                        "id": "ae_nasa",
                        "title": "NASA Internships & Co-ops",
                        "desc": "NASA offers paid student internships across all centers. Apply early — deadlines are 3–4 months before start dates.",
                        "resources": [
                            {"label": "NASA Internships Portal", "url": "https://intern.nasa.gov/"},
                            {"label": "NASA Student Opportunities", "url": "https://www.nasa.gov/learning-resources/internships-and-fellowships/"},
                        ],
                    },
                ],
            },
        ],
    },

    "environmental_scientist": {
        "title": "Environmental Scientist",
        "stages": [
            {
                "id": "env_s1",
                "title": "Sciences Foundations",
                "nodes": [
                    {
                        "id": "env_ecology",
                        "title": "Ecology & Earth Systems",
                        "desc": "Ecosystems, food webs, biogeochemical cycles, climate science. The conceptual foundation of environmental work.",
                        "resources": [
                            {"label": "Khan Academy – Ecology (free)", "url": "https://www.khanacademy.org/science/ap-biology/ecology-ap"},
                            {"label": "CrashCourse Ecology (YouTube)", "url": "https://www.youtube.com/playlist?list=PL8dPuuaLjXtNdTKZkV_GiIYXpV9yOmaDe"},
                        ],
                    },
                    {
                        "id": "env_chem",
                        "title": "Environmental Chemistry",
                        "desc": "Water chemistry, soil contaminants, air pollutants, and toxicology. How chemicals move through and impact ecosystems.",
                        "resources": [
                            {"label": "EPA – Environmental Chemistry Resources (free)", "url": "https://www.epa.gov/environmental-topics/chemicals-toxics-and-pesticides"},
                            {"label": "Khan Academy – Chemistry (free)", "url": "https://www.khanacademy.org/science/chemistry"},
                        ],
                    },
                    {
                        "id": "env_geology",
                        "title": "Geology & Hydrology",
                        "desc": "Rock cycles, groundwater flow, watersheds, and soil science. Essential for site remediation and environmental impact assessment.",
                        "resources": [
                            {"label": "USGS Learning Web (free)", "url": "https://www.usgs.gov/educational-resources"},
                            {"label": "Khan Academy – Geology (free)", "url": "https://www.khanacademy.org/science/cosmology-and-astronomy"},
                        ],
                    },
                ],
            },
            {
                "id": "env_s2",
                "title": "Field & Lab Skills",
                "nodes": [
                    {
                        "id": "env_sampling",
                        "title": "Environmental Sampling",
                        "desc": "Water, soil, and air sampling protocols. Chain of custody, field safety, and quality assurance/quality control (QA/QC).",
                        "resources": [
                            {"label": "EPA Sampling Methods (free)", "url": "https://www.epa.gov/measurements"},
                            {"label": "USGS Field Methods (free)", "url": "https://pubs.usgs.gov/tm/09/a02/"},
                        ],
                    },
                    {
                        "id": "env_lab",
                        "title": "Laboratory Analysis",
                        "desc": "Spectrophotometry, chromatography, titration, and biological testing. Read and interpret environmental lab reports.",
                        "resources": [
                            {"label": "EPA Standard Methods (free)", "url": "https://www.epa.gov/water-research/environmental-laboratory-methods"},
                            {"label": "iBiology Lab Videos (free)", "url": "https://www.ibiology.org/"},
                        ],
                    },
                ],
            },
            {
                "id": "env_s3",
                "title": "Data Analysis & GIS",
                "nodes": [
                    {
                        "id": "env_stats",
                        "title": "Environmental Statistics",
                        "desc": "R or Python for analyzing environmental datasets. Regression, ANOVA, time-series analysis, and outlier detection.",
                        "resources": [
                            {"label": "R for Data Science (free book)", "url": "https://r4ds.had.co.nz/"},
                            {"label": "StatQuest with Josh Starmer (YouTube)", "url": "https://www.youtube.com/@statquest"},
                        ],
                    },
                    {
                        "id": "env_gis",
                        "title": "GIS & Remote Sensing",
                        "desc": "ArcGIS and QGIS for mapping environmental data. Satellite imagery analysis, land cover classification, and spatial analysis.",
                        "resources": [
                            {"label": "QGIS – Free GIS Software", "url": "https://qgis.org/"},
                            {"label": "Esri ArcGIS for Students (free)", "url": "https://www.esri.com/en-us/landing-page/product/2019/arcgis-for-personal-use/overview"},
                            {"label": "Google Earth Engine (free)", "url": "https://earthengine.google.com/"},
                        ],
                    },
                ],
            },
            {
                "id": "env_s4",
                "title": "Policy & Regulation",
                "nodes": [
                    {
                        "id": "env_law",
                        "title": "Environmental Law & Policy",
                        "desc": "Clean Air Act, Clean Water Act, CERCLA (Superfund), NEPA. Understanding regulations is essential for compliance work.",
                        "resources": [
                            {"label": "EPA Laws & Regulations (free)", "url": "https://www.epa.gov/laws-regulations"},
                            {"label": "Yale Environmental Law Journal (free articles)", "url": "https://elj.yale.edu/"},
                        ],
                    },
                    {
                        "id": "env_eia",
                        "title": "Environmental Impact Assessment",
                        "desc": "NEPA EIS reports, Phase I/II site assessments, risk communication with communities and regulators.",
                        "resources": [
                            {"label": "EPA NEPA Overview (free)", "url": "https://www.epa.gov/nepa"},
                            {"label": "Sample EIS Documents (free)", "url": "https://www.epa.gov/nepa/eis-database"},
                        ],
                    },
                ],
            },
            {
                "id": "env_s5",
                "title": "Career Pathways",
                "nodes": [
                    {
                        "id": "env_certs",
                        "title": "Professional Certifications",
                        "desc": "HAZWOPER 40-hour, OSHA-10, AIHA credentials, and Registered Environmental Manager (REM). Opens doors to field and compliance roles.",
                        "resources": [
                            {"label": "OSHA HAZWOPER Training Info (free)", "url": "https://www.osha.gov/hazwoper"},
                            {"label": "AIHA – Environmental Health Credentials", "url": "https://www.aiha.org/"},
                        ],
                    },
                    {
                        "id": "env_internship",
                        "title": "Federal & NGO Internships",
                        "desc": "EPA, USGS, NOAA, The Nature Conservancy, and local state DEP agencies all offer student opportunities.",
                        "resources": [
                            {"label": "EPA Student Internships", "url": "https://www.epa.gov/careers/student-internship-program"},
                            {"label": "USGS Student Programs", "url": "https://www.usgs.gov/human-capital/internships-and-student-programs"},
                            {"label": "NOAA Student Opportunities", "url": "https://www.noaa.gov/opportunities/education"},
                        ],
                    },
                ],
            },
        ],
    },

    "cybersecurity_analyst": {
        "title": "Cybersecurity Analyst",
        "stages": [
            {
                "id": "cs_s1",
                "title": "Networking & OS Basics",
                "nodes": [
                    {
                        "id": "cs_networking",
                        "title": "Computer Networking",
                        "desc": "OSI model, TCP/IP stack, DNS, HTTP/S, firewalls, VPNs, subnetting (CIDR). Hacking and defending require deep network knowledge.",
                        "resources": [
                            {"label": "Professor Messer – CompTIA Network+ (free)", "url": "https://www.professormesser.com/network-plus/"},
                            {"label": "Cisco Networking Academy (free courses)", "url": "https://www.netacad.com/"},
                            {"label": "TryHackMe – Pre-Security Path", "url": "https://tryhackme.com/path/outline/presecurity"},
                        ],
                    },
                    {
                        "id": "cs_linux",
                        "title": "Linux Administration",
                        "desc": "Most servers and hacking tools run on Linux. Learn the filesystem, permissions, users, processes, and scripting.",
                        "resources": [
                            {"label": "OverTheWire Bandit Wargame (free)", "url": "https://overthewire.org/wargames/bandit/"},
                            {"label": "The Linux Command Line (free book)", "url": "https://linuxcommand.org/tlcl.php"},
                            {"label": "TryHackMe – Linux Fundamentals", "url": "https://tryhackme.com/module/linux-fundamentals"},
                        ],
                    },
                    {
                        "id": "cs_windows",
                        "title": "Windows & Active Directory",
                        "desc": "Windows security, registry, Group Policy, and Active Directory are the target in >80% of corporate breaches.",
                        "resources": [
                            {"label": "TryHackMe – Windows Fundamentals", "url": "https://tryhackme.com/module/windows-fundamentals"},
                            {"label": "Microsoft Learn – Active Directory (free)", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/ad-ds-getting-started"},
                        ],
                    },
                ],
            },
            {
                "id": "cs_s2",
                "title": "Security Fundamentals",
                "nodes": [
                    {
                        "id": "cs_cryptography",
                        "title": "Cryptography",
                        "desc": "Symmetric/asymmetric encryption, hashing, PKI, TLS/SSL, and how crypto is broken. The math behind secure communications.",
                        "resources": [
                            {"label": "Cryptopals – Hands-on Crypto Challenges", "url": "https://cryptopals.com/"},
                            {"label": "Khan Academy – Cryptography (free)", "url": "https://www.khanacademy.org/computing/computer-science/cryptography"},
                        ],
                    },
                    {
                        "id": "cs_threats",
                        "title": "Threat Landscape & Attack Patterns",
                        "desc": "OWASP Top 10, MITRE ATT&CK framework, phishing, ransomware, supply chain attacks, and social engineering.",
                        "resources": [
                            {"label": "MITRE ATT&CK Navigator (free)", "url": "https://attack.mitre.org/"},
                            {"label": "OWASP Top 10 (free)", "url": "https://owasp.org/Top10/"},
                        ],
                    },
                    {
                        "id": "cs_soc",
                        "title": "SOC & Incident Response",
                        "desc": "SIEM tools (Splunk, Sentinel), log analysis, alert triage, and incident response playbooks. The day-to-day of a SOC analyst.",
                        "resources": [
                            {"label": "Splunk Free Training", "url": "https://www.splunk.com/en_us/training.html"},
                            {"label": "TryHackMe – SOC Level 1 Path", "url": "https://tryhackme.com/path/outline/soclevel1"},
                        ],
                    },
                ],
            },
            {
                "id": "cs_s3",
                "title": "Offensive Security",
                "nodes": [
                    {
                        "id": "cs_pentest",
                        "title": "Penetration Testing",
                        "desc": "Reconnaissance, exploitation, post-exploitation, and reporting. Practice legally on TryHackMe and HackTheBox.",
                        "resources": [
                            {"label": "TryHackMe – Jr Penetration Tester Path", "url": "https://tryhackme.com/path/outline/jrpenetrationtester"},
                            {"label": "Hack The Box (free tier)", "url": "https://www.hackthebox.com/"},
                            {"label": "PortSwigger Web Security Academy (free)", "url": "https://portswigger.net/web-security"},
                        ],
                    },
                    {
                        "id": "cs_ctf",
                        "title": "CTF Competitions",
                        "desc": "Capture the Flag competitions build practical skills across web, crypto, forensics, and reverse engineering. Great resume items.",
                        "resources": [
                            {"label": "CTFtime – Upcoming Competitions", "url": "https://ctftime.org/"},
                            {"label": "picoCTF – Beginner-Friendly CTF", "url": "https://picoctf.org/"},
                        ],
                    },
                    {
                        "id": "cs_webapp",
                        "title": "Web Application Security",
                        "desc": "SQL injection, XSS, CSRF, IDOR, and business logic bugs. Web vulns are the most common attack surface.",
                        "resources": [
                            {"label": "PortSwigger Web Security Academy (free)", "url": "https://portswigger.net/web-security"},
                            {"label": "DVWA – Damn Vulnerable Web App", "url": "https://dvwa.co.uk/"},
                        ],
                    },
                ],
            },
            {
                "id": "cs_s4",
                "title": "Certifications",
                "nodes": [
                    {
                        "id": "cs_comptia",
                        "title": "CompTIA Certifications",
                        "desc": "A+, Network+, Security+. These are the baseline employer requirements. Security+ is DoD 8570 compliant — opens federal roles.",
                        "resources": [
                            {"label": "Professor Messer – Free Security+ Study", "url": "https://www.professormesser.com/security-plus/"},
                            {"label": "CompTIA Security+ Exam Info", "url": "https://www.comptia.org/certifications/security"},
                        ],
                    },
                    {
                        "id": "cs_ehc",
                        "title": "CEH or OSCP",
                        "desc": "Certified Ethical Hacker (entry-friendly) or Offensive Security Certified Professional (OSCP, challenging, highly respected).",
                        "resources": [
                            {"label": "EC-Council – CEH Info", "url": "https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/"},
                            {"label": "Offensive Security – OSCP Info", "url": "https://www.offsec.com/courses/pen-200/"},
                        ],
                    },
                ],
            },
            {
                "id": "cs_s5",
                "title": "Specialization & Career",
                "nodes": [
                    {
                        "id": "cs_homelab",
                        "title": "Build a Home Lab",
                        "desc": "Run virtual machines (Kali Linux, vulnerable VMs) to practice attacks safely. Demonstrates initiative to every interviewer.",
                        "resources": [
                            {"label": "VirtualBox (free)", "url": "https://www.virtualbox.org/"},
                            {"label": "VulnHub – Free Vulnerable VMs", "url": "https://www.vulnhub.com/"},
                        ],
                    },
                    {
                        "id": "cs_bugbounty",
                        "title": "Bug Bounty Programs",
                        "desc": "Earn real money finding vulnerabilities legally on HackerOne and Bugcrowd. One critical bug find can transform your career.",
                        "resources": [
                            {"label": "HackerOne – Bug Bounty Programs", "url": "https://www.hackerone.com/"},
                            {"label": "Bugcrowd – Bug Bounty Programs", "url": "https://www.bugcrowd.com/"},
                        ],
                    },
                ],
            },
        ],
    },

    "robotics_engineer": {
        "title": "Robotics Engineer",
        "stages": [
            {
                "id": "rb_s1",
                "title": "Math & Physics",
                "nodes": [
                    {
                        "id": "rb_linear_algebra",
                        "title": "Linear Algebra & Geometry",
                        "desc": "Rotation matrices, quaternions, transformations, coordinate frames. Every robot's position in space is described with these tools.",
                        "resources": [
                            {"label": "3Blue1Brown – Linear Algebra Series", "url": "https://www.3blue1brown.com/topics/linear-algebra"},
                            {"label": "MIT OCW – Linear Algebra (free)", "url": "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"},
                        ],
                    },
                    {
                        "id": "rb_dynamics",
                        "title": "Dynamics & Kinematics",
                        "desc": "Forward and inverse kinematics, robot joints, degrees of freedom, and Newton-Euler dynamics for robotic arms.",
                        "resources": [
                            {"label": "Modern Robotics – Northwestern (free textbook + Coursera)", "url": "https://modernrobotics.northwestern.edu/nu-gm-book-resource/"},
                            {"label": "Robotics Academy (free)", "url": "https://www.education.rec.ri.cmu.edu/"},
                        ],
                    },
                    {
                        "id": "rb_control",
                        "title": "Control Theory",
                        "desc": "PID controllers, feedback loops, stability analysis. How robots maintain balance, velocity, and position precisely.",
                        "resources": [
                            {"label": "Brian Douglas – Control Systems (YouTube, free)", "url": "https://www.youtube.com/@BrianBDouglas"},
                            {"label": "MIT OCW – Control Systems (free)", "url": "https://ocw.mit.edu/courses/6-302-feedback-systems-spring-2007/"},
                        ],
                    },
                ],
            },
            {
                "id": "rb_s2",
                "title": "Programming & Electronics",
                "nodes": [
                    {
                        "id": "rb_cpp",
                        "title": "C++ for Robotics",
                        "desc": "Memory management, pointers, real-time performance. C++ is the primary language for performance-critical robot software.",
                        "resources": [
                            {"label": "learncpp.com (free, comprehensive)", "url": "https://www.learncpp.com/"},
                            {"label": "C++ Primer (standard textbook)", "url": "https://www.amazon.com/Primer-5th-Stanley-B-Lippman/dp/0321714113"},
                        ],
                    },
                    {
                        "id": "rb_python_ros",
                        "title": "Python & ROS",
                        "desc": "Robot Operating System (ROS2) is the middleware standard. Python is used for rapid prototyping and high-level robot logic.",
                        "resources": [
                            {"label": "ROS2 Tutorials (free, official)", "url": "https://docs.ros.org/en/humble/Tutorials.html"},
                            {"label": "The Construct – ROS Learning Platform", "url": "https://www.theconstructsim.com/"},
                        ],
                    },
                    {
                        "id": "rb_arduino",
                        "title": "Microcontrollers & Electronics",
                        "desc": "Arduino, Raspberry Pi, sensors, actuators, PWM, I2C/SPI. Hands-on electronics is the foundation of hardware robotics.",
                        "resources": [
                            {"label": "Arduino Official Tutorials", "url": "https://docs.arduino.cc/tutorials/"},
                            {"label": "Adafruit Learning System (free)", "url": "https://learn.adafruit.com/"},
                        ],
                    },
                ],
            },
            {
                "id": "rb_s3",
                "title": "Mechanical Design",
                "nodes": [
                    {
                        "id": "rb_cad",
                        "title": "CAD & 3D Printing",
                        "desc": "Design robot chassis, brackets, and mechanisms in Fusion 360 or SolidWorks. Prototype with FDM 3D printers.",
                        "resources": [
                            {"label": "Autodesk Fusion 360 (free for students)", "url": "https://www.autodesk.com/education/edu-software/overview"},
                            {"label": "Prusa 3D Printing Guide (free)", "url": "https://help.prusa3d.com/"},
                        ],
                    },
                    {
                        "id": "rb_mechanisms",
                        "title": "Mechanisms & Actuators",
                        "desc": "Gears, belts, cams, servo vs DC motors, pneumatics, and hydraulics. How to translate rotational motion into robot action.",
                        "resources": [
                            {"label": "FIRST Robotics – Mechanical Design (free)", "url": "https://docs.wpilib.org/en/stable/"},
                            {"label": "VEX Robotics Engineering Notebooks (free)", "url": "https://www.vexrobotics.com/vexiq/education/iq-curriculum"},
                        ],
                    },
                ],
            },
            {
                "id": "rb_s4",
                "title": "Perception & AI",
                "nodes": [
                    {
                        "id": "rb_perception",
                        "title": "Sensors & Perception",
                        "desc": "LiDAR, cameras (RGB-D), IMU, SLAM (Simultaneous Localization and Mapping). How robots understand their environment.",
                        "resources": [
                            {"label": "Cyrill Stachniss – SLAM Lectures (YouTube, free)", "url": "https://www.youtube.com/@CyrillStachniss"},
                            {"label": "OpenCV Python Tutorials (free)", "url": "https://docs.opencv.org/4.x/d9/df8/tutorial_root.html"},
                        ],
                    },
                    {
                        "id": "rb_planning",
                        "title": "Motion Planning",
                        "desc": "A*, RRT, potential fields, and trajectory optimization. How robots plan safe, collision-free paths through environments.",
                        "resources": [
                            {"label": "MoveIt – ROS Motion Planning (free)", "url": "https://moveit.ros.org/"},
                            {"label": "PythonRobotics – Algorithms Library (free)", "url": "https://github.com/AtsushiSakai/PythonRobotics"},
                        ],
                    },
                ],
            },
            {
                "id": "rb_s5",
                "title": "Projects & Career",
                "nodes": [
                    {
                        "id": "rb_frc",
                        "title": "FIRST Robotics (FRC)",
                        "desc": "The single best thing a high school student can do for a robotics career. Builds teamwork, real engineering, and industry connections.",
                        "resources": [
                            {"label": "FIRST Robotics Competition", "url": "https://www.firstinspires.org/robotics/frc"},
                            {"label": "WPILib Documentation (FRC programming)", "url": "https://docs.wpilib.org/en/stable/"},
                        ],
                    },
                    {
                        "id": "rb_portfolio",
                        "title": "Project Portfolio",
                        "desc": "Build a line-following robot, a robotic arm, and a simulation in Gazebo. Document on GitHub with videos and writeups.",
                        "resources": [
                            {"label": "Gazebo Simulator (free)", "url": "https://gazebosim.org/"},
                            {"label": "Instructables – Robotics Projects", "url": "https://www.instructables.com/circuits/robots/projects/"},
                        ],
                    },
                ],
            },
        ],
    },

    "quantitative_analyst": {
        "title": "Quantitative Analyst",
        "stages": [
            {
                "id": "qa_s1",
                "title": "Math Foundations",
                "nodes": [
                    {
                        "id": "qa_calculus",
                        "title": "Advanced Calculus",
                        "desc": "Multivariable calculus, series, and analysis. Derivatives of complex functions appear constantly in option pricing and optimization.",
                        "resources": [
                            {"label": "MIT OCW – Multivariable Calculus (free)", "url": "https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/"},
                            {"label": "3Blue1Brown – Calculus Series", "url": "https://www.3blue1brown.com/topics/calculus"},
                        ],
                    },
                    {
                        "id": "qa_prob",
                        "title": "Probability Theory",
                        "desc": "Random variables, distributions, expected value, stochastic processes, and Brownian motion. The language of financial modeling.",
                        "resources": [
                            {"label": "MIT OCW – Probability (free)", "url": "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"},
                            {"label": "StatQuest – Probability (YouTube)", "url": "https://www.youtube.com/@statquest"},
                        ],
                    },
                    {
                        "id": "qa_linalg",
                        "title": "Linear Algebra & Optimization",
                        "desc": "Matrix factorization, convex optimization, Lagrange multipliers, and portfolio optimization via quadratic programming.",
                        "resources": [
                            {"label": "3Blue1Brown – Linear Algebra Series", "url": "https://www.3blue1brown.com/topics/linear-algebra"},
                            {"label": "Convex Optimization – Stanford (free)", "url": "https://web.stanford.edu/~boyd/cvxbook/"},
                        ],
                    },
                ],
            },
            {
                "id": "qa_s2",
                "title": "Programming",
                "nodes": [
                    {
                        "id": "qa_python",
                        "title": "Python for Quant Finance",
                        "desc": "NumPy, Pandas, SciPy, and Matplotlib for financial data analysis, backtesting, and statistical modeling.",
                        "resources": [
                            {"label": "Yves Hilpisch – Python for Finance (sample chapters free)", "url": "https://home.tpq.io/books/"},
                            {"label": "QuantLib Python Tutorials", "url": "https://quantlib-python-docs.readthedocs.io/"},
                        ],
                    },
                    {
                        "id": "qa_cpp",
                        "title": "C++ for High-Performance",
                        "desc": "HFT and execution systems are built in C++. Learn STL, templates, and low-latency programming patterns.",
                        "resources": [
                            {"label": "learncpp.com (free, comprehensive)", "url": "https://www.learncpp.com/"},
                            {"label": "Effective Modern C++ (Scott Meyers)", "url": "https://www.amazon.com/Effective-Modern-Specific-Ways-Improve/dp/1491903996"},
                        ],
                    },
                    {
                        "id": "qa_sql",
                        "title": "SQL & Financial Databases",
                        "desc": "Query market data from financial databases. Window functions, time-series aggregation, and OLAP queries are essential.",
                        "resources": [
                            {"label": "Mode SQL Tutorial (free)", "url": "https://mode.com/sql-tutorial/"},
                            {"label": "Quandl / Nasdaq Data Link (free tier)", "url": "https://data.nasdaq.com/"},
                        ],
                    },
                ],
            },
            {
                "id": "qa_s3",
                "title": "Finance Theory",
                "nodes": [
                    {
                        "id": "qa_derivatives",
                        "title": "Derivatives & Options Pricing",
                        "desc": "Black-Scholes model, Greeks (delta, gamma, vega), put-call parity, and Monte Carlo pricing. Core quant interview material.",
                        "resources": [
                            {"label": "Paul Wilmott – Quant Finance (introductory chapters free)", "url": "https://www.wilmott.com/"},
                            {"label": "Khan Academy – Options & Derivatives (free)", "url": "https://www.khanacademy.org/economics-finance-domain/core-finance/derivative-securities"},
                        ],
                    },
                    {
                        "id": "qa_portfolio",
                        "title": "Portfolio Theory",
                        "desc": "Mean-variance optimization, Sharpe ratio, CAPM, factor models (Fama-French), and risk management metrics (VaR, CVaR).",
                        "resources": [
                            {"label": "Yale Financial Markets – Shiller (free on Coursera)", "url": "https://www.coursera.org/learn/financial-markets-global"},
                            {"label": "PyPortfolioOpt – Python Library", "url": "https://pyportfolioopt.readthedocs.io/"},
                        ],
                    },
                    {
                        "id": "qa_fixed_income",
                        "title": "Fixed Income & Macro",
                        "desc": "Bond pricing, duration, convexity, yield curves, and interest rate models (Vasicek, CIR). Essential for rates desks.",
                        "resources": [
                            {"label": "Investopedia – Fixed Income (free)", "url": "https://www.investopedia.com/fixed-income-essentials-4689788"},
                            {"label": "CFA Institute – Fixed Income Basics (free)", "url": "https://www.cfainstitute.org/"},
                        ],
                    },
                ],
            },
            {
                "id": "qa_s4",
                "title": "Quantitative Methods",
                "nodes": [
                    {
                        "id": "qa_timeseries",
                        "title": "Time Series Analysis",
                        "desc": "ARIMA, GARCH, cointegration, and state-space models. Financial data is inherently time-dependent.",
                        "resources": [
                            {"label": "Statsmodels Time Series Tutorial (free)", "url": "https://www.statsmodels.org/stable/tsa.html"},
                            {"label": "Towards Data Science – ARIMA Guide", "url": "https://towardsdatascience.com/"},
                        ],
                    },
                    {
                        "id": "qa_backtesting",
                        "title": "Backtesting Strategies",
                        "desc": "Test trading strategies on historical data. Avoid overfitting, account for transaction costs, and measure risk-adjusted returns.",
                        "resources": [
                            {"label": "Backtrader – Python Backtesting (free)", "url": "https://www.backtrader.com/"},
                            {"label": "QuantConnect – Cloud Backtesting (free)", "url": "https://www.quantconnect.com/"},
                        ],
                    },
                    {
                        "id": "qa_ml_finance",
                        "title": "ML in Finance",
                        "desc": "Alpha generation with ML: NLP on earnings calls, reinforcement learning for execution, and alternative data (satellite, web).",
                        "resources": [
                            {"label": "Advances in Financial Machine Learning – López de Prado", "url": "https://www.amazon.com/Advances-Financial-Machine-Learning-Marcos/dp/1119482089"},
                            {"label": "Alpaca – Free Paper Trading API", "url": "https://alpaca.markets/"},
                        ],
                    },
                ],
            },
            {
                "id": "qa_s5",
                "title": "Career Preparation",
                "nodes": [
                    {
                        "id": "qa_brain_teasers",
                        "title": "Quant Interviews",
                        "desc": "Brain teasers, probability puzzles, option pricing questions, and coding challenges. Jane Street and Citadel interviews are very different from standard SWE interviews.",
                        "resources": [
                            {"label": "A Practical Guide to Quant Finance Interviews (green book)", "url": "https://www.amazon.com/Practical-Guide-Quantitative-Finance-Interviews/dp/1438236662"},
                            {"label": "Heard on the Street (brain teasers)", "url": "https://www.amazon.com/Heard-Street-Quantitative-Questions-Interviews/dp/0994103867"},
                            {"label": "LeetCode – Quant Tags", "url": "https://leetcode.com/problemset/?topicSlugs=math"},
                        ],
                    },
                    {
                        "id": "qa_networking",
                        "title": "Quant Finance Networking",
                        "desc": "Attend Wolfram Quant Finance, QuantMinds, or university quant clubs. Cold-email quant researchers at funds — many respond.",
                        "resources": [
                            {"label": "Quantnet Forum (free)", "url": "https://quantnet.com/"},
                            {"label": "r/quant on Reddit", "url": "https://www.reddit.com/r/quant/"},
                        ],
                    },
                    {
                        "id": "qa_grad",
                        "title": "Graduate Programs",
                        "desc": "Top quant roles require a PhD in math/physics/CS or a Master's in Financial Engineering (MFE). Plan early — admissions are highly competitive.",
                        "resources": [
                            {"label": "Quantnet MFE Rankings", "url": "https://quantnet.com/mfe-programs-rankings/"},
                            {"label": "Cornell MFE Program Info", "url": "https://www.orie.cornell.edu/orie/programs/meng/financial-engineering"},
                        ],
                    },
                ],
            },
        ],
    },
}
