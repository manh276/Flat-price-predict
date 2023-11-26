# Flat-price-predict
Using some ML method to predict Flat price
---
I have created some ML method from sklearn lib to predict Flat sale price.
Data collected from HDB flat resale (Singapore)
---
**To use**:
- run **Flat_Building Model.ipynb** to create and pack the model into pickle file (if you want to deploy on Flask web app)
- **Flat_Preprocessing Data.ipynb** is file processing dataset at **Unprocessed data folder** to others in **Processed data folder**
- I have made a basic web app demo by **Flask**. You must run **Flat_Building Model.ipynb** to pack the model before run **app.py** because
this app uses model packed to deploy.
- I havent optimized paramaters for the models.
- The web display look like this
![Alt text](https://i.ibb.co/Wv6nkfG/flat.png)
**It's just a test so I haven't written a transformation script yet to transform user input on the web app. You can add the transformation script to the completed or typed number instead of string data in the unprocessed dataset ^^.**
