class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0) return false;
        return search(matrix, target, 0, matrix[0].length-1);
    }
    
    private boolean search(int[][] matrix, int target, int i, int j) {
        while (i<matrix.length && j>=0) {
            if (matrix[i][j]==target) return true;
            else if (matrix[i][j]>target) j--;
            else i++;
        } return false;
    }
}
