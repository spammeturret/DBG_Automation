# define Python user-defined exceptions
class error(Exception):
   """Base class for other exceptions"""
   pass

class ad_refresh_error(error):
   """Having trouble refreshing Ads"""
   pass

class daily_reward_error(error):
   """Having trouble claiming daily reward popup"""
   pass



var = "C:\\project\\DBG_Automation\\img\\daily\\checkInClaim.PNG"
var.split('\\')[-1]