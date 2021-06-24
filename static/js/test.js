function form_trim(form_element){ // 輸入框,去除 空白
    var form = $(form_element);
    var formArr = form. serializeArray();
    jQuery.each(formArr , function(i, field) {
    formArr[i].value = $.trim(field.value);
    });
    var serializedForm = $.param(formArr);
    return serializedForm
}

function button_disabled(element){// 按扭送出後  置灰
    var element_disabled = $(element).attr('disabled','true');
    $(element).css({'background':'gray'})
    return element_disabled
}
function button_RemoveDisabeld(element){// 取消置灰{
    var element_remove  = $(element).removeAttr('disabled');
    $(element).removeAttr('style') 
    return element_remove
}