# 1. BACKTRACK_SEARCH(csp) {
# 2. return BACKTRACK_DFS({},csp);
# 3. }
# 4. BACKTRACK_DFS(assignment,csp) {
# 5. if ((i = PICK_VAR(assignment,csp)) == NO_UNASSIGNED_VAR) {
# 6. return TRUE;
# 7. } // X_i is the chosen variable.
# 8. for each x in D_i {
# 9. assignment += {X_i = x};
# 10. if (CONSISTENT(csp)) {
# 11. if (BACKTRACK_DFS(assignment,csp) == TRUE) {
# 12. return TRUE;
# 13. }
# 14. }
# 15. assignment -= {X_i = x};
# 16. }
# 17. return FALSE; // failure
# 18.}