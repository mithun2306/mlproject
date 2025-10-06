# Deployment to Render

## Prerequisites
- GitHub account
- Render account (sign up at render.com)

## Steps
1. Commit and push code to GitHub
   - Ensure artifacts/ folder is committed (models and preprocessor)
   - Push all changes to a GitHub repository

2. Connect to Render
   - Go to render.com and sign in
   - Click "New" > "Web Service"
   - Connect your GitHub repository

3. Configure the service
   - Name: Choose a name for your app
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn application:application`
   - Plan: Free

4. Deploy
   - Click "Create Web Service"
   - Render will build and deploy your app
   - Once deployed, you'll get a URL like https://your-app-name.onrender.com

## Testing
- Visit the deployed URL
- Test the prediction form
