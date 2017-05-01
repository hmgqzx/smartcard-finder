$(document).on("click", "#changePassword", function() {
        $.prompt({
          text: "请输入旧密码",
          title: "输入姓名",
          onOK: function(text) {
           //测试是否输入正确密码，正确则返回这个
                $.prompt({
                text: "请输入新密码",
                title: "新密码",
                empty:false,
                onOK: function(text) {
                //修改数据库 ,如果成功则下面                 
                  $.alert("修改成功");
                  //$.alert('密码错误', 'error'); //if false
                },
                onCancel: function() {
                  $.toast('取消', 'cancel');                  
                },                
              });
            },
          onCancel: function() {
            $.toast('取消', 'cancel');
          }          
        });
      });

$(document).on("click","#showLostState",function(){
  /*如已挂失
    $.alert("您已挂失");*/
  //如未挂失
      $.confirm({
          title: '未挂失!',
          text: '您尚未挂失!<br>确定=返回<br>取消=挂失',
          onOK: function () {
            //点击确认
          },
          onCancel: function () {
            //调用挂失脚本
            $.alert("挂失成功");              
          }
});

});