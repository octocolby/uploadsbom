# Upload SBOM to Dependency Track GitHub Action

Usage: Generate a SBOM CyclondDX json file as part of your GitHub actions then call this action to upload it to Dependency Track.
```
    - name: Upload SBOM
      uses: octocolby/uploadsbom@v1.0.5
      with:
        dependency_track_url: "https://localhost"
        dependency_track_api_key: "${{ secrets.DTRACK_KEY }}"
        project_name: "my-project"
        version: "${{ env.BUILD_NUMBER }}"
        sbom-file: 'sbom.json'
        tags: 'myteam,cooltag'
        description: 'This is my cool app'
```