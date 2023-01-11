#include <stdio.h>

int a[9][9] = { 0, };

int printing() {
    int i, j, k;
    for (i = 0; i < 9; i++) {
        for (j = 0; j < 9; j++) {
            printf("%d ", a[i][j]);
            if (j == 2 || j == 5) {
                printf("| ");
            }
        }
        printf("\n");
        if (i == 2 || i == 5) {
            printf("------+-------+------");
            printf("\n");
        }
    }
    printf("Write row, colum, number \n");
    printf("ex) 1, 3, 5\n");
    return 0;
}

bool check(int row, int col, int num) {
    int i, j, result = 1;
    if (row < 3) {
        if (col < 3) {
            for (i = 0; i < 3; i++) {
                for (j = 0; j < 3; j++) {
                    if (a[i][j] == num) {
                        printf("error in col:%d row:%d\n", i + 1, j + 1);
                        printf("There is same number in same box\n");
                        printf("\n");
                        result = 0;
                        break;
                    }
                }
            }
        }
        else if (col >= 3 && col < 6) {
            for (i = 0; i < 3; i++) {
                for (j = 3; j < 6; j++) {
                    if (a[i][j] == num) {
                        printf("error in col:%d row:%d\n", i + 1, j + 1);
                        printf("There is same number in same box\n");
                        printf("\n");
                        result = 0;
                        break;
                    }
                }
            }
        }
        else if (col >= 6) {
            for (i = 0; i < 3; i++) {
                for (j = 6; j < 9; j++) {
                    if (a[i][j] == num) {
                        printf("error in col:%d row:%d\n", i + 1, j + 1);
                        printf("There is same number in same box\n");
                        printf("\n");
                        result = 0;
                        break;
                    }
                }
            }
        }
    }
    else if (row >= 3 && row < 6) {
        if (col < 3) {
            for (i = 3; i < 6; i++) {
                for (j = 0; j < 3; j++) {
                    if (a[i][j] == num) {
                        printf("error in col:%d row:%d\n", i + 1, j + 1);
                        printf("There is same number in same box\n");
                        printf("\n");
                        result = 0;
                        break;
                    }
                }
            }
        }
        else if (col >= 3 && col < 6) {
            for (i = 3; i < 6; i++) {
                for (j = 3; j < 6; j++) {
                    if (a[i][j] == num) {
                        printf("error in col:%d row:%d\n", i + 1, j + 1);
                        printf("There is same number in same box\n");
                        result = 0;
                        break;
                    }
                }
            }
        }
        else if (col >= 6) {
            for (i = 3; i < 6; i++) {
                for (j = 6; j < 9; j++) {
                    if (a[i][j] == num) {
                        printf("error in col:%d row:%d\n", i + 1, j + 1);
                        printf("There is same number in same box\n");
                        printf("\n");
                        result = 0;
                        break;
                    }
                }
            }
        }
    }
    else if (row >= 6) {
        if (col < 3) {
            for (i = 6; i < 9; i++) {
                for (j = 0; j < 3; j++) {
                    if (a[i][j] == num) {
                        printf("error in col:%d row:%d\n", i + 1, j + 1);
                        printf("There is same number in same box\n");
                        printf("\n");
                        result = 0;
                        break;
                    }
                }
            }
        }
        else if (col >= 3 && col < 6) {
            for (i = 6; i < 9; i++) {
                for (j = 3; j < 6; j++) {
                    if (a[i][j] == num) {
                        printf("error in col:%d row:%d\n", i + 1, j + 1);
                        printf("There is same number in same box\n");
                        result = 0;
                        break;
                    }
                }
            }
        }
        else if (col >= 6) {
            for (i = 6; i < 9; i++) {
                for (j = 6; j < 9; j++) {
                    if (a[i][j] == num) {
                        printf("error in col:%d row:%d\n", i + 1, j + 1);
                        printf("There is same number in same box\n");
                        printf("\n");
                        result = 0;
                        break;
                    }
                }
            }
        }
    }
    for (i = 0; i < 9; i++) {
        if (a[row][i] == num) {
            printf("error in col:%d row:%d\n", row + 1, i + 1);
            printf("There is same number in same row\n");
            printf("\n");
            result = 0;
        }
    }
    for (i = 0; i < 9; i++) {
        if (a[i][col] == num) {
            printf("error in col:%d row:%d\n", i + 1, col + 1);
            printf("There is same number in same colum\n");
            printf("\n");
            result = 0;
        }
    }
    if (result == 0) {
        return false;
    }
    else if (result == 1) {
        return true;
    }
}

int change(int row, int col, int num) {
    a[row][col] = num;
    return 0;
}

bool checking_end() {
    int i, j;
    bool check=true;
    for (i = 0; i < 9; i++) {
        for (j = 0; j < 9; j++) {
            if (a[i][j] == 0) {
                check = false;
            }
        }
    }
    if (check == true) {
        return true;
    }
    else {
        return false;
    }
}


int main(){
    int row, col, num;
    bool result, done=false;
    a[0][0] = 8;
    a[0][2] = 6;
    a[0][3] = 7;
    a[0][6] = 5;
    a[0][7] = 9;
    a[1][1] = 7;
    a[1][6] = 6;
    a[1][8] = 1;
    a[3][0] = 2;
    a[3][3] = 3;
    a[3][4] = 9;
    a[3][7] = 4;
    a[4][0] = 6;
    a[4][1] = 9;
    a[4][7] = 3;
    a[5][4] = 6;
    a[5][5] = 5;
    a[6][3] = 9;
    a[6][6] = 7;
    a[6][7] = 8;
    a[7][0] = 4;
    a[7][1] = 6;
    a[7][5] = 3;
    a[8][2] = 1;

    while (done!=true) {
//        system("cls");
        printing();
        scanf_s("%d, %d, %d", &row, &col, &num);
        printf("\n");
        row--;
        col--;
        result = check(row, col, num);
        if (result == true) {
            change(row, col, num);
        }
        if (checking_end() == true) {
            done = true;
        }
    }
}
