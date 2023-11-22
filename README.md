# LLM Deployment on AWS
## AWS Sagemaker:
	* Open the AWS console and select region.
	* Search with Sagemaker and open it.
	* Got to Notebooks and click on notebook instances.
	* Make necessary settings and then create a notebook instance.
	* Go to Huggingface models, select model which we want to deploy.
	* After instance created, open jupyter lab and select conda_pytorch_p310.
	* Write a required code(Notebook Avaialable on Github).
	* Go to inference->Endpoints = You can see model endpoint
	* Again go to call the endpoint and wriet the code for that.
	* These are the steps to deploy the LLM and access endpoint in sagemaker.

## Lambda:
	* It is serverless compute service and it helps to trigger events.
	* Go to console page and then click on Lambda.
	* In that page click on create a function.
	* After filling up basic deatils, click on create function. You can see generate function overview
	* click on add trigger
	* Now we can write code.
	* To test the code before deployement, we need to create event. In this we need to write evenjson and click on format json. And then click on test
	* back to code and click on deploy. after deploy click on test. we might face error.
	* The error due to the task time out need to be increased. Go to Configuration->edit->change time to max. And then click on test.
	* Now the time to create function URL to access the API endpoint.
	* Go to configuration->Function URL-> create a function URL
	* Once the function URL created, we can access that endpiont on the webpage.

## References:
YouTube Link: https://youtu.be/A9Pu4xg-Nas?si=WZJ-i5JLFeFE4c9a
