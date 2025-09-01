import streamlit as st
import pandas as pd

# -------------------------------
# Demo internship dataset
# -------------------------------
internships = pd.DataFrame([
    {"id": 1, "title": "AI Research Intern", "organization": "XYZ Labs", "location": "Bangalore",
     "eligibility": ["B.Tech", "M.Tech", "B.E.", "MSc"], "minimum_year": 2,
     "skills_required": ["machine learning", "python", "pytorch", "deep learning"],
     "description": "Work on ML models, implement experiments, and analyze results."},
    {"id": 2, "title": "Data Science Intern", "organization": "ABC Analytics", "location": "Remote",
     "eligibility": ["B.Tech", "B.Sc", "M.Sc", "BCA", "MCA"], "minimum_year": 3,
     "skills_required": ["python", "pandas", "statistics", "sql"],
     "description": "Data cleaning, exploratory analysis, and building predictive models."},
    {"id": 3, "title": "Frontend Developer Intern", "organization": "WebWorks", "location": "Delhi",
     "eligibility": ["B.Tech", "B.Des", "BSc"], "minimum_year": 1,
     "skills_required": ["javascript", "react", "html", "css"],
     "description": "Build UI components, collaborate with designers, optimize web performance."},
    {"id": 4, "title": "Product Management Intern", "organization": "FinStart", "location": "Mumbai",
     "eligibility": ["MBA", "BBA", "B.Tech"], "minimum_year": 4,
     "skills_required": ["communication", "product", "roadmap", "analytics"],
     "description": "Assist PM team with user research, roadmaps and KPI analysis."},
    {"id": 5, "title": "Research Intern - Public Policy", "organization": "PolicyNow", "location": "Bangalore",
     "eligibility": ["MA", "MPhil", "BA", "BSc"], "minimum_year": 2,
     "skills_required": ["research", "writing", "statistics"],
     "description": "Support policy research, draft reports, and perform literature reviews."},
    {"id": 6, "title": "Cloud Engineering Intern", "organization": "InfraCore", "location": "Hyderabad",
     "eligibility": ["B.Tech", "M.Tech"], "minimum_year": 3,
     "skills_required": ["aws", "docker", "python", "kubernetes"],
     "description": "Work on deployment, infra automation, and cloud best practices."},
    {
    "id": 7,
    "title": "AI Ethics Intern",
    "organization": "NeuroNet AI",
    "location": "Remote",
    "eligibility": ["B.Tech", "MA", "M.Tech", "BA"],
    "minimum_year": 3,
    "skills_required": ["ethics", "ai", "research", "writing"],
    "description": "Assist in evaluating ethical implications of AI models and drafting policy briefs."
  },
  {
    "id": 8,
    "title": "Backend Developer Intern",
    "organization": "DevStruct",
    "location": "Chennai",
    "eligibility": ["B.Tech", "BCA", "MCA"],
    "minimum_year": 2,
    "skills_required": ["node.js", "mongodb", "express", "api"],
    "description": "Build and maintain backend APIs and integrate third-party services."
  },
  {
    "id": 9,
    "title": "Cybersecurity Intern",
    "organization": "SecuCore",
    "location": "Pune",
    "eligibility": ["B.Tech", "M.Tech", "BSc"],
    "minimum_year": 3,
    "skills_required": ["network security", "linux", "penetration testing"],
    "description": "Conduct security assessments, vulnerability scans, and report findings."
  },
  {
    "id": 10,
    "title": "UX Design Intern",
    "organization": "PixelForge",
    "location": "Remote",
    "eligibility": ["B.Des", "B.Tech", "M.Des"],
    "minimum_year": 2,
    "skills_required": ["figma", "user research", "wireframing", "prototyping"],
    "description": "Work with design teams to create user-friendly interfaces and experiences."
  },
  {
    "id": 11,
    "title": "Marketing Intern",
    "organization": "BrandSphere",
    "location": "Mumbai",
    "eligibility": ["BBA", "MBA", "BA"],
    "minimum_year": 2,
    "skills_required": ["seo", "social media", "content", "analytics"],
    "description": "Create campaigns, analyze metrics, and grow brand presence."
  },
  {
    "id": 12,
    "title": "Android Developer Intern",
    "organization": "AppCrafters",
    "location": "Bangalore",
    "eligibility": ["B.Tech", "MCA", "BSc"],
    "minimum_year": 2,
    "skills_required": ["kotlin", "android studio", "firebase", "ui/ux"],
    "description": "Build Android apps, integrate APIs and handle mobile performance issues."
  },
  {
    "id": 13,
    "title": "Finance Intern",
    "organization": "QuantTrust",
    "location": "Delhi",
    "eligibility": ["B.Com", "MBA", "BBA"],
    "minimum_year": 3,
    "skills_required": ["excel", "financial modeling", "reporting", "accounting"],
    "description": "Support budgeting, forecasting and preparation of financial reports."
  },
  {
    "id": 14,
    "title": "Robotics Intern",
    "organization": "RoboTech Labs",
    "location": "Hyderabad",
    "eligibility": ["B.Tech", "M.Tech"],
    "minimum_year": 2,
    "skills_required": ["robotics", "arduino", "c++", "embedded systems"],
    "description": "Build robotic prototypes and assist in automation research."
  },
  {
    "id": 15,
    "title": "Full Stack Developer Intern",
    "organization": "StackBase",
    "location": "Remote",
    "eligibility": ["B.Tech", "BCA", "MCA"],
    "minimum_year": 3,
    "skills_required": ["react", "node.js", "sql", "git"],
    "description": "Develop full-stack applications and deploy web services."
  },
  {
    "id": 16,
    "title": "Operations Intern",
    "organization": "LogiChain",
    "location": "Mumbai",
    "eligibility": ["BBA", "MBA"],
    "minimum_year": 3,
    "skills_required": ["excel", "logistics", "coordination", "supply chain"],
    "description": "Handle day-to-day operations, vendor coordination and logistics support."
  },
  {
    "id": 17,
    "title": "Blockchain Intern",
    "organization": "BlockNova",
    "location": "Bangalore",
    "eligibility": ["B.Tech", "M.Tech"],
    "minimum_year": 3,
    "skills_required": ["solidity", "ethereum", "web3", "smart contracts"],
    "description": "Develop smart contracts, test DApps and contribute to blockchain projects."
  },
  {
    "id": 18,
    "title": "Data Annotation Intern",
    "organization": "DataSage AI",
    "location": "Remote",
    "eligibility": ["BSc", "BA", "BCA"],
    "minimum_year": 1,
    "skills_required": ["attention to detail", "labeling", "excel"],
    "description": "Label datasets for AI models and assist with annotation quality control."
  },
  {
    "id": 19,
    "title": "Technical Writing Intern",
    "organization": "DocuSoft",
    "location": "Chennai",
    "eligibility": ["BA", "MA", "B.Tech"],
    "minimum_year": 2,
    "skills_required": ["writing", "documentation", "api", "markdown"],
    "description": "Create technical documents, manuals and product guides."
  },
  {
    "id": 20,
    "title": "DevOps Intern",
    "organization": "DeployHQ",
    "location": "Pune",
    "eligibility": ["B.Tech", "M.Tech"],
    "minimum_year": 3,
    "skills_required": ["jenkins", "docker", "kubernetes", "linux"],
    "description": "Support CI/CD pipelines, infrastructure as code, and system monitoring."
  },
  {
    "id": 21,
    "title": "Graphic Design Intern",
    "organization": "CreativeNest",
    "location": "Delhi",
    "eligibility": ["B.Des", "BA", "BFA"],
    "minimum_year": 2,
    "skills_required": ["photoshop", "illustrator", "canva", "creativity"],
    "description": "Design visuals for marketing, branding, and digital campaigns."
  },
  {
    "id": 22,
    "title": "Legal Intern",
    "organization": "LexRight",
    "location": "Mumbai",
    "eligibility": ["LLB", "BA LLB"],
    "minimum_year": 4,
    "skills_required": ["legal research", "drafting", "contracts"],
    "description": "Assist legal team with documentation, research and case studies."
  },
  {
    "id": 23,
    "title": "Business Analyst Intern",
    "organization": "BizMetrics",
    "location": "Bangalore",
    "eligibility": ["B.Tech", "MBA", "BBA"],
    "minimum_year": 3,
    "skills_required": ["excel", "sql", "power bi", "analysis"],
    "description": "Analyze business trends, prepare dashboards and suggest improvements."
  },
  {
    "id": 24,
    "title": "Content Writing Intern",
    "organization": "StoryBuzz",
    "location": "Remote",
    "eligibility": ["BA", "MA", "BBA"],
    "minimum_year": 1,
    "skills_required": ["writing", "seo", "research", "grammar"],
    "description": "Write blog articles, website content, and assist content team."
  },
  {
    "id": 25,
    "title": "Biotech Research Intern",
    "organization": "GeneCore",
    "location": "Hyderabad",
    "eligibility": ["BSc", "MSc", "B.Tech"],
    "minimum_year": 3,
    "skills_required": ["lab techniques", "biology", "reporting"],
    "description": "Support ongoing research in genomics and molecular biology."
  },
  {
    "id": 26,
    "title": "Sales Intern",
    "organization": "QuickReach",
    "location": "Chennai",
    "eligibility": ["BBA", "MBA"],
    "minimum_year": 2,
    "skills_required": ["sales", "communication", "crm", "presentation"],
    "description": "Assist sales team in lead generation, client meetings, and CRM updates."
  },
  
  {
    "id": 27,
    "title": "HR Intern",
    "organization": "PeopleFirst",
    "location": "Mumbai",
    "eligibility": ["BBA", "MBA", "BA"],
    "minimum_year": 2,
    "skills_required": ["recruitment", "communication", "excel", "hr operations"],
    "description": "Assist with hiring, onboarding, and HR documentation processes."
  },
  {
    "id": 28,
    "title": "Public Relations Intern",
    "organization": "PRSpark",
    "location": "Delhi",
    "eligibility": ["BA", "MA", "BBA"],
    "minimum_year": 2,
    "skills_required": ["media", "communication", "press releases", "writing"],
    "description": "Support PR campaigns, draft press releases, and engage with media."
  },
  {
    "id": 29,
    "title": "Content Writing Intern",
    "organization": "WriteWise",
    "location": "Remote",
    "eligibility": ["BA", "MA", "BBA"],
    "minimum_year": 1,
    "skills_required": ["writing", "grammar", "seo", "editing"],
    "description": "Create and edit articles, blogs, and website content."
  },
  {
    "id": 30,
    "title": "Digital Marketing Intern",
    "organization": "SocialBoost",
    "location": "Bangalore",
    "eligibility": ["BBA", "BA", "MBA"],
    "minimum_year": 2,
    "skills_required": ["social media", "seo", "analytics", "campaigns"],
    "description": "Manage social platforms, run campaigns, and analyze performance."
  },
  {
    "id": 31,
    "title": "Psychology Research Intern",
    "organization": "MindMap",
    "location": "Remote",
    "eligibility": ["BA", "MA", "MSc"],
    "minimum_year": 2,
    "skills_required": ["research", "psychology", "report writing"],
    "description": "Assist with literature reviews, surveys, and psychological studies."
  },
  {
    "id": 32,
    "title": "Journalism Intern",
    "organization": "NewsNow",
    "location": "Delhi",
    "eligibility": ["BA", "MA"],
    "minimum_year": 2,
    "skills_required": ["reporting", "writing", "interviewing", "editing"],
    "description": "Cover news events, write articles, and conduct interviews."
  },
  {
    "id": 33,
    "title": "Event Management Intern",
    "organization": "Eventia",
    "location": "Mumbai",
    "eligibility": ["BBA", "BA", "MBA"],
    "minimum_year": 2,
    "skills_required": ["coordination", "planning", "communication", "logistics"],
    "description": "Help plan and execute corporate and social events."
  },
  {
    "id": 34,
    "title": "NGO Management Intern",
    "organization": "Helping Hands",
    "location": "Remote",
    "eligibility": ["BA", "MA", "BBA"],
    "minimum_year": 1,
    "skills_required": ["community work", "writing", "coordination"],
    "description": "Support NGO operations, outreach activities and reporting."
  },
  {
    "id": 35,
    "title": "Graphic Design Intern",
    "organization": "DesignFlow",
    "location": "Remote",
    "eligibility": ["BA", "B.Des", "BFA"],
    "minimum_year": 1,
    "skills_required": ["photoshop", "canva", "creativity", "illustrator"],
    "description": "Design creatives for marketing and social media."
  },
  {
    "id": 36,
    "title": "Legal Intern",
    "organization": "JurisLaw",
    "location": "Chennai",
    "eligibility": ["LLB", "BA LLB"],
    "minimum_year": 3,
    "skills_required": ["legal research", "drafting", "contracts"],
    "description": "Assist with legal drafting, case research, and compliance work."
  },
  {
    "id": 37,
    "title": "Market Research Intern",
    "organization": "MarketGaze",
    "location": "Remote",
    "eligibility": ["BBA", "MBA", "BA"],
    "minimum_year": 2,
    "skills_required": ["research", "survey", "reporting", "analysis"],
    "description": "Conduct surveys and analyze market trends and data."
  },
  {
    "id": 38,
    "title": "Teaching Intern",
    "organization": "EduSpark Academy",
    "location": "Kolkata",
    "eligibility": ["BA", "B.Ed", "MA"],
    "minimum_year": 2,
    "skills_required": ["teaching", "communication", "lesson planning"],
    "description": "Assist teachers with academic delivery and student engagement."
  },
  {
    "id": 39,
    "title": "Film Production Intern",
    "organization": "CineCraft",
    "location": "Mumbai",
    "eligibility": ["BA", "BFA", "BMM"],
    "minimum_year": 2,
    "skills_required": ["editing", "shooting", "script", "coordination"],
    "description": "Support video shoots, scriptwriting, and post-production editing."
  },
  {
    "id": 40,
    "title": "Public Policy Intern",
    "organization": "CivicPulse",
    "location": "Delhi",
    "eligibility": ["BA", "MA", "MPhil"],
    "minimum_year": 3,
    "skills_required": ["policy analysis", "writing", "research", "statistics"],
    "description": "Support policy evaluations, stakeholder research and report writing."
  },
  {
    "id": 41,
    "title": "Advertising Intern",
    "organization": "AdMaze",
    "location": "Bangalore",
    "eligibility": ["BA", "BBA", "MBA"],
    "minimum_year": 2,
    "skills_required": ["copywriting", "branding", "creativity", "campaigns"],
    "description": "Assist with ad creation, copywriting, and campaign planning."
  },
  {
    "id": 42,
    "title": "Finance Intern",
    "organization": "ValueEdge",
    "location": "Hyderabad",
    "eligibility": ["B.Com", "MBA", "BBA"],
    "minimum_year": 2,
    "skills_required": ["excel", "financial reporting", "budgeting"],
    "description": "Work on financial data, budget tracking and reporting."
  },
  {
    "id": 43,
    "title": "Sociology Research Intern",
    "organization": "SocialSphere",
    "location": "Remote",
    "eligibility": ["BA", "MA", "MPhil"],
    "minimum_year": 2,
    "skills_required": ["qualitative research", "surveys", "report writing"],
    "description": "Support social research projects, conduct interviews and draft reports."
  },
  {
    "id": 44,
    "title": "Copywriting Intern",
    "organization": "WriteCraft",
    "location": "Remote",
    "eligibility": ["BA", "MA", "BMM"],
    "minimum_year": 2,
    "skills_required": ["copywriting", "creative writing", "editing"],
    "description": "Write ad copies, slogans, and branding content."
  },
  {
    "id": 45,
    "title": "Customer Relations Intern",
    "organization": "ClientConnect",
    "location": "Delhi",
    "eligibility": ["BBA", "BA"],
    "minimum_year": 2,
    "skills_required": ["communication", "crm", "problem solving"],
    "description": "Manage customer queries, feedback and support CRM processes."
  },
  {
    "id": 46,
    "title": "Fashion Design Intern",
    "organization": "StyleNest",
    "location": "Mumbai",
    "eligibility": ["B.Des", "BFA"],
    "minimum_year": 2,
    "skills_required": ["fashion ske                                                                        tching", "trends", "styling"],
    "description": "Assist with design conceptualization, fashion shoots and styling."
  }
  ,
  {
    "id": 51,
    "title": "Investment Research Intern",
    "organization": "FinEdge Capital",
    "location": "Mumbai",
    "eligibility": ["MBA", "B.Com", "BBA"],
    "minimum_year": 3,
    "skills_required": ["financial analysis", "excel", "report writing", "research"],
    "description": "Conduct equity and sector research, assist in investment reports."
  },
  {
    "id": 52,
    "title": "AI Product Intern",
    "organization": "NeuraAI",
    "location": "Bangalore",
    "eligibility": ["B.Tech", "MBA", "M.Tech"],
    "minimum_year": 3,
    "skills_required": ["machine learning", "product", "communication", "user testing"],
    "description": "Support product lifecycle of AI tools with research and testing."
  },
  {
    "id": 53,
    "title": "SEO Intern",
    "organization": "GrowthFuel",
    "location": "Remote",
    "eligibility": ["BBA", "BA", "MBA"],
    "minimum_year": 2,
    "skills_required": ["seo", "google analytics", "keyword research", "content"],
    "description": "Optimize website pages, track SEO metrics, assist in link building."
  },
  {
    "id": 54,
    "title": "Legal Policy Intern",
    "organization": "JusticePoint",
    "location": "Delhi",
    "eligibility": ["LLB", "BA LLB", "MA"],
    "minimum_year": 3,
    "skills_required": ["legal writing", "policy", "research", "drafting"],
    "description": "Research legal policies and assist in public interest documentation."
  },
  {
    "id": 55,
    "title": "Corporate Communications Intern",
    "organization": "Veritas Corp",
    "location": "Chennai",
    "eligibility": ["BA", "MA", "MBA"],
    "minimum_year": 2,
    "skills_required": ["writing", "pr", "presentation", "branding"],
    "description": "Assist in internal and external corporate messaging."
  },
  {
    "id": 56,
    "title": "Machine Learning Intern",
    "organization": "MLHub",
    "location": "Remote",
    "eligibility": ["B.Tech", "M.Tech", "MSc"],
    "minimum_year": 3,
    "skills_required": ["scikit-learn", "python", "ml algorithms", "data preprocessing"],
    "description": "Build and evaluate ML models using structured datasets."
  },
  {
    "id": 57,
    "title": "UI/UX Research Intern",
    "organization": "DesignPixel",
    "location": "Hyderabad",
    "eligibility": ["B.Des", "B.Tech", "BFA"],
    "minimum_year": 2,
    "skills_required": ["user testing", "figma", "interviews", "research"],
    "description": "Conduct user studies and support UX designers with feedback loops."
  },
  {
    "id": 58,
    "title": "Journalism Intern",
    "organization": "VoiceWire",
    "location": "Delhi",
    "eligibility": ["BA", "MA", "BMM"],
    "minimum_year": 2,
    "skills_required": ["news writing", "editing", "interviews", "fact-checking"],
    "description": "Cover stories, conduct interviews, and edit news content."
  },
  {
    "id": 59,
    "title": "Cloud Security Intern",
    "organization": "SecureStack",
    "location": "Pune",
    "eligibility": ["B.Tech", "M.Tech"],
    "minimum_year": 3,
    "skills_required": ["aws", "cloud security", "network", "linux"],
    "description": "Assist with securing cloud environments and auditing configurations."
  },
  {
    "id": 60,
    "title": "Sustainability Intern",
    "organization": "GreenLeap",
    "location": "Bangalore",
    "eligibility": ["BA", "MA", "BSc"],
    "minimum_year": 2,
    "skills_required": ["research", "sustainability", "reporting"],
    "description": "Research sustainability initiatives and support CSR reporting."
  },
  {
    "id": 61,
    "title": "EdTech Operations Intern",
    "organization": "LearnSphere",
    "location": "Remote",
    "eligibility": ["BBA", "BA", "MBA"],
    "minimum_year": 2,
    "skills_required": ["excel", "coordination", "email communication"],
    "description": "Support day-to-day operations of EdTech courses and student management."
  },
  {
    "id": 62,
    "title": "E-commerce Intern",
    "organization": "ShopWiz",
    "location": "Mumbai",
    "eligibility": ["BBA", "B.Com", "MBA"],
    "minimum_year": 2,
    "skills_required": ["amazon seller central", "cataloging", "pricing", "excel"],
    "description": "Manage product listings and assist in e-commerce analytics."
  },
  {
    "id": 63,
    "title": "Speech and NLP Intern",
    "organization": "LinguaAI",
    "location": "Bangalore",
    "eligibility": ["B.Tech", "M.Tech", "MSc"],
    "minimum_year": 3,
    "skills_required": ["nlp", "python", "spacy", "text processing"],
    "description": "Work on NLP datasets and develop text classification models."
  },
  {
    "id": 64,
    "title": "Illustration Intern",
    "organization": "DoodleDesk",
    "location": "Remote",
    "eligibility": ["BFA", "B.Des"],
    "minimum_year": 2,
    "skills_required": ["illustrator", "procreate", "creativity", "digital art"],
    "description": "Create digital illustrations for products, websites, and campaigns."
  },
  {
    "id": 65,
    "title": "Insurance Analytics Intern",
    "organization": "Insurelytics",
    "location": "Delhi",
    "eligibility": ["B.Tech", "B.Com", "MBA"],
    "minimum_year": 3,
    "skills_required": ["excel", "claims analysis", "risk", "data entry"],
    "description": "Analyze insurance data and help streamline risk reporting processes."
  },
  {
    "id": 66,
    "title": "Art Curation Intern",
    "organization": "GalleryNova",
    "location": "Kolkata",
    "eligibility": ["BA", "MA", "BFA"],
    "minimum_year": 2,
    "skills_required": ["art history", "curation", "writing", "research"],
    "description": "Assist with art selection, cataloging, and event preparation."
  },
  {
    "id": 67,
    "title": "HR Analytics Intern",
    "organization": "TalentIQ",
    "location": "Bangalore",
    "eligibility": ["MBA", "BBA", "B.Com"],
    "minimum_year": 3,
    "skills_required": ["excel", "power bi", "data analysis", "hr data"],
    "description": "Support HR metrics reporting, dashboards, and performance analysis."
  },
  {
    "id": 68,
    "title": "Brand Strategy Intern",
    "organization": "BrandMint",
    "location": "Mumbai",
    "eligibility": ["MBA", "BBA", "BA"],
    "minimum_year": 3,
    "skills_required": ["branding", "marketing", "creativity", "communication"],
    "description": "Work on brand research, identity building and storytelling strategies."
  },
  {
    "id": 69,
    "title": "Data Journalism Intern",
    "organization": "DataScope Media",
    "location": "Remote",
    "eligibility": ["BA", "MA", "BSc"],
    "minimum_year": 3,
    "skills_required": ["data visualization", "storytelling", "journalism", "excel"],
    "description": "Create data-backed stories and visual content for digital publications."
  },
  {
    "id": 70,
    "title": "CSR Intern",
    "organization": "ImpactBridge",
    "location": "Chennai",
    "eligibility": ["BA", "MA", "MBA"],
    "minimum_year": 2,
    "skills_required": ["csr", "reporting", "impact assessment", "documentation"],
    "description": "Support corporate social responsibility initiatives and stakeholder outreach."
  }
])

