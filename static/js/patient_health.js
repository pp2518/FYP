$(document).ready(function () {

    var table


    function addPatienthealth(data) {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "patient_health",
            "method": "POST",
            "headers": {
                "content-type": "application/json",
                "cache-control": "no-cache",
                "postman-token": "2612534b-9ccd-ab7e-1f73-659029967199"
            },
            "processData": false,
            "data": JSON.stringify(data)
        }

        $.ajax(settings).done(function (response) {
            $('.modal.in').modal('hide')
            $.notify("Health record has been added successfully!", {"status":"success"});
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getPatienthealth()
        });

    }

    function deletePatienthealth(id) {
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "patient_health/" + id,
            "method": "DELETE",
            "headers": {
                "cache-control": "no-cache",
                "postman-token": "28ea8360-5af0-1d11-e595-485a109760f2"
            }
        }

swal({
    title: "Are you sure?",
    text: "You will not be able to recover this data",
    type: "warning",
    showCancelButton: true,
    confirmButtonColor: "#DD6B55",
    confirmButtonText: "Yes, delete it!",
    closeOnConfirm: false
}, function() {
 $.ajax(settings).done(function (response) {
   swal("Deleted!", "Health record has been removed.", "success");
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getPatienthealth()
        });


});

    }

    function updatePatienthealth(data, id) {
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "patient_health/" + id,
            "method": "PUT",
            "headers": {
                "content-type": "application/json",
                "cache-control": "no-cache"
            },
            "processData": false,
            "data": JSON.stringify(data)
        }

        $.ajax(settings).done(function (response) {
            $('.modal.in').modal('hide')
            $.notify("Health Record Updated Successfully", {"status":"success"});
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getPatienthealth()
        });


    }

    function getPatienthealth() {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "patient_health",
            "method": "GET",
            "headers": {
                "cache-control": "no-cache"
            }
        }

        $.ajax(settings).done(function (response) {



            table = $('#datatable4').DataTable({
                "bDestroy": true,
                'paging': true, // Table pagination
                'ordering': true, // Column ordering
                'info': true, // Bottom left status text
                aaData: response,
                 "aaSorting": [],
                aoColumns: [
                    {
                        mData: 'pat_first_name'
                    },
                    {
                        mData: 'pat_last_name'
                    },
                    {
                        mData: 'pat_blood_pressure'
                    },
                    {
                        mData: 'pat_blood_sugar'
                    },
                    {
                        mRender: function (o) {
                            return '<button class="btn-xs btn btn-success btn-edit" type="button" style="border-radius:0%;">Update</button> <button class="btn-xs btn btn-danger delete-btn" type="button" style="border-radius:0%;">Remove</button>';
                        }
                    },
                    
        ]
            });
            $('#datatable4 tbody').on('click', '.delete-btn', function () {
                var data = table.row($(this).parents('tr')).data();
                console.log(data)
                deletePatienthealth(data.pat_id)

            });
            $('.btn-edit').one("click", function(e) {
                var data = table.row($(this).parents('tr')).data();
                $('#myModal').modal().one('shown.bs.modal', function (e) {
                    for (var key in data) {
                        $("[name=" + key + "]").val(data[key])
                    }
                    $("#savethepatient").off("click").on("click", function(e) {
                    var instance = $('#detailform').parsley();
                    instance.validate()
                    console.log(instance.isValid())
                    if(instance.isValid()){
                        jsondata = $('#detailform').serializeJSON();
                        updatePatienthealth(jsondata, data.pat_id)
                        }

                    })
                })



            });

        });


    }




    $("#addpatient").click(function () {
$('#detailform input,textarea').val("")
        $('#myModal').modal().one('shown.bs.modal', function (e) {

console.log('innn')
            $("#savethepatient").off("click").on("click", function(e) {
            console.log("inn")
            var instance = $('#detailform').parsley();
            instance.validate()
                    if(instance.isValid()){
                jsondata = $('#detailform').serializeJSON();
                addPatienthealth(jsondata)
                }

            })

        })



    })


getPatienthealth()
})