# Blog
A web application that allow users to read blogs and for writers to post, edit and delete blogs:
https://nimo-blog.herokuapp.com/
## By Wairimu Maina
A student at Moringa School and an aspiring software developer.

## Description of application
Blog is a web application that users can use to view other blog posts, comment on the blogs and sign in as writers. Writers will be able to post new blog posts, edit existing posts, delete posts and comments. Random quote is also displayed on every blog.

## Specifications
* Users can view most recent blog posts
* Users can comment on blog posts
* Users can register and login to become writers
* Writers can create new blog posts
* Writers can update and delete blog posts
* Writers can delete comments

## Prerequisites
* Python 3.6 required

## Setup/Installation Requirements
Follow the following commands to run the project
* git clone/download ```https://github.com/kelvin-wahome/Blogs.git```
* cd Pitch
* Edit the start.sh file with your api key from the news.org website
* Install python 3.6
* Run ```chmod a+x start.py```
* Run ```./start.py```

### Behaviour Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Index Page loads as default | Home link | Loads the home page. |
| View Blogs| Click on view blogs | All posts are displayed starting with the most recent|
| View Blog | Click on Read More| All the details of that specific blog is displayed|
| Delete Blog | Click on Delete | Post is deleted|
| Write Blog| Click on Write Blogs| A form for a new blog is displayed|
| Comment| Full Blog Page| A comment form is displayed and older comments from other users|
| Update Blog | Click on Update | Form with the inital blog post that allows writer to edit|




## Known Bugs
No bugs discovered.

## Technologies Used
* Python
* HTML
* BOOTSTRAP
* Flask

## Support and contact details
In case of clarification email me at wahomekelving@gmail.com

## License
*MIT*
Copyright (c) 2019 **Kelvin Wahome**
