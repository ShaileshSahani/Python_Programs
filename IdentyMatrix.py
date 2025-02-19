class MATRIX:

    @classmethod
    def identity_matrix(cls, __x, __y):
        mat = []
        if __x == __y:
            for i in range(__x):
                sub_mat = []
                for j in range(__y):
                    if i == j:
                        sub_mat.append(1)
                    else:
                        sub_mat.append(0)
                mat.append(sub_mat)
            for i in range(__x):
                for j in range(__y):
                    print(mat[i][j], end="  ")
                print()
        else:
            print('Only a square matrix can be a identity matrix')


row = int(input())
col = int(input())
MATRIX.identity_matrix(row, col)
