# Flat-price-predict
Using some ML method to predict Flat price
---
I have created some ML method from sklearn lib to predict Flat sale price.
---
**To use**:
- run **Flat_Building Model.ipynb** to create and pack model into pickle file (if you want to deploy on Flask web app)
- **Flat_Preprocessing Data.ipynb** is file processing dataset at **Unprocessed data folder** to others in **Processed data folder**
- I have made a basic web app demo by **Flask**. You must run **Flat_Building Model.ipynb** to pack model before run **app.py** because
this app uses model packed to deploy.
