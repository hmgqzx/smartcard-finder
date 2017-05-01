function showPlacePicker() {
    $("#choosePlace")[0].style.display = 'inherit'; 
    $("#diy")[0].style.display = 'none'; 
        }
$("#placePicker").select({
  title: "选择手机",
  items: [
    {
        title:"",
        value:"000",
    },
    {
      title: "图书馆",
      value: "010",
    },
    {
      title: "AB宿舍区宿管值班室",
      value: "001",
    },
    {
      title: "CD宿舍区宿管值班室",
      value: "002",
    },
    {
      title: "EF宿舍区宿管值班室",
      value: "003",
    },
    {
      title: "研究生宿舍区宿管值班室",
      value: "004",
    },
    {
      title: "G座宿舍区宿管值班室",
      value: "005",
    },
    {
      title: "至诚书院物业前台",
      value: "006",
    },
    {
      title: "弘毅书院物业前台",
      value: "007",
    },
    {
      title: "思源书院物业前台",
      value: "008",
    },
    {
      title: "知行书院物业前台",
      value: "009",
    }
    ]
});

function showDiy(){
    $("#diy")[0].style.display = 'inherit'; 
    $("#choosePlace")[0].style.display = 'none'; 
}
