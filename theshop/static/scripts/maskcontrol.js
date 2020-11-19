 function mask() {

    console.log("od");

    const cardnumber= document.getElementById("card-number")
    const expirationdate = document.getElementById("exp-date")
    const securitycode = document.getElementById("security-code")



var cardnumber_mask = new IMask(cardnumber, {

    mask: [
        {
            mask: '0000 0000 0000 0000',
            regex: '^(5[1-5]\\d{0,2}|22[2-9]\\d{0,1}|2[3-7]\\d{0,2})\\d{0,12}',
            cardtype: 'mastercard'
        },
        {
            mask: '0000 0000 0000 0000',
            regex: '^4\\d{0,15}',
            cardtype: 'visa'
        },
        {
            mask: '0000 0000 0000 0000',
            cardtype: 'Unknown'
        }
    ]
});


var expirationdate_mask = new IMask(expirationdate, {
    mask: 'MM{/}YY',
    groups: {
        YY: new IMask.MaskedPattern.Group.Range([0, 99]),
        MM: new IMask.MaskedPattern.Group.Range([1, 12]),
    }
});

//Mask the security code
var securitycode_mask = new IMask(securitycode, {
    mask: '0000',
});


}
