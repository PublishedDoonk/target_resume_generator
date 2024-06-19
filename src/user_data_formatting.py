def format_jobs(user_data: dict):
    """Format the user's work experience data into a string."""
    jobs: list = user_data['work_info']['jobs']
    formatted_jobs: str = ''
    for job in jobs:
        formatted_jobs += f"""
        {job['start_date']} - {job['end_date']}
        {job['position']}
        {job['company name']}, {job['company city']}, {job['company state']}
        {job['experience bullets']}
        """
    return formatted_jobs

def format_jobs_and_skills(user_data: dict):
    skills_and_jobs: str = format_jobs(user_data)
    skills_and_jobs += f"""
    Skills:
    {user_data['skills']}
    """
    return skills_and_jobs

def format_all_master_data(user_data: dict):
    """Format all of the user's master data into a string."""
    master_data: str = format_jobs_and_skills(user_data)
    master_data += f"""
    Summary:
    {user_data['personal_info']['summary']}
    """
    
    return master_data

def format_job(job: dict):
    """Format a single job into a string."""
    header: str = '\n'.join(format_job_header(job))
    return f"""
    {header}
    {job['experience bullets']}
    """
    
def format_job_header(job: dict):
    """Format the header of a job into a list of strings."""
    return [
        f"{job['start_date']} - {job['end_date']}",
        job['position'],
        f"{job['company name']}, {job['company city']}, {job['company state']}",
    ]
    
def format_personal_info(user_data: dict) -> list[str]:
    """Format the user's personal information into a list of strings."""
    personal_info = user_data['personal_info']
    lines: list[str] = [
        personal_info['name'],
        personal_info['street'],
        f"{personal_info['city']}, {personal_info['state']} {personal_info['zip_code']}",
        'Phone: ' + personal_info['phone'],
        'Email: ' + personal_info['email'],
        personal_info['linkedin'],
        personal_info['github'],
    ]
    
    return [line for line in lines if line]