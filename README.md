# About Project
This project predicts Ebay stock prices based on historical data. The dataset comprises of stock data fields like
Open
High
Low
Close
Adj_close
Volume

To help in prediction, a Linear Regression machine learning model was used in training. Model performance was evaluated using regression metrics such as the r2_score and MSE score
To evaluate the generalization of the dataset, cross-validation was used and mean score of 6 folds was computed.

### Deployment
The model was deployed as a REST API using FASTAPI and can be accessed on http://localhost:8000/docs. To run the application use uvicorn main:app --reload in the app directory.
### Example Input(JSON)

{
  "open": 1.5,
  "high": 1.7,
  "low": 1,
  "close": 1.6,
  "adj_close": 1.9,
  "volume": 400.5
}
