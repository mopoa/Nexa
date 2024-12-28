%{
#include <stdio.h>
#include <string.h>
%}

%%


"main"            { printf("keyword :: %s\n", yytext); }
"use"             { printf("keyword :: %s\n", yytext); }
"if"              { printf("keyword :: %s\n", yytext); }
"while"           { printf("keyword :: %s\n", yytext); }
"else"            { printf("keyword :: %s\n", yytext); }
"return"          { printf("keyword :: %s\n", yytext); }
"int"             { printf("keyword :: %s\n", yytext); }
"bool"            { printf("keyword :: %s\n", yytext); }
"true"            { printf("keyword :: %s\n", yytext); }
"false"           { printf("keyword :: %s\n", yytext); }


[a-zA-Z][a-zA-Z0-9_'_]* { printf("identifier :: %s\n", yytext); }


"-"[1-9][0-9]*   { printf("integer :: %s\n", yytext); } 
[0-9]+           { printf("integer :: %s\n", yytext); }  


"=="              { printf("equality operator :: %s\n", yytext); }
"!="              { printf("inequality operator :: %s\n", yytext); }
"<"               { printf("less than operator :: %s\n", yytext); }
"<="              { printf("less than or equal operator :: %s\n", yytext); }
">"               { printf("greater than operator :: %s\n", yytext); }
">="              { printf("greater than or equal operator :: %s\n", yytext); }
"+"               { printf("addition operator :: %s\n", yytext); }
"-"               { printf("subtraction operator :: %s\n", yytext); }
"*"               { printf("multiplication operator :: %s\n", yytext); }
"/"               { printf("division operator :: %s\n", yytext); }
"%"               { printf("modulus operator :: %s\n", yytext); }
"&"               { printf("and operator :: %s\n", yytext); }
"|"               { printf("or operator :: %s\n", yytext); }
"!"               { printf("not operator :: %s\n", yytext); }


"("               { printf("function argument start :: %s\n", yytext); }
")"               { printf("function argument end :: %s\n", yytext); }
":"               { printf("return type declaration :: %s\n", yytext); }
"{"               { printf("block start :: %s\n", yytext); }
"}"               { printf("block end :: %s\n", yytext); }
","               { printf("argument separator :: %s\n", yytext); }
";"               { printf("semicolon (optional) :: %s\n", yytext); }
"="               { printf("assignment operator :: %s\n", yytext); }
"["               { printf("array index start :: %s\n", yytext); }
"]"               { printf("array index end :: %s\n", yytext); }



"//"[^\n]*        { printf("single line comment :: %s\n", yytext); }

"%%%"([^%]|\n|%[^%]|%%[^%])*"%%%" { printf("multi-line comment :: %s\n", yytext); }


[ \t\n]+          ;


.                 { printf("unknown token :: %s\n", yytext); }


%%

int main() {
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}
