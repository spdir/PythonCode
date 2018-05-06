function examResult(data) {
  if (typeof data === 'string') {
    var result = data;
    var obj = {
      'A': 0,
      'B': 1,
      'C': 2,
      'D': 3
    };
    var views = $('#tDANXUAN .view');
    for (var i = 0; i < views.length; i++) {
      var flag = null;
      var inputs = $(views[i]).find('input');
      for (var j = 0; j < inputs.length; j++) {
        if (obj[result[i]] == j) {
          inputs[j].checked = true;
        }
      }
    }
  } else if(Array.isArray(data)) {
    var views = $('#tPANDUAN .view');
    for (let i = 0; i < views.length; i++) {
      var inputs = $(views[i]).find('input');
      if (data[i] === '正确') {
        inputs.eq(0).attr('checked', true)
      } else {
        inputs.eq(1).attr('checked', true)
      }
    }
  } else {
    alert('暂无处理方式')
  }
}

/*如何使用?

进入作答页面 => 右击之后 => 点击检查 => console 选项下粘贴以上代码(```内的代码)
将对应的提供的答案集以参数的方式传递给 examResult
例如:
examResult('BABCCACCBC')
examResult(['正确', '正确', '正确', '正确', '正确', '错误', '正确'])
*/