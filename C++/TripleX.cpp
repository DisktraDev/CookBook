#include <iostream>
#include <ctime>

void PrintIntroduction(int Difficulty)
{
    // Print welcome messages to the terminal
    std::cout << "You are a secret agent breaking into a level "<< Difficulty <<" secure server room\n";
    std::cout << "Enter the correct code to continue\n\n";
}

bool PlayGame(int Difficulty)
{
    PrintIntroduction(Difficulty);

    // Declare 3 number code
    const int CodeA = rand() % Difficulty + Difficulty;
    const int CodeB = rand() % Difficulty + Difficulty;
    const int CodeC = rand() % Difficulty + Difficulty;

    int CodeSum = CodeA + CodeB + CodeC;
    int CodeProduct = CodeA * CodeB * CodeC;

    // Print CodeSum and CodeProduct to the terminal
    std::cout;
    std::cout << "+ There are 3 numbers in the code";
    std::cout << "\n+ The codes add-up to: " << CodeSum;
    std::cout << "\n+ The codes multiply to give: " << CodeProduct << std::endl;

    // Store player guess
    int GuessA, GuessB, GuessC;
    std::cin >> GuessA >> GuessB >> GuessC;
    
    int GuessSum = GuessA + GuessB + GuessC;
    int GuessProduct = GuessA * GuessB * GuessC;

    // Check if the player guess is correct
    if(GuessSum == CodeSum && GuessProduct == CodeProduct)
    {
        std::cout << "\nYou've entered the right code.\n";
        return true;
    } else
    {
        std::cout << "\nThe code you've entered makes the system changes the code. Be carefull...\n";
        return false;
    }
    
}

int main()
{
    srand(time(NULL)); // create new random sequence based on time of day

    int LevelDifficulty = 1;
    const int MaxLevel = 5;

    while (LevelDifficulty <= MaxLevel) // Loop game until all levels completed
    {
        
        bool bLevelComplete = PlayGame(LevelDifficulty);
        std::cin.clear(); // Clears any errors
        std::cin.ignore(); // Discards the buffer

        if (bLevelComplete)
        {
            ++LevelDifficulty;
        }
        
    }

    std::cout << "\n\nCongratulations !! You beat the game !\n";
    
    return 0;
}