

#내 답변
int solution(int num1, int num2) {
    if (num1 == num2)
        return 1;
    else return -1;
}

#다른 답변 
int solution(int num1, int num2) {
    int answer = 0;

    return num1 == num2? 1: -1;
}

int solution(int num1, int num2) {
    return num1-num2==0 ? 1 : -1;
}
