/*
PR -> isD int main() { S }          // Program structure starts with main()

D -> A D1                          // Variable declarations
A -> int L;                        // Variable declaration of type int
   L.type = int                    // Assign type attribute to variable L
   L -> I1 L1                      // Identifier I1 followed by more variable declarations L1
   I1.type = int                   // Type attribute for I1 is int
   I1 -> n                         // Identifier I1 is 'n'
   I1.type = int                   // Type attribute for I1 is int
   I1 -> ch                        // Identifier I1 is 'ch'
   ch.type = char                  // Type attribute for 'ch' is char

S -> A1                            // Statements start with variable assignments
A1 -> I2 = E;                      // Variable assignment
   I2.type = E.type                // Assign type of I2 from E
   E.type = int                    // Expression E has type int
   I2 -> n                         // Identifier I2 is 'n'
   n.type = int                   // Type attribute for I2 is int
   E -> num                        // Expression E is a number
   num.type = int                  // Type attribute for num is int
   E -> id                         // Expression E is an identifier
   id.type = lookup(id.entry)      // Look up and assign type attribute to id

S -> while ( C ) { S1 }            // While loop statement
C -> E1                           // Condition E1 for the while loop
E1.type = int                    // Condition type is int
S1 -> A2 S1                       // Statements in the while loop
A2 -> I3 = E2;                    // Variable assignment within the loop
   I3.type = E2.type              // Assign type of I3 from E2
   E2.type = int                  // Expression E2 has type int
   I3 -> n                       // Identifier I3 is 'n'
   n.type = int                  // Type attribute for I3 is int
   E2 -> E3 + E4                 // Expression E2 is a sum of E3 and E4
   E3.type = int                  // Type attribute for E3 is int
   E4.type = int                  // Type attribute for E4 is int
   E3 -> n                       // Expression E3 is 'n'
   n.type = int                  // Type attribute for E3 is int
   E3 -> id                      // Expression E3 is an identifier
   id.type = lookup(id.entry)    // Look up and assign type attribute to id

E4 -> ch                         // Expression E4 is 'ch'
   ch.type = char                // Type attribute for E4 is char

S1 -> ε { S1.type = void }       // End of the while loop body

*/