import csv

def find_specific_hypothesis():
    """Calculates the maximally specific hypothesis for the EnjoySport dataset."""

    num_attributes =4  # Number of attributes (excluding the classification)
    a = []  # List to store the training data

    # Open and read the CSV data
    print("\nThe Given Training Data Set \n")
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            a.append(row)
            print(row)

    # Initialize the hypothesis with the first instance's values
    print("\nThe initial value of hypothesis: ")
    hypothesis = ['0'] * num_attributes  
    for j in range(0, num_attributes):
        hypothesis[j] = a[0][j] 
    print(hypothesis) 

    # Find S: Finding a Maximally Specific Hypothesis
    print("\nFind S: Finding a Maximally Specific Hypothesis\n")
    for i in range(0, len(a)):
        if a[i][num_attributes] == 'YES':  # Check for positive examples
            for j in range(0, num_attributes):
                if a[i][j] != hypothesis[j]:
                    hypothesis[j] = '?'  # Generalize where attributes differ
                else:
                    hypothesis[j] = a[i][j]  # Maintain current value
        print("For Training instance No:{0} the hypothesis is ".format(i), hypothesis)

    # Display the final hypothesis
    print("\nThe Maximally Specific Hypothesis for a given Training Examples :\n")
    print(hypothesis) 

# Call the function to start the process
find_specific_hypothesis()

