### Binary Modeling for Petrophysical Sonic Well Logs (DTC-DTS) Analysis and Prediction using Machine Learning

Sonic well logs are vital in petroleum engineering, providing insights into subsurface formations, porosity, fluid types, and lithology. They ensure wellbore stability, guide drilling decisions like overpressure zone, aid geosteering, and characterize natural fractures. Moreover, they assist in seismic calibration, enhancing subsurface understanding for efficient hydrocarbon recovery.

This project utilizes the petrolib package to analyze and predict subsurface properties in the Volve field using well logs. The well data is loaded from LAS files and processed using Pandas and NumPy. The package also provides visualization capabilities for well log analysis.

The project uses Petrolib to seamlessly load well data from LAS files into Pandas DataFrames for analysis. Seven wells from the Volve field are utilized, each containing DT/DTC (compression: p-waves) and DTS (stress: s-waves) logs.

The dataset contains well logs for various petrophysical properties, including gamma ray (GR), resistivity (RT), compressional sonic (DT/DTC), bulk density (RHOB), neutron porosity index (NPHI), and shear sonic (DTS) logs. The goal is to build a machine learning model capable of accurately predicting DT/DTC and DTS logs.

Data preparation involves filtering well logs based on depth, addressing missing values, and handling outliers. The well logs are standardized and transformed to ensure robust and accurate predictions.

The machine learning model used is an ExtraTreesRegressor ensemble, which is known for its robustness in handling complex geological patterns. Hyperparameter optimization is performed using Optuna to improve model performance.
The model's performance is evaluated using R^2 score, mean squared error, root mean squared error, and mean absolute error metrics. The model achieves an impressive accuracy of 92.2%.

The predicted well logs values are compared with the true values, and visual plots are generated using petrolib package to analyze the model's performance in predicting both compressional (DTC) and shear (DTS) sonic logs.
