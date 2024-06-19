import streamlit as st
from datetime import date
from src import *
import json
import os

def save_data_exists():
    """Check if there is already save data stored."""
    if not os.path.exists('./execution_data'):
        return False
    if not os.path.isfile('./execution_data/data.json'):
        return False
    return True

def initialize_execution_data():
    """Initialize the execution data."""
    if not os.path.exists('./execution_data'):
        os.mkdir('./execution_data')
    with open('./execution_data/data.json', 'w') as fp:
        json.dump({}, fp)
        
def update_execution_data(data: dict):
    """Update the execution data."""
    with open('./execution_data/data.json', 'w') as fp:
        json.dump(data, fp)

def load_execution_data():
    """Load the execution data."""
    with open('./execution_data/data.json', 'r') as fp:
        return json.load(fp)

def update_personal_info(user_data: dict):
    """Populate the personal information expander with the user's personal information."""
    if 'personal_info' not in user_data:
        user_data['personal_info'] = {}
    
    personal_data_points: dict[str, str] = {
        'name': 'Full Name',
        'street': 'Street',
        'city': 'City',
        'state': 'State',
        'zip_code': 'Zip Code',
        'phone': 'Phone',
        'email': 'Email',
        'linkedin': 'LinkedIn',
        'github': 'GitHub',
        'website': 'Website',
    }
    
    for data, label in personal_data_points.items():
        if data not in user_data['personal_info']:
            user_data['personal_info'][data] = ''
        user_data['personal_info'][data] = st.text_input(label, user_data['personal_info'][data])
    
    if 'summary' not in user_data['personal_info']:
        user_data['personal_info']['summary'] = ''
    user_data['personal_info']['summary'] = st.text_area('Summary', user_data['personal_info']['summary'])
    
    update_execution_data(user_data)
    #json.dump(user_data, open('./execution_data/data.json', 'w'))
    

def update_educational_info(user_data: dict):
    """Populate the educational information expander with the user's educational information."""
    if 'educational_info' not in user_data:
        user_data['educational_info'] = {}
        
    if 'schools' not in user_data['educational_info']:
        user_data['educational_info']['schools'] = []
    
    def add_school():
        """Add a new school to the educational information."""
        user_data['educational_info']['schools'].append({k: '' for k in ['school', 'degree', 'major', 'gpa', 'grad_date']})
        update_execution_data(user_data)
        #json.dump(user_data, open('./execution_data/data.json', 'w'))
        
    def remove_school(index: int) -> None:
        """Remove a school from the educational information."""
        user_data['educational_info']['schools'].pop(index)
        update_execution_data(user_data)
        #json.dump(user_data, open('./execution_data/data.json', 'w'))
    
    for num, school in enumerate(user_data['educational_info']['schools']):
        st.write(f'School {num+1}')
        school['school'] = st.text_input(f'School Name {num+1}', school['school'])
        school['degree'] = st.text_input(f'Degree {num+1}', school['degree'])
        school['major'] = st.text_input(f'Major {num+1}', school['major'])
        school['gpa'] = st.text_input(f'GPA {num+1}', school['gpa'])
        school['grad_date'] = st.text_input(f'Graduation Date {num+1}', school['grad_date'])
        if st.button('Remove', key=f'Remove {num}'):
            remove_school(num)
    
    st.button('Add School', on_click=add_school)

    update_execution_data(user_data)

def update_work_info(user_data: dict):
    """Populate the work experience expander with the user's work experience."""
    if 'work_info' not in user_data:
        user_data['work_info'] = {}
    
    if 'jobs' not in user_data['work_info']:
        user_data['work_info']['jobs'] = []
    
    def add_job():
        """Add a new job to the work experience."""
        user_data['work_info']['jobs'].append({k: '' for k in ['company name', 'company city', 'company state', 'position', 'start_date', 'end_date', 'experience bullets']})
        json.dump(user_data, open('./execution_data/data.json', 'w'))
        
    def remove_job(index: int) -> None:
        """Remove a job from the work experience."""
        user_data['work_info']['jobs'].pop(index)
        json.dump(user_data, open('./execution_data/data.json', 'w'))
        
    for num, job in enumerate(user_data['work_info']['jobs']):
        st.write(f'Job {num+1}')
        job['company name'] = st.text_input(f'Company Name {num+1}', job['company name'])
        job['company city'] = st.text_input(f'Company City {num+1}', job['company city'])
        job['company state'] = st.text_input(f'Company State {num+1}', job['company state'])
        job['position'] = st.text_input(f'Position {num+1}', job['position'])
        job['start_date'] = st.text_input(f'Start Date {num+1}', job['start_date'])
        job['end_date'] = st.text_input(f'End Date {num+1}', job['end_date'])
        job['experience bullets'] = st.text_area(f'Experience Bullets {num+1}', job['experience bullets'])
        if st.button('Remove', key=f'Work Remove {num}'):
            remove_job(num)
    
    st.button('Add Job', on_click=add_job)
    
    update_execution_data(user_data)
    #json.dump(user_data, open('./execution_data/data.json', 'w'))

