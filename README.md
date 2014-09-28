HackJam2014: Cal HackJam - August 27, 2014
=============

We created PatentAssist API, which takes in a keyword and returns information on related patents.
We built this with Python / the Django web framework, and JSON / JS on the web front end. As  


;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;     API USE    ;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;

- METHOD 1 -
Input: keyword
Output: list of related patents' (1) patent ID, and (2) patent title/description


- METHOD 2 -
Input: Patent ID (i.e: US613809)
Output: PDF of the patent application submitted to the USPTO

http://patentassist.me


** Tech/software Used: **
- D3.js
- Python, JS, JSON, AJAX
- Bootstrap CSS & JS
- digitalocean cloud host / droplet
- Django python web framework


;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;      Notes     ;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;

End of Hackathon Update: Our hack has some known bugs which we intend to fix over the next few days.
The following are the known bugs: 
- on the webpage, single "left-clicking" a link doesn't open the link;
    - temp fix: right-click -> open in new tab
- DigitalOcean

What's next:
- data visualization - we got far with D3js, for visualizing a graph of these keywords and related claim words, but we weren't able to close it up to a finished product for the hackathon


Collaboration by Daniel Suryakusuma, Allan Zhao, Yi Chen


