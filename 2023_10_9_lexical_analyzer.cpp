// Program1Cosc311.cpp
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <fstream>
#include <set>

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
	SymbolInfo() {}
	SymbolInfo(int type) {
		this->type = type;
	}
};

std::vector<SymbolInfo> tokenList;
int currentParserPosition = 0;
std::map<string, SymbolInfo> symbolTableMap;

void insertIntoSymbolTable(const string& name, int type, int value = 0)
{
	SymbolInfo info;
	info.name = name;
	info.type = type;
	info.value = value;
	info.size = 0;
	info.elType = "";

	tokenList.push_back(info);
	if (type == RES || type == IDEN) {
		symbolTableMap[name] = info;
	}
}

string readCharLiteral(ifstream& myfile)
{
	string token = "";
	token += (char)myfile.get();
	token += (char)myfile.get();
	if (token == "@" || token == "$") {
		cout << "Illegal Character ERROR" << token << endl;
		return "";
	}
	char last = token.front();
	if (last != '\'')
	{
		token += (char)myfile.get();
	}
	token += (char)myfile.get();
	last = token.back();
	if (last != '\'')
	{
		cout << "Character literal ERROR" << token << endl;
		return "";
	}
	return token;
}

void lexAnalyze(const string& filename, const string& filenameOut)
{
	ifstream myfile(filename);
	ofstream myfileOut(filenameOut);
	string identifier = "";
	SymbolInfo symInfo;
	bool assignment = false;

	while (myfile.peek() != EOF)
	{
		string current_token = "";
		if (isalpha(myfile.peek()) || myfile.peek() == '_')
		{
			current_token += (char)myfile.get();
			while (isalpha(myfile.peek()) || isdigit(myfile.peek()) || myfile.peek() == '_')
			{
				current_token += (char)myfile.get();
			}
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
				cout << "Reserved Word: " << RES << " " << value << " " << current_token << endl;
				myfileOut << "Reserved Word: " << RES << " " << value << " " << current_token << endl;
			}
			else {

				identifier = current_token;
				symInfo.name = current_token;

				int value = tokenList.size();
				insertIntoSymbolTable(current_token, IDEN, value);
				myfileOut << "Identifier: " << IDEN << " " << value << " " << current_token << endl;
				current_token = "";
			}
		}
		else if (isdigit(myfile.peek()))
		{
			current_token += (char)myfile.get();
			while (isdigit(myfile.peek()))
			{
				current_token += (char)myfile.get();
			}

			if (isalpha(myfile.peek())) {
				cout << "Illegal int literal" << current_token << myfile.peek() << endl;
			}
			int myIntValue = stoi(current_token);
			cout << myIntValue << endl;

			insertIntoSymbolTable(current_token, Int, myIntValue);
			myfileOut << "Integer: " << Int << " " << myIntValue << " " << current_token << endl;
		}
		else if (myfile.peek() == '\'')
		{
			string token = readCharLiteral(myfile);
			if (token.empty()) {
				return;
			}
			else {
				current_token = token;
				int value = 0;
				value = int(current_token[1]);
				insertIntoSymbolTable(current_token, Char, value);
				myfileOut << "Character Literal " << Char << " " << value << " " << current_token << endl;
			}
		}
		else if (isspace(myfile.peek()))
		{
			myfile.get();
		}
		else if (myfile.peek() == '"') {
			current_token = (char)myfile.get();
			while (myfile.peek() != '"' && myfile.peek() != EOF && myfile.peek() != '\n')
			{
				current_token += (char)myfile.get();
			}
			if (myfile.peek() == EOF || myfile.peek() == '\n') {
				cout << "unterminated string " << current_token << endl;
				return;
			}
			current_token += (char)myfile.get();
			int value = 0;
			insertIntoSymbolTable(current_token, String, value);
			myfileOut << "String Literal" << String << " " << value << " " << current_token << endl;
		}
		else if (myfile.peek() == '(' || myfile.peek() == ';' || myfile.peek() == ')' || myfile.peek() == '[' || myfile.peek() == ']' || myfile.peek() == ',' || myfile.peek() == '.' || myfile.peek() == '{' || myfile.peek() == '}' || myfile.peek() == '#') {
			current_token += (char)myfile.get();
			int value;
			value = int(current_token[0]);
			insertIntoSymbolTable(current_token, INV, value);
			myfileOut << "Punctuation marks and delimiters: " << INV << " " << value << " " << current_token << endl;
		}
		else if (myfile.peek() == '=' || myfile.peek() == '+' || myfile.peek() == '-' || myfile.peek() == '*' || myfile.peek() == '/' || myfile.peek() == '>' || myfile.peek() == '<' || myfile.peek() == '!' || myfile.peek() == '&' || myfile.peek() == '|')
		{
			current_token += (char)myfile.get();
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
					char current_comment_char = (char)myfile.get();
					current_comment_char = (char)myfile.get();
					while (current_comment_char != '*' && myfile.peek() != '/') {
						current_comment_char = (char)myfile.get();
					}
					continue;
				}
				else if (myfile.peek() == '/') {
					if (myfile.peek() == '/') {
						while (myfile.peek() != EOF && myfile.peek() != '\n') {
							myfile.get();
						}
						continue;
					}
					else {
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
			myfileOut << "Operator: " << OP << " " << value << " " << current_token << endl;
		}
		else {
			current_token = (char)myfile.get();
			cout << "Invalid Character was found : " << current_token << endl;
		}
	};
	myfile.close();
}
void printSymbolTable(const string& filenameOut)
{
	ofstream myfileOut(filenameOut);

	cout << "Symbol Table:" << endl <<
		"      Name      Type     Value    elType" << endl;
	myfileOut << "Symbol Table:" << endl <<
		"      Name      Type     Value    elType" << endl;

	for (const auto& entry : symbolTableMap)
	{
		cout << setw(10) << entry.second.name
			<< setw(10) << entry.second.type
			<< setw(10) << entry.second.value
			<< setw(10) << entry.second.size
			<< setw(10) << entry.second.elType << endl;
		myfileOut << setw(10) << entry.second.name
			<< setw(10) << entry.second.type
			<< setw(10) << entry.second.value
			<< setw(10) << entry.second.size
			<< setw(10) << entry.second.elType << endl;
	}

}