def update_skills(user_data: dict):
    """Populate the skills expander with the user's skills."""
    if 'skills' not in user_data:
        user_data['skills'] = ''
    user_data['skills'] = st.text_area('Skills', user_data['skills'])
    update_execution_data(user_data)
    
def update_achievements(user_data: dict):
    """Populate the achievements expander with the user's achievements."""
    if 'achievements' not in user_data:
        user_data['achievements'] = ''
    user_data['achievements'] = st.text_area('Achievements', user_data['achievements'])
    update_execution_data(user_data)

def generate_resume_section(user_data: dict):
    st.write('2. Add a job description and click generate to get a targeted resume.')
    with st.expander('Job Description', expanded=True):
        if 'job_description' not in user_data:
            user_data['job_description'] = ''
        user_data['job_description'] = st.text_area('Job Description', user_data['job_description'])
        job_description = user_data['job_description']
    
    def generate_resume():
        master_data: str = format_all_master_data(user_data)
        user_data['target_resume'] = {}
        user_data['target_resume']['summary'] = generate_resume_summary(master_data, job_description)
        update_execution_data(user_data)
        user_data['target_resume']['bullets'] = []
        job_index = 0
        for job in user_data['work_info']['jobs']:
            user_data['target_resume']['bullets'].append(generate_job_bullets(format_job(job), job_description))
            update_execution_data(user_data)
        user_data['target_resume']['skills'] = generate_resume_skills(master_data, job_description)
        update_execution_data(user_data)

    if st.button('Generate Resume'):
        generate_resume()
        
    if 'target_resume' not in user_data:
        return
    
    st.write('3. Your New Target Resume!')
    with st.expander('Target Resume', expanded=True):
        
        personal_info_lines: list[str] = format_personal_info(user_data)
        for line in personal_info_lines:
            st.write(line)
        user_data['target_resume']['summary'] = st.text_area('Summary', user_data['target_resume']['summary'])
        if st.button('Regenerate Summary'):
            user_data['target_resume']['summary'] = generate_resume_summary(format_all_master_data(user_data), job_description)
            update_execution_data(user_data)
        for i, job in enumerate(user_data['work_info']['jobs']):
            job_lines: list[str] = format_job_header(job)
            for line in job_lines:
                st.write(line)
            st.text_area('Bullets', '•\t' + '\n•\t'.join(user_data['target_resume']['bullets'][i]), key=f'Job Bullets {i}')
            if st.button(f'Regenerate Job Bullets', key=f'Regenerate Job Bullets {i}'):
                user_data['target_resume']['bullets'][i] = generate_job_bullets(format_job(job), job_description)
                update_execution_data(user_data)
        user_data['target_resume']['skills'] = st.text_area('Skills', '•\t' + '\n•\t'.join(user_data['target_resume']['skills']))
        if st.button('Regenerate Skills'):
            user_data['target_resume']['skills'] = generate_resume_skills(format_all_master_data(user_data), job_description)        
            update_execution_data(user_data)
    filename = export_to_word('target_resume', user_data)
    with open(filename, 'rb') as file:
        btn = st.download_button(
            label='Download Resume',
            data=file,
            file_name='target_resume.docx',
            mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
    os.remove(filename)    
        
    #if st.button('Export to Word'):
    #    export_to_word('target_resume', user_data)

def display_interface(user_data: dict):
    """Display the user interface."""
    st.set_page_config(page_title="Free Resume GPT", page_icon="💼", layout="wide", initial_sidebar_state="expanded")
    st.title('Resume Builder')
    st.write('Use AI to generate targeted resumes for free! Fill out the form below to get started. If something doesn\'t load properly, press R to refresh the page.')
    st.write('1. Fill out as much as possible from your master resume.')
    with st.expander('Personal Information', expanded=False):
        update_personal_info(user_data)
    if not user_data['personal_info']['name']:
        return
    with st.expander('Educational Experience', expanded=False):
        update_educational_info(user_data)
    if not user_data['educational_info']['schools']:
        return
    with st.expander('Work Experience', expanded=False):
        update_work_info(user_data)
    if not user_data['work_info']['jobs']:
        return
    with st.expander('Skills', expanded=False):
        update_skills(user_data)
    if not user_data['skills']:
        return
    with st.expander('Achievements', expanded=True):
        update_achievements(user_data)
    generate_resume_section(user_data)
    
        
    

class App:
    def __init__(self):
        if not save_data_exists():
            initialize_execution_data()
        self.data = load_execution_data()
        
        display_interface(self.data)
        
if __name__ == '__main__':
    App()