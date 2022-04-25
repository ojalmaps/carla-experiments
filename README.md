
## CARLA
We modified internal_factors_default.yaml, __init__.py, SpeedModel.py, and SpeedModelFactory.py. We created a new speed model named jojoSpeedModel.py. To map relaxation time, we created a new variable into SpeedMode.py. 

To run the final simulation, the command is

    python r1v1m2-default.py

To create multiple simulations, include --max_tricks=n, n being the amount of simulations you would want to run. 

>  What changes can you observe in the simulation if the relaxation time is changed? Describe the effects of having a long relaxation time which are not easily observable?

 When the relaxation time increased (from 1 to 10), there was no visible change since the pedestrian would finish crossing the street before it could accelerate to the desired speed. When we decreased the relaxation time (from 1 to 0.1), we could see the pedestrian speed change quickly as the time to accelerate to desired speed decreased, hence the pedestrian reached the desired speed faster.

> Define and use your speed model. Submit the link to the  **github repository**. For example, you can return the desired speed from a uniform distribution of [1,2] instead of a constant value. You might also consider using one of the speed models from this week’s readings and invent a new one.

Our speed model was based off of the data “Observational-based study to explore pedestrian crossing behaviors at signalized and unsignalized crosswalks” where these properties were set
	
	1.  Relaxation time: 2
	    
	2.  Desired speed: 1.6
	    
	3.  Minimum crossing speed: 0
	    
	4.  Maximum crossing speed: 1.8

 > How is your speed model different from the StaticSpeedModel? Could you detect any changes visually? If not, why?
	 The different between static and joj speed model would be the desired, maximum and minmum speed. We kept the relaxation time the same since we are creating an average human speed base on the second paper we read. From the simulations we ran, our model was able to avoid cars when pedestrian gets really close while the static model vehicles tend to hit the pedestrian more.

 Since our pedestrian speed was faster than the static model, pedestrians could react faster and dodge the vehicle if they were too close while the static model had the pedestrian continue its path after the pedestrian was hit by the vehicle. We also played around and created multiple speed model versions. We created "hulk" speed model which was much faster desired speed along with max speed of 10 while minimum speed was 5. 

## Paper Questions
[Full Document](https://docs.google.com/document/d/1TYOvt4xHG5Fh4g82-UGlUd42quBzFpqwB9F470_xhc0/edit)