void matchName(string tokenName)
{
	// if the currentParserPosition is beyond the end of the tokenList
	if (currentParserPosition >= tokenList.size()) {
		//      error. There are no more tokens to match
		cout << "ERROR: no more tokens to match" << endl;
	}
	// otherwise
	else {
		// 		Get the current token from the tokenList.
		SymbolInfo token = tokenList[currentParserPosition];
		// 		If that token's name matches the given name
		if (token.name == tokenName) {
			// 			advance the current parser position
			currentParserPosition++;
		}
		else {
			cout << "Error mismatched tokens. Received: " << token.name << " | Expected: " << tokenName << endl;
		}

	}

}

SymbolInfo matchType(int tokenType)
{
	// if the currentParserPosition is beyond the end of the tokenList
	if (currentParserPosition >= tokenList.size()) {
		//      error. There are no more tokens to match
		cout << "ERROR: no more tokens to match" << endl;
	}
	// otherwise
	else {
		// 		Get the current token from the tokenList.
		SymbolInfo token = tokenList[currentParserPosition];
		// 		If that token's name matches the given name
		if (token.type == tokenType) {
			// 			advance the current parser position
			currentParserPosition++;
			return token;
		}
		else {
			cout << "Error mismatched tokens. Received: " << token.type << " | Expected: " << tokenType << endl;
		}

	}
	return SymbolInfo(0);
}

// Let's start working on that peekName function.
bool peekName(string tokenName)
{
	if (currentParserPosition >= tokenList.size())
	{
		return false;
	}

	else
	{

		SymbolInfo token = tokenList[currentParserPosition];

		if (token.name == tokenName)
		{
			return true;
		}
		else
		{
			return false;
		}

	}

}
bool peekType(int tokenType)
{
	// if the currentParserPosition is beyond the end of the tokenList
	if (currentParserPosition >= tokenList.size()) {
		return false;
	}
	// otherwise
	else {
		// 		Get the current token from the tokenList.
		SymbolInfo token = tokenList[currentParserPosition];
		// 		If that token's name matches the given name
		if (token.type == tokenType) {
			return true;
		}
		else {
			return false;
		}

	}

}

void parseDeclaration() // *const* int name;
{
	// determine whether this is const.
	// (C++ requires we initialize our variables - 
	//  we can get weird behavior if we don't).
	bool isConst = false;
	int dataType = 0;
	string variableName = "";

	// Print the current token just before we parse the expected "const" keyword.
	cout << "DEBUG: " << tokenList[currentParserPosition].name << endl;

	// if the next token is the "const" reserved word.
	if (peekType(RES) && peekName("const"))
	{
		// flag the current declaration as "const"
		isConst = true;

		// and 'match' this const reserved word,
		// thereby skipping past it.
		matchType(RES);

	}

	// Print the current token just before we parse the expected "int" data type.
	cout << "DEBUG: " << tokenList[currentParserPosition].name << endl;
	SymbolInfo varType = matchType(RES);

	if (varType.name == "int")
	{
		dataType = Int;
	}
	else if (varType.name == "char")
	{
		dataType = Char;
	}
	else
	{
		cout << "Parsing error: unrecognized data type." << endl;
	}

	// match an identifier
	// Print the current token just before we parse the expected identifier.
	cout << "DEBUG: " << tokenList[currentParserPosition].name << endl;
	SymbolInfo nameToken = matchType(IDEN);
	variableName = nameToken.name;

	// match a semicolon.
	// Print the current token just before we parse the expected semi-colon.
	cout << "DEBUG: " << tokenList[currentParserPosition].name << endl;
	//add if using peek functions to test wheteher or no the next character is the = or the ;
	if (peekType(RES) && peekName("=") || peekType(RES) && peekName(";")) {

	}
	matchName(";");


	cout << "Name :" << variableName << "   Type :" << dataType << "   const :" << isConst << endl;


}


int main()
{
	lexAnalyze("declarations.txt", "output.txt");
	// printSymbolTable("output.txt");

	//cout << "Is an identifier? " << peekType(IDEN) << endl;   // should print false
	//cout << "Is a reserved? " << peekType(RES) << endl;		  // should print true
	//cout << "is an int? " << peekName("int") << endl;		  // should print false
	//cout << "Is a const? " << peekName("const") << endl;      // should print true

	//matchName("const");	 // success
	//matchName("int");	 // success

	//SymbolInfo variableName = matchType(IDEN);  // success
	//cout << variableName.name << endl;  // should print foobar

	//matchName(";");	  // Error! The next token is a = 
	// not a semi-colon.   

	parseDeclaration();
	parseDeclaration();
	parseDeclaration();
	return 0;
}