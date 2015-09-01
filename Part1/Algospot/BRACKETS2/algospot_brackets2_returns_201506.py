class bracket :

    mBracket = { '(' : ')', '{' : '}', '[' : ']' }

    def isOpenBracket( self, aBracket ) :

        if aBracket in self.mBracket :
            sResult = True
        else :
            sResult = False

        return sResult 

    def isMatchBracket( self, aOpenBracket, aCloseBracket ) :

        if self.mBracket[aOpenBracket] == aCloseBracket :
            sResult = True
        else :
            sResult = False

        return sResult


    def isThereMatchBracket( self, aInputString ) :

        sStack = []
        sStackCount = 0
        sInputString = str( aInputString )

        for i in range( len( sInputString ) ) :

            if self.isOpenBracket( sInputString[i] ) == True :
                sStack.append( sInputString[i] )
                sStackCount = sStackCount + 1
            else :
                if ( sStackCount > 0 ) :
                    sBracket = sStack.pop()
                    sStackCount = sStackCount - 1

                    if self.isMatchBracket( sBracket, sInputString[i] ) == True :
                        sResult = 'YES'
                    else :
                        sResult = 'NO'
                        break
                else :
                    sResult = 'NO'
                    break 

        if sStackCount > 0 : 
            sResult = 'NO'

        return sResult


def main() :
    sCount = input()

    sBracket = bracket()

    for i in range( sCount ) :
        #sInput = raw_input()
        print sBracket.isThereMatchBracket( raw_input() )
        #print sResult

main()

