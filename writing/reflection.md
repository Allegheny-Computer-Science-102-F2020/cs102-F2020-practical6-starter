# Reflection by Add Your Name Here

## Using a fenced code block, please display the output from running your program for range(1, 10)

TODO: Please add the requested fenced code block.

## Explain `if number % 2 == 0:`

TODO: Please provide an explanation of the provided source code statement.

## Explain `number = number // 2`

TODO: Please provide an explanation of the provided source code statement.

## Please use one paragraph to explain the meaning of the following code segment

```
numbers_internal = copy.deepcopy(numbers)
numbers_internal.sort()
```

TODO: Please use one paragraph to explain the meaning of the source code segment.

## Please use one paragraph to explain the meaning of the following test case

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

TODO: Please use one paragraph to explain the meaning and purpose of this test case.

## What was the greatest technical challenge that you faced and how did you overcome it?

TODO: Please provide a response to this question.

## How did this assignment leverage Python source code from previous assignments?

TODO: Please provide a response to this question.

## What is one topic in the scope of this course that you would like to learn more about?

TODO: Please provide a response to this question.

## At your own option, do you have any other insights to share about this assignment?

At your own option, please add more insights about this assignment.
