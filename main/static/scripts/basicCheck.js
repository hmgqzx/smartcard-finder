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
		$.toptip('账号或密码错误','error');
		//$('.js_tooltips').show();
	}
	else {

	}
};

$(document).on("click","#lostButton",function(){
	//检查是否已经进行失卡登记
	/*如果没有
	$.confirm({
	  title: '失卡登记',
	  text: '是否进行失卡登记？',
	  onOK: function () {
	    //点击确认则进行失卡登记
	    //添加失卡登记的数据库操作
	    window.location.href = "./lostLog.html";
	  },
	  onCancel: function () {
	  	$.toast("操作取消","cancel");
	  }
	});*/

	/*如果已经登记*/
	//检测是否 lost 和 found 数据库是否有匹配
	/*若匹配数据成功返回 结果 页面*/
	window.location.href="./findSuccess.html"
	/*如果没有成功，返回
	$.alert("寻卡中...");*/
	
});