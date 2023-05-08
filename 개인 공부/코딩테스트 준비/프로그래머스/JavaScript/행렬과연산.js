function solution(rc, operations) {
    
    function shiftRow(array) {
        const lastArr = array.pop();
        return [lastArr, ...array]
    }
    
    function rotate(array) {
        let cur, r=0, c=0, move=0,nc,nr,next;
        const dr = [0,1,0,-1];
        const dc = [1,0,-1,0];
        const ROWLENGTH = array.length;
        const COLOMNLENGTH = array[0].length;
        
        cur = array[r][c];
        
        while(true) {
            nr = r + dr[move];
            nc = c + dc[move];
            if (nr >= 0 && nc >= 0 && nr < ROWLENGTH && nc < COLOMNLENGTH) {
                next = array[nr][nc];
                array[nr][nc] = cur;
                cur = next;
                r = nr;
                c = nc;
            } else {
                nr -= dr[move];
                nc -= dc[move];
                move = (move+1) % 4;
            }
            if (!nr && !nc) break;
        }
        return array;
    }
    
    for (const a of operations) {
        if (a === 'Rotate') rc=rotate(rc);
        else rc = shiftRow(rc);
    }
    
    return rc;
}