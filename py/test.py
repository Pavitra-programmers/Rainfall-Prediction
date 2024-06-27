import pickle

pick_out = open(r'C:\Users\dines\OneDrive\Desktop\Github\Rainfall-Prediction\RFCrainfallmodel.sav','rb')
data = pickle.load(pick_out)
pick_out.close()

# res = data.predict(x_test)
# print(accuracy_score(y_test,res))

     
#  1   Location       
#  2   MinTemp        
#  3   MaxTemp        
#  4   Rainfall       
#  7   WindGustDir    
#  8   WindGustSpeed  
#  9   WindDir9am     
#  10  WindDir3pm     
#  11  WindSpeed9am   
#  12  WindSpeed3pm   
#  13  Humidity9am    
#  14  Humidity3pm    
#  15  Pressure9am    
#  16  Pressure3pm    
#  17  Cloud9am       
#  18  Cloud3pm       
#  19  Temp9am        
#  20  Temp3pm        
#  21  RainToday      
#  22  RISK_MM        
#  23  RainTomorrow   