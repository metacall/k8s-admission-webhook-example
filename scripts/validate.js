module.exports={
    validate: function(payload){
        console.log(payload);
        if(payload.request.object.metadata.labels.app_owner && payload.request.object.metadata.labels.app_owner == "metacall"){
            return true;
        }
        return false;
    }
}
