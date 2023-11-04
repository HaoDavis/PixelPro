const imgPath = './test-img.png' //这个变量存   处理后图片的URL

//显示处理后的图片
document.querySelector('.showImg').innerHTML = `<img src=${imgPath} class="img-fluid" alt="加载中" title="处理后的图片">`

// 以下监听提交按钮
// 获取文件输入框和按钮元素
const fileInput = document.getElementById("inputGroupFile04");
const submitButton = document.getElementById("inputGroupFileAddon04");

// 添加事件监听器以在文件选择时执行操作
//获得的图片是全局变量
let selectedFile = null

fileInput.addEventListener("change", function () {
    // 获取选中的文件
    selectedFile = fileInput.files[0];
    // 如果有选中的文件
    if (selectedFile) {
        // 打印文件信息
        console.log("文件名称: " + selectedFile.name);
        console.log("文件大小: " + selectedFile.size + " 字节");
        console.log("文件类型: " + selectedFile.type);
    } else {
        console.log("未选择文件");
        // alert("未选择文件");
    }
});

submitButton.addEventListener("click", function () {
    console.log(selectedFile)
    if(selectedFile!=null){
        console.log('处理图片')
        //后续发给后端处理
    }
    else{
        console.log('没有选择图片')
        alert('请选择图片！')
    }
  });
