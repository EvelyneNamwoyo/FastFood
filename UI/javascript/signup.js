//Get the signup form modal
signin = document.getElementById("")
function logout_show(){
    document.getElementById("logout").style.display = "block";

}

function logout_hide(){
    document.getElementById("logout").style.display = "none";


}

function login_hide(){
    document.getElementById("login").style.display = "none";

}
function account_hide(){
    document.getElementById("account").style.display = "none";

}
function admin_hide(){
    document.getElementById("admin").style.display = "none";

}

function login_show(){
    document.getElementById("login").style.display = "block";

}
function account_show(){
    document.getElementById("account").style.display = "block";

}
function admin_show(){
    document.getElementById("admin").style.display = "block";

}
// function to display order histories
function history_show(){
    document.getElementById("history").style.display = "block";

}
// function to hide order histories
function history_hide(){
    document.getElementById("history").style.display = "none";

}

function logout(){
    admin_show();
    account_show();
    login_show();
    logout_show();
    logout_hide();
    history_hide();
    hide_cart1();
    show_cart2();

}

function login(){
    admin_hide();
    account_hide();
    login_hide();
    logout_show();
    signin_hide();
    signup_hide();
    history_show();
    hide_cart2();
    show_cart1();
}

//functions to display signup form and signin form

function signup_show(){
    document.getElementById("signup_modal").style.display = "block";
}

function signup_hide(){
    document.getElementById("signup_modal").style.display = "none";

}

function signin_show(){
    document.getElementById("signin_modal").style.display = "block";

}

function signin_hide(){
    document.getElementById("signin_modal").style.display = "none";

}


//Jvascript to show and hide the added items
function show_chicken(){
    document.getElementById("chicken").style.display = "block";
    document.getElementById("chicken-log").style.display = "block";
}

function show_chips(){
    document.getElementById("chips").style.display = "block";
    document.getElementById("chips-log").style.display = "block";
}

function hide_chicken(){
    document.getElementById("chicken").style.display = "none";
    document.getElementById("chicken-log").style.display = "none";
}

function hide_chips(){
    document.getElementById("chips").style.display = "none";
    document.getElementById("chips-log").style.display = "none";
}
// This function adds sausages to the cart
function show_sausages(){
    document.getElementById("sausages").style.display = "block";
    document.getElementById("sausages-logs").style.display = "block";
}
// adds hamburgers
function show_hamburger(){
    document.getElementById("hamburger").style.display = "block";
    document.getElementById("hamburger-logs").style.display = "block";
}
// adds salaads
function show_salaads(){
    document.getElementById("salaads").style.display = "block";
    document.getElementById("salaads-logs").style.display = "block";
}
// deletes sausages
function hide_sausages(){
    document.getElementById("sausages").style.display = "none";
    document.getElementById("sausages-logs").style.display = "none";
}
// deletes hamburgers
function hide_hamburger(){
    document.getElementById("hamburger").style.display = "none";
    document.getElementById("hamburger-logs").style.display = "none";
}

// deletes salaads
function hide_salaads(){
    document.getElementById("salaads").style.display = "none"
}

// The following functions enable addition and deletion of orders
function delete_order(){
    document.getElementById("item-1").style.display = "inline";
    document.getElementById("order1").style.display = "none";
}

// hides the second cart
function hide_cart2(){
    document.getElementById("unlogged").style.display = "none";
}
// show first caer
function show_cart1(){
    document.getElementById("loggedin_users").style.display = "block";
}
// show cart2, when logging out
function show_cart2(){
    document.getElementById("unlogged").style.display = "block";
}
// hide cart1(logged in users when logging out)
function hide_cart1(){
    document.getElementById("loggedin_users").style.display = "none";
}

// display success message
function success_message(){
    document.getElementById("success").style.display = "block";
    hide_cart1();
}
function success_hide(){
    document.getElementById("success").style.display = "none";
    show_cart1();
}