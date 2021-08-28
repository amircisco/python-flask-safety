jQuery(document).ready(function(){
    jQuery(".reset").click(function(){
        jQuery(".input_radio").each(function(){
            jQuery(this).prop("checked",false);
        });
    });

    jQuery("#frm").submit(function(){
        var count = 0;
        for(var i=0;i<23;i++){
            var index = 'r'+i.toString();        
            if(jQuery("input:radio[name='"+index+"']").is(":checked")){
                count++;
            }
        }

        if(count==23)
            return true;
        alert("please answer all questions..."); 
        return false;
    });


    jQuery(".spcheck").each(function(){            
        var html = jQuery(this).html();
        if(html.indexOf('.') > -1 ){
            var html1 = html.split('.')[0];
            var html2 = html.split('.')[1].substr(0,2);
            html = html1+'.'+html2;
            jQuery(this).html(html);
        }
    });
    

});