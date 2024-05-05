# Frontend Deployment

### Deploy to QA

To perform a QA deployment over AWS S3:

```bash
make deploy_qa
```

### Other environments deployment

To perform a Staging, Demo and Production deployment over AWS S3:

```bash
make deploy_staging
```
```bash
make deploy_demo
```
```bash
make deploy_prod
```

## Troubleshooting

If you receive the error `ERROR running aws s3api put-bucket-policy --bucket BUCKET_NAME --policy S3_BUCKET_POLICY`, probably the script was unable to deactivate the 'Block all public access' option on the S3 bucket.

To solve it:

* Go to the AWS Console.
* Go to S3.
* Search for App bucket (e.g. `exampleapp-frontend-website`).
* Click on the bucket name.
* Click on the 'Permissions' tab.
* Click on 'Edit' in the 'Block public access (bucket settings)' section.
* Uncheck 'Block all public access'.
* Click on 'Save changes'.
* Confirm the operation.
 
To link this S3 bucket to the App domain:"
 
* Go to Route 53.
* Click on the Zone corresponding to the App domain.
* Click on 'Create Record'.
* Enter the subdomain: 'app-qa', 'app-staging', 'app-demo' or 'app' (for production).
* Enable 'alias'.
* In 'Route traffic to' select the 'Alias to CloudFront' option.
* In 'Choose distribution' select the one corresponding to App stage.
* Click on 'Create Records'.
 