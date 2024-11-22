print('''
.: :::       :" ::       :        ::      .:'':      .yyy.':
                              .' ::F.     :'   ::    :::::::::::::.     :'  ':    .y::Fy ':
                              :  ::FF.   :'     : .::" ::      ::  ::  .:    ':  .yF::Fy  :
                              : .:F:FF..:       :::'    :      :     :::'     '::yF:::Fy  :
                              : ::FF:FF:'      .:::     :.     :      :.      .yFF::::Fy  :
                              : ::FFF:FF.      :' ::    ':    .:     : :.    .yFF:::::Fy  :
                              : :FFFF"FFFy.   .:   :     :    :'    :   :. .yyFF::::::Fy  :
                              : :FFFFyy:FFy. .:'   ':    ::::::   .'     "yyFF::::::::Fy  :
                              : :FFFFy:::FFFy:.     ':  : :  ::. .'     .yyFF:::::::::Fy  :
                              : :FFFFy::::FFFyy.     :::' :  : '::    .yyFF:::::::::::Fy:.:
                              : :FFFFy::::::"FFy.   :: :  : ::  : :  .yyF:::::::::::::FFy":
                              : ::FFFyy:::::::FFF.::    : : :  :  ::.yF:::::::::::::::Fy: :
                              :  :FFyyyy::::::::FFy.     ::::::   .yyF:::::::::::::::Fy': :
                              :  :FFyyyyYYY::::::.FFFy::  :::    yyFF::::::::::::::yyFy : :
                              : .::FFFyyyYYYYY:::::.FFF    ::   FFyyy:::::::::::yyyyFy' : :
                              :.:  'FFFyyyYYYYyyy::FFF::::::::::FFyyyy::::::::yyyyyyyY:.: :
                              :':   :FFFyyYYYYyyy:FF'   . ::::. 'FFFyyyyyy::yyyyyyyyY":::::
                              : :.  'FFFyyyyyYyyyFF:   :' :  : :  'FFFyyyyyyyyyyyyyY'  ":::   
                              ': :   'FyyyyyyyyFF'  :."  .:  :  ". ."FFFyyyyyyyyyyY'   :::'
                               : :    'FFyyyyFF:.   .:   :    :   :   'FFFyyyyyyyY'    : :
                               : ':    :FFyFF'  :. .: :  :    :   :     :FFFyyyyY'     : :    
                               ': :   :'FFFF'    :::    ::    :.:" :. .: 'FFFFYY'     : :'
                                . ': :' 'FF'     ::     :"::::::    : :   'FFFy::.   .: :     
                                ': ::'    ":    :':.    :      :     ::.      :" ":  :  :
                                 . .:      '.  :'  :.  .:      ::   ::':.    :"   "::" :'     
                                 ' ::.      : :     '. :       :: :::  ':.  :      ::  :
                                  ::  :     '::      '::.      ::::     ': :      :::  :      
                                  ':   :.   :::       :'::::::::::       ::      :' :.:'
                                   :   ':  :' '.      :        ':.      .:.     :'  :::
                                   :    "::'   ':.    :         ':     .:':.   :'   "::
                                   '.    ".      ':. :           :   .:'  ':. .:     :'
                                    ::.   ":.      ':::::.       :: ::'    ': :'     :
                                    : ": .: ':.     .:   ":::::::;:::'      :::     :'
                                    :  "::    '.    :'            :       ."":.     :
                                    :   ::     '.   :             :     .:'   :.   .'         
                                    ':  ::.     ':..:              :   .'     ':  :'
                                    _:".: ":      '':.             : .:"       :.:'
                 [WILU]      .....-'.: .:  ".      :"'':::::::..   .:'         ::
      _.-.:"'---....._   _.-:."     .: : ".  :.  ::           '":::::.        :":
   ."' ."             """ .".......: : :. :". ": :                  ::      .:" :.            
 .:.  :                .."        ..:  : ":  ". :                    :.   .::" :':".          
"   ':""'...        .."        ..:  :  :   :   ":                    ::  :"":  : :  "-.       
   ."       """"..::::........"  :. :  :   :     ".                  :.-:" .:  : ':    "-.
  :              ::         :   :  :'  :   :       '--____________---"  :  :'  :  :       '-.
''')
print("Welcome to the Spiderman Island")
print("Your mission is to find the treasure on this Island")
choice1 = input('You are on a crossroad, do you want to go "Left" or "Right"')
choice2 = input('You\'ve come to the middle of the lake, in an island. Type "wait" to wait for a boat, or type "swim" to swim across the lake')
choice3 = input('You arrived at the Island safely, there is a house with three doors. Which door colour do you want to use, "Red," "Yellow" or "Blue"?')
if choice1 == 'Left':
    print("You fell into a hole")
else:
    print("choice2")
if choice2 == 'wait':
    print("You fell into a hole")
else:
    print("choice3")
if choice2 == 'Yellow':
    print("You entered the Lions Den")
elif choice2 == 'Blue':
    print("You entered the Lions Den")
else:
    print("Congratulations!, you've seen Spidermans treasure")

