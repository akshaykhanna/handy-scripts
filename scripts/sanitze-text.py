import re

def sanitize_text(text):
    # Remove special characters if the same character is repeated more than four times
    sanitized_text = re.sub(r'([^a-zA-Z0-9\s])\1{4,}', '', text)
    # Remove special character from start of line
    sanitized_text = re.sub(r'^\s*([^a-zA-Z0-9\s])', '', sanitized_text, flags=re.MULTILINE)
    # Remove extra spaces if there are more than one space together
    sanitized_text = re.sub(r' {2,}', ' ', sanitized_text)
    return sanitized_text

chapter_obj ={"heading": "Linear Algebra in AI", "text": " The Importance of Linear Algebra in AI Applications\n\nLinear algebra is a fundamental mathematical discipline that has far-reaching implications in the field of artificial intelligence (AI). The concepts and techniques of linear algebra are crucial for understanding and implementing many machine learning algorithms, making it an essential tool for AI applications. In this section, we will explore the significance of linear algebra in AI and why it is a vital component of any AI-related field.\n\n1. Matrix Operations: The Building Blocks of Machine Learning\n\nMachine learning algorithms rely heavily on matrix operations, which are the cornerstone of linear algebra. Matrices are used to represent data, models, and solutions in various AI applications, such as image recognition, natural language processing, and predictive modeling. Linear algebra provides the mathematical frameworks for manipulating these matrices, enabling efficient computation and analysis of large datasets.\n\n2. Vectors and Vector Operations: Essential for Feature Extraction\n\nVectors are another critical component of linear algebra in AI applications. They represent features or attributes of data, such as image pixels, audio samples, or text documents. Linear algebra provides techniques for manipulating vectors, including addition, scalar multiplication, and vector multiplication. These operations are essential for extracting relevant features from raw data, which is a crucial step in many machine learning algorithms.\n\n3. Eigenvalues and Eigenvectors: Key to Dimensionality Reduction\n\nEigenvalues and eigenvectors are powerful tools for dimensionality reduction in AI applications. They allow us to simplify complex datasets by identifying the most important features or dimensions, leading to better performance in machine learning algorithms. Linear algebra provides the mathematical framework for computing eigenvalues and eigenvectors, enabling the extraction of meaningful insights from high-dimensional data.\n\n4. Singular Value Decomposition (SVD): Unlocking Hidden Patterns\n\nSingular value decomposition (SVD) is a linear algebraic technique that unlocks hidden patterns in large datasets. By decomposing a matrix into its singular values and vectors, SVD enables the discovery of latent structures and relationships within the data. This is particularly useful in image recognition, natural language processing, and recommendation systems, where SVD can help extract meaningful features from complex data.\n\n5. Matrix Factorization: Simplifying Complex Models\n\nMatrix factorization is a linear algebraic technique used to simplify complex machine learning models. By decomposing a matrix into two or more simpler matrices, matrix factorization enables the development of more efficient and interpretable models. This is particularly useful in recommender systems, where matrix factorization can help identify user preferences and item characteristics.\n\n6. Optimization Techniques: Leveraging Linear Algebra\n\nOptimization techniques are a crucial component of linear algebra in AI applications. By solving optimization problems using linear algebraic methods, we can find the optimal solutions for various machine learning algorithms, such as linear regression, logistic regression, and neural networks. These optimization techniques are essential for training models and making predictions accurately.\n\n7. Conclusion: The Unifying Force of Linear Algebra\n\nLinear algebra is a unifying force in AI applications, connecting various machine learning algorithms and techniques. By understanding the linear algebraic concepts and techniques, such as matrices, vectors, eigenvalues, eigenvectors, SVD, matrix factorization, and optimization methods, we can develop more efficient and accurate machine learning models. In conclusion, linear algebra is an essential tool for any AI-related field, providing the mathematical frameworks for understanding and implementing machine learning algorithms.", "imagePath": "./output/books/maths_for_ai/images/linear_algebra_in_ai.png"}

text_to_speech = chapter_obj["heading"] + "\n\n" + chapter_obj["text"]
# text = "Hello!!!! ____________________ --------------This is a test sentence ---------------- with @special characters and punctuation!!!"
# text = """
# !Hello!!!! This   is a test sentence with @special characters  and punctuation!!!
#     !Another   sentence with !!!! some bullet points
#         !And even more ********* with !! bullet points!!
#         __________ ============= !!!!!
#         *a=b+c
# """
# write text to file
# sanitized_text = sanitize_text(text)
with open("text-pre.txt", "w") as f:
    f.write(text_to_speech)
sanitized_text = sanitize_text(text_to_speech)
print(sanitized_text)
with open("text.txt", "w") as f:
    f.write(sanitized_text)
