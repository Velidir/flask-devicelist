$.fn.editable.defaults.mode = 'inline';

//For Submit button on the Modal Add Device Form
$("#add-submit-btn").on("click",function(){
    //Serialize the form into an array of objects
    var formOutput = $("#add-device-form").serializeArray();
    //Enter DataTable
    var ipFromForm = $('#add-ip').val();
    if(ValidateIPaddress(ipFromForm)===true)
    {
        var addResult=false;
        $.ajax({
                      type: "POST",
                      url: 'add_devices',
                      data: formOutput,
                      success: function(responseFromBE){
                          if(responseFromBE==="False"){
                            alert("IP already exists!")
                            
                          }
                          else
                          {
                              
                            rowArray = [];
                            //Enter the form Outputs' values as an Array to be fed to DataTables
                            for(i=0;i < formOutput.length; i++)
                            {
                                rowArray.push(formOutput[i].value);
                            }
                            var table = $('#example').DataTable();
                            var rows = table.row.add(rowArray).draw(false);
                            // $('#example').DataTable( {
                                 
                                  
                            $("#addDeviceModal").modal('toggle');
                            
                          }
                      }
                      
                    });    
    }
    else
    {
        //alert("IP is not valid!");
        $('#add-ip').addClass("has-error");
        $('#add-ip').val("IP is not Valid!");
        
    }
    
    
       
    
});
// $('#add-device-form').validate({


//     submitHandler: function(form) {
//         $.ajax({
//             url: form.action,
//             type: form.method,
//             data: $(form).serialize(),
//             success: function(response) {
//                 return "True";
//             }            
//         });
//     }
// });




$(document).ready(function(){
    $('#example').DataTable( {
        "pageLength":500,
         "createdRow": function( row, data, dataIndex ) {
                                      $(row).addClass( 'rows');
                                      var columns = ["country","project","ip","type","access","username","password","enable","backedup","description","dmvpn"];
                                      if(columns.length===row.childNodes.length){
                                          for(i=0;i<columns.length;i++)
                                          {
                                              row.childNodes[i].className = columns[i];
                                          } 
                                          $('td').css('border-bottom','none');

                                      }
                                     
                                      
                                      
                                    }
    }
    );
});

$(document).on('click','td.country ',function(){
      $(this).editable({
        type: 'select',
        source:populateArrayFromHTML($('#add-country')),
        url: 'edit_devices',
        send:'always',
        params: function(params) {
        var item = selectRowFromClick($(this));
        item.country= params.value;
        return item;
        }
        });
    
});


$(document).on('click','td.project',function(){
      $(this).editable({
        type: 'text',
        url: 'edit_devices',
        send:'always',
        params: function(params) {
        var item = selectRowFromClick($(this));
        item.project= params.value;
        return item;
        }
        });
    
});

$(document).on('click','td.ip',function(){
      $(this).editable({
            type: 'text',
            url: 'edit_devices',
            send:'always',
            params: function(params) {
                    var item = selectRowFromClick($(this));
                    item.changedIP = params.value;
                    return item;            
                    
            },
            validate: function(value) {
                if(ValidateIPaddress(value)===false)
                {
                    return "You have entered an invalid IP address!";
                }
                else{
                    var ipList= $('td.ip');
                        for(i=0;i < ipList.length;i++)
                        {
                            if(value===ipList[i].innerText){
                                return "This IP already exists";
                            }           
                        }
                
                }
            }
        
        
        });
    
});
//source: ["DMVPN Spoke","DMVPN Hub","Core Switch","Access Switch","ASA","Riverbed","Asterisk"],
$(document).on('click','td.type ',function(){
      $(this).editable({
        type: 'select',
        source: populateArrayFromHTML($('#add-type')),
        url: 'edit_devices',
        send:'always',
        params: function(params) {
        var item = selectRowFromClick($(this));
        item.type= params.value;
        return item;
        }
        });
    
});


