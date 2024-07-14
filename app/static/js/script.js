document.addEventListener('DOMContentLoaded', (event) => {
    const form = document.getElementById('cv-form');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    const cvContent = document.getElementById('cv-content');
    const downloadBtn = document.getElementById('download-btn');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(form);
        
        loading.style.display = 'block';
        form.style.display = 'none';
        
        try {
            const response = await fetch('/', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            
            if (data.error) {
                throw new Error(data.error);
            }
            
            cvContent.textContent = data.cvs;
            results.style.display = 'block';
        } catch (error) {
            alert('Error: ' + error.message);
        } finally {
            loading.style.display = 'none';
            form.style.display = 'block';
        }
    });

    downloadBtn.addEventListener('click', async () => {
        const response = await fetch('/download', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ cvs: cvContent.textContent }),
        });
        
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = 'generated_cvs.txt';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
    });
});