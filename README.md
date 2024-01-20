# TO_flaskapp_docker
Docker based TO-flaskapp


Web app developed as a tool-kit being part of my thesis project in Electrical Engineering.

Application and Server Description

Developed using HTML and Python back-end with the Flask framework. Javascript and CSS through Bootstrap was used for front-end design and to obtain screen size responsive design 

- Originally (in 2020) deployed using Linode. Hosted on a cloud Linux server using Nginx 1.16.1 and Ubuntu 19.10 as operating system. Running Python 2.7.17 with Flask 1.1.1 and Pygal 2.4.0
- Redeployed in 2023 via Docker file using fly.io with the addition of GitHub actions for automated code deployments when changes are pushed from the local machine.

Flask App Files and Structure

Consisting of six pages that inherits from layout.html. Page 1 to 4 contain various PV system sizing resources. The application was initially based on starter code snippets from Flask and Bootstrap, which was further developed. A couple of different Flask imports is necessary for template inheritance and user request handling. Pygal bar charts used for the interactive histograms on the application page #3.

