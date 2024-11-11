#!/bin/bash
PATH_TO_MACHINE=./etovucca

sanitize_string() {
  echo "$@" | sed 's/[{}(),\"@#$!\^|*]//g'
}

parse_query_string() {

    # string regex partially from https://unix.stackexchange.com/questions/63690

    readonly URI_REGEX='^name=([^&]+)&county=([^&]+)&zipc=([^&]+)&dob=(.*)'

    [[ $1 =~ $URI_REGEX ]]

    array[name]=${BASH_REMATCH[1]}
    array[county]=${BASH_REMATCH[2]}
    array[zipc]=${BASH_REMATCH[3]}
    array[dob]=${BASH_REMATCH[4]}

}

render_register() {
    echo "Content-Type: text/html"
    echo ""
    echo ""
    echo "<link rel='stylesheet' href='https://spar.isi.jhu.edu/teaching/443/main.css'>"
    echo '<h2 id="dlobeid-etovucca-voting-machine">DLOBEID EtovUcca Voting Machine</h2><h1 id="voter-registration">Voter Registration</h1><br><form><label for="name">Voter Name</label><br> <input type="text" id="name" name="name"><br> <label for="county">County</label><br> <input type="text" id="county" name="county"><br> <label for="zipc">ZIP Code</label><br> <input type="number" id="zipc" name="zipc"><br> <label for="dob">Date of Birth</label><br> <input type="date" id="dob" name="dob"><br> <input type="submit" value="Submit"></form>'
    echo '<a href="./home.cgi">Return to Homepage</a><br>'
}

register_voter() {
    command="$PATH_TO_MACHINE add-voter ${array[name]} ${array[county]} ${array[zipc]} ${array[dob]}"
    id=$(eval $command)
    if [ ! $id -eq 0 ]; then
        echo "<b>Voter registered. ID: $id</b>"
    else
        echo "<b>Error in registering voter. Please try again.</b>"
    fi
}

render_register

if [ ! -z $QUERY_STRING ]; then
    declare -A array
    parse_query_string $QUERY_STRING
    register_voter
fi


