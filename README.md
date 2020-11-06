# cs102-F2020-practical6-starter

![](../../workflows/build/badge.svg)

## Table of Contents

* [Objectives](#objectives)
* [Introduction](#introduction)
* [Continuous Learning](#continuous-learning)
* [Assignment Reminders](#assignment-reminders)
* [Accessing the Assignment](#accessing-the-assignment)
* [Practical Assignment Tasks](#practical-assignment-tasks)
  + [Installing Programs that Support Python Programming](#installing-programs-that-support-python-programming)
  + [Using Iteration to Compute the Numbers in the Collatz Sequence](#using-iteration-to-compute-the-numbers-in-the-collatz-sequence)
  + [Running a Test Suite for a Program that Computes the Collatz Sequence](#running-a-test-suite-for-a-program-that-computes-the-collatz-sequence)
  + [Reflecting on the Practical Assignment](#reflecting-on-the-practical-assignment)
* [Automated Checks with GatorGrader](#automated-checks-with-gatorgrader)
* [Assignment Assessment](#assignment-assessment)
* [Advance Feedback on an Assignment](#advance-feedback-on-an-assignment)
* [Discussion of a Graded Assignment](#discussion-of-a-graded-assignment)
* [Additional Resources](#additional-resources)
  + [System Commands](#system-commands)
* [Non-Interactive Docker Commands](#non-interactive-docker-commands)
* [Commands for an Interactive Docker Shell](#commands-for-an-interactive-docker-shell)
* [Upgrading the Docker Container](#upgrading-the-docker-container)
* [Downloading Project Updates](#downloading-project-updates)
* [Using GitHub Actions](#using-github-actions)
* [System Requirements](#system-requirements)
* [Reporting Problems](#reporting-problems)
* [Receiving Assistance](#receiving-assistance)

## Objectives

The learning objectives for this practical assignment are as follows:

- To transfer files from your laptop to your GitHub repository
- To use your text editor to manipulate code blocks in a Markdown file
- To use your text editor to manipulate code blocks in a Python file
- To use a Docker container to run the automated checks performed by GatorGrader
- To use a terminal window to run a Python program and observe its output
- To use a text editor and a terminal window to add functions to a Python program
- To use a terminal window to run test cases in a Pytest test suite
- To observe the behavior of a mathematical function that returns a sequence of numbers
- To implement a Pytest test case that tests a mathematical function
- To use a graphing function to plot the relationship between the inputs and outputs of a function

## Introduction

Designed for use with [GitHub Classroom](https://classroom.github.com/) and
[GatorGrader](https://github.com/GatorEducator/gatorgrader/), this repository
contains a practical assignment for an introductory computer science class that
uses the Python programming language. The source code and technical writing for
this assignment must pass tests set by the [GatorGrader
tool](https://github.com/GatorEducator/gatorgrader). When you use the `git
commit` command to transfer your source code to your GitHub repository, GitHub
Actions will initialize a build of your assignment, checking to see if it meets
all of the requirements. If both your source code and writing meet all of the
established requirements, then you will see a green ✔  in the listing of commits
in GitHub. If your submission does not meet the requirements, a red ❌ will
appear instead. Please note that, at the option of the course instructor, some
checks may be run in GitHub Actions that are not run locally by the [GatorGrader
tool](https://github.com/GatorEducator/gatorgrader).

## Continuous Learning

If you have not done so already, please read all of the relevant [GitHub
Guides](https://guides.github.com/) that explain how to use many of the features
that GitHub provides. In particular, please make sure that you have read the
following GitHub guides: [Mastering
Markdown](https://guides.github.com/features/mastering-markdown/), [Hello
World](https://guides.github.com/activities/hello-world/), and [Documenting Your
Projects on GitHub](https://guides.github.com/features/wikis/). Each of these
guides will help you to understand how to use both [GitHub](http://github.com) and
[GitHub Classroom](https://classroom.github.com/).

Students who want to learn more about how to use
[Docker](https://www.docker.com) should review the [Docker
Documentation](https://docs.docker.com/). Students are also encouraged to
review the documentation for their text editor, which is available at [VS
Code](https://code.visualstudio.com/docs). You should also review the [Git
documentation](https://git-scm.com/doc) to learn more about how to use the Git
command-line client. In addition to talking with the instructor and technical
leader for your course, students are encouraged to search
[StackOverflow](https://stackoverflow.com/) for answers to their technical
questions.

As outlined in the course schedule in the [course planning
repository](https://github.com/Allegheny-Computer-Science-102-F2020/cs102-F2020-plans),
students should also read all of the assigned readings for up to and including
the week of the semester on which this practical assignment was assigned.

## Assignment Reminders

- **Follow each step carefully**. Slowly read each sentence in this document,
  making sure that you precisely follow each instruction. Take notes about each
  step that you attempt, recording your questions and ideas and the challenges
  that you faced. If you are stuck, then please tell a technical leader or the
  course instructor what assignment step you recently completed.

- **Regularly ask and answer questions**. Please log into Slack at the start of
  the practical session and then join the appropriate channel. If you have a
  question about one of the steps in an assignment, then you can post it to the
  designated channel, discussing your questions through both Slack and the
  Google Meet designated for the class.

- **Store your files in GitHub**. Starting with this practical assignment, you
  will be responsible for storing all of your files (e.g., Python source code
  and Markdown-based writing) in a Git repository using GitHub Classroom. Please
  verify that you have saved your source code in your Git repository by using
  `git status` to ensure that everything is updated. You can see if your
  assignment submission meets the established correctness requirements by using
  the provided checking tools on your local computer and by checking the commits
  in GitHub.

- **Keep all of your files**. Don't delete your programs, output files, and
  written reports after you submit them through GitHub; you will need them
  again when you study for the course assessments and work on the other
  practical, practical, and technical challenge assignments.

- **Hone your technical writing skills**. Computer science assignments require
  to you write technical documentation and descriptions of your experiences when
  completing each task. Take extra care to ensure that your writing is
  interesting and both grammatically and technically correct, remembering that
  computer scientists must effectively communicate and collaborate with their
  team members and the student technical leaders and course instructor.

- **Review the Honor Code on the syllabus**. While you may discuss your
  assignments with others, copying source code or technical writing is a
  violation of Allegheny College's Honor Code.

## Accessing the Assignment

To access this assignment, you should go into the `#announcements` channel in
our Slack workspace and find the announcement that provides a link for it. Copy
this link and paste it into your web browser. Now, you should accept the
practical assignment and see that GitHub Classroom created a new GitHub
repository for you to access the assignment's starting materials and to store
the completed version of your assignment. Specifically, to access your new
GitHub repository for this assignment, please click the green "Accept" button
and then click the link that is prefaced with the label "Your assignment has
been created here". If you accepted the assignment and correctly followed these
steps, you should have created a GitHub repository with a name like
`Allegheny-Computer-Science-102-Fall-2020/computer-science-102-fall-2020-practical-6-gkapfham`.
Unless you provide the course instructor with documentation of the extenuating
circumstances that you are facing, not accepting the assignment means that you
automatically receive a failing grade for all of its components.

Before you move to the next step of this practical assignment, please make
sure that you read all of the content on the web site for your new GitHub
repository, paying close attention to the technical details about the commands
that you will type and the output that your program must produce. Now you are
ready to download the starting materials to your practical computer. Click the
"Clone or download" button and, after ensuring that you have selected "Clone
with SSH", please copy this command to your clipboard. To enter into your
course directory directory you should now type `cd cs102F2020`. Next, you can
type the either `ls` (on either MacOS or Linux) or `dir` (on Windows 10 Pro or
Windows 10 Enterprise) and see that there are no files or directories inside of
this directory. By typing `git clone` in your terminal and then pasting in the
string that you copied from the GitHub site you will "download" all of the code
for this assignment. For instance, if the course instructor ran the `git clone`
command in the terminal, it would look like:

```
git clone git@github.com:Allegheny-Computer-Science-102-F2020/computer-science-102-fall-2020-practical-6-gkapfham.git
```

After this command finishes, you can use `cd` to change into the new directory.
If you want to "go back" one directory from your current location, then you can
type the command `cd ..`. Finally, please continue to use the `cd` and `ls`
commands to explore the files that you automatically downloaded from GitHub. If
one of the aforementioned commands does not work correctly, then it is possible
that your terminal window is not up-to-date or not configured correctly. In this
case, please share your specific error messages with the instructor, ultimately
working to master the use of terminal commands. What files and directories do
you see? What do you think is their purpose? Spend some time exploring, telling
your discoveries to a student technical leader.

## Practical Assignment Tasks

### Installing Programs that Support Python Programming

If you have not done so already, then, in order to implement a full-fledge
Python program, you need to install the [Poetry
tool](https://python-poetry.org/docs/) for dependency management and packaging
of Python programs. After ensuring that you have Python 3.8 installed on your
laptop through Pyenv, please follow the installation instructions for Poetry.
For instance, you are using either MacOS or Linux you need to type the following
command in your terminal window `curl -sSL
https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py |
python`. Importantly, this command will only work if you have already installed
a program called `curl`. If you are using Windows 10 Pro then you will need to
follow the PowerShell installation instructions on Poetry's web site. With that
said, if you did not install Python 3.8.5 and Poetry on your laptop, then you
can use the versions of these programs that are available in the provided Docker
container. Ultimately, if you are not sure that all of the Python development
tools are working correctly on your laptop, then you should always use the
provided Docker container.

Now, making sure that you are in your "home base" directory for this practical
assignment, you need to install the dependencies for the `factorialmaker`
program that you will implement, debug, and observe. To complete this step you
need to type `cd factorialmaker` and then `poetry install`. What output did
this command produce? What do you think that this step did? Why is important to
type these commands? Make sure that you know the answers to these question
before moving onto the next step of the assignment. Finally, please remember
that when you want to run `gradle grade` you must be in the "home base"
directory for this practical assignment. However, when you want to run the
Python program you need to be in the directory called `factorialmaker`.

### Using Iteration to Compute the Numbers in the Collatz Sequence

For this practical assignment you are going to design, implement, and test a
program that can produce the numerical values in the Collatz sequence. To learn
more about this sequence of numbers, which has properties that have not yet been
mathematically proven, you can read your textbook and visit the [Longest Collatz
Sequence Problem on Project Euler](https://projecteuler.net/problem=14). This
assignment will required you to combine your knowledge of functions, iteration
constructs, the list discrete structure, and mathematics to create a Python
program that you implement in an industry-standard fashion. For instance, when
you run the completed version of the Python program with the command `poetry run
python collatzcreator --minimum 1 --maximum 10` it will produce the following
output:

```
Let's investigate the behavior of the Collatz sequence! 🔍

Does this sequence of numbers finish at the value of 1? ✨

The inputs to the Collatz function:

  [1, 2, 3, 4, 5, 6, 7, 8, 9]

The length of the resulting Collatz chain:

  [1, 2, 8, 3, 6, 9, 17, 4, 20]

The minimum length of a Collatz chain is: 1
The maximum length of a Collatz chain is: 20

The mean of the length of a Collatz chain is: 7.777777777777778
The median of the length of a Collatz chain is: 6
The standard deviation of the length of a Collatz chain is: 6.285393610547089

Can you find a pattern between the input number and the length of the Collatz chain? 🤷

Check the file called 'collatz.pdf' to see a graph that visualizes the results! 📈
```

When you run this program you should also notice that it produces a file called
`collatz.pdf`. Please make sure that you load this file with a PDF viewer on
your laptop and then use it to better understand the relationship between the
number that is input to the Collatz function and the length of the sequence
(sometimes called the "chain") of numbers output by the function. For example,
when the function is run with the input of `3` then it produces the output `[3,
10, 5, 16, 8, 4, 2, 1]`, which corresponds to a chain of length 8. Can you find
a pattern between the number that is input and the length of the chain? Finally,
can you answer the Project Euler question about the Collatz sequence?
Specifically, the question is "which starting number, under one million,
produces the longest chain?" To make a start at answering this question, you
might consider using the provided source code to determine the maximum length of
the resulting Collatz chain. While you are not required to answer the Project
Euler question as a part of this practical assignment, you are encouraged to
attempt to do so. Of course, you should ensure that your program is working
correctly and that you understand its input, outputs, and behavior.

### Running a Test Suite for a Program that Computes the Collatz Sequence

If you look in the Python file called `collatzcreator/tests/test_collatz.py`
that it contains a `TODO` marker indicating that you are responsible for adding
the test case for the `Collatz` function in the `collatz` module. If you look in
the book on page 92, you will see that the author explains that the `Collatz`
function should produce the output `[3, 10, 5, 16, 8, 4, 2, 1]` when it is given
the input of `3`. Can you write a test case that will ensure that the function
produces this output when it is given this input? For instance, you could write
the test case in the following fashion:

```
def test_collatz_input_three():
    """Ensure that input of the number 3 produces the sequence suggested by Stavely on page 92."""
    number = 3
    # create a generator function of all of the outputs
    collatz_output_generator = collatz.Collatz(number)
    # materialize a list from the generator function, which
    # will support multiple assertions on the list
    collatz_output_list = list(collatz_output_generator)
    # ensure that there are eight values in the list
    assert len(list(collatz_output_list)) == 8
    # confirm that the contents of the list are correct
    assert list(collatz_output_list) == [3, 10, 5, 16, 8, 4, 2, 1]
```

If the `Collatz` function is correct, you should be able to run the test suite by
typing `poetry run pytest -v` and see that it produces the following output:

```
================================================================== test session starts ==================================================================
platform linux -- Python 3.8.5, pytest-5.4.3, py-1.9.0, pluggy-0.13.1 -- /home/gkapfham/.cache/pypoetry/virtualenvs/collatzcreator-dr8P3RVT-py3.8/bin/python
cachedir: .pytest_cache
rootdir: /home/gkapfham/working/teaching/github-classroom/Allegheny-Computer-Science-102-F2020/solutions/cs102-F2020-practical6-solution/collatzcreator
collected 12 items

tests/test_collatz.py::test_collatz_input_three PASSED                                                                                            [  8%]
tests/test_summarize.py::test_summarize_empty_number_list_mean PASSED                                                                             [ 16%]
tests/test_summarize.py::test_summarize_pos_neg_number_list PASSED                                                                                [ 25%]
tests/test_summarize.py::test_summarize_equal_number_list PASSED                                                                                  [ 33%]
tests/test_summarize.py::test_summarize_different_number_list PASSED                                                                              [ 41%]
tests/test_summarize.py::test_summarize_empty_number_list_median PASSED                                                                           [ 50%]
tests/test_summarize.py::test_summarize_full_list_median_even PASSED                                                                              [ 58%]
tests/test_summarize.py::test_summarize_full_list_median_odd PASSED                                                                               [ 66%]
tests/test_summarize.py::test_compute_difference_empty_list PASSED                                                                                [ 75%]
tests/test_summarize.py::test_summarize_compute_difference PASSED                                                                                 [ 83%]
tests/test_summarize.py::test_summarize_full_list_variance_even PASSED                                                                            [ 91%]
tests/test_summarize.py::test_summarize_full_list_standard_deviation_even PASSED                                                                  [100%]

================================================================== 12 passed in 0.03s ===================================================================
```

Please note that this assignment also includes the test suite from a previous
assignment because this project is also using some of the main functions inside
of the `summarize.py` file that you previously implemented. Ultimately, you
should make sure that all of the test cases pass correctly. If they do not,
please make sure that you repair the broken Python function before continuing
with the steps of this practical assignment.

### Reflecting on the Practical Assignment

Once you have finished both of the previous technical tasks, use your text
editor to answer all of the questions in the `writing/reflection.md` file. For
instance, you should provide the output of the Python program in a fenced code
block, explain the meaning of the provided source code segments, and answer all
of the other questions about your experiences in completing this practical
assignment. One important aspect of the reflection is to make sure that you
understand each line of the source code provided on page 92 of your textbook.
Specifically, please make sure that you understand the conditional logic in the
statement `if number % 2 == 0:` and the type of division performed by the source
code statement `number = number // 2`.

## Automated Checks with GatorGrader

In addition to meeting all of the requirements outlined in this assignment
sheet, your submission must pass the following checks that
[GatorGrader](https://github.com/GatorEducator/gatorgrader) automatically
assesses:

If [GatorGrader's](https://github.com/GatorEducator/gatorgrader) automated
checks pass correctly, the tool will produce the output like the following in
addition to returning a zero exit code (which you can access by typing the
command `echo $?`). You will need to run
[GatorGrader](https://github.com/GatorEducator/gatorgrader) in a Docker
container by following the steps in the [Using Docker](#using-docker) section.

- The collatz.py in collatzcreator/collatzcreator has at least 1 of the `number // 2` fragment
- The collatz.py in collatzcreator/collatzcreator has at least 2 multiple-line Python comment(s)
- The collatz.py in collatzcreator/collatzcreator has at least 7 single-line Python comment(s)
- The collatz.py in collatzcreator/collatzcreator has exactly 0 of the `TODO` fragment
- The command `cd collatzcreator; poetry install; poetry run python collatzcreator; cd ..` executes correctly
- The file collatz.py exists in the collatzcreator/collatzcreator directory
- The file \_\_main\_\_.py exists in the collatzcreator/collatzcreator directory
- The file reflection.md exists in the writing directory
- The file test_collatz.py exists in the collatzcreator/tests directory
- The \_\_main\_\_.py in collatzcreator/collatzcreator has at least 2 multiple-line Python comment(s)
- The \_\_main\_\_.py in collatzcreator/collatzcreator has at least 4 single-line Python comment(s)
- The \_\_main\_\_.py in collatzcreator/collatzcreator has exactly 0 of the `TODO` fragment
- The \_\_main\_\_.py in collatzcreator/collatzcreator has exactly 1 of the `Option(10)` fragment
- The \_\_main\_\_.py in collatzcreator/collatzcreator has exactly 1 of the `Option(1)` fragment
- The \_\_main\_\_.py in collatzcreator/collatzcreator has exactly 1 of the `Option([])` fragment
- The \_\_main\_\_.py in collatzcreator/collatzcreator has exactly 1 of the `run(main)` fragment
- The reflection.md in writing has at least 2 of the `code` tag
- The reflection.md in writing has at least 600 word(s) in total
- The reflection.md in writing has exactly 0 of the `Add Your Name Here` fragment
- The reflection.md in writing has exactly 0 of the `TODO` fragment
- The reflection.md in writing has exactly 10 of the `heading` tag
- The reflection.md in writing has exactly 3 of the `code_block` tag
- The repository has at least 5 commit(s)
- The test_collatz.py in collatzcreator/tests has at least 1 multiple-line Python comment(s)
- The test_collatz.py in collatzcreator/tests has exactly 0 of the `TODO` fragment

```
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ Passed 25/25 (100%) of checks for cs102-F2020-practical6! ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## Assignment Assessment

Again taking inspiration from the principles of [specification-based
grading](https://www.amazon.com/Specifications-Grading-Restoring-Motivating-Students/dp/1620362422),
the grade that a student receives on either a practical assignment or a
technical challenge will be based on whether or not it meets the standards for
technical work in the fields of software engineering and discrete structures as
evidenced by:

- **GitHub Actions Build Status of Either ✔  or ❌**: Your work will receive a ✔
  if the last before-the-deadline build in GitHub Actions passes and a ✔ appears
  in the GitHub commit log instead of an ❌. The build status reported by
  GitHub Actions will only be a ✔ if the Python source code and technical
  writing in the GitHub repository pass all of both the GatorGrader checks and
  any additional checks.

## Advance Feedback on an Assignment

Students who wish to receive feedback on their work for any course assignment
should first open an issue on the issue tracker for their assignment's GitHub
repository, giving an appropriate title and description for the type of feedback
that you would like the course instructor to provide. After creating this issue,
you will see that GitHub has created a unique web site that references it. To
alert the course instructor to the fact that the issue was created and that you
want feedback on your work, please send it to him by a Slack direct message at
least 24 hours in advance of the project's due date. After the instructor
responds to the issue, please resolve all of the stated concerns and participate
in the discussion until the issue is resolved and ultimately marked as closed.

## Discussion of a Graded Assignment

Students who wish to receive feedback on their work for any graded course
assignment should leave question in the same region of Github where the course
instructor submitted the assignment's grade. For example, if the instructor
submits your grade to a pull request in your repository for a practical
assignment, then you should ask questions about your grade in that pull request,
bearing in mind the need to @-mention the course instructor in the body of your
comment. Students can continue to discuss the graded assignment with the course
instructor until they understand all the technical topics that were the
focus of the particular assignment.

## Additional Resources

### System Commands

This project invites students to enter system commands into a terminal window.
This assignment uses [Docker](https://www.docker.com) to deliver programs, such
as `gradle` and the source code and packages needed to run
[GatorGrader](https://github.com/GatorEducator/gatorgrader), to a students'
computer, thereby eliminating the need for a programmer to install them on their
development workstation. Individuals who do not want to install Docker can
optionally install of the programs mentioned in the [Project
Requirements](#requirements) section of this document.

## Non-Interactive Docker Commands

Once you have installed [Docker
Desktop](https://www.docker.com/products/docker-desktop), with MacOS and Linux
you can use the following `docker run` command to start `gradle grade` as a
containerized application, using the
[DockaGator](https://github.com/GatorEducator/dockagator) Docker image available
on
[DockerHub](https://cloud.docker.com/u/gatoreducator/repository/docker/gatoreducator/dockagator).

```bash
docker run --rm --name dockagator \
  -v "$(pwd)":/project \
  -v "$HOME/.dockagator":/root/.local/share \
  gatoreducator/dockagator
```

The aforementioned command will use `"$(pwd)"` (i.e., the current working
directory) as the project directory and `"$HOME/.dockagator"` as the cached
GatorGrader directory. Please note that both of these directories must exist,
although only the project directory must contain something. Generally, the
project directory should contain the source code and technical writing for an
assignment, as provided to a student by the instructor through GitHub.
Additionally, the cached directory should not contain anything other than
directories and programs created by DockaGator, thus ensuring that they are not
otherwise overwritten during the completion of the assignment.

To ensure that the previous command will work correctly, you should create the
cache directory by running the command `mkdir $HOME/.dockagator` on the MacOS
and Linux operating systems. However, if you are using the Windows operating
system then you will instead need to type the command `mkdir
%HomeDrive%%HomePath%/.dockagator`. Finally, since the above `docker run`
command does not work correctly on the Windows operating system, you will need
to instead run the following command to adapt to the differences in the `cmd`
terminal window:

```bash
docker run --rm --name dockagator \
  -v "%cd%:/project" \
  -v "%HomeDrive%%HomePath%/.dockagator:/root/.local/share" \
  gatoreducator/dockagator
```

Please note that not all version of the Windows terminal window will correctly
recognize the use of the `%cd%` and `%HomeDrive%%HomePath%` variables. In this
case, you should substitute the actual directory for a specific course
assignment for the `%cd%` variable and the drive letter that contains the
`.dockagator` directory for the `%HomeDrive%%HomePath%` variable. Finally, the
Windows terminal window may not work correctly when you attempt to run a
multi-line command. In this case, you should break up the aforementioned
four-line command into separate lines, like `docker run --rm --name dockagator`
and `-v "%cd%:/project"` and then connect them into a single long line that you
separate by a single space. Here is an example of what the long command would
look like, again assuming that the Windows `cmd` terminal correctly interprets
the `%cd%` and `%HomeDrive%%HomePath%` variables:

```bash
docker run -it --rm --name dockagator -v "%cd%:/project" -v "%HomeDrive%%HomePath%/.dockagator:/root/.local/share" gatoreducator/dockagator /bin/bash
```

Here are some additional commands that you may need to run when using Docker:

* `docker info`: display information about how Docker runs on your workstation
* `docker images`: show the Docker images installed on your workstation
* `docker container list`: list the active images running on your workstation
* `docker system prune`: remove many types of "dangling" components from your workstation
* `docker image prune`: remove all "dangling" docker images from your workstation
* `docker container prune`: remove all stopped docker containers from your workstation
* `docker rmi $(docker images -q) --force`: remove all docker images from your workstation

## Commands for an Interactive Docker Shell

Since the above `docker run` command uses a Docker images that, by default, runs
`gradle grade` and then exits the Docker container, you may want to instead run
the following command so that you enter an "interactive terminal" that will
allow you to repeatedly run commands within the Docker container. Don't forget
that, if you are using the Windows operating system, then you will need to use a
different command to run Docker, as explained previously in this document.
Importantly, the command that you type if you are a Windows user should still
contain the `-it` at the start of the `docker run` and the `/bin/bash` at the
end of the command. However, the other components of this command need to be
customized for the Windows operating system.

If you use either MacOS or Linux, then this is the command that you would run to
enter into the interactive terminal provided by a Docker container:

```bash
docker run -it --rm --name dockagator \
  -v "$(pwd)":/project \
  -v "$HOME/.dockagator":/root/.local/share \
  gatoreducator/dockagator /bin/bash
```

If you use Windows, then this is the command that you would run to enter into
the interactive terminal provided by a Docker container:

```bash
docker run -t --rm --name dockagator \
  -v "%cd%:/project" \
  -v "%HomeDrive%%HomePath%/.dockagator:/root/.local/share" \
  gatoreducator/dockagator /bin/bash
```

Once you have typed this command, you can use the [GatorGrader
tool](https://github.com/GatorEducator/gatorgrader) in the Docker container by
typing the command `gradle grade` in your terminal. Running this command will
produce a lot of output that you should carefully inspect. If GatorGrader's
output shows that there are no mistakes in a course assignment, then your source
code and technical writing are passing all of the automated baseline checks.
However, if the output indicates that there are mistakes, then you will need to
understand what they are and then try to fix them.

Remember, to correctly run any of the commands mentioned in this guide, you must
be in the main (i.e., "home base") directory for a course assignment where the
`build.gradle` file is located.

## Upgrading the Docker Container

If the course instructor provides a new version of the Docker container called
`gatoreducator/dockagator` and you want to receive it immediately, you must
first delete the existing Docker container on your laptop by running the command
`docker rmi gatoreducator/dockagator`. Next, you can re-run one of the
aforementioned Docker commands, like the following one, which would work on
MacOS or Linux:

```
docker run -it --rm --name dockagator \
  -v "$(pwd)":/project \
  -v "$HOME/.dockagator":/root/.local/share \
  gatoreducator/dockagator /bin/bash
```

Please note that if you attempt to run `gradle grade` in an updated Docker
container it is possible that the command will execute incorrectly if you
previously used GatorGrader with a Docker container that featured a different
version of the Python programming language. In this situation, you should delete
the directories inside of the `.dockagator` directory and then again attempt to
run the `gradle grade` command inside of the Docker container. Specifically, you
will need to delete directories in `.dockagator` that are normally called
`gatorgrader`, `virtualenv`, and `virtualenvs`.

## Downloading Project Updates

If GatorGrader's maintainers push updates to this sample assignment and you
received it through GitHub Classroom and you would like to also receive these
updates, then you can type this command in the main directory for this
assignment:

```
git remote add download git@github.com:Allegheny-Computer-Science-102-F2020/cs102-F2020-practical6-starter.git
```

You should only need to type this command once; running the command additional
times may yield an error message but will not negatively influence the state of
your Git repository. Now, you are ready to download the updates provided by the
GatorGrader maintainers by typing this command:

```
git pull download master
```

This second command can be run whenever the maintainers needs to provide you
with new source code for this assignment. However, please note that, if you have
edited the files that we updated, running the previous command may lead to Git
merge conflicts. If this happens, you may need to manually resolve them with the
help of the instructor or a student technical leader. Finally, please note that
the [Gradle plugin](https://github.com/GatorEducator/gatorgradle) for
[GatorGrader](https://github.com/GatorEducator/gatorgrader) will automatically
download the newest version of GatorGrader.

## Using GitHub Actions

This assignment uses [GitHub Actions](https://github.com/features/actions) to
automatically run [GatorGrader](https://github.com/GatorEducator/gatorgrader)
and additional checking programs every time you commit to your GitHub
repository. The checking will start as soon as you have accepted the assignment
&mdash; thus creating your own private repository &mdash; and the course
instructor and/or GitHub enables GitHub Actions on it. If you do not see either
a yellow &#9679; or a green ✔ or a red ❌ in your listing of commits, then
please ask the instructor to see whether or not GitHub Actions was correctly
enabled.

## System Requirements

This assignment was developed to work with the following software and versions:

- Docker Desktop
- Operating Systems
  - Linux
  - MacOS
  - Windows 10 Pro
  - Windows 10 Enterprise
- Programming Language Tools
  - Gradle 6.6
  - MDL 0.5.0
  - Python 3.7 or 3.8

## Reporting Problems

If you have found a problem with this assignment's provided source code or
documentation, then you can go to the [Computer Science 102 Fall 2020 Planning
Repository](https://github.com/Allegheny-Computer-Science-102-F2020/cs102-F2020-plans)
and [raise an
issue](https://github.com/Allegheny-Computer-Science-102-F2020/cs102-F2020-plans/issues).
If you have found a problem with the [GatorGrader
tool](https://github.com/GatorEducator/gatorgrader) and the way that it checks
your assignment, then you can also [raise an
issue](https://github.com/GatorEducator/gatorgrader/issues) in that repository.
To ensure that your issue is properly resolved, please provide as many details
as is possible about the problem that you experienced. Individuals who find, and
use the appropriate GitHub issue tracker to correctly document, a mistake in any
aspect of this assignment will receive extra credit towards their grade for the
course.

## Receiving Assistance

If you are having trouble completing any part of this project, then please talk
with either the course instructor or a student technical leader during the
course session. Alternatively, you may ask questions in the Slack workspace for
this course. Finally, you can schedule a meeting during the course instructor's
office hours.
