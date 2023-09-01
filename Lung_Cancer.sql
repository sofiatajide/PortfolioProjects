-- looking at the total values in the dataset
SELECT COUNT(*) AS TotalValues
FROM lung_cancer;

-- looking at the  average age of individuals in the given dataset
SELECT AVG(Age) AS AverageAge
FROM lung_cancer;

-- looking at the total count of 'Smokers' in the given dataset
SELECT COUNT(*) AS TotalSmokers
FROM lung_cancer
WHERE Smokes = 'YES';

-- looking at the 'Name', 'Age', and 'Alcohol Category' columns for 'Mediocore Drinkers'
SELECT Name, Age, Alcohol_Category
FROM lung_cancer
WHERE Alcohol_Category = 'Mediocre Drinkers';

-- looking at the 'Name' and 'Age' of the oldest individual in the given dataset.
SELECT Name, Age
FROM lung_cancer
WHERE Age = (SELECT MAX(Age) FROM lung_cancer);

-- looking at the 'Name' and 'Surname' of individuals whose names start with 'A'.
SELECT Name, Surname
FROM lung_cancer
WHERE Name LIKE 'A%';

-- looking at the 'Name', 'Age', and 'Alcohol' columns for individuals who are both 'Heavy Smokers' and 'Mediocre Drinkers'
SELECT Name, Age, Alcohol
FROM lung_cancer
WHERE Smoking_Category = 'Heavy Smokers'
  AND Alcohol_Category = 'Mediocre Drinkers';
  
-- looking at the percentage of lung cancer for individuals whose age is greater than 18.
SELECT
    Result,
    COUNT(*) AS Count,
    FORMAT((COUNT(*) / (SELECT COUNT(*) FROM lung_cancer WHERE Age > 18)) * 100, 5) AS Percentage
FROM lung_cancer
WHERE Age > 18
GROUP BY Result;

-- looking at the names and ages of individuals whose names contain the word "John".
SELECT Name, Age
FROM lung_cancer
WHERE Name LIKE '%John%';

-- looking at the count of people who have lung cancer with different 'Smoking Category'.
SELECT
    CASE
        WHEN Smoking_Category = 'Mediocre Smokers' THEN 'Mediocre Smokers'
        WHEN Smoking_Category = 'Heavy Smokers' THEN 'Heavy Smokers'
    END AS Smoking_Category,
    COUNT(*) AS Count
FROM lung_cancer
WHERE Result = 1
  AND (Smoking_Category = 'Mediocre Smokers' OR Smoking_Category = 'Heavy Smokers')
GROUP BY Smoking_Category;

-- looking at the count of people who have lung cancer with different 'Alcohol Category'.
SELECT Alcohol_Category, COUNT(*) AS Count
FROM lung_cancer
WHERE Result = 1
GROUP BY "Alcohol Category";
