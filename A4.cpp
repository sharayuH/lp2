/*
 * Assg62.cpp
 *
 *  Created on: 04-Nov-2020
 *      Author: Isha
 */

/*
#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;
void printBoard(vector<vector<int>> &board)
{
    for (int i = 0; i < board.size(); i++)
    {
        for (int j = 0; j < board.size(); j++)
        {
            cout << board[i][j] << "\t";
        }
        cout << endl;
    }
}
bool isSafe(vector<vector<int>> &board, int x, int y)
{

    for (int row = 0; row < x; row++)
    {
        if (board[row][y] == true)
        {
            return false;
        }
    }

    int row = x;
    int col = y;

    while (row >= 0 && col >= 0)
    {
        if (board[row][col] == true)
        {
            return false;
        }
        row--;
        col--;
    }
    row = x;
    col = y;

    while (row >= 0 && col < board.size())
    {
        if (board[row][col] == true)
        {
            return false;
        }
        row--;
        col++;
    }
    return true;
}
// x: row fixed
bool helper(vector<vector<int>> &board, int x)
{
    int n = board.size();
    // base case:
    if (x >= n)
    {
        return true;
    }
    else
    {
        for (int col = 0; col < n; col++)
        {
            if (isSafe(board, x, col))
            {
                board[x][col] = 1;

                if (helper(board, x + 1))
                {
                    return true;
                }
                // if not true: there's a problem in the placing of a queen in a row A
                // backtrack the solution to change the position of the previous queen if possible
                board[x][col] = 0;
            }
        }
    }
    return false;
}
void NQueen_Backtrack(int N)
{
    vector<vector<int>> board(N, vector<int>(N, 0));
    if (helper(board, 0))
    {
        printBoard(board);
    }
    else
    {
        cout << "No solution found";
    }
}


bool isSafe_2(int row, int col, vector<vector<int>> &slashCode, vector<vector<int>> &backslashCode,
              vector<bool> &rowLookup, vector<bool> &slashCodeLookup, vector<bool> &backslashCodeLookup)
{
    if (slashCodeLookup[slashCode[row][col]] || backslashCodeLookup[backslashCode[row][col]] ||
        rowLookup[row])
        return false;

    return true;
}

bool recurNqueen_2(vector<vector<int>> &board, vector<vector<int>> &slashCode,
                   vector<vector<int>> &backslashCode, vector<bool> &rowLookup,
                   vector<bool> &slashCodeLookup, vector<bool> &backslashCodeLookup, int col)
{

    int N = rowLookup.size();
    // base case: If all queens are placed then return true
    if (col >= N)
        return true;

    // Consider the column col and try placing the queen in all rows one by one
    for (int i = 0; i < N; i++)
    {
        // Check if queen can be placed on board[i][col]
        if (isSafe_2(i, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup))
        {
            // Place this queen in board[i][col]
            board[i][col] = 1;
            rowLookup[i] = true;
            slashCodeLookup[slashCode[i][col]] = true;
            backslashCodeLookup[backslashCode[i][col]] = true;

            // recursive call to place rest of the queens
            if (recurNqueen_2(board, slashCode, backslashCode, rowLookup, slashCodeLookup,
                              backslashCodeLookup, col + 1))
                return true;

            // /If placing queen in board[i][col]
            // doesn't lead to a solution, then backtrack
            // Remove queen from board[i][col]

            board[i][col] = 0;
            rowLookup[i] = false;
            slashCodeLookup[slashCode[i][col]] = false;
            backslashCodeLookup[backslashCode[i][col]] = false;
        }
    }

    // If queen can not be place in any row in
    // this column col then return false
    return false;
}

void voidNQueen_2(int N)
{
    // create a board of size N X N
    vector<vector<int>> board(N, vector<int>(N, 0));

    // helper matrices
    vector<vector<int>> slashCode(N, vector<int>(N, 0));
    vector<vector<int>> backslashCode(N, vector<int>(N, 0));

    // array to tell us which rows are occupied
    vector<bool> rowLookup(N, false);

    // maintain two arrays to tell us which diagonals are occupied
    vector<bool> slashCodeLookup(2 * N - 1, false);
    vector<bool> backslashCodeLookup(2 * N - 1, false);

    // initialize helper matrices with their respective values
    for (int r = 0; r < N; r++)
    {
        for (int c = 0; c < N; c++)
        {
            slashCode[r][c] = r + c,
            backslashCode[r][c] = r - c + (N - 1);
        }
    }
    if (recurNqueen_2(board, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup, 0) == false)
    {
        cout << "No placing possible\n\n";
        return;
    }

    // solution found
    printBoard(board);
    return;
}
int main()
{
    int opt;
    while (true)
    {
        cout << "\n-------------------------------------------------------------------------------\n1.Solve N Queens Problem using Backtracking\n2.Solve N Queens Problem using Branch Bound\n3.Exit\n-------------------------------------------------------------------------------\n";
        cout << "Select an option: ";
        cin >> opt;
        if (opt == 1)
        {
            int N;
            cout << "Enter the dimension of chess board :";
            cin >> N;
            NQueen_Backtrack(N);
        }
        else if (opt == 2)
        {
            int N;
            cout << "Enter the dimension of chess board :";
            cin >> N;
            voidNQueen_2(N);
        }
        else
        {
            break;
        }
    }
}
*/
