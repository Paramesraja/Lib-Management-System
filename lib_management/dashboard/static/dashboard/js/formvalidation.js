function validate(){
    var rollnum=document.getElementById("roll_no");
    var bookid=document.getElementById("bookid");
    var copynum=document.getElementById("copyno");
    var val=1;
    const pattern=/[1-9][0-9][a-zA-Z][a-zA-Z][a-zA-Z][0-9][0-9][0-9]/;
    var res = pattern.test(rollnum.value);
    if(rollnum.value.trim().length!=8 || res==false){
        val=0;
        rollnum.style.border="solid 1px red";
        document.getElementById("rollnum_alert").style.visibility="visible";
        
    }

    else{
        rollnum.style.border="solid 1px #ced4da";
        document.getElementById("rollnum_alert").style.visibility="hidden";
        
        
    }

    if(bookid.value.trim().length!=5){
        val=0;
        bookid.style.border="solid 1px red";
        document.getElementById("bookid_alert").style.visibility="visible";
        return false;
    }

    else{
        bookid.style.border="solid 1px #ced4da";
        document.getElementById("bookid_alert").style.visibility="hidden";
    }


    if(val==1){
        return true;
    }
    else{
        return false;
    }
    
    
}

function backtolib_validate(){
    var rollnum=document.getElementById("backtolib_roll_no");
    var bookid=document.getElementById("backtolib_bookid");
    var copynum=document.getElementById("backtolib_copyno");
    var val=1;
    const pattern=/[1-9][0-9][a-zA-Z][a-zA-Z][a-zA-Z][0-9][0-9][0-9]/;
    var res = pattern.test(rollnum.value);
    if(rollnum.value.trim().length!=8 || res==false){
        val=0;
        rollnum.style.border="solid 1px red";
        document.getElementById("backtolib_rollnum_alert").style.visibility="visible";
        
    }

    else{
        rollnum.style.border="solid 1px #ced4da";
        document.getElementById("backtolib_rollnum_alert").style.visibility="hidden";
    }

    if(bookid.value.trim().length!=5){
        val=0;
        bookid.style.border="solid 1px red";
        document.getElementById("backtolib_bookid_alert").style.visibility="visible";
        
    }

    else{
        bookid.style.border="solid 1px #ced4da";
        document.getElementById("backtolib_bookid_alert").style.visibility="hidden";
    }
    
    if(val==1){
        return true;
    }
    else{
        return false;
    }
}

function renew_validate(){
    var rollnum=document.getElementById("renew_roll_no");
    var bookid=document.getElementById("renew_bookid");
    var copynum=document.getElementById("renew_copyno");
    var val=1;
    const pattern=/[1-9][0-9][a-zA-Z][a-zA-Z][a-zA-Z][0-9][0-9][0-9]/;
    var res = pattern.test(rollnum.value);
    if(rollnum.value.trim().length!=8 || res==false){
        val=0;
        rollnum.style.border="solid 1px red";
        document.getElementById("renew_rollnum_alert").style.visibility="visible";
        
    }

    else{
        rollnum.style.border="solid 1px #ced4da";
        document.getElementById("renew_rollnum_alert").style.visibility="hidden";
    }
    

    if(bookid.value.trim().length!=5){
        val=0;
        bookid.style.border="solid 1px red";
        document.getElementById("renew_bookid_alert").style.visibility="visible";
        
    }

    else{
        bookid.style.border="solid 1px #ced4da";
        document.getElementById("renew_bookid_alert").style.visibility="hidden";
    }
    if(val==1){
        return true;
    }
    else{
        return false;
    }
    
}


function reportdamage_validate(){
    console.log("heeeeellllooooo");
    var rollnum=document.getElementById("reportdamage_rollno");
    var bookid=document.getElementById("reportdamage_bookid");
    //var copynum=document.getElementById("reportdamage_copyno");
    var damagedescription=document.getElementById("reportdamage_damagedescription");
    var val=1;
    const pattern=/[1-9][0-9][a-zA-Z][a-zA-Z][a-zA-Z][0-9][0-9][0-9]/;
    var res = pattern.test(rollnum.value);
    if(rollnum.value.trim().length!=8 || res==false){
        val=0;
        rollnum.style.border="solid 1px red";
        document.getElementById("a").style.visibility="visible";
        
    }

    else{
        rollnum.style.border="solid 1px #ced4da";
        document.getElementById("reportdamage_rollno_alert").style.visibility="hidden";
    }

    if(bookid.value.trim().length!=5){
        val=0;
        bookid.style.border="solid 1px red";
        document.getElementById("reportdamage_bookid_alert").style.visibility="visible";
        
    }

    else{
        bookid.style.border="solid 1px #ced4da";
        document.getElementById("reportdamage_bookid_alert").style.visibility="hidden";
    }
    if(damagedescription.value.trim().length==0){
        val=0;
        damagedescription.style.border="solid 1px red";
        document.getElementById("reportdamage_damagedescription_alert").style.visibility="visible";
        
    }

    else{
        damagedescription.style.border="solid 1px #ced4da";
        document.getElementById("reportdamage_damagedescription_alert").style.visibility="hidden";
    }
    
    if(val==1){
        return true;
    }
    else{
        return false;
    }
}

// function renew_validate(){
    
//     var rollnum=document.getElementById("renew_roll_no");
//     var bookid=document.getElementById("renew_bookid");
//     var copynum=document.getElementById("renew_copyno");
//     var val=1;
//     const pattern=/[1-9][0-9][a-zA-Z][a-zA-Z][a-zA-Z][0-9][0-9][0-9]/;
//     var res = pattern.test(rollnum.value);
//     if(rollnum.value.trim().length!=8 || res==false){
//         val=0;
//         rollnum.style.border="solid 1px red";
//         document.getElementById("renew_rollnum_alert").style.visibility="visible";
        
//     }

//     else{
//         rollnum.style.border="solid 1px #ced4da";
//         document.getElementById("renew_rollnum_alert").style.visibility="hidden";
//     }
    

//     if(bookid.value.trim().length!=5){
//         val=0;
//         bookid.style.border="solid 1px red";
//         document.getElementById("renew_bookid_alert").style.visibility="visible";
        
//     }

//     else{
//         bookid.style.border="solid 1px #ced4da";
//         document.getElementById("renew_bookid_alert").style.visibility="hidden";
//     }
//     if(val==1){
//         return true;
//     }
//     else{
//         return false;
//     }
// }