# -------------------------------
# Text processing + similarity
# -------------------------------
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    use_sklearn = True
except:
    use_sklearn = False

def make_internship_text(row):
    return " ".join([row["title"], row["organization"],
                     " ".join(row["skills_required"]), row["description"]]).lower()

internships["text"] = internships.apply(make_internship_text, axis=1)

tfidf_vectorizer, tfidf_matrix = None, None
if use_sklearn:
    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf_vectorizer.fit_transform(internships["text"].tolist())

def jaccard_similarity(a, b):
    aset, bset = set(a.split()), set(b.split())
    return len(aset & bset) / len(aset | bset) if aset and bset else 0.0

def compute_similarity(text, idx):
    if use_sklearn:
        vec = tfidf_vectorizer.transform([text])
        return cosine_similarity(vec, tfidf_matrix[idx])[0][0]
    return jaccard_similarity(text, internships.loc[idx, "text"])

def recommend(candidate, top_n=3):
    cand_text = " ".join([candidate["degree"]] + candidate["skills"] + candidate["interests"]).lower()
    results = []
    for idx, row in internships.iterrows():
        score = compute_similarity(cand_text, idx)
        results.append({
            "title": row["title"],
            "organization": row["organization"],
            "location": row["location"],
            "score": round(score, 3),
            "description": row["description"]
        })
    return pd.DataFrame(results).sort_values("score", ascending=False).head(top_n)

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Internship Recommender", page_icon="🎯", layout="wide")

