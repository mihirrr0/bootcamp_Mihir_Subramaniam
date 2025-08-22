## Homework 6: Cleaning Strategy

# fill_missing_median(df, columns)
Fills missing values in the specified columns with their median values. Useful for numeric data where you want to impute missing entries without skewing the distribution.

# drop_missing(df, threshold=0.5)
Drops rows where the proportion of missing values exceeds the given threshold (e.g., 0.5 means more than 50% of a row’s values are missing). Helps remove incomplete records while keeping most of your data intact.

# normalize_data(df, columns)
Scales the specified columns to a [0, 1] range using min-max normalization. Great for preparing numeric data for machine learning models that require standardized input.

