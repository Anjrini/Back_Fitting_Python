# Back_Fitting_Python

In scenarios where we need to calculate the coefficients of a multiple linear regression but we only have the formulas to calculate the coefficients of a single variable of a linear regression B0 and B1, so in this case we can make use of an iterative approch called back fitting using only the formulas of B0 and B1 to calculate all of the Beta values.

The implementation has been done in Python using a function called back_fitting in the file bf.py.
The variables needed for this function are "response" and "data frame". The "response" has to be supplied as a string name of the column and the data frame as a matrix of numerics (using the Pandas library). Unfortunately categortial variables has to be converted into numerics in advance before applying this function.

The result is a vector containing all the coefficients of a multiple linear regression. The function also shows the number of iterations needed to converge. However, in scenarios where the convergence has not been reached, a message is going to appear in the console confirming that.

Should you have any query, please feel free to contact me.

Best regards,
Mustafa Anjrini


