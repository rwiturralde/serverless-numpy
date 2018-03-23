# NumPy Wrapper
Simple [AWS Lambda](https://aws.amazon.com/lambda) function that wraps the popular python library, [NumPy](http://www.numpy.org/).

## Usage
#### Input
The AWS Lambda function event expects an JSON dictionary with two entries: 'method' and 'arguments'.
* method - String - The name of the NumPy method to invoke
* arguments - Array - An ordered array of arguments to pass to the method.

```json
{
  "method": "some_method",
  "arguments": [
    1,
    2,
    3
  ]
}
```

#### Output
The return JSON dictionary will contain a single entry: 'result' holding the result of the computation. If an error occurs, the function will return the [AWS Lambda error object](https://docs.aws.amazon.com/lambda/latest/dg/python-exceptions.html).

```json
{
  "result": 123.456
}
```

## Examples

Computing [future value](https://docs.scipy.org/doc/numpy/reference/generated/numpy.fv.html) 
```json
{
  "method": "fv",
  "arguments": [
    0.004166666666666666,
    120,
    -100,
    -100
  ]
}
```

Computing the [net present value](https://docs.scipy.org/doc/numpy/reference/generated/numpy.npv.html) of a cash flow series.
```json
{
  "method": "npv",
  "arguments": [
    0.281,
    [
      -100,
      39,
      59,
      55,
      20
    ]
  ]
}
```
##