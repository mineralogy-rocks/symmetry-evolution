# Symmetry Evolution Codebase

The repository we use to answer questions about the symmetry evolution in the light
of paragenetic modes, defined by 📖 [Bob Hazen and Shaunna Morrison in 2021](http://minsocam.org/MSA/Ammin/AM_Preprints/8099HazenPreprint.pdf).

We are using open-access [RRUFF](https://rruff.info/) data for building the warehouse and testing
our hypotheses 🤔.

Clone the repo and feel free to contribute by using command
~~~
git clone git@github.com:mineralogy-rocks/symmetry-evolution.git
~~~

Next, open the repo using your favourite IDE and initialize virtual environment using
~~~
python3 -m venv venv
~~~
Point your IDE to use the Python Interpreter from ``venv/bin/python``.

Next, install all the dependencies in the project from ``src/requirements.txt`` if your IDE didn't installed
those automatically. Navigate to your repo from the terminal and enter:
~~~
1. source venv/bin/activate  # activates virtual environment

2. pip3 install -r src/requirements.txt # install dependencies

3. deactivate # deactivate virtual environment
~~~

All contributors are welcome! 🤗

Please, don't push your code directly into **main**
branch - create new branch instead eg *feature/calculate-symmetry-indices* and use that one for
the development. Once ready for the deployment, you can create a **PR** and Liubomyr Gavryliv will
review your code and merge it into the **main** branch.


## Support

This project No. 3007/01/01 has received funding from the **European Union´s Horizon 2020 research and innovation programme** under the *Marie Skłodowska-Curie grant agreement No. 945478*.


## License

All code is hosted under the [MIT License](LICENSE) -
feel free to reuse it, contribute, share or do anything  you wish as long as you are doing research/science/education.
