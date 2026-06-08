from fastapi.testclient import TestClient
from src.main import app
client = TestClient(app)
def test_health():
    r=client.get('/api/health')
    assert r.status_code == 200
    assert r.json()['ok'] is True

def test_resume_analysis():
    payload={'company':'Acme','role':'Developer','resume':'Python FastAPI React automation OCR data projects','job_description':'Need Python FastAPI React SQL automation engineer'}
    data=client.post('/api/analyze', json=payload).json()
    assert data['match_score'] > 20
    assert 'python' in data['matched_keywords']
