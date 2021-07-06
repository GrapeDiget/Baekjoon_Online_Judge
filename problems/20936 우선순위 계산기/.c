#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

//// �������� �켱������ ��� 
//int order(char oper) {
//	if (oper == '+')
//		return 0;
//	if (oper == '-')
//		return 0;
//	if (oper == '*')
//		return 1;
//	if (oper == '/')
//		return 1;
//}
//
//// ���� ����� ����
//int cal(int a, char oper, int b) {
//	if (oper == '+')
//		return a + b;
//	if (oper == '-')
//		return a - b;
//	if (oper == '*')
//		return a * b;
//	if (oper == '/')
//		return a / b;
//}
//
//// ���� ��Ÿ���� ����ü
//typedef struct {
//	int heap_index;
//	int term_index;
//	int left;
//	char oper;
//	int right;
//	int result;
//	struct Term *leftlink;
//	struct Term *rightlink;
//} Term;
//
//// �� ������ ���� �Լ�
//Term* create_term(int index, int l, char o, int r) {
//	Term* t = (Term*)malloc(sizeof(Term));
//	t->heap_index = -1;
//	t->term_index = index;
//	t->left = l;
//	t->oper = o;
//	t->right = r;
//	t->result = cal(l, o, r);
//	t->leftlink = NULL;
//	t->rightlink = NULL;
//	return t;
//}
//
//// �� ����
//int heap[100001];
//int heap_size;
//
//#define Parent(i) (heap[i / 2])
//#define Left(i) (heap[2 * i])
//#define Right(i) (heap[2 * i + 1])
//
//// term_A�� term_B���� �켱������ ������ 1�� ���, �ƴϸ� 0�� ���
//int verdict(Term *term_A, Term *term_B) {
//	if (term_A->result > term_B->result) {
//		return 1;
//	}
//	if (term_A->result == term_B->result) {
//		if (order(term_A->oper) > order(term_B->oper))
//			return 1;
//		else if (order(term_A->oper) == order(term_B->oper))
//			if (term_A->term_index < term_B->term_index)
//				return 1;
//	}
//	return 0;
//}
//
//// ���� ���� ����
//void insert_heap(Term* node) {
//	int i;
//	i = ++(heap_size);
//	while(i != 1 && verdict(node, heap[i/2])) {
//		heap[i] = Parent(i);
//		i /= 2;
//	}
//	heap[i] = node;
//}

//
void delete_heap() {}

//
void update_heap() {}

int main() {
	int number=0;
	int i;
	char S[200000];
	char exp[200000];
	int cursor = 0;
	int ch;
	scanf("%s", &S);
	for(i=0; ;i++) {
		ch = S[i];
		if (ch == 0)
			break;
		if(ch >= 48 && ch <= 57)
			number = number*10 + (ch-48);
		else {
			exp[cursor++] = number;
			number = 0;
			exp[cursor++] = ch;
		}
	}
	exp[cursor++] = number;
	
	for(i=0; i<cursor; i++)
		if(exp[i] >= 0 && exp[i] <= 9)
			printf("%d", exp[i]);
		else
			printf("%c", exp[i]);
	
	return 0;
}
