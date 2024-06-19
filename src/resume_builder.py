from src.models.groq_mixtral import GroqMixtral

def generate_resume_summary(work_experiences: str, job_description: str) -> str:
    instructions: str = f'Below is a set of work experiences from a job seeker. Learn the material present and think about the best ways you can best represent the hard work of the applicant. When given a job description, write a one paragraph summary of the applicants work experiences that will wow the reader of their resume. Be formal and descriptive. Use as many keywords from the job description as possible. Write the summary as if you are the applicant, but do not use first person such as "I am" or "I have".\n\nWork Experiences:\n{work_experiences}'
    schema: dict = {'summary': 'summary based on work experiences of applicant'}
    model = GroqMixtral(instructions=instructions, schema=schema)
    summary = model.prompt_model(f'Job Description:\n{job_description}')
    if isinstance(summary, dict):
        return summary['summary'].split('\n')[0]
    return summary.split('\n')[0]


def generate_job_bullets(job_experiences: str, job_description: str) -> list:
    instructions: str = f'Below is a set of job experiences from a job seeker. Learn the material present and think about the best ways you can best represent the hard work of the applicant. When given a job description, write a set of THREE bullet points that summarize the applicants work experiences that will wow the reader of their resume. Be formal and descriptive. EMPHASIZE VALUE DELIVERY AND RESULTS. Use as many keywords from the job description as possible. Write the bullet points as if you are the applicant, but do not use first person such as "I am" or "I have".\n\nJob Experiences:\n{job_experiences}'
    schema: dict = {'bullets': ['bullet point 1', 'bullet point 2', 'bullet point 3']}
    model = GroqMixtral(instructions=instructions, schema=schema)
    bullets = model.prompt_model(f'Job Description:\n{job_description}')
    if isinstance(bullets, dict):
        return bullets['bullets'][:4]
    if isinstance(bullets, list):
        return bullets[:4]
    return bullets.strip().split('\n')[:4]

def generate_resume_skills(work_experiences: str, job_description: str) -> str:
    instructions: str = f'Below is a set of skills from a job seeker. Learn the material present and think about the best ways you can best represent the hard work of the applicant. When given a job description, generate a list of SEVEN skills that accurately reflect the skills and experiences below. Use as many keywords from the job description as possible in the skills bullets. Be extremely brief and concise (12 words or less per bullet). Write the summary as if you are the applicant, but do not use first person such as "I am" or "I have".\n\nSkills:\n{work_experiences}'
    schema: dict = {'skills': ['skill 1', 'skill 2', 'skill 3', 'skill 4', 'skill 5', 'skill 6', 'skill 7']}
    model = GroqMixtral(instructions=instructions, schema=schema)
    skills = model.prompt_model(f'Job Description:\n{job_description}')
    if isinstance(skills, dict):
        return skills['skills'][:7]
    if isinstance(skills, list):
        return skills[:7]
    return skills.split('\n')[:7]

