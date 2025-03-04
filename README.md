<h1>CloudFlare Dynamic DNS Update Script</h1>

<h4>Description</h4>
<p>This is a Python script which will dynamically update CloudFlare DNS using the CloudFlare API <a href="https://developers.cloudflare.com/api/python/resources/dns/subresources/records/methods/edit/#(params)%200%20%3E%20(param)%20zone_id%20%3E%20(schema)">CloudFlare API</a>.
Great for if you have a Dynamic Internet connection (typically consumer broadband) but you you have services running at home that you need to connect to from an external source.</p>
<hr>
<h4>Usage</h4>
<p>To use this script, you will need a CloudFlare account with a DNS Zone hosted with CloudFlare. Once you are setup, configure a record within the zone that you wish to keep updated with this script.
You will need to obtain the following details from you account for this to work, and store them ae Enviromental Variables, or just change the Key/Value pairs within the script:
<ul>
  <li>API_EMAIL = "Your account email address"</li>
  <li>API_KEY = "Global API Key (from your profile API Tokens page"</li>
  <li>ZONE_ID = "Zone ID from your DNS Zone"</li>
  <li>RECORD_NAME = "DNS Record you would likt to update" </li>
</ul>
Example:<br>
<code>
API_EMAIL = "mytestaccount@test.com"<br>
API_KEY = "12323423459028aabbbcccc11223322"<br>
ZONE_ID = "43219047283bcdebb31239b123"<br>
RECORD_NAME = "mytest.test.com"<br>
</code>
  <br>
To use, create your environmental variables (can create and use via a .env file is the scripts root directory - copy, paste and update the details above. Create a virtual environment<br>python -m venv venv<br>
activate the virtual environment<br>
<i>Linux/macOS</i>
<br><code># source venv/bin/activate</code>
<br><i>Windows</i><br>
<code>> venv/bin/activate</code><br>
Install the dependencies<br>
<code>pip install -r requirements.txt</code><br><i>or</i><br><code>python -m pip install -r requirements.txt</code></p>
<h4>Testing</h4>
<p>This has been tested using Python3.12.8. If you do need any assistance, please feel free to reaech out or raise an issue and I'll review when I can.</p>
