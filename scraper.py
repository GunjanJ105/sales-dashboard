import requests
from bs4 import BeautifulSoup

def get_jobs(keyword="python"):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    jobs = []
    rows = soup.find_all("tr", class_="job")[:10]  # top 10 jobs
    
    for row in rows:
        try:
            title = row.find("h2").text.strip()
            company = row.find("h3").text.strip()
            tags = [t.text.strip() for t in row.find_all("div", class_="tag")]
            link = "https://remoteok.com" + row.get("data-url", "")
            
            jobs.append({
                "Title": title,
                "Company": company,
                "Tags": ", ".join(tags[:3]),
                "Link": link
            })
        except:
            continue
    
    return jobs