#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

int n;
int* arr;

// �ܼ� ������ �ذ�
int maxSubarray() {

	int maxSum = -100000;
	int sum = 0;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			sum = 0;

			for (int k = i; k <= j; k++) {
				sum = sum + arr[k];
			}
			
			if (maxSum < sum) {
				maxSum = sum;
			}
		}
	}
	
	return maxSum;
}

// �������� �̿�
int maxSubarray2() {

	int maxSum = -100000;
	int sum = 0;

	for (int i = 0; i < n; i++) {
		sum = 0;

		for (int j = i; j < n; j++) {
			sum = sum + arr[j];

			if (maxSum < sum) {
				maxSum = sum;
			}
		}
	}
	
	return maxSum;
}

// DP ���
int maxSubarray3() {

	int maxSum = -100000;
	int sum = 0;

	int *s = (int*)malloc(sizeof(int) * n);

	int i = 0,tmp;

	while (i < n) {

		if (i == 0)
			tmp = 0;
		else
			tmp = s[i - 1];

		s[i] = tmp + arr[i];

		if (maxSum < s[i]) {

			if (s[i - 1] < 0) {

				// ������ �����ϰ� �ٽ� ���� 
				maxSum = arr[i];
				s[i] = arr[i];
			}
			else {
				// ����� ���, �״��
				maxSum = s[i];
			}
		}
		i++;
	}
	return maxSum;
}

int main() {

	n = 10;

	arr = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < 10; i++) {
		scanf("%d", &arr[i]);
	}

	printf("%d", maxSubarray3());

	return 0;
}

