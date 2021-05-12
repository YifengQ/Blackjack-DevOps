# Blackjack-DevOps
Project designed around Test-Driven Development. Created a simple blackjack game that automates the unit testing and deployment upon commit. 
Upon every commit Jenkins will run a test suite to make sure changes haven't negatively affected the output. Then if it passes all the 
test cases it will create a Docker image and push that to a repository. 
