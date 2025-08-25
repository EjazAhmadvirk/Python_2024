import java.util.Scanner;

public class TicTacToe {

    static char[][] board = {
        { ' ', ' ', ' ' },
        { ' ', ' ', ' ' },
        { ' ', ' ', ' ' }
    };

    public static void printBoard() {
        System.out.println("\n");
        for (int i = 0; i < 3; i++) {
            System.out.println(" " + board[i][0] + " | " + board[i][1] + " | " + board[i][2]);
            if (i < 2) {
                System.out.println("---+---+---");
            }
        }
        System.out.println("\n");
    }

    public static boolean checkWinner(char player) {
        // Rows
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == player && board[i][1] == player && board[i][2] == player)
                return true;
        }
        // Columns
        for (int j = 0; j < 3; j++) {
            if (board[0][j] == player && board[1][j] == player && board[2][j] == player)
                return true;
        }
        // Diagonals
        if (board[0][0] == player && board[1][1] == player && board[2][2] == player)
            return true;
        if (board[0][2] == player && board[1][1] == player && board[2][0] == player)
            return true;

        return false;
    }

    public static boolean isDraw() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == ' ')
                    return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char currentPlayer = 'X';
        boolean gameOver = false;

        System.out.println("🎮 Welcome to Tic Tac Toe!");
        printBoard();

        while (!gameOver) {
            System.out.println("Player " + currentPlayer + "'s turn.");
            System.out.print("Enter row (0,1,2): ");
            int row = sc.nextInt();
            System.out.print("Enter column (0,1,2): ");
            int col = sc.nextInt();

            if (row < 0 || row > 2 || col < 0 || col > 2) {
                System.out.println("❌ Invalid position! Try again.");
                continue;
            }

            if (board[row][col] != ' ') {
                System.out.println("❌ Cell already taken! Try again.");
                continue;
            }

            board[row][col] = currentPlayer;
            printBoard();

            if (checkWinner(currentPlayer)) {
                System.out.println("🎉 Player " + currentPlayer + " wins! 🎉");
                gameOver = true;
            } else if (isDraw()) {
                System.out.println("🤝 It's a draw!");
                gameOver = true;
            } else {
                currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
            }
        }

        sc.close();
    }
}
