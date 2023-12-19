
// Program1Cosc311.cpp 

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <fstream>
#include <iomanip>

using namespace std;

const int RES = 111; // reserved word
const int OP = 112;  // operator(arithmetic, relational, or logical)
const int INV = 113; //puncntion AND DELIMITERS
const int IDEN = 114; //IDENTIFIER

const int NE = 200; //!=
const int LE = 201; //<=
const int GE = 202; //>=
const int EQ = 203; //==
const int AD = 43; //+
const int SU = 45; //-
const int MU = 42; //*
const int DI = 47; // /
const int EL = 61; // =
const int L = 60; // <
const int G = 62; // >
const int AN = 38; //&
const int EX = 33; // !
const int OR = 124; //|
const int AA = 214; //&&
const int OO = 215; //||
const int AP = 216; //++
const int SB = 217; //--


const int Int = 1;
const int Char = 2;
const int String = 3;
const int IF = 4;
struct SymbolInfo {
	string name;
	int type;
	int value;
	int size;
	string elType;
};

std::vector<SymbolInfo> symbolTable;

void insertIntoSymbolTable(const string& name, int type, int value = 0) {
	SymbolInfo info = { name, type, value, 0, "" };
	symbolTable.push_back(info);
}

string readCharLiteral(ifstream& myfile)
{
	string token = "";
	// Step 1) Consume this character and add it to our token.
	//		   (this is the first apostrophe)
	token += (char)myfile.get();

	// Step 2) Consume another character and add it to our token.
	token += (char)myfile.get();
	if (token == "@" || token == "$") {
		cout << "Illegal Character ERROR" << token << endl;
		return "";  // Return "" for error
	}

	// If 2nd token is \ you might have '\'' or '\n'
	// Then you need 4 characters not 3
	char last = token.front();
	if (last != '\'')
	{
		token += (char)myfile.get();
	}
	token += (char)myfile.get();
	last = token.back();
	if (last != '\'')
	{
		// Print error message
		cout << "Character literal ERROR" << token << endl;
		return "";  // Return "" for error
	}
	return token;
}


