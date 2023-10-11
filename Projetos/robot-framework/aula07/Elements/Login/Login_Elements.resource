*** Variables ***
&{Login}
#    Elements register
...  Input_PrimeiroNome=xpath://input[@placeholder="First Name"]
...  Input_UltimoNome=xpath://input[@placeholder="Last Name"]
...  Input_Telefone=xpath://input[@placeholder="Phone"]
...  Input_Email=xpath://input[@placeholder="Email"]
...  Input_Senha=xpath://input[@placeholder="Password"]
...  Button_Signup=xpath://button[@class="btn btn-default btn-lg btn-block effect ladda-button waves-effect"]
...  Button_Cookie=xpath://button[@id="cookie_stop"]
#    Elements login
...  Input_EmailLogin=xpath://input[@placeholder="Email"] 
...  Input_SenhaLogin=xpath://input[@placeholder="Password"]
...  $Button_Logar=xpath://span[contains(text(),"Login")]
...  A_OpcaoLogin=xpath:(//a[@href="https://www.phptravels.net/login"])[2]

