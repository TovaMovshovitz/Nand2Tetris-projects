// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

  (START)
    // There are 8192 registers dealing with the screen
    @8192
    D=A
    @numScreenRegistersToPaint
    M=D

    @SCREEN
    D=A
    @currentScreenRegister
    M=D

    @KBD
    D=M

    //set paint color
    @SETWHITE
    D; JEQ

    @SETBLACK
    0; JMP


  (SETWHITE)
    @color
    M=0

    @PAINT
    0;JMP


  (SETBLACK)
    @color
    M=-1

    @PAINT
    0;JMP

  (PAINT)
    
    @color
    D=M

    @currentScreenRegister
    A=M
    M=D

    @currentScreenRegister
    M=M+1

    @numScreenRegistersToPaint
    M=M-1
    D=M

    // if numScreenRegistersToPaint is 0 => go to start program
    @START
    D; JEQ

    // if numScreenRegistersToPaint is not 0, continue painting
    @PAINT
    0; JMP

