class Solution {
    public int[][] allCellsDistOrder(int R, int C, int r0, int c0) {
        int[][] cells = new int[R*C][2];
        int index = 0;
        int n = 0;
        while (index<cells.length){
            for (int i = 0; i <= n; i++){
                int k = -1;
                int p = -1;
                for (int j = 0; j<4;j++){
                    if (j%2 == 0){
                        k *= -1;
                    }
                    p *= -1;
                    int r1 = r0 + k*i;
                    int c1 = c0 + p*(n - i);
                    if (i==n && j%2 != 0){
                        continue;
                    }
                    if (i==0 && j>=2){
                        continue;
                    }
                    
                    if (0<=r1 && r1<R && 0<=c1 && c1<C){
                        int[] additional = {r1, c1};
                        cells[index] = additional;
                        index++;
                    }
                    if (index>=cells.length){
                        break;
                    }
                }
                if (index>=cells.length){
                    break;
                }
            }
            n++;
        }
        return cells;     
    }
            
}
