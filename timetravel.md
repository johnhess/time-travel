# Coding Practices Worth Stealing from Industry

---

## Who am I?

* Former TPPer
* Perpetrator of countless great sins of programming
* Working software engineer, among other things

## Presenter Notes

* Repentent sinner, I have been to the desert and seen the light!

---

## What's this talk about?

* Sharing a few things I wish *I'd* have known 7 years ago when I started creating a body of research built on thousands of lines of code
* Giving you some practices to think about and tools to try them out
* Dispelling belief in magic (maybe)

## Presenter Notes

* I don't claim to know everything, this is just about what I *do* know, and feel is worth sharing
* Having some threads to pull
* Some people -- or at least I -- have this belief in magic.  Magic is anything you don't understand *yet*.  Sufficiently advanced technology and all that.  Maybe you know how to program, but the idea of making a web application like facebook is still a dark art.  Or Artificial Intelligence which is basically sorcery until someone points out it's really just statistics and for loops.

---

# What's this talk *not* about?

<img src="images/python.jpg" />

.fx: imageslide whiteheading

---

## Why bother?

As we all know, research, collaboration, peer review and publishing are perfect processes because people don't make mistakes and always understand one another perfectly.

Right...

---

So, let's take a look at a few things we could do better.

* Correctness
* Collaboration
* Replicability
* Publishing code

---

<img src="images/reinhart-rogoff.jpg" />

---

<img src="images/reinhart-rogoff-colbert.jpg" />

.fx: imageslide

## Presenter Notes

* It's never good to see your face in the monologue...

---

## Getting code right turns out to be difficult...

* Hard to believe, but this isn't a problem unique to Harvard!
* Industry Average: "about 15 - 50 errors per 1000 lines of delivered
code." *[Code Complete, Steve McConnel]*
* Your research is important &#8756; *correctness matters*.
* There are tools for this!

---

How do *you* verify correctness?

---

# Automated Testing

---

## Automated Testing

Code that tests other code.  It has the same advantages code does:

* It's fast & easy
* It's consistent
* Other people can read it

## Presenter Notes

Until a friend and mentor of mine sat with me and helped me write my first tests, testing was black magic to me.  

The difference it's made in my productivity & quality is too big to understate.

---

<img src="images/beautiful-mind.jpg" />

.fx: imageslide

---

## Example!

    !python
    # fib.py
    def fib(n):
        # recursively calculate Fibonaacci numbers
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)


---

How do we know it's right?  I mean, it *looks* right...  Right?

---

## A test!

    !python
    # tests.py
    from fib import fib

    def test_fib_output():
        # Check some known values
        assert fib(0) == 0
        assert fib(1) == 1
        assert fib(2) == 1
        assert fib(3) == 2
        assert fib(4) == 3
        assert fib(5) == 5

---

## Run the tests!

(nosetests is just a program that automatically finds and runs your tests)

    !bash
    $ nosetests
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s

    OK

Success!

---

## Good!  Now what?

On with our lives!  We can change the code, our colleagues can change it, we can build on top of it, etc.

Alas, we soon find that this algorithm only gets us so far.

    !python
    >>> fib(1000)
    ...
    RuntimeError: maximum recursion depth exceeded

Well, crap.

---

## Crap!  Now what?

We *could* just go and fix this.

But we can do one better!  Let's write a *new* test to cover this case:

    !python
    def test_fibr_large_numbers():
        assert fibr(1000) > 0 # who even knows the 1000th Fibonacci number?!

and run it...

---

## Run the tests!

    !bash
    .E
    ----------------------------------------------------------------------
    Ran 2 tests in 0.015s

    FAILED (errors=1)
    Failed - Back to work!

---

## A safety net for our high-flying mathematical and programming tricks

Let's replace our recursive `fib()` function with an iterative one!

Normally, we'd have to be really careful and make sure the new one just right.  But instead, we have tests now to make sure we don't break anything.

---

## A safety net for our high-flying mathematical and programming tricks

Iterative version!

    !python
    # fib.py
    def fib(n):
        # iterative Fibonaacci calculation
        a, b = 0, 1
        for i in range(0, n):
            a, b = b, a + b
        return a

Now run our exact same existing tests...

---

## Run the tests!

    !bash
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.015s

    OK

Hooray!

---

## Testing

* Tests at different levels
    * lowest levels (a.k.a. "Unit Testing")
    * highest levels (a.k.a. "Functional/Integration Testing")
* Check out what's available in your language.  You'd be surprised how easy people have made it to write and run tests.

---

# Collaboration

## Presenter Notes

Including collaboration with *future* you!

---

How do you collaborate with your colleagues?  Email?  Dropbox?  Something better?  Something worse?

Who here routinely runs software written by other researchers?  Who improves on it?

## Presenter Notes

* This is a big problem out there in the world, and it only gets bigger as you work on more in-depth projects
* It's not only a problem you find, but *if you have a solution*, you can do all sorts of things nobody'd bother with in the first place, like building off one another's code instead of writing every damned thing from scratch.

---

## Enter Version Control

*The* way that coders collaborate in the modern world.


---

## Wisdom from Stack Overflow 

Have you ever:

* Made a change to code, realised it was a mistake and wanted to revert back?
* Lost code or had a backup that was too old?
* Had to maintain multiple versions of a product?
* Wanted to see the difference between two (or more) versions of your code?
* Wanted to prove that a particular change broke or fixed a piece of code?

