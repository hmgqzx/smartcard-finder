function basicCheck(){
	var studentNum;
	var cardNum;
	if(document.title=="注册"){
		studentNum=document.getElementById("studentNum");
		cardNum=document.getElementById("cardNum");		
	}
	else if (document.title=="拾卡登记") {}{
		studentNum=document.getElementById("pickStudentNum");
		cardNum=document.getElementById("pickCardNum");
	}
	var checkStuN=/^[0-9]{5,10}$/;
	var checkCardN=/^0[0-9]{5}$/;
	var flag=checkCardN.test(cardNum.value)==true&&checkStuN.test(studentNum.value)==true;
	if(flag==false){		
		studentNum.value="";
		cardNum.value="";
		//$('.js_tooltips').show();
	}
	else {

	}
}