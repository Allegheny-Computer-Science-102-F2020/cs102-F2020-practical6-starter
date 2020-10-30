"""Define the command-line interface for the collatzcreator program."""

from typing import List

from matplotlib import pyplot

import typer


from collatzcreator import collatz
from collatzcreator import summarize


def main(
    number: List[int] = typer.Option([]),
    minimum: int = typer.Option(1),
    maximum: int = typer.Option(10),
):
    """Run an experiment with the Collatz function to see if it terminates for each given number."""
    # TODO: Make sure that you understand how this function handles the command-line arguments
    # create a list of the input numbers that has
    # a name that is more convenient to remember
    collatz_inputs = list(number)
    # if no list of numbers was specified through the (potentially repeated)
    # use of the "--number" command-line argument, then create a list of
    # values using the range for a specified minimum and maximum value
    if collatz_inputs == []:
        collatz_inputs = list(range(minimum, maximum))
    # create an empty list that can store the length of the Collatz chain
    collatz_output_list_length = []
    # display the debugging output for the program's command-line arguments
    typer.echo("")
    typer.echo("Let's investigate the behavior of the Collatz sequence! 🔍")
    typer.echo("")
    typer.echo("Does this sequence of numbers finish at the value of 1? ✨")
    # execute the collatz function for each of the numbers in the list
    for collatz_input in collatz_inputs:
        collatz_output_generator = collatz.Collatz(collatz_input)
        # materialize the list from the returned generator function
        collatz_output_list = list(collatz_output_generator)
        collatz_output_list_length.append(len(collatz_output_list))
    # display the details about the numbers that were input to the function
    typer.echo("")
    typer.echo("The inputs to the Collatz function:")
    typer.echo("")
    typer.echo("  " + str(collatz_inputs))
    # display the details about the length of the output chain
    typer.echo("")
    typer.echo("The length of the resulting Collatz chain:")
    typer.echo("")
    typer.echo("  " + str(collatz_output_list_length))
    typer.echo("")
    # TODO: Make sure that you understand how the min and max functions work
    # display the minimum and maximum length of the Collatz chain
    minimum_chain_length = min(collatz_output_list_length)
    maximum_chain_length = max(collatz_output_list_length)
    typer.echo(f"The minimum length of a Collatz chain is: {minimum_chain_length}")
    typer.echo(f"The maximum length of a Collatz chain is: {maximum_chain_length}")
    typer.echo("")
    # TODO: Make sure that you understand how this program uses the summarize module
    # display the mean, median, and standard deviation of the length of the Collatz chain
    mean_chain_length = summarize.compute_mean(collatz_output_list_length)
    median_chain_length = summarize.compute_median(collatz_output_list_length)
    stdev_chain_length = summarize.compute_standard_deviation(
        collatz_output_list_length
    )
    typer.echo(f"The mean of the length of a Collatz chain is: {mean_chain_length}")
    typer.echo(f"The median of the length of a Collatz chain is: {median_chain_length}")
    typer.echo(
        f"The standard deviation of the length of a Collatz chain is: {stdev_chain_length}"
    )
    typer.echo("")
    # TODO: Make sure that you understand how this program creates the graph
    # create a visualization in the form of a scatter plot
    # Reference:
    # https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html
    pyplot.style.use("seaborn-whitegrid")
    pyplot.plot(collatz_inputs, collatz_output_list_length, "o", color="black")
    pyplot.xlabel("Integer Input to the Collatz Function")
    pyplot.ylabel("Length of the Output Collatz Chain")
    # save the scatterplot in a PDF that a person can easily view
    pyplot.savefig("collatz.pdf")
    # display a question about the relationship between the input number and the length of the chain
    typer.echo(
        "Can you find a pattern between the input number and the length of the Collatz chain? 🤷"
    )
    typer.echo("")
    typer.echo(
        "Check the file called 'collatz.pdf' to see a graph that visualizes the results! 📈"
    )
    typer.echo("")


if __name__ == "__main__":
    typer.run(main)
