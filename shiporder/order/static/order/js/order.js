var order = function () {
    return {
        add_goods:function (){
            var $tr = $(`<tr></tr>`)
            $tr.append(`<td> <input style="width:100px" type="text" name="goods_selects" value="`+ $("#goods_select").val()+`"></td>`)
            $tr.append(`<td> <input style="width:100px" type="text" name="FBAID_selects" value="`+ $("#FBAID_select").val()+`"></td>`)
            $tr.append(`<td> <input style="width:100px" type="text" name="referenceID_selects" value="`+ $("#referenceID_select").val()+`"></td>`)
            $tr.append(`<td> <input style="width:100px" type="text" name="boxNum_selects" value="`+ $("#boxNum_select").val()+`"></td>`)
            $tr.append(`<td> <input style="width:100px" type="text" name="goodsNum_selects" value="`+ $("#goodsNum_select").val()+`"></td>`)
            $tr.append(`<td> <input style="width:100px" type="text" name="goodsWeight_selects" value="`+ $("#goodsWeight_select").val()+`"></td>`)
            $tr.append(`<td>` + `<a href="javascript:;" className="td_a_3" id="Button2" onClick="deltr(this)">删除</a>` + `</td>`)
            $tr.appendTo($("#showGoods"))
            syalert.syhide('alert4')
        },
        update_warehouse : function () {
            $.get(
                "update_data",
                {"data_header":"warehouse"},
                function (data){
                    if (data === 'ok'){
                        alert("更新完成")
                    }
                },
            );
        },
        update_server : function () {
            $.get(
                "update_data",
                {"data_header":"server"},
                function (data){
                    if (data === 'ok'){
                        alert("更新完成")
                    }
                },
            );
        },
        update_goods : function () {
            $.get(
                "update_data",
                {"data_header":"goods"},
                function (data){
                    if (data === 'ok'){
                        alert("更新完成")
                    }
                },
            );
        }
    }
}();





