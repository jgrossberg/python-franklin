# Franklin Real Estate Copy Writer

This is an app built to take in property information and call ChatGPT for an MLS-style property description. The app is built with Flask and uses the ChatGPT python sdk for api calls. Can be viewed in production at: [url.com](jonahgrossberg.us)

## Running locally

1. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

2. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

3. Inject environment variables

   ```bash
   $ .
   ```

4. Run the app

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)