void lexAnalyze(const string& filename)
{
	ifstream myfile(filename);

	// For symbol table
	string identifier = "";
	SymbolInfo symInfo;
	bool assignment = false;

	// Take a peek at the next character in the file.
	while (myfile.peek() != EOF)
	{
		string current_token = "";

		// If the next character in the file represents the beginning of an identifier...
		if (isalpha(myfile.peek()) || myfile.peek() == '_')
		{
			// ... then consume this character and add it to our token.
			current_token += (char)myfile.get();

			// while the next character in the file continues our identififier...
			while (isalpha(myfile.peek()) || isdigit(myfile.peek()) || myfile.peek() == '_')
			{
				// then consume this next character and add it to our token.
				current_token += (char)myfile.get();
			}

			// Your job:
			// if current_token is a valid reserved word
			if (current_token == "if" ||
				current_token == "while" ||
				current_token == "for" ||
				current_token == "else" ||
				current_token == "main" ||
				current_token == "void" ||
				current_token == "include" ||
				current_token == "int" ||
				current_token == "const" ||
				current_token == "string" ||
				current_token == "struct" ||
				current_token == "endl" ||
				current_token == "char")
			{
				//cout << "Reserved Word: " << current_token << endl;
				int value = 0;
				if (current_token == "int") {
					symInfo.type = Int;
					value = Int;
				}
				if (current_token == "char") {
					symInfo.type = Char;
					value = Char;
				}
				if (current_token == "string") {
					symInfo.type = String;
					value = String;
				}
				if (current_token == "if") {
					value = IF;
				}
				insertIntoSymbolTable(current_token, RES, value);
			}
			else {
				//cout << "Identifier: " << current_token << endl;
				identifier = current_token;
				symInfo.name = current_token;

				size_t value = symbolTable.size();
				insertIntoSymbolTable(current_token, IDEN, value);
				current_token = "";


			}

		}

		// If the next character is a digit
		else if (isdigit(myfile.peek()))
		{
			// then consume this character and add it to our token
			current_token += (char)myfile.get();

			// while there are more digits to read from the file
			while (isdigit(myfile.peek()))
			{
				// consume them and add them to our token too
				current_token += (char)myfile.get();
			}

			if (isalpha(myfile.peek())) {
				cout << "Illegal int literal" << current_token << myfile.peek() << endl;
			}

			int myIntValue = stoi(current_token);

			//cout << myIntValue << endl;			// will print the integer 123

			insertIntoSymbolTable(current_token, Int, myIntValue);
			//cout << "Integer: " << current_token << endl;


		}

		// If the next character in our file is an apostrophe...
		else if (myfile.peek() == '\'')
		{ //myfile.get()extracts
			// then we're processing a character literal!
			string token = readCharLiteral(myfile);
			if (token.empty()) {
				// Error printed in readCharLiteral
			 // Bonus: If this third character wasn't an apostrophe,
			 //		  print that there's a lexical error and immediately return from this function.
				return;
			}
			else {
				current_token = token;
				int value = 0;
				value = int(current_token[1]);
				insertIntoSymbolTable(current_token, Char, value);
				//cout << "Character Literal " << current_token << endl;
			}
		}

		// if the next character is whitespace
		else if (isspace(myfile.peek()))
		{
			// then just skip over it.
			myfile.get();
		}

		// Next step:
		// Try adding support for string literals next.
		// Something like
		// "Hello, world!"
		// "How are you today?"

		// They begin with a quotation mark " 
		// then contain any number of characters up to, and including, the next quotation mark " 
		else if (myfile.peek() == '"') {
			current_token = (char)myfile.get();
			while (myfile.peek() != '"' && myfile.peek() != EOF && myfile.peek() != '\n')
			{
				// then consume this next character and add it to our token.
				current_token += (char)myfile.get();
			}
			if (myfile.peek() == EOF || myfile.peek() == '\n') {
				// print error
				// EOF before reaching end of string
				//cout << "unterminated string " << current_token << endl;
				return;
			}
			current_token += (char)myfile.get();
			int value = 0;
			insertIntoSymbolTable(current_token, String, value);
			//cout << "String Literal" << current_token << endl;

		}
		else if (myfile.peek() == '(' || myfile.peek() == ';' || myfile.peek() == ')' || myfile.peek() == '[' || myfile.peek() == ']' || myfile.peek() == ',' || myfile.peek() == '.' || myfile.peek() == '{' || myfile.peek() == '}' || myfile.peek() == '#') {
			current_token += (char)myfile.get();
			if (current_token == "/*")
			{
				while (current_token != "*/")
				{
					if (myfile.peek() == EOF) {
						cout << "unterminated comment:" << current_token << endl;
						return;
					}
					(char)myfile.get(); // Instead of setting it equal to the current token, this will grab it and throw away result
				}
			}

			if (current_token == "//")
			{
				while (current_token != "/n")
				{
					(char)myfile.get(); // Instead of setting it equal to the current token, this will grab it and throw away result
				}
			}
			int value;
			value = int(current_token[0]);
			insertIntoSymbolTable(current_token, INV, value);
			//cout << "Punctuation marks and delimiters: " << current_token << endl;
		}
		// We'll modify this to look for operators in general, not just = 
		else if (myfile.peek() == '=' || myfile.peek() == '+' || myfile.peek() == '-' || myfile.peek() == '*' || myfile.peek() == '/' || myfile.peek() == '>' || myfile.peek() == '<' || myfile.peek() == '!' || myfile.peek() == '&' || myfile.peek() == '|')
		{
			current_token += (char)myfile.get();
			// Check assignment operator
			if (myfile.peek() == '=' || myfile.peek() == '+' || myfile.peek() == '-' || myfile.peek() == '&' || myfile.peek() == '|') {
				current_token += (char)myfile.get();

			}
			int value = 0;
			if (current_token == "!=")
				value = NE;
			else if (current_token == "<=")
				value = LE;
			else if (current_token == ">=")
				value = GE;
			else if (current_token == "==")
				value = EQ;
			else if (current_token == "+")
				value = AD;
			else if (current_token == "-")
				value = SU;
			else if (current_token == "*")
				value = MU;
			else if (current_token == "/")

				if (myfile.peek() == '*') {
					// read the next character using .get() and store it to a new 
					// variable called current_comment_char  
					int current_comment_char = (char)myfile.get();
					while (current_comment_char != '*' && myfile.peek() != '/') { //while current_comment_char is
						//different from * and the next character is different from /

						// store the next character into current_comment_char
						current_comment_char = (char)myfile.get();
					}
				}
				else if (myfile.peek() == '/') {
					if (myfile.peek() == '/') {
						// found one-liner comment
						// simply myfile.get() to discard until a \n is encountered
						while (myfile.peek() != EOF && myfile.peek() != '\n') {
							myfile.get();
						}
						continue;        // there can be multiple lines of single-line comments 
					}
					else {
						// just a division symbol
						value = DI;
					}
				}


				else if (current_token == "=")
					value = EL;
				else if (current_token == "<")
					value = L;
				else if (current_token == ">")
					value = G;
				else if (current_token == "&")
					value = AN;
				else if (current_token == "!")
					value = EX;
				else if (current_token == "|")
					value = OR;
				else if (current_token == "&&")
					value = AA;
				else if (current_token == "||")
					value = OO;
				else if (current_token == "++")
					value = AP;
				else if (current_token == "--")
					value = SB;



			insertIntoSymbolTable(current_token, OP, value);
			//cout << "Operator: " << current_token << endl;

		}

	}
	;
	myfile.close();

}




void printSymbolTable() {
	cout << "Symbol Table:" << endl;
  
    // print the header
    cout << left << setw(20) << "Name"
                     << setw(10) << "Type"
                     << setw(10) << "Value" 
                     << setw(10) << "Size"
                     << setw(10) << "elType"
                     << endl;
  
    // print the columns
	for (const auto& entry : symbolTable) {
        cout << left << setw(20) << entry.name
                     << setw(10) << entry.type 
                     << setw(10) << entry.value 
                     << setw(10) << entry.size
                     << setw(10) << entry.elType
                     << endl;
	}
}

int main() {
	lexAnalyze("example.txt");
	printSymbolTable();
	return 0;
}