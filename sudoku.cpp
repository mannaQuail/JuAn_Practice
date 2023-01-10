#include <stdio.h>
#include <Windows.h>

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
    a[0][6] = ;
    a[1][2] = 8;
    a[1][4] = 2;
    a[1][5] = 4;
    a[1][7] = 7;
    a[3][0] = 4;
    a[3][1] = 2;
    a[3][4] = 8;
    a[4][0] = 5;
    a[3][0] = 4;

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

// 프로그램 실행: <Ctrl+F5> 또는 [디버그] > [디버깅하지 않고 시작] 메뉴
// 프로그램 디버그: <F5> 키 또는 [디버그] > [디버깅 시작] 메뉴

// 시작을 위한 팁: 
//   1. [솔루션 탐색기] 창을 사용하여 파일을 추가/관리합니다.
//   2. [팀 탐색기] 창을 사용하여 소스 제어에 연결합니다.
//   3. [출력] 창을 사용하여 빌드 출력 및 기타 메시지를 확인합니다.
//   4. [오류 목록] 창을 사용하여 오류를 봅니다.
//   5. [프로젝트] > [새 항목 추가]로 이동하여 새 코드 파일을 만들거나, [프로젝트] > [기존 항목 추가]로 이동하여 기존 코드 파일을 프로젝트에 추가합니다.
//   6. 나중에 이 프로젝트를 다시 열려면 [파일] > [열기] > [프로젝트]로 이동하고 .sln 파일을 선택합니다.