## Presenter Notes

...you *do* use Stack Overflow, right?

---

* Wanted to review the history of some code?
* Wanted to submit a change to someone else's code?
* Wanted to share your code, or let other people work on your code?
* Wanted to see how much work is being done, and where, when and by whom?
* Wanted to experiment with a new feature without interfering with working code?

*(courtesy of the illustrious SO user si618, content CC BY-SA)*

---

## Okay, okay.  I see the light!  How do I use version control?

Think of it like email.

Github : Git :: Gmail : Email

## Presenter Notes

* Explain email analogy.  Talk about command line, GUI, web-based, etc.
* There's this other neat corrolary of that relationship.  When you have such a well defined protocol lots of stuff works with it (foreshadowing!)
* You thought you were done with those after you took the SAT, huh?

---

## How to use Git in 5 minutes or less

*(or, how to keep your sanity working in teams!)*

We start by creating a git repository and hosting it somewhere everyone can get to it.  Think of it like a dropbox folder with super powers tailor made for coding.

---

All the cool kids these days are using github, so we will too!

<img src="images/silicon-valley-tv-show.jpg" />

---

## Step 0: Make that repository! 

Creating a repository is actually pretty easy, and GitHub's documentation is particularly good:

https://help.github.com/ 

*(see "Good Resources for Learing Git and Github")*

---

## Desktop GUI applications

<img src="images/github-desktop.png" />

## Presenter Notes

Remember, it's like email -- you can use git via a GUI

---

## The command line

<img src="images/github-terminal.png" />

---

## Web applications

*(at least for some functionality)*

<img src="images/github-web.png" />

---

## Make some changes on their own "branch"

* Git is *all* about changes!

---

## When those changes are ready, pull them into the master version

* If you've ever heard the term "Pull Request", that's exactly what we're talking about
* You can use this on your own or with a team
* It means multiple people can work on the same code without ending up with the dreaded diverging "personal" versions

<img src="images/git-branches.png" />

---

## The "Pull Request"

* This is where it gets cool!
* A more true to life example

## Presenter Notes

* We were perfectly happy with our (slow & limited) recursive fibonacci number calculator, but one of our labmates is using our code and pesky, such as labmates are, they need it to calculate really big fibonacci numbers
* We get to go with the famous and passive agressive (in some circles) "Pull Requests Welcome!"
    * In other words, you want it, you write it!
    * Plus, we can optionally pull those changes back into our master version!

---

## An example Pull Request

<img src="images/pull-request-convo.png" />

---

## An example Pull Request

<img src="images/pull-request-diff.png" />

---

## So with just a bit of git-fu

* You can publish/distribute your code in a convenient way
    * You can even mark specific versions like ("As used in Paper XYZ")
* You can work on the same code with others in your lab or around the world
* So, so much more (just you wait and see...)

---

## Oh! And, you can use it for other things!

* Multiple people try to edit one thing... sound familiar?
* These slides! [https://github.com/johnhess/time-travel](https://github.com/johnhess/time-travel)

---

<img src="images/version-all-the-things.jpg" />

.fx: imageslide

---

## A brief reality check

* Git actually has a pretty steep learning curve :-/

But, if you program every week and especially if you program with other people it is *SO* worth learning.

## Presenter Notes

And it works with all sorts of great tools

---

# Let's be serious academics for a minute

---

# Publishing

## Presenter Notes

It matters.

We can go through the motions, but we can also do better.

And, we can do better in two ways.

* Replicability
* Reach

---

## Replicability

* Publish your methodology
* *Publish your code*
    * Archivally
    * Accessibly
    * Understandably
    * Extensibly
    * Interactively

---

# Crash Course:  Internet

<img src="images/client-server.svg" />

## Presenter Notes

Administering and maintaining the whole thing is expensive and time consuming.

There is a better way!

---

# Use a Cookie Cutter!

<img src="images/cookie-cutter.jpg" />

.fx: imageslide whiteheading

## Presenter Notes

I can't stress enough how many ways there are to make software available on the Internet.

I'll talk about just one, my favorite, but there are many, many good ones out there.

It turns out that this makes life easier even if you don't use heroku, etc.

---

## Heroku

* Give it your code
* Makes running version available at yourthing.herokuapp.com

---

## What shape is this cookie-cutter?

* Needs to be in a supported language
* Needs one script to run that can "answer the phone"
    * What should the user get at `yourthing.herokuapp.com`
    * What should the user get at `yourthing.herokuapp.com/some/path/to/thing/10`
* Needs to know how to start that script
* Needs to know what dependencies you code has (any libraries you use, etc.)

---

If only there was a good way to express exactly what that looked like compared to our existing code...

---

If only there was a good way to express exactly what that looked like compared to our existing code...

[A wild pull request appeared](https://github.com/johnhess/fibonacci/pull/3/files)

---

# [Heroku Demo]

## Presenter Notes

* Walk through pull request
* Heroku
    * Create application
    * It attaches straight to github, that's cool
    * 

---

So, starting from our original fibonacci code, we've got

* Some guarantee of correctness
* A medium for collaboration
* A sane way for others to inspect and run the code behind our research publications
* A sane way for others to offer improvements
* A way to reach non-coders and share the ideas in our code

---

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
John Hess
<br/>
john@jthess.com