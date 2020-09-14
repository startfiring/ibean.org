ACI_PERS_RESOURCE_GROUP=MSDNRGKangZian
ACI_PERS_STORAGE_ACCOUNT_NAME=kangzianstorage
ACI_PERS_LOCATION=eastasia
ACI_PERS_SHARE_NAME=ibean

az container create \
    --resource-group $ACI_PERS_RESOURCE_GROUP \
    --name ibean \
    --image kangzian/www.ibean.org \
    --dns-name-label ibean \
    --ports 80 \
    --azure-file-volume-account-name $ACI_PERS_STORAGE_ACCOUNT_NAME \
    --azure-file-volume-account-key $STORAGE_KEY \
    --azure-file-volume-share-name $ACI_PERS_SHARE_NAME \
    --azure-file-volume-mount-path /mnt/azure \
    --environment-variables 'AZUREFILE'='/mnt/azure'
