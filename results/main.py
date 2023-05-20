from fastapi import FastAPI, Query, HTTPException
from jntuh.Executables.jntuhresultscraper import ResultScraper

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Go to http://localhost:8000/docs"}

@app.get('/api/{university}/academicresult')
def academicResult(university: str, htno: str = Query(...)):

    # Check if the university code is 'jntuh'
    if university.lower() == 'jntuh':

        # Check if the hall ticket number is valid
        if len(htno) != 10:
            raise HTTPException(status_code=401, detail="Invalid hall ticket number")
        
        # Create an instance of ResultScraper
        jntuhresult = ResultScraper(htno.upper())
        
        try:
            # Run the scraper and return the result
            result = jntuhresult.run()
            
            # Calculate the total marks and credits
            total = sum(i.get("total", 0) for i in result["Results"].values() if i.get("credits", 0) != 0)
            total_credits = sum(i["credits"] for i in result["Results"].values() if i.get("credits", 0) != 0)

            # Calculate the CGPA if there are non-zero credits
            if total_credits != 0:
                result["CGPA"] =  total / total_credits

            # Return the result
            return result
        except Exception as e:
            # Catch any exceptions raised during scraping
            raise HTTPException(status_code=500, detail=str(e))

