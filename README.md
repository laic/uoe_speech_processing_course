# Speech Processing Labs: How to use these notebooks


## 1 Labs with Python and Jupyter Notebooks

People taking the Speech Processing course come from lots of different backgrounds. While we assume everybody has a bit of programming experience, we've tried to design these labs so that you don't actually need to write code to work through them. Hopefully the code blocks have enough comments that you'll be able to follow even if you don't have much coding experience. Mostly you'll just need to change some variables here and there to do the exercises.  But, of course, you're welcome to play with the code to explore the topics we cover and to write your own code! 


### 1.1 Jupyter Notebooks 

These labs use [Jupyter Notebooks](https://jupyter.org). These provide an interactive way to run python code and write nicely formatted text using [Markdown](https://www.markdownguide.org/cheat-sheet/). 

There are many tutorials about using Jupyter Notebooks on the internet.  If you've never used them before, it's a good idea to go through at least one to get used to how they work. Here's just a sample: 

* [A very quick overview from the Jupyter docs](https://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb)
* [An interactive tutorial from the Binder project that's made up of Jupyter notebooks](https://gke.mybinder.org/v2/gh/ipython/ipython-in-depth/master?filepath=binder/Index.ipynb)
* [Another quick overview from Towards Data Science](https://towardsdatascience.com/a-beginners-tutorial-to-jupyter-notebooks-1b2f8705888a)
* [Jupyter docs](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)



If you're reading this, you've obviously figured out how to view these notebooks! There are some instructions on how to set up Jupyter Notebooks for interactive use below. 


### 1.2 NumPy and Matplotlib

 

The main python packages we'll be using are [NumPy](https://numpy.org) and [Matplotlib](https://matplotlib.org). 

NumPy is _the_ python package for doing scientific computing.  That is, if you want to write programs that use vectors and matrices, you'll be using NumPy. It includes lots of efficient methods for calculating various types of functions (e.g. trig functions like sin, cos, exp) and applying them to variable sized vectors and matrices.  If you're used to using R or Matlab, you'll probably find it very familiar. If you go on to do more machine learning you'll definitely use NumPy (or packages based on it) a lot, so it's well worth getting to know.  But for this course, knowing the basics just make the code blocks a little more interpretable. 

Matplotlib is a comprehensive python visualization package that works well with NumPy. It is vast and complicated and we will not use that much of it's capabilities in these notebooks.  But again, you'll likely see this used in examples of plotting graphs with python in many speech processing related code bases. So, being able to recognize it's basic syntax will be helpful, but you definitely don't need to know much about this to use these notebooks.  

This machine learning tutorial conveniently covers jupyter, python, numpy and matplotlib: 
* [Python Numpy Tutorial (CNNs for visual recognition)](https://cs231n.github.io/python-numpy-tutorial/#jupyter-and-colab-notebooks)
 

Some other numpy tutorials (there are many others):
* [Official NumPy Getting Started](https://numpy.org/devdocs/user/quickstart.html)
* [W3 School's interactive NumPy tutorial](https://www.w3schools.com/python/numpy_intro.asp)


Some matplotlib tutorials: 
* [Official matplotlib user guide](https://matplotlib.org/users/index.html)
* [Tutorial on Towards Data Science](https://towardsdatascience.com/matplotlib-tutorial-learn-basics-of-pythons-powerful-plotting-library-b5d1b8f67596)
* [Matplotlib crash course](https://pythonprogramming.net/matplotlib-python-3-basics-tutorial/)


## 0 List of Notebooks 

### M0 Preliminaries
* [How to use these notebooks](./slp-m0-how-to-start.ipynb) (same as this readme, minus interactive code fragment)


### M1 Analyzing Sounds in Time and Frequency
* [Sounds and Signals (praat)](./slp-m1-1-sounds-signals.ipynb)
* [Digital Signals: Complex numbers and sinusoids](./slp-m1-2-digital-signals-complex-numbers.ipynb)
* [Digital Signals: Sampling sinusoids](./slp-m1-3-sampling-sinusoids.ipynb)
* [The Discrete Fourier Transform](./slp-m1-4-discrete-fourier-transform.ipynb)
* [Interpreting the DFT](./slp-m1-5-interpreting-the-dft.ipynb)

### M2 Source and Filter
* [Building the source: impulse trains](slp-m2-1-impulse-as-source.ipynb)
* [FIR filters](slp-m2-2-fir-filters.ipynb)
* [IIR filters](slp-m2-5-iir-filters.ipynb)
* [The Inverse DFT]()
* [Poles and zeros (extension)]()

## 2 Interacting with the Notebooks

### 2.1 The Easy Online Way: Edina Noteable

If you have a decent internet connection, the easiest way to start using jupyter notebooks is to use the University of Edinburgh's Noteable service.  This allows you to use Jupyter Notebooks, Python and all the extra packages we need through your browser (you don't need to install anything on your side).  

You can find lots of information on how to use Edina Noteable (including some videos) [here](https://noteable.edina.ac.uk/user_guide/#hide_ge_2).  

The main steps to loading up these labs is as follows.

* Start up Noteable by: 
    * going to the following URL in your browser login in with your EASE username and password:
        * https://noteable.edina.ac.uk/login
    * **or** clicking on the Noteable link on the course Learn page

* Select Standard Notebook and click on start

* You'll then see the jupyter start directory, showing you links to the files in it (probably empty at this point). 

* You can now import the notebook git repository by clicking the +GitRepo button and putting in the git repo address:
    * https://github.com/laic/uoe_speech_processing_course
 
* You should now be able to see a link called `uoe_speech_processing_course`. If you click on this, you should see the notebooks.  

* Click on a notebook to start it!  
    
#### Alternative: Using the terminal ####

Noteable also supports a unix terminal interface.
If you're happy with using the unix command line, you can click on the 'new' button and start a new _terminal_ instance.  You could then, for example, use the git clone command to get the repo: 
```
git clone https://github.com/laic/uoe_speech_processing_course
```
This isn't really necessary for our class work, but it may be useful thing for you to get familiar with in the future.  For example, you'll need to use the terminal if you want to clone a private git repository. Once you've got the hang of it, tt can also be a lot easier to use the terminal to do a lot of things, e.g. organize your files.

#### Tips #### 

* if you're using noteable, you might as well just use it through your normal computer browser (i.e. not through the virtual machine or guacamole!).  It'll save your computer a little bit of work. 

### 2.2 The 'Normal' Way: Running Jupyter Notebooks on your computer

You can also run Jupyter Notebooks locally on your own computer. Once you have everything installed, you should be able to go through all the lab materials offline. To do this, you'll need to have a few things installed: 

* Python 3.x
* Jupyter notebook
* numpy
* matplotlib

If you already have Python 3 install, you could just use `pip` to get the rest.  But, I'd recommend using miniconda because it will be useful for many other things later. 

#### Install Python 3.8 and Miniconda

Download the Miniconda 3.8 installer. You'll need to choose the appropriate version for your operating system (Window, MacOs or Linux) and the number of bits your CPU uses (64 or 32).  

https://docs.conda.io/en/latest/miniconda.html

Once you've downloaded the installer, open up a terminal and go to the directory you installed it into (probably `Downloads`).  

Run the following command checks the downloaded file isn't corrupted.  You can check that the string it returns matches SHA256 hash listed next to the download link you used. 
```
sha256sum ./Miniconda3-latest-Linux-x86_64.sh
```

Change the permissions on the Miniconda installer so you can run it ('u' for user, 'x' for execute), and then run it. 
```
chmod u+x ./Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
```
The installer will ask you a bunch of questions (agree to the license etc) which you basically have to say yes to if you want to use Miniconda.  You can also choose where it installs Miniconda, but usually the default location (in your home directory) is fine.


You'll then need to close and reopen your terminal.  Now run the following command to create a new Python 3 environment called `slp` (actually you can call it whatever you want!). 

```
conda create -n slp python=3
```
Now, activate the environment. 
```
conda activate slp
```
Doing this basically means that you're telling the shell to use this version of python instead of the default version of python on your computer (For example, on Guacamole the default version of python is 2.7, which is a version of python no longer being maintained).  Activating the environment also means you can download python packages in a systematic way and you (probably) won't run into permission problems on computers where you don't have administrator access.  

In general, it's good practice you use python enviroments for your projects so that you can keep track of dependencies.  New updates to python packages can sometimes mess up how old code works, so if you want someone else to run your code, having a specific conda environment means someone  else (maybe even your future self?) can easily recreate the conditions in which your code was created on a different machine. 

#### Install Jupyter Notebooks and other dependencies





Now we need can use conda to install a bunch of stuff, i.e. jupyter notebooks:
```
conda install -c conda-forge  notebook numpy matplotlib ipython
```

Now we can finally startup jupyter notebooks! Note you need to be in the slp environment we just created for this to work (i.e. run `conda activate slp` before this). 
```
jupyter notebook
```

This command starts a local notebook server and will give you a link to it. Open that link in your browser and you're all set!  

Note: You'll need to get the notebook repository from gitlab the 'normal way'.  Go to the directory you want to download the notebooks into and run the following command:
```
git clone https://git.ecdf.ed.ac.uk/clai/speech_processing.git
```
You should now see a directory call `uoe_speech_processing_course` in the directory where you called the `git clone` command. 



#### Notes

* The remote desktop service, Guacamole, uses python 2.7 by so you'll need to set up a python 3 enviroment to run these labs.
* As noted above, if you're ok working online you should probably just use the Edina Noteable servers!

#### Jupyter Notebooks official install info:

* https://jupyter.org/install
* https://jupyter.readthedocs.io/en/latest/running.html

## 3 Some Very Basic Jupyter Notebook Commands

You definitely don't need to be a Jupyter expert to do these labs. You basically just need to run every cell in turn! Here's the very bare bones of what you need to do.

#### Cells: 

Jupyter notebooks have two types of cells: 

* Code cells: i.e. code you can actually run
* Markdown cells: html-ish writing cells, we're you can write your notes (like this one you're reading now).
    * You can include various types of formatting: [Markdown reference](https://wordpress.com/support/markdown-quick-reference/)
    * You can also write equations in [latex math mode!](https://towardsdatascience.com/write-markdown-latex-in-the-jupyter-notebook-10985edb91fd)

After you've written something in a cell, you can run it by clicking the _Run_ button on the menu bar. 

**Note** You don't have to run the cells in the order they appear on the page.  When you run a code cell the variables set there will retain those values for the next cell you run.  This means that variables are updated in the order that you run the cells, not necessarily the order they appear on the page!  

As you go through a notebook, you'll probably soon find yourself wanting to use the keyboard shortcuts. 

#### Basic commands: 
* Click on a cell to edit it
* Cmd-Enter: Run the current cell
* Shift-Enter: Run the current cell and move to the next
    * Useful if you're moving through a notebook (which is what you'll likely be doing)
* Alt-Enter: Run the current cell and insert another after it
    * Useful if you're writing a notebook! 

If you click on the small keyboard icon on the menu bar (next to the cell type), you'll see many more command short cuts. 

**Note**: You'll need to double click on a markdown cell to edit it (if it's already been run).

### Try it out! 
* Click on the next cell
* Edit the python code to print out your own name instead of `YOUR_NAME_HERE`
* Press Shift-Enter to run the code 
* You should see the output directly under the cell


```python
print("Hello! My name is YOUR_NAME_HERE")
a = 793  ## This is a comment
b = 13   ## You could also change this value and see a change in the second sentence printed out
print("Did you know that %d + %d = %d?" % (a, b, a+b))
```

    Hello! My name is YOUR_NAME_HERE
    Did you know that 793 + 13 = 806?


Double click on this markdown cell to edit it! 

## 4 Getting the Latest Version of these  Lab Notebooks

You can get the latest version of the notebooks from this github repository:
https://github.com/laic/uoe_speech_processing_course


The usual way to download a git repository like this is to run the following on the command line (i.e. in your terminal

```
git clone https://github.com/laic/uoe_speech_processing_course
```

This will download the a folder called `uoe_speech_processing_course` into your current working directory.  

### Updating the repo

If you've already cloned the repository somewhere, you can get the lastest version by going to the `uoe_speech_processing_course` directory
and typing in the following command: 

```
git pull
```

**Note** This may cause merge conflicts (i.e., your version local clashes with the new version)  if you've modified and saved the notebooks already (which you should be doing!).  We'll try to avoid this by making sure we create notebooks with different names if we update one you might already have worked on.  In practice, though, merging and resolving conflicts is a very normal thing in software engineering when you're working with other people.  You can read more about updating repositories in the [github documentation](https://docs.github.com/en/github/using-git/getting-changes-from-a-remote-repository)



You can also download a zip file of the all the labs from the github page. 




### More info on git (and github)

Pretty much everyone uses git, and specifically github, for sharing and tracking code (i.e. version control). Knowing some basic git is really quite essential for working with code these days. 

* [The github guide to git](https://guides.github.com/introduction/git-handbook/)



## 5 What should I do for these labs? 

The goal of these labs is to get you to think through the concepts introduced in the lecture videos.  The labs **aren't** about coding (that's what the CPSLP course is for). You don't need to understand all the workings of the code and you definitely won't need to reproduce it. However, we do want you to get some exposure to how these abstract concepts get translated into concrete programming (and do so something a bit interactive with the computer and each other!).

The main tasks for the labs are these:

* Go through the notebooks and discuss the answers to the questions with your tutorial group before meeting your tutor.
    * Don't worry if you can't answer all the questions in the exercises - bring them to your tutor!
* Discuss what you've learned and what questions you have to your tutor: 
    * Everyone in the group should take a turn leading this discussion with the tutor. Note this **doesn't** mean that person should do all the work for the week. That person should just be noting what the group did as a whole. 


## 6 Help! 

People taking this course come from lots of different backgrounds. If you run into trouble or this is all a bit much, ask for help! 

* Matt Spike is our designated tech support contact for Speech Processing (and the MSc SLP in general). He can help you with all sorts of technical issues. 
* You can and should also talk your tutors/lecturers:
    * Catherine Lai (who wrote these notebooks)
    * Simon King
    * Jason Taylor
    * Jason Fong