$(document).on('click','td.access',function(){
      $(this).editable({
        type: 'select',
        source: populateArrayFromHTML($('#add-access')),
        url: 'edit_devices',
        send:'always',
        params: function(params) {
        var item = selectRowFromClick($(this));
        item.access= params.value;
        return item;
        }
        });
    
});


$(document).on('click','td.username',function(){
      $(this).editable({
        type: 'text',
        url: 'edit_devices',
        send:'always',
        params: function(params) {
        var item = selectRowFromClick($(this));
        item.username= params.value;
        return item;
        }
        });
    
});


$(document).on('click','td.password',function(){
      $(this).editable({
        type: 'text',
        url: 'edit_devices',
        send:'always',
        params: function(params) {
        var item = selectRowFromClick($(this));
        item.password= params.value;
        return item;
        }
        });
    
});


$(document).on('click','td.enable',function(){
      $(this).editable({
        type: 'text',
        url: 'edit_devices',
        send:'always',
        params: function(params) {
        var item = selectRowFromClick($(this));
        item.enable= params.value;
        return item;
        }
        });
    
});




$(document).on('click','td.backedup',function(){
      $(this).editable({
        type: 'text',
        url: 'edit_devices',
        send:'always',
        params: function(params) {
        var item = selectRowFromClick($(this));
        item.backedup= params.value;
        return item;
        }
        });
    
});

$(document).on('click','td.description',function(){
      $(this).editable({
        type: 'text',
        url: 'edit_devices',
        send:'always',
        params: function(params) {
        var item = selectRowFromClick($(this));
        item.description= params.value;
        return item;
        }
        });
    
});

$(document).on('click','td.dmvpn',function(){
      $(this).editable({
        type: 'select',
        source: ["Yes","No"],
        url: 'edit_devices',
        send:'always',
        params: function(params) {
        var item = selectRowFromClick($(this));
        item.dmvpn= params.value;
        return item;
        }
        });
    
});



$.contextMenu({
    selector: '.rows',
    items: {
        
        add : {
            name : "Add",
            callback: function(){
                $("#addDeviceModal").modal();
            }
            
        },
        delete : {
            name: "Delete",
            callback: function(){
                var rowOriginal = $(this);
                var item = $(this);
                var parsedItem= item[0].getElementsByClassName('ip');
                var iptoDelete =parsedItem[0].innerText;
                $.ajax({
                      type: "POST",
                      url: 'delete_devices',
                      data: JSON.stringify(iptoDelete, null, '\t'),
                      contentType: 'application/json;charset=UTF-8',
                      success: null
                    });
                var table = $('#example').DataTable();
                var deletedRow = table.rows( item);
                deletedRow.remove().draw(false);
           }
        }
        
    }
});
//remove the dashed line from x-editable
$('td').css('border-bottom','none');

////////Start of functions for the Script

function selectRowFromClick(htmlItem){
    var item =htmlItem[0];
    var unparsedObject = item.parentElement.querySelectorAll('td');
    var objectDB = {};
    objectDB.country= unparsedObject[0].innerText;
    objectDB.project= unparsedObject[1].innerText;
    objectDB.ip= unparsedObject[2].innerText;
    objectDB.type= unparsedObject[3].innerText;
    objectDB.access= unparsedObject[4].innerText;
    objectDB.username= unparsedObject[5].innerText;
    objectDB.password= unparsedObject[6].innerText;
    objectDB.enable= unparsedObject[7].innerText;
    objectDB.backedup= unparsedObject[8].innerText;
    objectDB.description= unparsedObject[9].innerText;
    objectDB.dmvpn= unparsedObject[10].innerText;
    return objectDB;
}

function ValidateIPaddress(ipaddress) 
{
 if (/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(ipaddress))
  {
    return (true);
  }
return (false);
}

function populateArrayFromHTML(jQueryArray){
    var tempVar= jQueryArray[0];
    jQueryArray = tempVar.options;
    var returnArray = [];
    for(i=0;i < jQueryArray.length;i++)
    {
        returnArray[i] = jQueryArray[i].innerText;
    }
    return returnArray;
}