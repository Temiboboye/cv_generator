import anthropic
from config import Config

client = anthropic.Anthropic(api_key=Config.ANTHROPIC_API_KEY)

def generate_cvs(job_description, candidate_info):
    prompt = f"""
You are an expert CV writer and career coach. Your task is to create multiple unique and tailored CVs based on a given job description and a candidate's basic information. Each CV should be optimized to pass Applicant Tracking Systems (ATS) while highlighting the most relevant skills and experiences for the position.

Job Description:
{job_description}

Candidate's Basic Information:
{candidate_info}

Instructions:
1. Analyze the job description thoroughly, identifying key requirements, skills, and qualifications.
2. Create 3 distinct CV versions, each with a different focus or style, but all tailored to the job description.
3. For each CV:
   a. Create a compelling professional summary
   b. Highlight relevant skills and experiences
   c. Use industry-specific keywords from the job description
   d. Ensure the format is ATS-friendly
   e. Tailor the work experience section to emphasize relevant achievements
   f. Include appropriate sections such as Skills, Education, Certifications, etc.
4. Each CV should be unique in its presentation and focus, while still accurately representing the candidate's qualifications.
5. After each CV, provide a brief explanation of its focus and how it differs from the others.

Please generate these 3 CVs now, formatted clearly and ready for use.
"""

    response = client.completions.create(
        model="claude-2",
        prompt=f"{anthropic.HUMAN_PROMPT} {prompt}{anthropic.AI_PROMPT}",
        max_tokens_to_sample=3000,
        temperature=0.7,
    )

    return response.completion