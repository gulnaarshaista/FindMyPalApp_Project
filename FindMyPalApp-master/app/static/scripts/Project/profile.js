// Initialize Firebase


$(document).ready(function () {



    var config = {
        apiKey: "AIzaSyD8_nEsadS4xowGxBSAzipb5r1uqRiu6V4",
        authDomain: "dev-findmypal.firebaseapp.com",
        databaseURL: "https://dev-findmypal.firebaseio.com",
        projectId: "dev-findmypal",
        storageBucket: "dev-findmypal.appspot.com",
        messagingSenderId: "116241201934"
    };

    firebase.initializeApp(config);


    var currentUrl = window.location.href;

    var url_values = currentUrl.split('?');
    url_values = url_values[1].split('&');

    var user_id = url_values[0].split('=');
    var joinedUser_id = url_values[1].split('=');
    var joinedStatus = url_values[2].split('=');

    var uid = user_id[1];
    var joinedUserId = joinedUser_id[1];
    var joinedUserStatus = joinedStatus[1];


    var currentUser;

    //sign In and Sign Out recognition

    $(".success-msg").hide();

    if (!joinedUserId) {

        firebase.auth().onAuthStateChanged(function (user) {


            if (user) {
                currentUser = user;
                document.getElementById("username").innerHTML = "Hello " + user.displayName;
                var userName = user.displayName.split(" ");
                document.getElementById("firstname").value = userName[0];
                document.getElementById("lastname").value = userName[userName.length - 1];
            }
            else {
                console.log('error');
            }

        });

        profile(uid);
        profilePicture(uid);
        $("#update_profile").show();
    }
    else {
        profile(joinedUserId);
        profilePicture(joinedUserId);
        $('#profilePic input').prop('readonly', true);
        $('#profilePic input[type=radio],#profilePic input[type=checkbox],#profilePic select,#profilePic input[type=file]').prop('disabled', true);
        $("#update_profile,.update_pic").hide();

    }

    //Sign out

    function profile(id) {

        firebase.database().ref('/user_profiles/' + id).once('value').then(function (snapshot) {

            var user_info = snapshot.val();
            $("#firstname").val(user_info.firstname);
            $("#lastname").val(user_info.lastname);
            $("#nickname").val(user_info.nickname);
            $("#middlename").val(user_info.middlename);

            $("#gender").val(user_info.gender);

            $('.user-education-level input[value=' + user_info.eduction_level + ']').prop('checked', true);
            $('.user-education-year input[value=' + user_info.education_year + ']').prop('checked', true);


            $.each(user_info.interested_category, function (index, value) {

                $('.user-interested-category input[value=' + value + ']').prop('checked', true);

            });

            // $("#profile_picture").attr('src', snapshot.val().profile_picture);
        });
    }


    //Profile Page

    $("#update_profile").click(function(){

        var userProfile= {};
        userProfile.firstname = $("#firstname").val();
        userProfile.lastname = $("#lastname").val();
        userProfile.middlename = $("#middlename").val();
        userProfile.nickname = $("#nickname").val();
        userProfile.gender = $("#gender option:selected").text();
        userProfile.email = currentUser.email;
        userProfile.eduction_level = $("input[name='education-level']:checked").val();
        userProfile.education_year = $("input[name='education-year']:checked").val();



        var interested_category = [];
        $.each($("input[name='interested-category']:checked"), function () {
            interested_category.push($(this).val());
        });
        userProfile.interested_category = interested_category;




        //Script for validation

        if (userProfile.firstname === "") {

            document.getElementById('profilePageMsg').innerHTML = "Please update your First Name";
            document.getElementById("profilePageMsg").style.backgroundColor = 'red';
            showMessage();
            return;
        }
        if (userProfile.lastname === "") {

            document.getElementById('profilePageMsg').innerHTML = "Please update your Last Name";
            document.getElementById("profilePageMsg").style.backgroundColor = 'red';
            showMessage();
            return;
        }
        if (userProfile.nickname === "") {

            document.getElementById('profilePageMsg').innerHTML = "Please update your Nick Name";
            document.getElementById("profilePageMsg").style.backgroundColor = 'red';
            showMessage();
            return;
        }
        if (userProfile.gender === "Choose Gender") {

            document.getElementById('profilePageMsg').innerHTML = "Please update your Gender";
            document.getElementById("profilePageMsg").style.backgroundColor = 'red';
            showMessage();
            return;
        }

        var educationLevel = $("input[name='education-level']:checked");
        if (educationLevel.length === 0) {

            document.getElementById('profilePageMsg').innerHTML = "Please update your Education Level";
            document.getElementById("profilePageMsg").style.backgroundColor = 'red';
            showMessage();
            return
        } else {
            userProfile.eduction_level = educationLevel.val();
        }

        var educationYear = $("input[name='education-year']:checked");
        console.log(educationYear);
        if (educationYear.length == 0) {

            document.getElementById('profilePageMsg').innerHTML = "Please update your Education Year";
            document.getElementById("profilePageMsg").style.backgroundColor = 'red';
            showMessage();
            return;
        }
        /*else if (educationYear.val().trim() == "Other") {
            var otherYear = $("#other-edu-year").val().trim();
            if (otherYear === "") {
                alert("Please input that other education year");
                return;
            } else {
                userProfile.education_year = otherYear;
            }
            } */
        else {
            userProfile.education_year = educationYear.val();
        }


        //script for validation



        writeUserData(userProfile);
    });




    function writeUserData(userProfile) {
        document.getElementById('profilePageMsg').innerHTML = "Your Profile has been Updated!!! ";
        document.getElementById("profilePageMsg").style.backgroundColor = 'green';
        firebase.database().ref('user_profiles/' + currentUser.uid).set({
            displayName:currentUser.displayName,
            firstname: userProfile.firstname,
            lastname: userProfile.lastname,
            middlename: userProfile.middlename,
            nickname: userProfile.nickname,
            gender: userProfile.gender,
            eduction_level: userProfile.eduction_level,
            education_year: userProfile.education_year,
            email: userProfile.email,
            interested_category:userProfile.interested_category


        });


        $(".success-msg").slideDown();
        setTimeout(function () {
            $(".success-msg").slideUp();
        }, 3000)
    }

    function showMessage() {

        $(".success-msg").slideDown();
        setTimeout(function () {
            $(".success-msg").slideUp();
        }, 3000)
    }

    //Profile Page



    var storageRef = firebase.storage().ref();
    var storageReference;
    function profilePicture(id) {

        // Create a root reference for storage

        storageReference = firebase.storage().ref('/userProfilePictures/' + id);

        //Checking for an Profile picture
        storageReference.getDownloadURL().then(function (url) {

            // Or inserted into an <img> element:
            var img = document.getElementById('profile_picture');
            img.src = url;
        }).catch(function (error) {

            // Attaching the image to the image source
            storageRef.child('images/default-avatar.jpg').getDownloadURL().then(function (url) {

                // Or inserted into an <img> element:
                var img = document.getElementById('profile_picture');
                img.src = url;
            }).catch(function (error) {
                console.log(error.message);
            });


        });

    }


    //Uploading the profie picture

    $('input[type=file]').on('change', function () {
        var file = this.files[0];
        var user = firebase.auth().currentUser;
        var user_id = user.uid;


        storageReference.put(file).on('state_changed', function (snapshot) {

            // Loading GIF while the image is uploading
            //storageRef.child('images/loading.gif').getDownloadURL().then(function (url) {

            //    // Or inserted into an <img> element:
            //    var img = document.getElementById('profile_picture');
            //    img.src = url;



            //}).catch(function (error) {
            //    console.log(error.message);
            //});

            storageReference.getDownloadURL().then(function (url) {

                // Or inserted into an <img> element:

                var img = document.getElementById('profile_picture');
                img.src = url;
            }).catch(function (error) {
                console.log(error.message);
            });

        });

    });

    //Signout function


    $("#logout").on('click', function () {

        firebase.auth().signOut().then(function () {
            // Sign-out successful.

        }, function (error) {
            // An error happened.
        });

    });



    //Profile Page Forwarding

    $(".activity #profile_picture").on('click', function () {


        $("#homepage input").val(uid);
        $("#homepage").submit();


    });

    $(".profile #site-logo,#activityPage,#siteTitle").on('click', function () {


        $("#homepage input").val(uid);
        $("#homepage").submit();


    });



});