st.title("🎯 Internship Recommender System")
st.markdown("Find the **best internships** based on your profile, skills, and interests 🚀")

# Input form
st.header("👤 Candidate Profile")
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Your Name")
    degree = st.selectbox("Degree", [
        "BA","BA LLB","BBA","BCA","B.Com","B.Des","B.E.","B.Ed","BFA","BMM","BSc","B.Tech",
        "History","LLB","MA","MBA","MCA","MPhil","MSc","M.Tech","Anthropology"
    ])
    year = st.number_input("Year of Study", min_value=1, max_value=5, step=1)

with col2:
    skills = st.text_area("Your Skills (comma separated)", "python, statistics, machine learning")
    interests = st.text_area("Your Interests (comma separated)", "data science, AI")
    location = st.text_input("Preferred Location(s) (comma separated)", "Bangalore, Remote")

# Button action
if st.button("✨ Get Recommendations", use_container_width=True):
    candidate = {
        "name": name,
        "degree": degree,
        "year": year,
        "skills": [s.strip() for s in skills.split(",") if s.strip()],
        "interests": [i.strip() for i in interests.split(",") if i.strip()],
        "location_preferences": [l.strip() for l in location.split(",") if l.strip()]
    }
    
    recs = recommend(candidate, top_n=3)
    st.subheader(f"📌 Top Recommendations for {candidate['name'] or 'you'}:")

    # Display recommendations as nice cards
    for _, r in recs.iterrows():
        with st.container():
            st.markdown(
                f"""
                <div style="padding:15px; border-radius:12px; 
                            background-color:#f9f9f9; margin-bottom:15px;
                            border:1px solid #ddd; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                    <h4 style="margin-bottom:5px;">🎓 {r['title']}</h4>
                    <p style="margin:0;"><b>Organization:</b> {r['organization']}</p>
                    <p style="margin:0;"><b>Location:</b> {r['location']}</p>
                    <p style="margin:0; color:#666;"><b>Match Score:</b> {r['score']}</p>
                    <hr style="margin:8px 0;">
                    <p style="margin:0;">{r['description']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
