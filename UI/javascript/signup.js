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

}

function login(){
    admin_hide();
    account_hide();
    login_hide();
    logout_show();
    signin_hide();
    signup_hide();
    history_show();
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
}

function show_chips(){
    document.getElementById("chips").style.display = "block";
}

function hide_chicken(){
    document.getElementById("chicken").style.display = "none";
}

function hide_chips(){
    document.getElementById("chips").style.display = "none";
}

// The following functions enable addition and deletion of orders
function delete_order(){
    document.getElementById("item-1").style.display = "inline";
    document.getElementById("order1").style.display = "none";
}