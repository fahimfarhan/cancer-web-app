<script type="text/javascript">
$(function(){
    var comor = {{ my_list|safe }}
    if(comor[0]==0){document.getElementById("id_hypertension").checked = false;}


    if(comor[1]==0){ document.getElementById("id_diabetes").checked = false; }

    if(comor[2]==0){ document.getElementById("id_cardiac").checked = false; }


    if(comor[3]==0){ document.getElementById("id_liver").checked = false; }

    if(comor[4]==0){ document.getElementById("id_kedney").checked = false; }

    if(comor[5]==0){ document.getElementById("id_others").checked = false; }
});
</script>

<script type="text/javascript">
$(function(){
    var options_inv = ['marker','CBC','RBS','LFT','KFT','Serum-Electrolytes','Others'];
    var b = 0;
    var input = document.getElementById('id_type');
    for(i=0;i<options_inv.length;i++){
        if(input == options_inv[i]){
            b=1; break;
        }
    }

    if(b == 0){   document.getElementById("id_type").value = "";   }
});
</script>

<option class="w3-text-blue" value="marker">marker</option>
    <option class="w3-text-blue" value="CBC">CBC</option>
    <option class="w3-text-blue" value="RBS">RBS</option>
    <option value="LFT">LFT</option>
    <option value="KFT">KFT</option>
    <option value="Serum-Electrolytes">Serum-Electrolytes</option>
    <option value="Others">Others</option>