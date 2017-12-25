$(function(){
    var $from = $('.from');
    var $to = $('.to');
    var $fun = $('.fun');
    button = document.getElementById('graph_button');
    var $plot1 = $('.plot1');
    var check;
    const $dx = 0.01
    check=document.getElementById('iddd');

    button.click(function(e){
        e.preventDefault();
        $funn = $fun.val()
        if ($funn!=0) {


            $fromm = parseFloat($from.val());
            $too = parseFloat($to.val());
            var $values = []
            for (var x = $fromm; x <= $too; x += $dx) {
                $values.push([x, eval($funn)])
            }

            $.plot($plot1, [{label: $funn, data: $values}], {})
            if (check.checked){
				karl = setInterval(function(){
                $fromm += $dx;
                $too += $dx;
                $values = []

                for(var x = $fromm; x <= $too; x += $dx){
                    $values.push([x, eval($funn)])
                }

                $.plot($plot1, [{label: $funn, data: $values}], {})
            }, 1);} else {clearInterval(karl);}

        } else
        {
            {alert("Вы не ввели функцию")}
        }
    });
})