def test():
    work_experiences: str = """
    ●	Analyzed raw, unstructured customer experience survey data and call transcripts with generative AI, python scripts, and SQL queries transforming it into several well-designed dashboards that presented business trends and insights to customers.
    ●	Designed 14 python Jupyter notebooks that analyzed and interpreted large data sets to generate accurate, high-quality reports and data visualizations enabling myself and other teams across the agency to identify trends and insights while conducting faster data analysis.
    ●	Developed and deployed 4 web apps to Amazon Web Services (AWS) S3 buckets that automate time-consuming workflows and ensure data quality and consistency by implementing data validation checks attracting 40 active daily users.
    ●	Regularly provided code review of Jupyter notebooks written by other analysts to improve design, improve documentation, and troubleshoot issues resulting in clean, efficient code. 
    ●	Trained non-technical analysts how to use Jupyter notebooks to automate and improve their workflows which resulted in much wider adoption of my notebooks, saved hundreds of manhours, and enabled new avenues for analysis.
    September 2023 – present
    Data Scientist/Machine Learning Engineer 
    United Natural Foods, Providence, RI
    ●	Independently planned and developed production ready NLP workflow that used open-source sentiment analysis models, NLTK, and cloud hosted generative AI models to transcribe and analyze customer calls which generated over $3 million in value added.
    ●	Designed and maintained python library to simplify accessing all generative AI models via Databricks API and add the ability to easily generate structured python dictionaries from unstructured text data using generative AI models.
    ●	Regularly met with customers, IT, and leadership to gather requirements, develop new functionality, and present findings demonstrating exceptional communication skills when discussing technical concepts with both technical and non-technical audiences. 
    """

    job_description: str = """ About the job
    The Insights, Data Engineering & Analytics Group (IDEAs), is a central data science team for M365 engineering and marketing. As one of the largest data science groups at Microsoft, our team plays a key role in providing data and analytics for M365 and owns the end to end ML and decision sciences charter. By joining our team, you will be at the heart of data, insights, machine learning, AI, and technology, lighting up actionable insights that drive key business decisions for the entire M365 organization.

    Machine Learning Scientist II - Insights, Data Engineering & Analytics Group

    As a Machine Learning Scientist II - Insights, Data Engineering & Analytics Group in the IDEAs Group, you will be bringing relevant data into a central systems to create the single version of truth and perform opportunity analysis and hypothesis generation for stages throughout the end-to-end customer lifecycle. This opportunity will allow you to gain expertise in designing, prototyping, implementing and machine learning approaches, forecasting, causal inference models and also thrive in a team environment that values cross team collaboration and building on the success of others.

    Microsoft’s mission is to empower every person and every organization on the planet to achieve more. As employees we come together with a growth mindset, innovate to empower others, and collaborate to realize our shared goals. Each day we build on our values of respect, integrity, and accountability to create a culture of inclusion where everyone can thrive at work and beyond.

    Responsibilities

        You will build advanced machine learning models (classifiers, reinforcement learning, recommendation engines, causal inference and forecasting) with impact spanning engineering, marketing, and finance. 
        As you identify and explore opportunities for the application of machine learning, AI and predictive analysis, you will partner with teams across product, marketing, sales and engineering teams. 
        You will work with engineers to architect and develop operational models that run at scale. 
        You will communicate with technical and non-technical audiences, and contribute with your modeling expertise as a team player. 
        You will tackle hard problems in innovative ways, drive self-directed initiatives, focusing on delivering the right results. 
        Embody our culture and values .

    Qualifications

    Required Qualifications: 

    Bachelor's Degree in Statistics, Econometrics, Computer Science, Electrical or Computer Engineering, or related field AND 2+ years related experience (e.g., statistics, predictive analytics, research)

        OR Master's Degree in Statistics, Econometrics, Computer Science, Electrical or Computer Engineering, or related field AND 1+ year(s) related experience (e.g., statistics, predictive analytics, research)
        OR Doctorate in Statistics, Econometrics, Computer Science, Electrical or Computer Engineering, or related field
        OR equivalent experience.
        2+ years of experience building advanced machine learning models with impact spanning engineering, marketing, and finance, on areas such as: reinforcement learning, forecasting, Large Language Models (LLM), recommendation engines, causal inference models etc.

    Other Requirements

    Ability to meet Microsoft, customer and/or government security screening requirements are required for this role. These requirements include but are not limited to the following specialized security screenings:

        Microsoft Cloud Background Check: This position will be required to pass the Microsoft Cloud background check upon hire/transfer and every two years thereafter.

    Preferred Qualifications

        2+ years of experience with written and verbal communication to educate and work with cross functional teams. 
        1+ year of experience in delivering on ambiguous projects with incomplete or imperfect data. 
        3+ years of experience with SQL, R, Python to implement statistical models, machine learning, and analysis (Recommenders, Prediction, Classification, Clustering, etc.) in big data environment. 
        Experience on large scale computing systems like COSMOS, Hadoop, MapReduce and/or similar systems. 
        Experience with programming skills, e.g. Java, C#. 
        Familiarity with deep learning toolkits, e.g. CNTK, TensorFlow. 
    """
    print(generate_resume_skills(work_experiences, job_description))
    
    
if __name__ == '__main__':
    test()
    