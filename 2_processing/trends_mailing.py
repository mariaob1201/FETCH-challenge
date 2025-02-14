'''
Maria Oros
Third: communicate with stakeholders
Construct an email or slack message that is understandable to a product or business leader
who is not familiar with your day-to-day work. Summarize the results of your investigation. Include:

Key data quality issues and outstanding questions about the data
One interesting trend in the data
Use a finding from part 2 or come up with a new insight
Request for action: explain what additional help, info, etc. you need to make sense of the data and resolve any outstanding issues

--------------------------------

Dear Stakeholders,

Thank you for your patience as I have been reviewing the data related to transactions, products, and users. After analyzing the dataset, I would appreciate your assistance in addressing a few minor and major points to ensure a more accurate analysis. Some of these points may require collaboration with the SE team to streamline the data for easier analysis.

Technical Details (to Address with the SE Team):
- Data Types: It would be beneficial to standardize the formatting of all time-related fields across entities, ensuring consistency with Central Time and a uniform format.
- Non-Numerical Sales and Quantity Values: Some sales and quantity data contain non-numerical values, which lead to inconsistencies and make trend analysis difficult. Addressing this will improve the reliability of the dataset for analysis.
- Barcode Data Consistency: As barcode data is critical, ensuring consistency in its data type across the dataset is essential.
- Missing Barcode Data: There is a small portion of missing barcode data. While not critical, addressing this would improve the completeness of the dataset.
- Duplicate Transactions: I’ve identified duplicates in the transactions dataset. While these are not significant, it may be worth investigating whether they are due to data entry or pipeline errors.
- Merging Datasets: I encountered challenges when merging the datasets into a single entity.

I mention those points because ensuring consistent formatting across entities and mitigate any potential error from our pipelines will be critical to have later accurate and reliable analysis from the Data Analysis team.

Business Sales Trends:
- After thoroughly exploring the data, I have identified the following key findings:
- Transaction Period: The data primarily reflects transactions from the year 2024.
- Sales Trends:
    June to July 2024: An increase in total sales.
    July to August 2024: A slight dip in sales, followed by a recovery from August to September 2024.
    Monthly Growth: Average monthly sales increments ranged between 3.6% and 4%. However, July showed high variation from the mean, suggesting potential correlation with internal processes or specific brands.
- Sales and Customer Age: No clear pattern was observed between sales and customer age, indicating that age may not be a strong predictor in this case.
- Product Category Insights:
    Most Frequent Sales: Snacks are the most frequently sold products, followed by Health and Wellness.
    Top Sales Category: Alcohol consistently led in total sales, with beer accounting for 57% of alcohol sales.
    Sales Consistency: Alcohol shows a higher mean sales over time, indicating a strong and stable sales performance.
Statistical Significance: There are statistically significant differences in sales across product categories, which suggests that a focus on certain brands or categories could potentially optimize sales further.

Next Steps:
Collaboration with SE Team: I would like to schedule a meeting with the SE team to discuss how we can enhance the data pipeline and align our efforts to better support this analysis.
Sales Perspective Feedback: It would be helpful to get your input on the direction I’m currently taking with the sales analysis, to ensure we are aligned and moving on what provides value to Fetch.

If you have any questions please let me know,
Maria
'''




