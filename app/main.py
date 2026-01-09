#Import all necessary libraries to create REST API

from fastapi import FastAPI, HTTPException, BackgroundTasks
from schema import StockFields
import joblib, logging

#load the LinearReression Model
linmodel = joblib.load("ebay_stock_linmodel.pkl")

#Log API request information
logging.basicConfig(filename="api.log", level=logging.INFO, format="%(asctime)s - %(message)s")

#Create FASTAPI app
app = FastAPI()

#Define endpoint that accepts post request with input data
@app.post("/predict")


def predict(input_data: StockFields, background_tasks: BackgroundTasks):
    # Use try except blocks to handle errors gracefully
    try:
        data = [[input_data.open, input_data.high,input_data.low,
                          
                          input_data.close, input_data.adj_close, input_data.adj_close]]
        pred = linmodel.predict(data)
        #background task responsible for saving logs
        background_tasks.add_task(log_request, input_data)
        return pred[0]
    except Exception as e:
        logging.exception("Prediction Failed")
        raise HTTPException(status_code=500, detail="Internal error")

#background logging task function
def log_request(data: StockFields):
        logging.info(f"Input: {data.model_dump()}")